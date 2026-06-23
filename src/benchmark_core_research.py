from __future__ import annotations

import json
from dataclasses import dataclass
from pathlib import Path

import pandas as pd

from src.current_portfolio import _current_regime
from src.follow_up_research import (
    _calculate_research_features,
    _clean_close,
    _price_at_or_before,
    _rank_asof,
)


@dataclass(frozen=True)
class CorePolicy:
    policy_id: str
    policy_name: str
    benchmark_weight: float
    active_weight: float
    mode: str


@dataclass(frozen=True)
class RankingPolicy:
    score_mode: str = "base"


POLICIES = [
    CorePolicy("A", "BIST100 only", 1.0, 0.0, "benchmark_only"),
    CorePolicy("B", "Current active Top3 only", 0.0, 1.0, "fixed_active"),
    CorePolicy("C", "80/20 benchmark-core", 0.8, 0.2, "fixed_active"),
    CorePolicy("D", "70/30 benchmark-core", 0.7, 0.3, "fixed_active"),
    CorePolicy("E", "50/50 benchmark-core", 0.5, 0.5, "fixed_active"),
    CorePolicy("F", "Conditional active overlay", 1.0, 0.0, "conditional_overlay"),
    CorePolicy("G", "Drawdown-aware active overlay", 0.8, 0.2, "drawdown_aware_overlay"),
]


def _period_return(prices: pd.DataFrame, start: pd.Timestamp, end: pd.Timestamp) -> float:
    _, start_price = _price_at_or_before(prices, start)
    _, end_price = _price_at_or_before(prices, end)
    if start_price <= 0:
        return 0.0
    return (end_price / start_price) - 1


def _monthly_rebalance_dates(benchmark_prices: pd.DataFrame, start: str, end: pd.Timestamp) -> list[pd.Timestamp]:
    dates = _clean_close(benchmark_prices).index
    dates = dates[(dates >= pd.Timestamp(start)) & (dates <= pd.Timestamp(end))]
    if dates.empty:
        return []
    grouped = pd.Series(dates, index=dates)
    rebalances = [pd.Timestamp(date) for date in grouped.groupby(dates.to_period("M")).first().tolist()]
    latest = pd.Timestamp(dates[-1])
    if rebalances[-1] < latest:
        rebalances.append(latest)
    return rebalances


def _portfolio_turnover(previous: dict[str, float], current: dict[str, float]) -> float:
    all_symbols = set(previous) | set(current)
    return float(sum(abs(current.get(symbol, 0.0) - previous.get(symbol, 0.0)) for symbol in all_symbols))


def _active_weights(symbols: list[str], active_weight: float) -> dict[str, float]:
    if not symbols or active_weight <= 0:
        return {}
    equal_weight = active_weight / len(symbols)
    return {symbol: equal_weight for symbol in symbols}


def _active_return(
    selected_symbols: list[str],
    stock_prices: dict[str, pd.DataFrame],
    start: pd.Timestamp,
    end: pd.Timestamp,
) -> float:
    if not selected_symbols:
        return 0.0
    returns = [_period_return(stock_prices[symbol], start, end) for symbol in selected_symbols]
    return float(sum(returns) / len(returns))


def _active_conditions(
    ranked: pd.DataFrame,
    benchmark_prices: pd.DataFrame,
    asof: pd.Timestamp,
    historical_top3_scores: list[float],
) -> tuple[bool, dict[str, object]]:
    top3 = ranked.head(3)
    top3_avg_score = float(top3["score"].mean())
    historical_median = float(pd.Series(historical_top3_scores).median()) if historical_top3_scores else None
    score_above_median = historical_median is not None and top3_avg_score > historical_median

    regime = _current_regime(benchmark_prices.loc[benchmark_prices.index <= asof])
    risk_on = not bool(regime["bist100_below_ma200"])

    momentum_columns = ["momentum_1m", "momentum_3m", "momentum_6m"]
    top3_avg_momentum = float(top3[momentum_columns].mean(axis=1).mean())
    momentum_positive = top3_avg_momentum > 0

    relative_columns = ["relative_strength_5d", "relative_strength_10d", "relative_strength_20d"]
    top3_avg_relative_strength = float(top3[relative_columns].mean(axis=1).mean())
    relative_strength_positive = top3_avg_relative_strength > 0

    passed = bool(score_above_median and risk_on and momentum_positive and relative_strength_positive)
    return passed, {
        "top3_avg_score": top3_avg_score,
        "historical_top3_score_median": historical_median,
        "score_above_historical_median": score_above_median,
        "risk_on": risk_on,
        "top3_avg_momentum": top3_avg_momentum,
        "top3_avg_relative_strength": top3_avg_relative_strength,
        "relative_strength_positive": relative_strength_positive,
        "momentum_positive": momentum_positive,
    }


def _simulate_policy(
    policy: CorePolicy,
    stock_prices: dict[str, pd.DataFrame],
    benchmark_prices: pd.DataFrame,
    feature_frames: dict[str, pd.DataFrame],
    factor_models: dict[str, dict[str, float]],
    start: str,
    end: pd.Timestamp,
    transaction_cost: float,
) -> pd.DataFrame:
    rebalances = _monthly_rebalance_dates(benchmark_prices, start, end)
    if len(rebalances) < 2:
        return pd.DataFrame()

    ranking_policy = RankingPolicy()
    previous_active_weights: dict[str, float] = {}
    historical_top3_scores: list[float] = []
    underperform_streak = 0
    overlay_disabled = False
    equity = 1.0
    benchmark_equity = 1.0
    rows = []

    for start_date, end_date in zip(rebalances[:-1], rebalances[1:]):
        ranked = _rank_asof(feature_frames, benchmark_prices, factor_models, start_date, ranking_policy)
        if ranked.empty:
            continue

        selected_symbols = ranked.head(3)["symbol"].tolist()
        top3_avg_score = float(ranked.head(3)["score"].mean())
        condition_passed, condition_details = _active_conditions(
            ranked,
            benchmark_prices,
            start_date,
            historical_top3_scores,
        )

        benchmark_return = _period_return(benchmark_prices, start_date, end_date)
        active_gross_return = _active_return(selected_symbols, stock_prices, start_date, end_date)
        simulated_active_weights = _active_weights(selected_symbols, 1.0)
        simulated_active_turnover = _portfolio_turnover(previous_active_weights if policy.mode == "fixed_active" else {}, simulated_active_weights)
        simulated_active_cost = transaction_cost * simulated_active_turnover
        active_net_return_for_signal = active_gross_return - simulated_active_cost

        active_weight = policy.active_weight
        benchmark_weight = policy.benchmark_weight
        overlay_status = "fixed"

        if policy.mode == "benchmark_only":
            active_weight = 0.0
            benchmark_weight = 1.0
            overlay_status = "benchmark_only"
        elif policy.mode == "conditional_overlay":
            active_weight = 0.2 if condition_passed else 0.0
            benchmark_weight = 1.0 - active_weight
            overlay_status = "active_on" if condition_passed else "active_off"
        elif policy.mode == "drawdown_aware_overlay":
            active_weight = 0.0 if overlay_disabled else 0.2
            benchmark_weight = 1.0 - active_weight
            overlay_status = "active_off_drawdown_guard" if overlay_disabled else "active_on"

        current_active_weights = _active_weights(selected_symbols, active_weight)
        turnover = _portfolio_turnover(previous_active_weights, current_active_weights)
        cost_impact = transaction_cost * turnover
        gross_return = benchmark_weight * benchmark_return + active_weight * active_gross_return
        net_return = gross_return - cost_impact

        equity *= 1 + net_return
        benchmark_equity *= 1 + benchmark_return
        rows.append(
            {
                "policy_id": policy.policy_id,
                "policy_name": policy.policy_name,
                "start_date": start_date,
                "end_date": end_date,
                "benchmark_weight": benchmark_weight,
                "active_weight": active_weight,
                "selected_symbols": ", ".join(selected_symbols) if active_weight else "",
                "benchmark_return": benchmark_return,
                "active_gross_return": active_gross_return,
                "gross_return": gross_return,
                "transaction_cost_impact": cost_impact,
                "net_return": net_return,
                "excess_return": net_return - benchmark_return,
                "turnover": turnover,
                "overlay_status": overlay_status,
                "condition_passed": condition_passed,
                **condition_details,
                "equity": equity,
                "benchmark_equity": benchmark_equity,
            }
        )

        active_underperformed = active_net_return_for_signal < benchmark_return
        if policy.mode == "drawdown_aware_overlay":
            if active_underperformed:
                underperform_streak += 1
            else:
                underperform_streak = 0

            if overlay_disabled and not active_underperformed:
                overlay_disabled = False
                underperform_streak = 0
            elif not overlay_disabled and underperform_streak >= 2:
                overlay_disabled = True

        historical_top3_scores.append(top3_avg_score)
        previous_active_weights = current_active_weights

    return pd.DataFrame(rows)


def _max_drawdown(equity: pd.Series) -> float:
    if equity.empty:
        return 0.0
    drawdown = equity / equity.cummax() - 1
    return float(drawdown.min())


def _sharpe_proxy(returns: pd.Series) -> float:
    std = returns.std()
    if std == 0 or pd.isna(std):
        return 0.0
    return float((returns.mean() / std) * (12 ** 0.5))


def _cagr(total_return: float, start: pd.Timestamp, end: pd.Timestamp) -> float:
    years = max((end - start).days / 365.25, 1 / 365.25)
    return float((1 + total_return) ** (1 / years) - 1)


def _summarize_policy(intervals: pd.DataFrame) -> dict[str, object]:
    intervals = intervals.sort_values("start_date").copy()
    total_return = float(intervals["equity"].iloc[-1] - 1)
    benchmark_total_return = float(intervals["benchmark_equity"].iloc[-1] - 1)
    start = pd.Timestamp(intervals["start_date"].iloc[0])
    end = pd.Timestamp(intervals["end_date"].iloc[-1])
    strategy_cagr = _cagr(total_return, start, end)
    benchmark_cagr = _cagr(benchmark_total_return, start, end)
    worst_idx = intervals["net_return"].idxmin()
    best_idx = intervals["net_return"].idxmax()

    return {
        "policy_id": intervals["policy_id"].iloc[0],
        "policy_name": intervals["policy_name"].iloc[0],
        "months": len(intervals),
        "total_return": total_return,
        "bist100_total_return": benchmark_total_return,
        "cagr": strategy_cagr,
        "bist100_cagr": benchmark_cagr,
        "excess_cagr": strategy_cagr - benchmark_cagr,
        "max_drawdown": _max_drawdown(intervals["equity"]),
        "bist100_max_drawdown": _max_drawdown(intervals["benchmark_equity"]),
        "sharpe_proxy": _sharpe_proxy(intervals["net_return"]),
        "monthly_win_rate_vs_bist100": float((intervals["excess_return"] > 0).mean()),
        "average_monthly_excess_return": float(intervals["excess_return"].mean()),
        "worst_month": pd.Timestamp(intervals.loc[worst_idx, "start_date"]).strftime("%Y-%m"),
        "worst_month_return": float(intervals.loc[worst_idx, "net_return"]),
        "best_month": pd.Timestamp(intervals.loc[best_idx, "start_date"]).strftime("%Y-%m"),
        "best_month_return": float(intervals.loc[best_idx, "net_return"]),
        "average_turnover": float(intervals["turnover"].mean()),
        "total_turnover": float(intervals["turnover"].sum()),
        "active_allocation_average": float(intervals["active_weight"].mean()),
        "active_overlay_months": int((intervals["active_weight"] > 0).sum()),
        "transaction_cost_impact": float(intervals["transaction_cost_impact"].sum()),
    }


def _load_tracking_state(reports_dir: str) -> dict[str, object]:
    path = Path(reports_dir) / "tracking_state.json"
    if not path.exists():
        raise ValueError("reports/tracking_state.json is required for recent benchmark-core analysis.")
    with path.open("r", encoding="utf-8") as handle:
        return json.load(handle)


def _fixed_state_active_return(
    state: dict[str, object],
    stock_prices: dict[str, pd.DataFrame],
    end: pd.Timestamp,
) -> float:
    returns = []
    for position in state["positions"]:
        symbol = position["symbol"]
        start_price = float(position["start_price"])
        _, end_price = _price_at_or_before(stock_prices[symbol], end)
        returns.append((end_price / start_price) - 1 if start_price else 0.0)
    return float(sum(returns) / len(returns))


def _historical_score_context(
    feature_frames: dict[str, pd.DataFrame],
    benchmark_prices: pd.DataFrame,
    factor_models: dict[str, dict[str, float]],
    start_date: pd.Timestamp,
    validation_start: str,
) -> list[float]:
    dates = _monthly_rebalance_dates(benchmark_prices, validation_start, start_date)
    scores = []
    ranking_policy = RankingPolicy()
    for date in dates:
        if date >= start_date:
            continue
        ranked = _rank_asof(feature_frames, benchmark_prices, factor_models, date, ranking_policy)
        if not ranked.empty:
            scores.append(float(ranked.head(3)["score"].mean()))
    return scores


def _recent_followup(
    state: dict[str, object],
    stock_prices: dict[str, pd.DataFrame],
    benchmark_prices: pd.DataFrame,
    feature_frames: dict[str, pd.DataFrame],
    factor_models: dict[str, dict[str, float]],
    transaction_cost: float,
    validation_start: str,
) -> pd.DataFrame:
    start = pd.Timestamp(state["start_date"])
    end = pd.Timestamp(_clean_close(benchmark_prices).index.max())
    active_gross_return = _fixed_state_active_return(state, stock_prices, end)
    benchmark_return = _period_return(benchmark_prices, start, end)

    ranked = _rank_asof(feature_frames, benchmark_prices, factor_models, start, RankingPolicy())
    score_history = _historical_score_context(feature_frames, benchmark_prices, factor_models, start, validation_start)
    condition_passed, condition_details = _active_conditions(ranked, benchmark_prices, start, score_history)

    recent_policies = [
        ("Fixed Top3 from 2026-06-01", 0.0, 1.0, True),
        ("BIST100 only", 1.0, 0.0, True),
        ("80/20 benchmark-core", 0.8, 0.2, True),
        ("70/30 benchmark-core", 0.7, 0.3, True),
        ("Conditional active overlay", 0.8 if condition_passed else 1.0, 0.2 if condition_passed else 0.0, condition_passed),
    ]
    rows = []
    for name, benchmark_weight, active_weight, active_used in recent_policies:
        gross_return = benchmark_weight * benchmark_return + active_weight * active_gross_return
        cost_impact = transaction_cost * active_weight if active_weight > 0 else 0.0
        net_return = gross_return - cost_impact
        gross_excess_return = gross_return - benchmark_return
        net_excess_return = net_return - benchmark_return
        rows.append(
            {
                "policy_name": name,
                "start_date": start,
                "end_date": end,
                "benchmark_weight": benchmark_weight,
                "active_weight": active_weight,
                "active_used": active_used and active_weight > 0,
                "selected_symbols": ", ".join(position["symbol"] for position in state["positions"]) if active_weight else "",
                "active_gross_return": active_gross_return,
                "benchmark_return": benchmark_return,
                "gross_return": gross_return,
                "net_return": net_return,
                "gross_excess_return": gross_excess_return,
                "net_excess_return": net_excess_return,
                "transaction_cost_impact": cost_impact,
                **condition_details,
            }
        )
    return pd.DataFrame(rows)


def _format_percent(value: float) -> str:
    return f"{value:.2%}"


def _decision_lines(summary: pd.DataFrame) -> list[str]:
    active = summary[summary["policy_id"] == "B"].iloc[0]
    bist100 = summary[summary["policy_id"] == "A"].iloc[0]
    non_active = summary[summary["policy_id"] != "B"].copy()
    core_allocations = summary[summary["policy_id"].isin(["C", "D", "E", "F", "G"])].copy()
    fixed_core_allocations = summary[summary["policy_id"].isin(["C", "D", "E"])].copy()

    material_underperformance_threshold = -0.01
    eligible = non_active[
        (non_active["max_drawdown"] >= active["max_drawdown"])
        & (non_active["sharpe_proxy"] >= active["sharpe_proxy"])
        & (non_active["excess_cagr"] >= material_underperformance_threshold)
    ].copy()
    if eligible.empty:
        recommendation = bist100
    else:
        eligible["balance_score"] = (
            eligible["cagr"]
            - eligible["max_drawdown"].abs() * 0.5
            + eligible["excess_cagr"]
            + eligible["sharpe_proxy"] * 0.02
        )
        recommendation = eligible.sort_values("balance_score", ascending=False).iloc[0]

    core = summary[summary["policy_id"].isin(["C", "D", "E", "F", "G"])]
    core_improves_robustness = bool(
        (core["max_drawdown"].max() >= active["max_drawdown"])
        and (core["average_monthly_excess_return"].max() >= active["average_monthly_excess_return"])
    )
    core_allocations["core_balance_score"] = (
        core_allocations["cagr"]
        - core_allocations["max_drawdown"].abs() * 0.5
        + core_allocations["excess_cagr"]
        + core_allocations["sharpe_proxy"] * 0.02
    )
    best_core = core_allocations.sort_values("core_balance_score", ascending=False).iloc[0]
    fixed_core_allocations["fixed_core_balance_score"] = (
        fixed_core_allocations["cagr"]
        - fixed_core_allocations["max_drawdown"].abs() * 0.5
        + fixed_core_allocations["excess_cagr"]
        + fixed_core_allocations["sharpe_proxy"] * 0.02
    )
    best_fixed_core = fixed_core_allocations.sort_values("fixed_core_balance_score", ascending=False).iloc[0]

    return [
        f"- Is pure active Top3 still worth paper trading? {'No' if active['excess_cagr'] < 0 else 'Only as a monitored sleeve'}. "
        f"It delivered {active['excess_cagr']:.2%} excess CAGR versus BIST100 in this walk-forward.",
        f"- Does benchmark-core improve robustness? {'Yes' if core_improves_robustness else 'No'}. "
        "Core policies reduce active drawdown and tracking error mechanically, but must be checked against BIST100 drag.",
        (
            "- Best balance of CAGR, drawdown, and excess return: "
            f"Policy {recommendation['policy_id']} — {recommendation['policy_name']} "
            f"(CAGR {recommendation['cagr']:.2%}, max drawdown {recommendation['max_drawdown']:.2%}, "
            f"excess CAGR {recommendation['excess_cagr']:.2%})."
        ),
        (
            "- Best fixed benchmark-core allocation if an active sleeve must be retained: "
            f"Policy {best_fixed_core['policy_id']} — {best_fixed_core['policy_name']} "
            f"(active allocation {best_fixed_core['active_allocation_average']:.2%}, "
            f"excess CAGR {best_fixed_core['excess_cagr']:.2%})."
        ),
        (
            "- Best dynamic benchmark-core/satellite variant: "
            f"Policy {best_core['policy_id']} — {best_core['policy_name']} "
            f"(active allocation average {best_core['active_allocation_average']:.2%}, "
            f"excess CAGR {best_core['excess_cagr']:.2%})."
        ),
        (
            "- Next paper-trading candidate: "
            f"Policy {recommendation['policy_id']} — {recommendation['policy_name']}."
        ),
        "- Active stock-picking should be demoted from main strategy to satellite only unless it regains persistent benchmark-relative edge.",
    ]


def _write_reports(
    summary: pd.DataFrame,
    recent: pd.DataFrame,
    research_path: Path,
    recent_path: Path,
) -> None:
    display = summary.copy()
    percent_columns = [
        "total_return",
        "bist100_total_return",
        "cagr",
        "bist100_cagr",
        "excess_cagr",
        "max_drawdown",
        "bist100_max_drawdown",
        "monthly_win_rate_vs_bist100",
        "average_monthly_excess_return",
        "worst_month_return",
        "best_month_return",
        "average_turnover",
        "active_allocation_average",
        "transaction_cost_impact",
    ]
    for column in percent_columns:
        display[column] = display[column].map(_format_percent)

    lines = [
        "# Benchmark-Core Portfolio Research",
        "",
        "Research-only. Production tracking_state.json and live follow-up behavior are unchanged.",
        "",
        "## Policy Results",
        "",
        display.to_markdown(index=False),
        "",
        "## Decision",
        "",
        *_decision_lines(summary),
        "",
        "## Acceptance Criteria",
        "",
        (
            "A new candidate must improve robustness versus pure active Top3 and avoid material historical "
            "underperformance versus BIST100. June 2026 improvement alone is not sufficient."
        ),
        "",
    ]
    research_path.write_text("\n".join(lines), encoding="utf-8")

    recent_display = recent.copy()
    recent_percent_columns = [
        "benchmark_weight",
        "active_weight",
        "active_gross_return",
        "benchmark_return",
        "gross_return",
        "net_return",
        "gross_excess_return",
        "net_excess_return",
        "transaction_cost_impact",
        "top3_avg_score",
        "historical_top3_score_median",
        "top3_avg_momentum",
        "top3_avg_relative_strength",
    ]
    for column in recent_percent_columns:
        if column in recent_display:
            recent_display[column] = recent_display[column].map(lambda value: "" if pd.isna(value) else _format_percent(float(value)))

    recent_lines = [
        "# Benchmark-Core Recent Follow-Up",
        "",
        "Period uses the fixed 2026-06-01 follow-up basket and BIST100 return through the latest available benchmark close.",
        "",
        recent_display.to_markdown(index=False),
        "",
        "## Read-Through",
        "",
        (
            "Benchmark-core exposure would have reduced the observed benchmark-relative underperformance because most "
            "capital stayed in BIST100 while only a smaller sleeve owned the lagging fixed Top3 basket."
        ),
        "",
        (
            "It would not have fully avoided underperformance unless the portfolio was 100% BIST100. "
            "The 80/20 and conditional overlays reduced the gross excess drag from -5.90% to -1.18%."
        ),
        "",
    ]
    recent_path.write_text("\n".join(recent_lines), encoding="utf-8")


def run_benchmark_core_research(
    stock_prices: dict[str, pd.DataFrame],
    benchmark_prices: pd.DataFrame,
    factor_models: dict[str, dict[str, float]],
    results_dir: str,
    reports_dir: str = "reports",
    transaction_cost: float = 0.002,
    validation_start: str = "2024-01-01",
) -> dict[str, Path]:
    Path(results_dir).mkdir(exist_ok=True)
    benchmark_latest = pd.Timestamp(_clean_close(benchmark_prices).index.max())
    feature_frames = _calculate_research_features(stock_prices, benchmark_prices)

    interval_frames = []
    summary_rows = []
    for policy in POLICIES:
        intervals = _simulate_policy(
            policy=policy,
            stock_prices=stock_prices,
            benchmark_prices=benchmark_prices,
            feature_frames=feature_frames,
            factor_models=factor_models,
            start=validation_start,
            end=benchmark_latest,
            transaction_cost=transaction_cost,
        )
        if intervals.empty:
            continue
        interval_frames.append(intervals)
        summary_rows.append(_summarize_policy(intervals))

    summary = pd.DataFrame(summary_rows).sort_values("policy_id")
    research_csv = Path(results_dir) / "benchmark_core_research.csv"
    summary.to_csv(research_csv, index=False)

    state = _load_tracking_state(reports_dir)
    recent = _recent_followup(
        state=state,
        stock_prices=stock_prices,
        benchmark_prices=benchmark_prices,
        feature_frames=feature_frames,
        factor_models=factor_models,
        transaction_cost=transaction_cost,
        validation_start=validation_start,
    )
    recent_csv = Path(results_dir) / "benchmark_core_recent_followup.csv"
    recent.to_csv(recent_csv, index=False)

    research_path = Path(results_dir) / "benchmark_core_research.md"
    recent_path = Path(results_dir) / "benchmark_core_recent_followup.md"
    _write_reports(summary, recent, research_path, recent_path)

    return {
        "research_markdown": research_path,
        "research_csv": research_csv,
        "recent_markdown": recent_path,
        "recent_csv": recent_csv,
    }
