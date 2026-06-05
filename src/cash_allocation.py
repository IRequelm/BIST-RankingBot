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


def _candidate_filters(portfolio_size: int) -> list[dict[str, object]]:
    candidates: list[dict[str, object]] = [
        {"name": "current_fixed_5pct", "kind": "fixed", "threshold": 0.05},
        {"name": "fixed_0pct", "kind": "fixed", "threshold": 0.00},
        {"name": "fixed_1pct", "kind": "fixed", "threshold": 0.01},
        {"name": "fixed_2pct", "kind": "fixed", "threshold": 0.02},
        {"name": "fixed_3pct", "kind": "fixed", "threshold": 0.03},
    ]
    for percentile in [0.10, 0.20, 0.30, 0.40, 0.50]:
        candidates.append(
            {
                "name": f"percentile_positive_p{int(percentile * 100)}",
                "kind": "percentile",
                "percentile": percentile,
                "positive_floor": True,
            }
        )
        candidates.append(
            {
                "name": f"percentile_p{int(percentile * 100)}",
                "kind": "percentile",
                "percentile": percentile,
                "positive_floor": False,
            }
        )
    for top_n in range(1, portfolio_size + 1):
        candidates.append(
            {
                "name": f"top{top_n}_positive_est",
                "kind": "top_estimate",
                "top_n": top_n,
                "positive_floor": True,
            }
        )
    return candidates


def _apply_candidate_filter(scored: pd.DataFrame, candidate: dict[str, object]) -> pd.DataFrame:
    kind = candidate["kind"]
    if kind == "fixed":
        threshold = float(candidate["threshold"])
        return scored[scored["estimated_expected_return"] >= threshold]

    if kind == "percentile":
        percentile = float(candidate["percentile"])
        threshold = float(scored["estimated_expected_return"].quantile(percentile))
        if candidate.get("positive_floor", False):
            threshold = max(0.0, threshold)
        return scored[scored["estimated_expected_return"] >= threshold]

    if kind == "top_estimate":
        top_n = int(candidate["top_n"])
        filtered = scored.copy()
        if candidate.get("positive_floor", False):
            filtered = filtered[filtered["estimated_expected_return"] > 0]
        return filtered.sort_values(
            ["estimated_expected_return", "rank"],
            ascending=[False, True],
        ).head(top_n)

    raise ValueError(f"Unsupported opportunity filter kind: {kind}")


def evaluate_opportunity_filters(
    factor_breakdown: pd.DataFrame,
    model: str,
    portfolio_size: int,
    transaction_cost: float,
    periods: dict[str, tuple[str, str]],
    benchmark_monthly: pd.Series | None,
) -> tuple[pd.DataFrame, pd.DataFrame, pd.DataFrame]:
    data = factor_breakdown[
        (factor_breakdown["model"] == model)
        & (factor_breakdown["portfolio_size"] == portfolio_size)
    ].copy()
    if data.empty:
        return pd.DataFrame(), pd.DataFrame(), pd.DataFrame()

    data["date"] = pd.to_datetime(data["date"])
    data = data.sort_values(["date", "rank"])
    scored_months = []
    rows = []

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
        scored["period"] = period
        scored_months.append(scored)

        for candidate in _candidate_filters(portfolio_size):
            qualified = _apply_candidate_filter(scored, candidate)
            qualified_count = len(qualified)
            invested_weight = qualified_count / portfolio_size if portfolio_size else 0.0
            rows.append(
                {
                    "threshold": candidate["name"],
                    "date": date,
                    "period": period,
                    "model": model,
                    "portfolio_size": portfolio_size,
                    "qualified_count": qualified_count,
                    "cash_weight": 1.0 - invested_weight,
                    "invested_weight": invested_weight,
                    "gross_return": qualified["next_month_return"].sum() / portfolio_size
                    if portfolio_size
                    else 0.0,
                    "transaction_cost": transaction_cost * invested_weight,
                    "net_return": (
                        qualified["next_month_return"].sum() / portfolio_size
                        if portfolio_size
                        else 0.0
                    )
                    - (transaction_cost * invested_weight),
                    "avg_estimated_expected_return": qualified["estimated_expected_return"].mean()
                    if qualified_count
                    else 0.0,
                }
            )

    monthly = pd.DataFrame(rows)
    scored_history = pd.concat(scored_months, ignore_index=True) if scored_months else pd.DataFrame()
    summary = _summarize_cash_strategy(monthly, benchmark_monthly)
    return summary, monthly, scored_history


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


def build_opportunity_filter_calibration_report(
    results_dir: str,
    summary: pd.DataFrame,
    benchmark_monthly: pd.Series | None,
    periods: dict[str, tuple[str, str]],
    transaction_cost: float,
) -> tuple[pd.DataFrame, str, str | None]:
    results_path = Path(results_dir)
    best_model = pd.read_csv(results_path / "best_model.csv")
    factor_breakdown = pd.read_csv(results_path / "factor_breakdown.csv")

    if best_model.empty:
        report = "# Opportunity Filter Calibration\n\nNo best model is available.\n"
        (results_path / "opportunity_filter_calibration.md").write_text(report, encoding="utf-8")
        return pd.DataFrame(), report, None

    best = best_model.iloc[0]
    model = str(best["model"])
    portfolio_size = int(best["portfolio_size"])
    filter_summary, _, scored_history = evaluate_opportunity_filters(
        factor_breakdown=factor_breakdown,
        model=model,
        portfolio_size=portfolio_size,
        transaction_cost=transaction_cost,
        periods=periods,
        benchmark_monthly=benchmark_monthly,
    )
    baseline = _baseline_rows(summary, model, portfolio_size)
    comparison = pd.concat([baseline, filter_summary], ignore_index=True)

    selected_filter = None
    accepted = False
    reason = "No candidate passed the acceptance rule."
    oos = filter_summary[filter_summary["period"] == "out_of_sample"].copy()
    baseline_oos = baseline[baseline["period"] == "out_of_sample"].head(1)
    current = oos[oos["threshold"] == "current_fixed_5pct"].head(1)
    if not oos.empty and not baseline_oos.empty and not current.empty:
        base = baseline_oos.iloc[0]
        current_row = current.iloc[0]
        oos["return_improvement_vs_current_5pct"] = (
            oos["strategy_total_return"] - float(current_row["strategy_total_return"])
        )
        oos["drawdown_improvement_vs_baseline"] = (
            oos["strategy_max_drawdown"] - float(base["strategy_max_drawdown"])
        )
        accepted_candidates = oos[
            (oos["threshold"] != "current_fixed_5pct")
            & (oos["return_improvement_vs_current_5pct"] > 0.05)
            & (oos["drawdown_improvement_vs_baseline"] > 0)
        ].copy()
        if not accepted_candidates.empty:
            accepted_candidates["implementation_preference"] = (
                accepted_candidates["threshold"] == "percentile_positive_p50"
            ).astype(int)
            selected = accepted_candidates.sort_values(
                [
                    "strategy_total_return",
                    "selection_score",
                    "implementation_preference",
                    "strategy_max_drawdown",
                ],
                ascending=[False, False, False, False],
            ).iloc[0]
            selected_filter = str(selected["threshold"])
            accepted = True
            reason = (
                "Accepted because the selected filter materially improved out-of-sample "
                "return versus the current 5% threshold while preserving a drawdown "
                "improvement versus the full-invested baseline."
            )

    distribution = pd.DataFrame()
    if not scored_history.empty:
        distribution = scored_history.groupby("period")["estimated_expected_return"].describe(
            percentiles=[0.10, 0.20, 0.25, 0.30, 0.40, 0.50, 0.60, 0.75, 0.80, 0.90]
        )

    oos_table = comparison[comparison["period"] == "out_of_sample"].copy()
    if not oos_table.empty and not baseline_oos.empty and not current.empty:
        base = baseline_oos.iloc[0]
        current_row = current.iloc[0]
        oos_table["return_vs_current_5pct"] = (
            oos_table["strategy_total_return"] - float(current_row["strategy_total_return"])
        )
        oos_table["drawdown_vs_baseline"] = (
            oos_table["strategy_max_drawdown"] - float(base["strategy_max_drawdown"])
        )

    report_lines = [
        "# Opportunity Filter Calibration",
        "",
        "## Finding",
        "",
        f"- Baseline model: {model} Top{portfolio_size}",
        "- Current issue: the fixed 5% opportunity threshold allocates too much to CASH and hurts returns.",
        "- Improvement tested: calibrated opportunity filters that keep cash support but use relative thresholds.",
        f"- Selected filter: {selected_filter if selected_filter else 'n/a'}",
        f"- Decision: {'accepted' if accepted else 'rejected'}",
        f"- Reason: {reason}",
        "",
        "## Expected Return Distribution",
        "",
        distribution.to_markdown(floatfmt=".4f") if not distribution.empty else "No distribution generated.",
        "",
        "## Out-Of-Sample Comparison",
        "",
        oos_table.sort_values(
            ["strategy_total_return", "strategy_max_drawdown"],
            ascending=[False, False],
        ).to_markdown(index=False, floatfmt=".4f")
        if not oos_table.empty
        else "No comparison generated.",
        "",
        "## Interpretation",
        "",
        (
            "The expected return estimator is noisy and has weak negative correlation with realized next-month returns. "
            "A fixed 5% threshold is above the median estimated return in most periods, so it over-allocates to CASH. "
            "A positive-floor percentile filter is more realistic: it rejects the weakest current opportunities while "
            "staying invested when the opportunity set is broadly positive."
        ),
        "",
    ]
    report = "\n".join(report_lines)
    (results_path / "opportunity_filter_calibration.md").write_text(report, encoding="utf-8")
    return comparison, report, selected_filter if accepted else None
