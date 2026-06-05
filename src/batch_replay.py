from __future__ import annotations

from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd

from src.current_portfolio import generate_current_month_portfolio
from src.replay import (
    _build_historical_factor_state,
    _daily_portfolio_curve,
    _first_trading_day_on_or_after,
    _max_drawdown,
    _portfolio_return,
    _return_between,
    _selected_positions,
    _truncate_prices,
)


def _month_starts(start_date: str, benchmark_prices: pd.DataFrame) -> list[pd.Timestamp]:
    close = benchmark_prices["Close"].dropna().sort_index()
    if close.empty:
        return []

    start = pd.Timestamp(start_date).to_period("M").to_timestamp()
    end = pd.Timestamp(close.index.max()).to_period("M").to_timestamp()
    return [pd.Timestamp(date) for date in pd.date_range(start, end, freq="MS")]


def _compound_cagr(returns: pd.Series) -> float:
    clean = pd.to_numeric(returns, errors="coerce").dropna()
    if clean.empty:
        return 0.0

    equity = float((1 + clean).prod())
    years = len(clean) / 12
    if years <= 0 or equity <= 0:
        return 0.0
    return equity ** (1 / years) - 1


def _format_pct(value: float | None) -> str:
    if value is None or pd.isna(value):
        return "-"
    return f"{float(value):.2%}"


def _plot_equity_curve(results: pd.DataFrame, path: Path) -> None:
    plot = results.sort_values("actual_trading_date").copy()
    plot["strategy_equity"] = (1 + plot["portfolio_return"]).cumprod()
    plot["bist100_equity"] = (1 + plot["bist100_return"]).cumprod()

    plt.figure(figsize=(10, 5))
    plt.plot(pd.to_datetime(plot["actual_trading_date"]), plot["strategy_equity"], label="Strategy", linewidth=2)
    plt.plot(pd.to_datetime(plot["actual_trading_date"]), plot["bist100_equity"], label="BIST100", linewidth=2)
    plt.title("Batch Replay Equity Curve")
    plt.xlabel("Replay Month")
    plt.ylabel("Growth of 1 TL")
    plt.grid(True, alpha=0.3)
    plt.legend()
    plt.tight_layout()
    plt.savefig(path, dpi=150)
    plt.close()


def _plot_excess_heatmap(results: pd.DataFrame, path: Path) -> None:
    plot = results.copy()
    plot["date"] = pd.to_datetime(plot["actual_trading_date"])
    plot["year"] = plot["date"].dt.year
    plot["month"] = plot["date"].dt.month
    heatmap = plot.pivot_table(index="year", columns="month", values="excess_return", aggfunc="mean")
    heatmap = heatmap.reindex(columns=range(1, 13))

    fig, ax = plt.subplots(figsize=(11, max(2.5, 0.6 * len(heatmap))))
    values = heatmap.to_numpy(dtype=float)
    max_abs = max(abs(pd.Series(values.ravel()).dropna()).max(), 0.01) if values.size else 0.01
    image = ax.imshow(values, cmap="RdYlGn", vmin=-max_abs, vmax=max_abs, aspect="auto")

    ax.set_xticks(range(12))
    ax.set_xticklabels(["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"])
    ax.set_yticks(range(len(heatmap.index)))
    ax.set_yticklabels([str(year) for year in heatmap.index])
    ax.set_title("Monthly Excess Return vs BIST100")

    for row_index, year in enumerate(heatmap.index):
        for col_index, month in enumerate(heatmap.columns):
            value = heatmap.loc[year, month]
            if pd.notna(value):
                ax.text(col_index, row_index, f"{value:.1%}", ha="center", va="center", fontsize=8)

    fig.colorbar(image, ax=ax, fraction=0.025, pad=0.02, label="Excess return")
    plt.tight_layout()
    plt.savefig(path, dpi=150)
    plt.close()


def _summary_markdown(results: pd.DataFrame, start_date: str) -> str:
    if results.empty:
        return "# Batch Historical Replay Summary\n\nNo successful replay periods were generated.\n"

    sorted_results = results.sort_values("actual_trading_date").copy()
    best = sorted_results.loc[sorted_results["excess_return"].idxmax()]
    worst = sorted_results.loc[sorted_results["excess_return"].idxmin()]
    best_portfolio = sorted_results.loc[sorted_results["portfolio_return"].idxmax()]
    worst_portfolio = sorted_results.loc[sorted_results["portfolio_return"].idxmin()]
    top10 = sorted_results.sort_values("excess_return", ascending=False).head(10)
    bottom10 = sorted_results.sort_values("excess_return", ascending=True).head(10)

    strategy_cagr = _compound_cagr(sorted_results["portfolio_return"])
    bist100_cagr = _compound_cagr(sorted_results["bist100_return"])
    win_rate = float((sorted_results["excess_return"] > 0).mean())

    answer = (
        "Yes, the bot beat BIST100 consistently in this replay window."
        if win_rate >= 0.55 and sorted_results["excess_return"].mean() > 0
        else "No, the bot did not beat BIST100 consistently in this replay window."
    )

    lines = [
        "# Batch Historical Replay Summary",
        "",
        "## Main Question",
        "",
        '"Would I have beaten BIST100 consistently if I had followed the bot every month?"',
        "",
        f"**Answer:** {answer}",
        "",
        "## Test Setup",
        "",
        f"- Replay start: {start_date}",
        f"- Replay periods: {len(sorted_results)}",
        "- Holding period: 1 month / 30 calendar days",
        "- Recommendation uses only data available up to each replay date.",
        "- Each month uses the active regime, model, opportunity filter, and cash allocation framework.",
        "",
        "## Summary Metrics",
        "",
        f"- Number of replay periods: {len(sorted_results)}",
        f"- Average portfolio return: {_format_pct(sorted_results['portfolio_return'].mean())}",
        f"- Average BIST100 return: {_format_pct(sorted_results['bist100_return'].mean())}",
        f"- Average excess return: {_format_pct(sorted_results['excess_return'].mean())}",
        f"- Win rate vs BIST100: {_format_pct(win_rate)}",
        f"- Best month: {best_portfolio['replay_month']} ({_format_pct(best_portfolio['portfolio_return'])})",
        f"- Worst month: {worst_portfolio['replay_month']} ({_format_pct(worst_portfolio['portfolio_return'])})",
        f"- Largest outperformance: {best['replay_month']} ({_format_pct(best['excess_return'])})",
        f"- Largest underperformance: {worst['replay_month']} ({_format_pct(worst['excess_return'])})",
        f"- Average cash allocation: {_format_pct(sorted_results['cash_weight'].mean())}",
        f"- Average drawdown: {_format_pct(sorted_results['max_drawdown'].mean())}",
        f"- Final strategy CAGR: {_format_pct(strategy_cagr)}",
        f"- Final BIST100 CAGR: {_format_pct(bist100_cagr)}",
        "",
        "## Top 10 Replay Months",
        "",
        top10[
            [
                "replay_month",
                "portfolio_return",
                "bist100_return",
                "excess_return",
                "cash_weight",
                "selected_model",
                "selected_stocks",
            ]
        ].to_markdown(index=False, floatfmt=".4f"),
        "",
        "## Worst 10 Replay Months",
        "",
        bottom10[
            [
                "replay_month",
                "portfolio_return",
                "bist100_return",
                "excess_return",
                "cash_weight",
                "selected_model",
                "selected_stocks",
            ]
        ].to_markdown(index=False, floatfmt=".4f"),
        "",
    ]
    return "\n".join(lines)


def _load_policy_winners(results_dir: str | Path) -> tuple[tuple[str, int], tuple[str, int]]:
    summary_path = Path(results_dir) / "summary_report.csv"
    if not summary_path.exists():
        return ("mixed_model", 15), ("low_volatility", 15)

    summary = pd.read_csv(summary_path)
    out_of_sample = summary[summary["period"] == "out_of_sample"].copy()
    if out_of_sample.empty:
        return ("mixed_model", 15), ("low_volatility", 15)

    winner = out_of_sample.loc[out_of_sample["selection_score"].idxmax()]
    grouped = (
        out_of_sample.groupby(["model", "portfolio_size"], as_index=False)
        .agg(
            mean_score=("selection_score", "mean"),
            mean_drawdown=("strategy_max_drawdown", "mean"),
            win_rate=("win_rate", "mean"),
        )
    )
    grouped["robust_score"] = grouped["mean_score"] + grouped["win_rate"] * 0.25 + grouped["mean_drawdown"].abs().rsub(1) * 0.10
    robust = grouped.loc[grouped["robust_score"].idxmax()]
    return (str(winner["model"]), int(winner["portfolio_size"])), (str(robust["model"]), int(robust["portfolio_size"]))


def _policy_definitions(results_dir: str | Path) -> list[dict[str, object]]:
    oos_winner, robust = _load_policy_winners(results_dir)
    return [
        {"policy": "Baseline", "base_model": "volume_heavy", "defensive_model": "low_volatility", "base_size": 10, "defensive_size": 5, "selection_mode": "buy", "cash_cap": None, "regime": True, "opportunity_filter": True},
        {"policy": "A_No_cash_allocation", "base_model": "volume_heavy", "defensive_model": "low_volatility", "base_size": 10, "defensive_size": 5, "selection_mode": "buy", "cash_cap": 0.0, "regime": True, "opportunity_filter": True},
        {"policy": "B_Max_cash_25pct", "base_model": "volume_heavy", "defensive_model": "low_volatility", "base_size": 10, "defensive_size": 5, "selection_mode": "buy", "cash_cap": 0.25, "regime": True, "opportunity_filter": True},
        {"policy": "C_Max_cash_50pct", "base_model": "volume_heavy", "defensive_model": "low_volatility", "base_size": 10, "defensive_size": 5, "selection_mode": "buy", "cash_cap": 0.50, "regime": True, "opportunity_filter": True},
        {"policy": "D_Always_Top5", "base_model": "volume_heavy", "defensive_model": "low_volatility", "base_size": 5, "defensive_size": 5, "selection_mode": "buy", "cash_cap": None, "regime": True, "opportunity_filter": True},
        {"policy": "E_Always_Top10", "base_model": "volume_heavy", "defensive_model": "low_volatility", "base_size": 10, "defensive_model_override": "low_volatility", "defensive_size": 10, "selection_mode": "buy", "cash_cap": None, "regime": True, "opportunity_filter": True},
        {"policy": "F_Out_of_sample_winner", "base_model": oos_winner[0], "defensive_model": oos_winner[0], "base_size": oos_winner[1], "defensive_size": oos_winner[1], "selection_mode": "buy", "cash_cap": None, "regime": False, "opportunity_filter": True},
        {"policy": "G_Most_robust_model", "base_model": robust[0], "defensive_model": robust[0], "base_size": robust[1], "defensive_size": robust[1], "selection_mode": "buy", "cash_cap": None, "regime": False, "opportunity_filter": True},
        {"policy": "H_Disable_opportunity_filter", "base_model": "volume_heavy", "defensive_model": "low_volatility", "base_size": 10, "defensive_size": 5, "selection_mode": "recommended", "cash_cap": 0.0, "regime": True, "opportunity_filter": False},
        {"policy": "I_Disable_regime_filter", "base_model": "volume_heavy", "defensive_model": "volume_heavy", "base_size": 10, "defensive_size": 10, "selection_mode": "buy", "cash_cap": None, "regime": False, "opportunity_filter": True},
    ]


def _select_for_policy(
    recommendation: pd.DataFrame,
    full_stock_prices: dict[str, pd.DataFrame],
    trading_date: pd.Timestamp,
    selection_mode: str,
    cash_cap: float | None,
) -> tuple[pd.DataFrame, float]:
    if selection_mode == "recommended":
        selected_rows = recommendation[recommendation["recommended"] == True].copy()
    else:
        selected_rows = recommendation[recommendation["action"] == "BUY"].copy()

    active_size = int(recommendation["active_portfolio_size"].iloc[0])
    selected = _selected_positions(
        recommendation.assign(action=["BUY" if symbol in set(selected_rows["symbol"]) else action for symbol, action in zip(recommendation["symbol"], recommendation["action"])]),
        full_stock_prices,
        trading_date,
    )
    original_cash = max(1.0 - (len(selected) / active_size if active_size else 0.0), 0.0)
    cash_weight = min(original_cash, cash_cap) if cash_cap is not None else original_cash

    if not selected.empty:
        invested_weight = 1.0 - cash_weight
        selected["Portfoy Agirligi"] = invested_weight / len(selected)

    return selected, cash_weight


def _evaluate_policy_rows(
    stock_prices: dict[str, pd.DataFrame],
    benchmark_prices: pd.DataFrame,
    results_dir: str,
    factor_models: dict[str, dict[str, float]],
    portfolio_sizes: list[int],
    transaction_cost: float,
    min_buy_expected_return: float,
    opportunity_filter_percentile: float,
    illiquid_avg_traded_value_threshold: float,
    speculative_daily_volatility_threshold: float,
    start_date: str,
    holding_days: int,
) -> pd.DataFrame:
    rows = []
    rankings_by_model_full, factor_breakdown_full = _build_historical_factor_state(
        stock_prices=stock_prices,
        benchmark_prices=benchmark_prices,
        factor_models=factor_models,
        portfolio_sizes=portfolio_sizes,
        transaction_cost=transaction_cost,
        illiquid_avg_traded_value_threshold=illiquid_avg_traded_value_threshold,
        speculative_daily_volatility_threshold=speculative_daily_volatility_threshold,
    )
    if not factor_breakdown_full.empty and "date" in factor_breakdown_full:
        factor_breakdown_full = factor_breakdown_full.copy()
        factor_breakdown_full["date"] = pd.to_datetime(factor_breakdown_full["date"])

    for month_start in _month_starts(start_date, benchmark_prices):
        trading_date = _first_trading_day_on_or_after(benchmark_prices, month_start.strftime("%Y-%m-%d"))
        historical_stocks = _truncate_prices(stock_prices, trading_date)
        historical_benchmark = benchmark_prices.loc[benchmark_prices.index <= trading_date].copy()
        rankings_by_model = {
            model: rankings[pd.to_datetime(rankings["date"]) <= trading_date].copy()
            for model, rankings in rankings_by_model_full.items()
        }
        factor_cutoff = trading_date - pd.Timedelta(days=holding_days)
        factor_breakdown = (
            factor_breakdown_full[factor_breakdown_full["date"] <= factor_cutoff].copy()
            if not factor_breakdown_full.empty and "date" in factor_breakdown_full
            else factor_breakdown_full
        )
        bist100_return = _return_between(
            benchmark_prices,
            trading_date,
            trading_date + pd.Timedelta(days=holding_days),
        ) or 0.0

        for policy in _policy_definitions(results_dir):
            recommendation, _ = generate_current_month_portfolio(
                stock_prices=historical_stocks,
                benchmark_prices=historical_benchmark,
                factor_models=factor_models,
                rankings_by_model=rankings_by_model,
                results_dir=results_dir,
                base_model=str(policy["base_model"]),
                base_portfolio_size=int(policy["base_size"]),
                defensive_model=str(policy["defensive_model"]),
                defensive_portfolio_size=int(policy["defensive_size"]),
                min_buy_expected_return=min_buy_expected_return,
                opportunity_filter_percentile=opportunity_filter_percentile,
                factor_breakdown=factor_breakdown,
                write_outputs=False,
            )
            selected, cash_weight = _select_for_policy(
                recommendation=recommendation,
                full_stock_prices=stock_prices,
                trading_date=trading_date,
                selection_mode=str(policy["selection_mode"]),
                cash_cap=policy["cash_cap"],
            )
            portfolio_return = _portfolio_return(selected, stock_prices, trading_date, holding_days)
            curve = _daily_portfolio_curve(
                selected,
                stock_prices,
                trading_date,
                trading_date + pd.Timedelta(days=holding_days),
                cash_weight,
            )
            first = recommendation.iloc[0]
            rows.append(
                {
                    "policy": policy["policy"],
                    "replay_month": month_start.strftime("%Y-%m"),
                    "actual_trading_date": trading_date.strftime("%Y-%m-%d"),
                    "portfolio_return": portfolio_return,
                    "bist100_return": bist100_return,
                    "excess_return": portfolio_return - bist100_return,
                    "max_drawdown": _max_drawdown(curve),
                    "cash_weight": cash_weight,
                    "selected_model": first["active_model"],
                    "active_portfolio_size": int(first["active_portfolio_size"]),
                    "selected_stock_count": len(selected),
                    "selected_stocks": ", ".join(selected["Hisse"].tolist()) if not selected.empty else "",
                    "regime_state": first["regime_status"],
                    "opportunity_filter_enabled": bool(policy["opportunity_filter"]),
                }
            )
    return pd.DataFrame(rows)


def _policy_summary(policy_results: pd.DataFrame) -> pd.DataFrame:
    rows = []
    for policy, group in policy_results.groupby("policy"):
        group = group.sort_values("actual_trading_date").copy()
        best = group.loc[group["excess_return"].idxmax()]
        worst = group.loc[group["excess_return"].idxmin()]
        strategy_cagr = _compound_cagr(group["portfolio_return"])
        bist100_cagr = _compound_cagr(group["bist100_return"])
        rows.append(
            {
                "policy": policy,
                "months": len(group),
                "cagr": strategy_cagr,
                "bist100_cagr": bist100_cagr,
                "excess_cagr": strategy_cagr - bist100_cagr,
                "win_rate_vs_bist100": float((group["excess_return"] > 0).mean()),
                "max_drawdown": float(group["max_drawdown"].min()),
                "average_cash_weight": float(group["cash_weight"].mean()),
                "worst_month": worst["replay_month"],
                "worst_month_excess": worst["excess_return"],
                "best_month": best["replay_month"],
                "best_month_excess": best["excess_return"],
            }
        )
    return pd.DataFrame(rows).sort_values(["excess_cagr", "win_rate_vs_bist100"], ascending=False)


def _diagnostic_summary(baseline: pd.DataFrame, policy_summary: pd.DataFrame) -> str:
    if baseline.empty:
        return "No baseline rows available."

    cash_corr = baseline["cash_weight"].corr(baseline["excess_return"])
    defensive = baseline[baseline["regime_state"].str.contains("BELOW", na=False)]
    risk_on = baseline[baseline["regime_state"].str.contains("ABOVE", na=False)]
    low_selected = baseline[baseline["selected_stock_count"] <= 3]
    broad_weakness = float((baseline["excess_return"] < 0).mean())
    top_bad = baseline.nsmallest(5, "excess_return")
    bad_contribution = float(top_bad["excess_return"].sum() / baseline.loc[baseline["excess_return"] < 0, "excess_return"].sum())
    best_policy = policy_summary.iloc[0]

    lines = [
        "# Batch Replay Diagnostics",
        "",
        "## Diagnosis",
        "",
        f"- Baseline average cash allocation: {_format_pct(baseline['cash_weight'].mean())}",
        f"- Cash/excess return correlation: {cash_corr:.2f}",
        f"- Negative excess months: {_format_pct(broad_weakness)} of replay months",
        f"- Worst 5 months explain {bad_contribution:.2%} of total negative excess return.",
        f"- Risk ON average excess: {_format_pct(risk_on['excess_return'].mean()) if not risk_on.empty else '-'}",
        f"- Defensive regime average excess: {_format_pct(defensive['excess_return'].mean()) if not defensive.empty else '-'}",
        f"- Months with 3 or fewer selected stocks: {len(low_selected)} / {len(baseline)}",
        "",
        "## Cause Checks",
        "",
        f"- Excessive CASH allocation: {'Yes' if baseline['cash_weight'].mean() > 0.35 and cash_corr < 0 else 'Likely not the only cause'}",
        f"- Wrong model selection: {'Likely' if policy_summary.iloc[0]['policy'] not in {'Baseline', 'C_Max_cash_50pct'} else 'Not clearly proven'}",
        f"- Top3 portfolio size: {'No; baseline is not Top3-only.' if baseline['active_portfolio_size'].median() > 3 else 'Possible'}",
        f"- Opportunity filter: {'Likely' if policy_summary.loc[policy_summary['policy'] == 'H_Disable_opportunity_filter', 'excess_cagr'].iloc[0] > policy_summary.loc[policy_summary['policy'] == 'Baseline', 'excess_cagr'].iloc[0] else 'Not supported'}",
        f"- Regime filter: {'Likely' if policy_summary.loc[policy_summary['policy'] == 'I_Disable_regime_filter', 'excess_cagr'].iloc[0] > policy_summary.loc[policy_summary['policy'] == 'Baseline', 'excess_cagr'].iloc[0] else 'Not supported'}",
        "- Transaction cost: No. Batch replay holding returns do not deduct transaction cost, so transaction cost is not the measured cause here.",
        f"- Few bad months or broad weakness: {'Broad weakness' if broad_weakness >= 0.50 else 'Driven by fewer bad months'}",
        "",
        "## Policy Comparison",
        "",
        policy_summary.to_markdown(index=False, floatfmt=".4f"),
        "",
        "## Best Next Experiment",
        "",
        (
            f"Test `{best_policy['policy']}` as the next controlled experiment, because it has the strongest excess CAGR "
            f"({_format_pct(best_policy['excess_cagr'])}) and win rate ({_format_pct(best_policy['win_rate_vs_bist100'])}) "
            "in this diagnostic replay. Keep it outside production until validated on a longer replay window and with trading costs."
        ),
        "",
    ]
    return "\n".join(lines)


def run_batch_replay_diagnostics(
    stock_prices: dict[str, pd.DataFrame],
    benchmark_prices: pd.DataFrame,
    results_dir: str,
    factor_models: dict[str, dict[str, float]],
    portfolio_sizes: list[int],
    transaction_cost: float,
    min_buy_expected_return: float,
    opportunity_filter_percentile: float,
    illiquid_avg_traded_value_threshold: float,
    speculative_daily_volatility_threshold: float,
    start_date: str = "2024-01-01",
    holding_days: int = 30,
) -> dict[str, object]:
    results_path = Path(results_dir)
    policy_results = _evaluate_policy_rows(
        stock_prices=stock_prices,
        benchmark_prices=benchmark_prices,
        results_dir=results_dir,
        factor_models=factor_models,
        portfolio_sizes=portfolio_sizes,
        transaction_cost=transaction_cost,
        min_buy_expected_return=min_buy_expected_return,
        opportunity_filter_percentile=opportunity_filter_percentile,
        illiquid_avg_traded_value_threshold=illiquid_avg_traded_value_threshold,
        speculative_daily_volatility_threshold=speculative_daily_volatility_threshold,
        start_date=start_date,
        holding_days=holding_days,
    )
    comparison = _policy_summary(policy_results)
    detail_path = results_path / "batch_replay_diagnostics.csv"
    md_path = results_path / "batch_replay_diagnostics.md"
    policy_results.merge(comparison.add_prefix("policy_"), left_on="policy", right_on="policy_policy", how="left").to_csv(detail_path, index=False)
    baseline = policy_results[policy_results["policy"] == "Baseline"].copy()
    md_path.write_text(_diagnostic_summary(baseline, comparison), encoding="utf-8")
    return {
        "policy_results": policy_results,
        "comparison": comparison,
        "diagnostics_path": detail_path,
        "diagnostics_md_path": md_path,
    }


def run_batch_replay(
    stock_prices: dict[str, pd.DataFrame],
    benchmark_prices: pd.DataFrame,
    results_dir: str,
    factor_models: dict[str, dict[str, float]],
    portfolio_sizes: list[int],
    transaction_cost: float,
    min_buy_expected_return: float,
    opportunity_filter_percentile: float,
    illiquid_avg_traded_value_threshold: float,
    speculative_daily_volatility_threshold: float,
    start_date: str = "2024-01-01",
    holding_days: int = 30,
) -> dict[str, object]:
    """Run monthly historical replays from start_date through the latest available month."""
    results_path = Path(results_dir)
    results_path.mkdir(exist_ok=True)
    rows = []
    rankings_by_model_full, factor_breakdown_full = _build_historical_factor_state(
        stock_prices=stock_prices,
        benchmark_prices=benchmark_prices,
        factor_models=factor_models,
        portfolio_sizes=portfolio_sizes,
        transaction_cost=transaction_cost,
        illiquid_avg_traded_value_threshold=illiquid_avg_traded_value_threshold,
        speculative_daily_volatility_threshold=speculative_daily_volatility_threshold,
    )
    if not factor_breakdown_full.empty and "date" in factor_breakdown_full:
        factor_breakdown_full = factor_breakdown_full.copy()
        factor_breakdown_full["date"] = pd.to_datetime(factor_breakdown_full["date"])

    for month_start in _month_starts(start_date, benchmark_prices):
        trading_date = _first_trading_day_on_or_after(benchmark_prices, month_start.strftime("%Y-%m-%d"))
        historical_stocks = _truncate_prices(stock_prices, trading_date)
        historical_benchmark = benchmark_prices.loc[benchmark_prices.index <= trading_date].copy()
        rankings_by_model = {
            model: rankings[pd.to_datetime(rankings["date"]) <= trading_date].copy()
            for model, rankings in rankings_by_model_full.items()
        }
        factor_cutoff = trading_date - pd.Timedelta(days=holding_days)
        factor_breakdown = (
            factor_breakdown_full[factor_breakdown_full["date"] <= factor_cutoff].copy()
            if not factor_breakdown_full.empty and "date" in factor_breakdown_full
            else factor_breakdown_full
        )
        recommendation, _ = generate_current_month_portfolio(
            stock_prices=historical_stocks,
            benchmark_prices=historical_benchmark,
            factor_models=factor_models,
            rankings_by_model=rankings_by_model,
            results_dir=results_dir,
            base_model="volume_heavy",
            base_portfolio_size=10,
            defensive_model="low_volatility",
            defensive_portfolio_size=5,
            min_buy_expected_return=min_buy_expected_return,
            opportunity_filter_percentile=opportunity_filter_percentile,
            factor_breakdown=factor_breakdown,
            write_outputs=False,
        )
        selected = _selected_positions(recommendation, stock_prices, trading_date)
        active_size = int(recommendation["active_portfolio_size"].iloc[0])
        cash_weight = max(1.0 - (len(selected) / active_size if active_size else 0.0), 0.0)
        portfolio_return = _portfolio_return(selected, stock_prices, trading_date, holding_days)
        bist100_return = _return_between(
            benchmark_prices,
            trading_date,
            trading_date + pd.Timedelta(days=holding_days),
        ) or 0.0
        curve = _daily_portfolio_curve(
            selected,
            stock_prices,
            trading_date,
            trading_date + pd.Timedelta(days=holding_days),
            cash_weight,
        )
        first = recommendation.iloc[0]
        rows.append(
            {
                "replay_month": month_start.strftime("%Y-%m"),
                "requested_date": month_start.strftime("%Y-%m-%d"),
                "actual_trading_date": trading_date.strftime("%Y-%m-%d"),
                "holding_days": holding_days,
                "portfolio_return": portfolio_return,
                "bist100_return": bist100_return,
                "excess_return": portfolio_return - bist100_return,
                "max_drawdown": _max_drawdown(curve),
                "cash_weight": cash_weight,
                "selected_model": first["active_model"],
                "active_portfolio_size": active_size,
                "selected_stock_count": len(selected),
                "selected_stocks": ", ".join(selected["Hisse"].tolist()) if not selected.empty else "",
                "regime_state": first["regime_status"],
                "bist100_below_ma200": bool(first["bist100_below_ma200"]),
                "opportunity_threshold": first["opportunity_threshold"],
                "confidence_score": first["confidence_score"],
            }
        )

    results = pd.DataFrame(rows)
    results_path.joinpath("batch_replay_results.csv").write_text(results.to_csv(index=False), encoding="utf-8")

    summary_md = _summary_markdown(results, start_date)
    summary_path = results_path / "batch_replay_summary.md"
    summary_path.write_text(summary_md, encoding="utf-8")

    if not results.empty:
        _plot_equity_curve(results, results_path / "batch_replay_equity_curve.png")
        _plot_excess_heatmap(results, results_path / "batch_replay_heatmap.png")

    return {
        "results": results,
        "results_path": results_path / "batch_replay_results.csv",
        "summary_path": summary_path,
        "equity_curve_path": results_path / "batch_replay_equity_curve.png",
        "heatmap_path": results_path / "batch_replay_heatmap.png",
        "strategy_cagr": _compound_cagr(results["portfolio_return"]) if not results.empty else 0.0,
        "bist100_cagr": _compound_cagr(results["bist100_return"]) if not results.empty else 0.0,
    }
