from pathlib import Path

import pandas as pd

from src.reporting import summarize_returns, selection_score


def _benchmark_for_dates(benchmark_monthly: pd.Series | None, dates: pd.Series) -> pd.Series:
    if benchmark_monthly is None or benchmark_monthly.empty:
        return pd.Series(dtype=float)

    benchmark = benchmark_monthly.copy()
    benchmark.index = pd.to_datetime(benchmark.index)
    return benchmark.reindex(pd.to_datetime(dates)).dropna()


def _estimate_expected_return(history: pd.DataFrame, row: pd.Series, min_rows: int = 5) -> float:
    if history.empty:
        return 0.0

    symbol_history = history[
        (history["symbol"] == row["symbol"])
        & (history["score"].between(row["score"] - 0.05, row["score"] + 0.05))
    ]
    if len(symbol_history) >= min_rows:
        returns = symbol_history["next_month_return"].dropna()
        return float(returns.median()) if not returns.empty else 0.0

    model_history = history[history["score"].between(row["score"] - 0.05, row["score"] + 0.05)]
    if len(model_history) >= min_rows:
        returns = model_history["next_month_return"].dropna()
        return float(returns.median()) if not returns.empty else 0.0

    returns = history["next_month_return"].dropna()
    return float(returns.median()) if not returns.empty else 0.0


def _period_for_date(date: pd.Timestamp, periods: dict[str, tuple[str, str]]) -> str | None:
    for period_name, (start, end) in periods.items():
        if pd.Timestamp(start) <= date <= pd.Timestamp(end):
            return period_name
    return None


def _summarize_cash_strategy(
    results: pd.DataFrame,
    benchmark_monthly: pd.Series | None,
) -> pd.DataFrame:
    rows = []
    if results.empty:
        return pd.DataFrame()

    for (threshold, period), group in results.groupby(["threshold", "period"], dropna=False):
        group = group.sort_values("date")
        strategy_stats = summarize_returns(group["net_return"])
        benchmark_returns = _benchmark_for_dates(benchmark_monthly, group["date"])
        benchmark_stats = summarize_returns(benchmark_returns)
        excess = strategy_stats["total_return"] - benchmark_stats["total_return"]
        rows.append(
            {
                "threshold": threshold,
                "period": period,
                "months": len(group),
                "avg_cash_weight": group["cash_weight"].mean(),
                "avg_qualified_count": group["qualified_count"].mean(),
                "selection_score": selection_score(
                    excess,
                    strategy_stats["max_drawdown"],
                    strategy_stats["win_rate"],
                ),
                "strategy_total_return": strategy_stats["total_return"],
                "bist100_total_return": benchmark_stats["total_return"],
                "excess_return_over_benchmark": excess,
                "strategy_max_drawdown": strategy_stats["max_drawdown"],
                "bist100_max_drawdown": benchmark_stats["max_drawdown"],
                "win_rate": strategy_stats["win_rate"],
            }
        )

    return pd.DataFrame(rows).sort_values(["threshold", "period"])


def evaluate_cash_thresholds(
    factor_breakdown: pd.DataFrame,
    model: str,
    portfolio_size: int,
    transaction_cost: float,
    thresholds: list[float],
    periods: dict[str, tuple[str, str]],
    benchmark_monthly: pd.Series | None,
) -> tuple[pd.DataFrame, pd.DataFrame]:
    data = factor_breakdown[
        (factor_breakdown["model"] == model)
        & (factor_breakdown["portfolio_size"] == portfolio_size)
    ].copy()
    if data.empty:
        return pd.DataFrame(), pd.DataFrame()

    data["date"] = pd.to_datetime(data["date"])
    data = data.sort_values(["date", "rank"])
    rows = []

    for threshold in thresholds:
        for date, group in data.groupby("date"):
            period = _period_for_date(pd.Timestamp(date), periods)
            if period is None:
                continue

            prior = data[data["date"] < date]
            scored = group.copy()
            scored["estimated_expected_return"] = [
                _estimate_expected_return(prior, row)
                for _, row in scored.iterrows()
            ]
            qualified = scored[scored["estimated_expected_return"] >= threshold].copy()
            qualified_count = len(qualified)
            invested_weight = qualified_count / portfolio_size if portfolio_size else 0.0
            cash_weight = 1.0 - invested_weight

            gross_return = qualified["next_month_return"].sum() / portfolio_size if portfolio_size else 0.0
            net_return = gross_return - (transaction_cost * invested_weight)
            rows.append(
                {
                    "threshold": threshold,
                    "date": date,
                    "period": period,
                    "model": model,
                    "portfolio_size": portfolio_size,
                    "qualified_count": qualified_count,
                    "cash_weight": cash_weight,
                    "invested_weight": invested_weight,
                    "gross_return": gross_return,
                    "transaction_cost": transaction_cost * invested_weight,
                    "net_return": net_return,
                    "avg_estimated_expected_return": qualified["estimated_expected_return"].mean()
                    if qualified_count
                    else 0.0,
                }
            )

    monthly = pd.DataFrame(rows)
    summary = _summarize_cash_strategy(monthly, benchmark_monthly)
    return summary, monthly


def _baseline_rows(summary: pd.DataFrame, model: str, portfolio_size: int) -> pd.DataFrame:
    baseline = summary[
        (summary["model"] == model)
        & (summary["portfolio_size"] == portfolio_size)
        & (summary["period"].isin(["validation", "out_of_sample"]))
    ].copy()
    baseline["threshold"] = "baseline_full_invested"
    baseline["avg_cash_weight"] = 0.0
    baseline["avg_qualified_count"] = portfolio_size
    return baseline[
        [
            "threshold",
            "period",
            "months",
            "avg_cash_weight",
            "avg_qualified_count",
            "selection_score",
            "strategy_total_return",
            "bist100_total_return",
            "excess_return_over_benchmark",
            "strategy_max_drawdown",
            "bist100_max_drawdown",
            "win_rate",
        ]
    ]


def build_cash_allocation_reports(
    results_dir: str,
    summary: pd.DataFrame,
    benchmark_monthly: pd.Series | None,
    periods: dict[str, tuple[str, str]],
    transaction_cost: float,
    thresholds: list[float],
) -> tuple[pd.DataFrame, str, float | None]:
    results_path = Path(results_dir)
    best_model = pd.read_csv(results_path / "best_model.csv")
    factor_breakdown = pd.read_csv(results_path / "factor_breakdown.csv")

    if best_model.empty:
        comparison = pd.DataFrame()
        report = "# Cash Allocation Report\n\nNo best model is available.\n"
        return comparison, report, None

    best = best_model.iloc[0]
    model = str(best["model"])
    portfolio_size = int(best["portfolio_size"])
    cash_summary, _ = evaluate_cash_thresholds(
        factor_breakdown=factor_breakdown,
        model=model,
        portfolio_size=portfolio_size,
        transaction_cost=transaction_cost,
        thresholds=thresholds,
        periods=periods,
        benchmark_monthly=benchmark_monthly,
    )
    baseline = _baseline_rows(summary, model, portfolio_size)
    comparison = pd.concat([baseline, cash_summary], ignore_index=True)
    comparison_path = results_path / "cash_allocation_comparison.csv"
    comparison.to_csv(comparison_path, index=False)

    baseline_oos = baseline[baseline["period"] == "out_of_sample"].head(1)
    candidates = cash_summary[cash_summary["period"] == "out_of_sample"].copy()
    selected_threshold = None
    accepted = False
    reason = "No out-of-sample cash-allocation rows were generated."
    if not baseline_oos.empty and not candidates.empty:
        base = baseline_oos.iloc[0]
        candidates["drawdown_improvement"] = (
            candidates["strategy_max_drawdown"] - float(base["strategy_max_drawdown"])
        )
        candidates["score_improvement"] = candidates["selection_score"] - float(base["selection_score"])
        candidates["excess_improvement"] = (
            candidates["excess_return_over_benchmark"] - float(base["excess_return_over_benchmark"])
        )
        accepted_candidates = candidates[
            (candidates["excess_improvement"] > 0)
            | (candidates["drawdown_improvement"] > 0.03)
            | (candidates["score_improvement"] > 0)
        ].copy()
        if not accepted_candidates.empty:
            selected = accepted_candidates.sort_values(
                ["score_improvement", "drawdown_improvement", "excess_improvement"],
                ascending=False,
            ).iloc[0]
            selected_threshold = float(selected["threshold"])
            accepted = True
            reason = (
                "Accepted because the selected threshold improved out-of-sample "
                "risk-adjusted selection score or drawdown versus the full-invested baseline."
            )
        else:
            selected = candidates.sort_values("selection_score", ascending=False).iloc[0]
            selected_threshold = float(selected["threshold"])
            reason = "Rejected because no tested threshold improved out-of-sample excess return, drawdown, or risk-adjusted score."

    report_lines = [
        "# Cash Allocation Report",
        "",
        "## Experiment",
        "",
        f"- Baseline model: {model} Top{portfolio_size}",
        "- Baseline behavior: force all portfolio slots into stocks.",
        "- Cash behavior: each stock must meet the threshold; failed slots remain in CASH.",
        f"- Thresholds tested: {', '.join(f'{threshold:.0%}' for threshold in thresholds)}",
        f"- Selected threshold: {selected_threshold:.0%}" if selected_threshold is not None else "- Selected threshold: n/a",
        f"- Decision: {'accepted' if accepted else 'rejected'}",
        f"- Reason: {reason}",
        "",
        "## Comparison",
        "",
        comparison.to_markdown(index=False, floatfmt=".4f") if not comparison.empty else "No comparison generated.",
        "",
    ]
    report = "\n".join(report_lines)
    (results_path / "cash_allocation_report.md").write_text(report, encoding="utf-8")
    return comparison, report, selected_threshold if accepted else None
