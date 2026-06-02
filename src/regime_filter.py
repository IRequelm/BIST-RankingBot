from pathlib import Path

import pandas as pd

from src.indicators import get_forward_month_return
from src.reporting import assign_periods, max_drawdown, selection_score, summarize_returns


def build_bist100_regime_signal(benchmark_prices: pd.DataFrame) -> pd.DataFrame:
    """Return month-end BIST100 MA200 regime signal."""
    close = benchmark_prices["Close"].sort_index()
    signal = pd.DataFrame(index=close.index)
    signal["bist100_close"] = close
    signal["bist100_ma200"] = close.rolling(200).mean()
    monthly = signal.resample("ME").last().dropna()
    monthly["bist100_below_ma200"] = monthly["bist100_close"] < monthly["bist100_ma200"]
    monthly["date"] = monthly.index
    return monthly.reset_index(drop=True)


def _selected_return(
    stock_prices: dict[str, pd.DataFrame],
    rankings: pd.DataFrame,
    ranking_date: pd.Timestamp,
    portfolio_size: int,
) -> tuple[float | None, int]:
    month_rankings = rankings[pd.to_datetime(rankings["date"]) == ranking_date]
    if month_rankings.empty:
        return None, 0

    selected = month_rankings.sort_values("rank").head(portfolio_size)
    returns = []
    for _, row in selected.iterrows():
        symbol = row["symbol"]
        stock_return = get_forward_month_return(stock_prices[symbol], ranking_date)
        if stock_return is not None:
            returns.append(stock_return)

    if not returns:
        return None, 0

    return sum(returns) / len(returns), len(returns)


def run_regime_policy_backtests(
    stock_prices: dict[str, pd.DataFrame],
    rankings_by_model: dict[str, pd.DataFrame],
    benchmark_prices: pd.DataFrame,
    portfolio_sizes: list[int],
    transaction_cost: float,
    periods: dict[str, tuple[str, str]],
    defensive_model: str = "low_volatility",
    defensive_portfolio_size: int = 5,
) -> tuple[pd.DataFrame, pd.DataFrame]:
    """Run baseline, cash, defensive, and reduced-exposure regime policies."""
    regime_signal = build_bist100_regime_signal(benchmark_prices)
    signal_by_date = regime_signal.set_index("date")
    result_rows = []

    if defensive_model not in rankings_by_model:
        raise ValueError(f"Missing defensive model rankings: {defensive_model}")

    for model_name, rankings in rankings_by_model.items():
        ranking_dates = sorted(pd.to_datetime(rankings["date"].unique()))
        for portfolio_size in portfolio_sizes:
            for policy in ["baseline", "cash_mode", "defensive_mode", "reduced_exposure_mode"]:
                equity = 1.0
                for ranking_date in ranking_dates:
                    if ranking_date not in signal_by_date.index:
                        continue

                    is_bear = bool(signal_by_date.loc[ranking_date, "bist100_below_ma200"])
                    active_model = model_name
                    active_portfolio_size = portfolio_size
                    exposure = 1.0

                    if policy == "cash_mode" and is_bear:
                        gross_return = 0.0
                        net_return = 0.0
                        holdings = 0
                        active_model = "cash"
                        active_portfolio_size = 0
                    else:
                        selected_rankings = rankings
                        if policy == "defensive_mode" and is_bear:
                            active_model = defensive_model
                            active_portfolio_size = defensive_portfolio_size
                            selected_rankings = rankings_by_model[defensive_model]
                        elif policy == "reduced_exposure_mode" and is_bear:
                            exposure = 0.5

                        selected = _selected_return(
                            stock_prices=stock_prices,
                            rankings=selected_rankings,
                            ranking_date=ranking_date,
                            portfolio_size=active_portfolio_size,
                        )
                        gross_return, holdings = selected
                        if gross_return is None:
                            continue

                        net_return = exposure * (gross_return - transaction_cost)

                    equity *= 1 + net_return
                    result_rows.append(
                        {
                            "date": ranking_date,
                            "policy": policy,
                            "base_model": model_name,
                            "base_portfolio_size": portfolio_size,
                            "active_model": active_model,
                            "active_portfolio_size": active_portfolio_size,
                            "bist100_below_ma200": is_bear,
                            "exposure": exposure,
                            "holdings": holdings,
                            "gross_return": gross_return,
                            "transaction_cost": transaction_cost if holdings else 0.0,
                            "net_return": net_return,
                            "equity": equity,
                        }
                    )

    results = pd.DataFrame(result_rows)
    results = assign_periods(results, periods)
    return results, regime_signal


def _benchmark_returns(benchmark_prices: pd.DataFrame) -> pd.Series:
    monthly_close = benchmark_prices["Close"].resample("ME").last()
    return ((monthly_close.shift(-1) / monthly_close) - 1).rename("BIST100").dropna()


def _summarize_policy_group(group: pd.DataFrame, benchmark_monthly: pd.Series) -> dict[str, object]:
    group = group.sort_values("date").copy()
    strategy_stats = summarize_returns(group["net_return"])
    benchmark = benchmark_monthly.reindex(pd.to_datetime(group["date"])).dropna()
    benchmark_stats = summarize_returns(benchmark)
    excess = strategy_stats["total_return"] - benchmark_stats["total_return"]

    return {
        "policy": group["policy"].iloc[0],
        "base_model": group["base_model"].iloc[0],
        "base_portfolio_size": int(group["base_portfolio_size"].iloc[0]),
        "period": group["period"].iloc[0],
        "months": len(group),
        "bear_months": int(group["bist100_below_ma200"].sum()),
        "avg_exposure": group["exposure"].mean(),
        "total_return": strategy_stats["total_return"],
        "bist100_total_return": benchmark_stats["total_return"],
        "excess_return_vs_bist100": excess,
        "max_drawdown": strategy_stats["max_drawdown"],
        "bist100_max_drawdown": benchmark_stats["max_drawdown"],
        "win_rate": strategy_stats["win_rate"],
        "robustness_score": selection_score(excess, strategy_stats["max_drawdown"], strategy_stats["win_rate"]),
    }


def summarize_regime_results(
    results: pd.DataFrame,
    benchmark_prices: pd.DataFrame,
) -> tuple[pd.DataFrame, pd.DataFrame]:
    benchmark_monthly = _benchmark_returns(benchmark_prices)
    detail = pd.DataFrame(
        [
            _summarize_policy_group(group, benchmark_monthly)
            for _, group in results.groupby(["policy", "base_model", "base_portfolio_size", "period"])
        ]
    )

    full = detail[detail["period"].isin(["train", "validation", "out_of_sample"])].copy()
    policy_rows = []
    for policy, policy_df in full.groupby("policy"):
        out_sample = policy_df[policy_df["period"] == "out_of_sample"]
        policy_rows.append(
            {
                "policy": policy,
                "avg_total_return": policy_df["total_return"].mean(),
                "avg_excess_return_vs_bist100": policy_df["excess_return_vs_bist100"].mean(),
                "avg_max_drawdown": policy_df["max_drawdown"].mean(),
                "avg_out_of_sample_return": out_sample["total_return"].mean(),
                "avg_robustness_score": policy_df["robustness_score"].mean(),
                "best_combo_count": int((policy_df["robustness_score"] == policy_df["robustness_score"].max()).sum()),
            }
        )

    policy_summary = pd.DataFrame(policy_rows).sort_values("avg_robustness_score", ascending=False)
    return detail, policy_summary


def save_regime_filter_report(
    results: pd.DataFrame,
    detail_summary: pd.DataFrame,
    policy_summary: pd.DataFrame,
    regime_signal: pd.DataFrame,
    results_dir: str,
) -> str:
    Path(results_dir).mkdir(exist_ok=True)
    results.to_csv(Path(results_dir) / "regime_filter_results.csv", index=False)
    detail_summary.to_csv(Path(results_dir) / "regime_filter_detail.csv", index=False)
    policy_summary.to_csv(Path(results_dir) / "regime_filter_policy_summary.csv", index=False)
    regime_signal.to_csv(Path(results_dir) / "bist100_regime_signal.csv", index=False)

    recommendation = policy_summary.iloc[0]["policy"] if not policy_summary.empty else "none"
    best_oos = (
        detail_summary[detail_summary["period"] == "out_of_sample"]
        .sort_values("robustness_score", ascending=False)
        .head(10)
    )

    lines = [
        "# Regime Filter Report",
        "",
        "Policies tested:",
        "- baseline: current ranking/backtest system",
        "- cash_mode: hold cash when BIST100 is below MA200",
        "- defensive_mode: switch to low_volatility Top 5 when BIST100 is below MA200",
        "- reduced_exposure_mode: invest 50% when BIST100 is below MA200",
        "",
        f"Recommended policy: **{recommendation}**",
        "",
        "Recommendation is based on average robustness score across model and portfolio combinations.",
        "",
        "## Policy Summary",
        "",
        policy_summary.to_markdown(index=False, floatfmt=".4f") if not policy_summary.empty else "No policy results.",
        "",
        "## Best Out-Of-Sample Combinations",
        "",
        best_oos.to_markdown(index=False, floatfmt=".4f") if not best_oos.empty else "No out-of-sample results.",
        "",
        "## Regime Signal Coverage",
        "",
        f"- Total signal months: {len(regime_signal)}",
        f"- BIST100 below MA200 months: {int(regime_signal['bist100_below_ma200'].sum())}",
        f"- Below-MA200 rate: {regime_signal['bist100_below_ma200'].mean():.2%}",
        "",
    ]

    markdown = "\n".join(lines)
    (Path(results_dir) / "regime_filter_report.md").write_text(markdown, encoding="utf-8")
    return recommendation
