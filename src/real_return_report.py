from pathlib import Path

import pandas as pd

from src.reporting import max_drawdown, summarize_returns


def _load_csv(path: Path, parse_dates: list[str] | None = None) -> pd.DataFrame:
    if path.exists():
        return pd.read_csv(path, parse_dates=parse_dates)
    return pd.DataFrame()


def _monthly_usdtry_returns(usdtry_prices: pd.DataFrame | None) -> pd.Series:
    if usdtry_prices is None or usdtry_prices.empty or "Close" not in usdtry_prices:
        return pd.Series(dtype=float)

    close = usdtry_prices["Close"].dropna().sort_index()
    monthly = close.resample("ME").last().pct_change().dropna()
    monthly.name = "usdtry_return"
    return monthly


def _to_usd_returns(tl_returns: pd.Series, usdtry_returns: pd.Series) -> pd.Series:
    if tl_returns.empty or usdtry_returns.empty:
        return pd.Series(dtype=float)

    tl = tl_returns.copy()
    tl.index = pd.to_datetime(tl.index)
    fx = usdtry_returns.copy()
    fx.index = pd.to_datetime(fx.index)
    aligned = pd.concat([tl.rename("tl_return"), fx.rename("usdtry_return")], axis=1, join="inner").dropna()
    if aligned.empty:
        return pd.Series(dtype=float)

    return ((1 + aligned["tl_return"]) / (1 + aligned["usdtry_return"]) - 1).rename("usd_return")


def _format_pct(value: float | None) -> str:
    if value is None or pd.isna(value):
        return "n/a"
    return f"{value:.2%}"


def _paper_real_return_section(results_path: Path, usdtry_prices: pd.DataFrame | None) -> list[str]:
    history = _load_csv(results_path / "paper_portfolio_history.csv", parse_dates=["date"])
    if history.empty:
        return ["## Paper Portfolio TL / USD", "", "Paper portfolio history is unavailable.", ""]

    latest = history.sort_values("date").tail(1).iloc[0]
    initial_value = float(history.sort_values("date")["portfolio_value"].iloc[0])
    latest_value = float(latest["portfolio_value"])
    tl_return = (latest_value / initial_value) - 1 if initial_value else 0.0

    usd_return = None
    fx_return = None
    if usdtry_prices is not None and not usdtry_prices.empty:
        fx = usdtry_prices["Close"].dropna().sort_index()
        if not fx.empty:
            start_date = pd.Timestamp(history["date"].min())
            end_date = pd.Timestamp(latest["date"])
            start_fx = fx.loc[fx.index >= start_date]
            end_fx = fx.loc[fx.index <= end_date]
            if not start_fx.empty and not end_fx.empty:
                start_rate = float(start_fx.iloc[0])
                end_rate = float(end_fx.iloc[-1])
                fx_return = (end_rate / start_rate) - 1
                initial_usd = initial_value / start_rate
                latest_usd = latest_value / end_rate
                usd_return = (latest_usd / initial_usd) - 1 if initial_usd else None

    return [
        "## Paper Portfolio TL / USD",
        "",
        f"- Latest portfolio value TL: {latest_value:,.2f}",
        f"- Portfolio TL return: {_format_pct(tl_return)}",
        f"- USDTRY return over paper period: {_format_pct(fx_return)}",
        f"- Portfolio USD return: {_format_pct(usd_return)}",
        f"- Benchmark TL return: {_format_pct(float(latest.get('benchmark_return', 0.0)))}",
        "",
    ]


def _best_model_real_return_section(results_path: Path, usdtry_prices: pd.DataFrame | None) -> list[str]:
    best = _load_csv(results_path / "best_model.csv")
    best_results = _load_csv(results_path / "best_model_results.csv", parse_dates=["date"])
    if best.empty or best_results.empty:
        return ["## Best Model TL / USD", "", "Best model results are unavailable.", ""]

    usdtry_returns = _monthly_usdtry_returns(usdtry_prices)
    tl_returns = best_results.sort_values("date").set_index("date")["net_return"]
    usd_returns = _to_usd_returns(tl_returns, usdtry_returns)
    tl_stats = summarize_returns(tl_returns)
    usd_stats = summarize_returns(usd_returns)
    fx_stats = summarize_returns(usdtry_returns.reindex(pd.to_datetime(tl_returns.index)).dropna())

    best_row = best.iloc[0]
    rows = pd.DataFrame(
        [
            {
                "metric": "total_return",
                "TL": tl_stats["total_return"],
                "USD": usd_stats["total_return"],
                "USDTRY": fx_stats["total_return"],
            },
            {
                "metric": "avg_monthly_return",
                "TL": tl_stats["avg_monthly_return"],
                "USD": usd_stats["avg_monthly_return"],
                "USDTRY": fx_stats["avg_monthly_return"],
            },
            {
                "metric": "max_drawdown",
                "TL": tl_stats["max_drawdown"],
                "USD": usd_stats["max_drawdown"],
                "USDTRY": max_drawdown((1 + usdtry_returns.reindex(pd.to_datetime(tl_returns.index)).dropna()).cumprod())
                if not usdtry_returns.empty
                else 0.0,
            },
            {
                "metric": "win_rate",
                "TL": tl_stats["win_rate"],
                "USD": usd_stats["win_rate"],
                "USDTRY": "",
            },
        ]
    )

    return [
        "## Best Model TL / USD",
        "",
        f"- Model: {best_row.get('model')}",
        f"- Portfolio size: {best_row.get('portfolio_size')}",
        f"- Period in `best_model_results.csv`: all available rows for selected model/size",
        "",
        rows.to_markdown(index=False, floatfmt=".4f"),
        "",
        "Interpretation: USD return converts TL strategy returns by the monthly USDTRY change. "
        "When USDTRY rises faster than the TL portfolio, USD-based performance falls.",
        "",
    ]


def _cash_allocation_section(results_path: Path) -> list[str]:
    current = _load_csv(results_path / "current_month_portfolio.csv")
    if current.empty:
        return ["## Cash Allocation", "", "Current portfolio is unavailable.", ""]

    min_buy = float(current["min_buy_expected_return"].iloc[0]) if "min_buy_expected_return" in current else 0.10
    buy_count = int((current["action"] == "BUY").sum())
    active_size = int(current["active_portfolio_size"].iloc[0]) if "active_portfolio_size" in current else 10
    cash_weight = max(1 - (buy_count / max(active_size, 1)), 0)

    return [
        "## Cash Allocation",
        "",
        f"- Minimum BUY expected return: {min_buy:.2%}",
        f"- BUY candidates meeting threshold: {buy_count}",
        f"- Active portfolio slot count: {active_size}",
        f"- Implied CASH weight when using equal opportunity slots: {cash_weight:.2%}",
        "",
    ]


def save_real_return_report(
    results_dir: str,
    benchmark_prices: pd.DataFrame | None,
    usdtry_prices: pd.DataFrame | None,
) -> Path:
    results_path = Path(results_dir)
    report_path = results_path / "real_return_report.md"
    lines = [
        "# Real Return Report",
        "",
        "This report evaluates performance in both TL and USD terms. USD performance is estimated with USDTRY.",
        "",
    ]
    lines.extend(_cash_allocation_section(results_path))
    lines.extend(_paper_real_return_section(results_path, usdtry_prices))
    lines.extend(_best_model_real_return_section(results_path, usdtry_prices))

    if benchmark_prices is not None and not benchmark_prices.empty:
        close = benchmark_prices["Close"].dropna().sort_index()
        if not close.empty:
            lines.extend(
                [
                    "## Market Reference",
                    "",
                    f"- Latest BIST100 close: {float(close.iloc[-1]):,.2f}",
                    "",
                ]
            )

    report_path.write_text("\n".join(lines), encoding="utf-8")
    return report_path
