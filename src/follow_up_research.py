from __future__ import annotations

import json
from dataclasses import dataclass
from pathlib import Path

import pandas as pd

from src.current_portfolio import _current_regime
from src.indicators import calculate_features
from src.ranking import _cross_sectional_score


SECTOR_MAP = {
    "AKBNK.IS": "Banks",
    "GARAN.IS": "Banks",
    "YKBNK.IS": "Banks",
    "ASELS.IS": "Defense/Technology",
    "TCELL.IS": "Telecom",
    "BIMAS.IS": "Retail",
    "EREGL.IS": "Steel",
    "SISE.IS": "Glass/Industrial",
    "FROTO.IS": "Autos",
    "TOASO.IS": "Autos",
    "KCHOL.IS": "Holdings",
    "SAHOL.IS": "Holdings",
    "THYAO.IS": "Airlines",
    "PGSUS.IS": "Airlines",
    "TUPRS.IS": "Energy/Refinery",
    "PETKM.IS": "Petrochemicals",
    "KOZAL.IS": "Mining",
    "ARCLK.IS": "Durables",
}

LARGE_CAP_PROXY = {
    "AKBNK.IS",
    "ASELS.IS",
    "BIMAS.IS",
    "EREGL.IS",
    "GARAN.IS",
    "KCHOL.IS",
    "SAHOL.IS",
    "SISE.IS",
    "TCELL.IS",
    "THYAO.IS",
    "TUPRS.IS",
    "YKBNK.IS",
}

FACTOR_MAP = {
    "momentum_1m": ("momentum_1m", True),
    "momentum_3m": ("momentum_3m", True),
    "momentum_6m": ("momentum_6m", True),
    "volume_increase": ("volume_increase", True),
    "above_ma": ("above_ma", True),
    "volatility_penalty": ("volatility", False),
}

BASE_REQUIRED_COLUMNS = [
    "momentum_1m",
    "momentum_3m",
    "momentum_6m",
    "volume_increase",
    "above_ma",
    "volatility",
]


@dataclass(frozen=True)
class Policy:
    policy_id: str
    name: str
    frequency: str
    portfolio_size: int
    score_mode: str


POLICIES = [
    Policy("A", "Current baseline monthly Top3", "monthly", 3, "base"),
    Policy("B", "Weekly rebalance Top3", "weekly", 3, "base"),
    Policy("C", "Weekly rebalance Top5", "weekly", 5, "base"),
    Policy("D", "Relative Strength Top3", "weekly", 3, "relative_strength"),
    Policy("E", "Benchmark-aware Top3", "weekly", 3, "benchmark_aware"),
    Policy("F", "Leadership Rotation Overlay", "weekly", 3, "leadership_overlay"),
]


def _clean_close(prices: pd.DataFrame) -> pd.Series:
    return prices["Close"].dropna().sort_index()


def _price_at_or_before(prices: pd.DataFrame, date: pd.Timestamp) -> tuple[pd.Timestamp, float]:
    close = _clean_close(prices)
    available = close[close.index <= date]
    if available.empty:
        available = close
    return pd.Timestamp(available.index[-1]), float(available.iloc[-1])


def _period_return(prices: pd.DataFrame, start: pd.Timestamp, end: pd.Timestamp) -> float | None:
    _, start_price = _price_at_or_before(prices, start)
    _, end_price = _price_at_or_before(prices, end)
    if start_price <= 0:
        return None
    return (end_price / start_price) - 1


def _benchmark_regime_asof(benchmark_prices: pd.DataFrame, asof: pd.Timestamp) -> dict[str, object]:
    sliced = benchmark_prices.loc[benchmark_prices.index <= asof].copy()
    if sliced.empty:
        raise ValueError(f"No benchmark data at or before {asof.date()}")
    return _current_regime(sliced)


def _calculate_research_features(
    stock_prices: dict[str, pd.DataFrame],
    benchmark_prices: pd.DataFrame,
) -> dict[str, pd.DataFrame]:
    benchmark_close = _clean_close(benchmark_prices)
    feature_frames = {}
    for symbol, prices in stock_prices.items():
        features = calculate_features(prices)
        close = _clean_close(prices)
        aligned_benchmark = benchmark_close.reindex(close.index).ffill()
        for window in [5, 10, 20]:
            stock_return = close.pct_change(window)
            benchmark_return = aligned_benchmark.pct_change(window)
            features[f"relative_strength_{window}d"] = stock_return - benchmark_return
        features["sector"] = SECTOR_MAP.get(symbol, "Other")
        features["large_cap_proxy"] = symbol in LARGE_CAP_PROXY
        feature_frames[symbol] = features
    return feature_frames


def _base_score(snapshot: pd.DataFrame, weights: dict[str, float]) -> pd.Series:
    score = pd.Series(0.0, index=snapshot.index)
    for factor_name, weight in weights.items():
        source_column, higher_is_better = FACTOR_MAP[factor_name]
        score += weight * _cross_sectional_score(snapshot[source_column], higher_is_better=higher_is_better).fillna(0)
    return score


def _rank_asof(
    feature_frames: dict[str, pd.DataFrame],
    benchmark_prices: pd.DataFrame,
    factor_models: dict[str, dict[str, float]],
    asof: pd.Timestamp,
    policy: Policy,
) -> pd.DataFrame:
    rows = []
    for symbol, features in feature_frames.items():
        valid = features.loc[features.index <= asof].dropna(subset=BASE_REQUIRED_COLUMNS)
        if valid.empty:
            continue
        row = valid.iloc[-1].copy()
        row["symbol"] = symbol
        row["signal_date"] = valid.index[-1]
        rows.append(row)

    if not rows:
        return pd.DataFrame()

    snapshot = pd.DataFrame(rows).set_index("symbol")
    regime = _benchmark_regime_asof(benchmark_prices, asof)
    active_model = "low_volatility" if regime["bist100_below_ma200"] else "volume_heavy"
    weights = factor_models[active_model]
    snapshot["base_score"] = _base_score(snapshot, weights)

    relative_cols = ["relative_strength_5d", "relative_strength_10d", "relative_strength_20d"]
    for column in relative_cols:
        snapshot[column] = pd.to_numeric(snapshot[column], errors="coerce")
    snapshot["relative_strength_avg"] = snapshot[relative_cols].mean(axis=1)
    snapshot["relative_strength_score"] = (
        _cross_sectional_score(snapshot["relative_strength_5d"]).fillna(0) * 0.25
        + _cross_sectional_score(snapshot["relative_strength_10d"]).fillna(0) * 0.35
        + _cross_sectional_score(snapshot["relative_strength_20d"]).fillna(0) * 0.40
    )
    snapshot["positive_relative_momentum"] = (snapshot["relative_strength_avg"] > 0).astype(float)

    sector_strength = snapshot.groupby("sector")["relative_strength_avg"].mean()
    sector_score = _cross_sectional_score(sector_strength).fillna(0)
    snapshot["sector_strength"] = snapshot["sector"].map(sector_strength).astype(float)
    snapshot["sector_strength_score"] = snapshot["sector"].map(sector_score).astype(float).fillna(0)
    snapshot["large_cap_leadership_score"] = (
        snapshot["large_cap_proxy"].astype(float)
        * _cross_sectional_score(snapshot["relative_strength_avg"]).fillna(0)
    )

    if policy.score_mode == "base":
        snapshot["score"] = snapshot["base_score"]
    elif policy.score_mode == "relative_strength":
        snapshot["score"] = 0.55 * snapshot["base_score"] + 0.45 * snapshot["relative_strength_score"]
    elif policy.score_mode == "benchmark_aware":
        positive_bonus = snapshot["positive_relative_momentum"]
        negative_penalty = (1 - positive_bonus) * 0.15
        snapshot["score"] = (
            0.50 * snapshot["base_score"]
            + 0.35 * snapshot["relative_strength_score"]
            + 0.15 * positive_bonus
            - negative_penalty
        )
    elif policy.score_mode == "leadership_overlay":
        snapshot["score"] = (
            0.55 * snapshot["base_score"]
            + 0.25 * snapshot["relative_strength_score"]
            + 0.15 * snapshot["sector_strength_score"]
            + 0.05 * snapshot["large_cap_leadership_score"]
        )
    else:
        raise ValueError(f"Unknown policy score mode: {policy.score_mode}")

    ranked = snapshot.sort_values("score", ascending=False).reset_index()
    ranked["rank"] = range(1, len(ranked) + 1)
    ranked["active_model"] = active_model
    ranked["asof"] = asof
    return ranked


def _rebalance_dates(benchmark_prices: pd.DataFrame, start: str, end: pd.Timestamp, frequency: str) -> list[pd.Timestamp]:
    dates = _clean_close(benchmark_prices).index
    dates = dates[(dates >= pd.Timestamp(start)) & (dates <= pd.Timestamp(end))]
    if dates.empty:
        return []

    grouped = pd.Series(dates, index=dates)
    if frequency == "monthly":
        selected = grouped.groupby(dates.to_period("M")).first().tolist()
    elif frequency == "weekly":
        selected = grouped.groupby(dates.to_period("W-FRI")).first().tolist()
    else:
        raise ValueError(f"Unsupported rebalance frequency: {frequency}")

    selected = [pd.Timestamp(date) for date in selected]
    latest = pd.Timestamp(dates[-1])
    if selected[-1] < latest:
        selected.append(latest)
    return selected


def _turnover_and_trades(previous: dict[str, float], current: dict[str, float]) -> tuple[float, int]:
    if not previous:
        return 1.0, len(current)
    all_symbols = set(previous) | set(current)
    turnover = sum(abs(current.get(symbol, 0.0) - previous.get(symbol, 0.0)) for symbol in all_symbols)
    trades = len(set(current) - set(previous)) + len(set(previous) - set(current))
    return turnover, trades


def _simulate_policy(
    policy: Policy,
    stock_prices: dict[str, pd.DataFrame],
    benchmark_prices: pd.DataFrame,
    factor_models: dict[str, dict[str, float]],
    feature_frames: dict[str, pd.DataFrame],
    start: str,
    end: pd.Timestamp,
    transaction_cost: float,
) -> pd.DataFrame:
    rebalances = _rebalance_dates(benchmark_prices, start, end, policy.frequency)
    if len(rebalances) < 2:
        return pd.DataFrame()

    previous_weights: dict[str, float] = {}
    equity = 1.0
    gross_equity = 1.0
    benchmark_equity = 1.0
    rows = []

    for start_date, end_date in zip(rebalances[:-1], rebalances[1:]):
        if end_date <= start_date:
            continue

        ranked = _rank_asof(feature_frames, benchmark_prices, factor_models, start_date, policy)
        if ranked.empty:
            continue

        selected = ranked.head(policy.portfolio_size).copy()
        weights = {symbol: 1.0 / len(selected) for symbol in selected["symbol"]}
        turnover, trades = _turnover_and_trades(previous_weights, weights)
        cost_impact = transaction_cost * turnover

        stock_returns = []
        for symbol in selected["symbol"]:
            stock_return = _period_return(stock_prices[symbol], start_date, end_date)
            if stock_return is not None:
                stock_returns.append(stock_return)

        if not stock_returns:
            continue

        gross_return = sum(stock_returns) / len(stock_returns)
        net_return = gross_return - cost_impact
        benchmark_return = _period_return(benchmark_prices, start_date, end_date)
        if benchmark_return is None:
            benchmark_return = 0.0

        gross_equity *= 1 + gross_return
        equity *= 1 + net_return
        benchmark_equity *= 1 + benchmark_return
        rows.append(
            {
                "policy_id": policy.policy_id,
                "policy_name": policy.name,
                "frequency": policy.frequency,
                "portfolio_size": policy.portfolio_size,
                "score_mode": policy.score_mode,
                "start_date": start_date,
                "end_date": end_date,
                "selected_symbols": ", ".join(selected["symbol"]),
                "selected_sectors": ", ".join(selected["sector"]),
                "gross_return": gross_return,
                "net_return": net_return,
                "benchmark_return": benchmark_return,
                "excess_return": net_return - benchmark_return,
                "transaction_cost_impact": cost_impact,
                "turnover": turnover,
                "trades": trades,
                "equity": equity,
                "gross_equity": gross_equity,
                "benchmark_equity": benchmark_equity,
            }
        )
        previous_weights = weights

    return pd.DataFrame(rows)


def _max_drawdown(equity: pd.Series) -> float:
    if equity.empty:
        return 0.0
    drawdown = equity / equity.cummax() - 1
    return float(drawdown.min())


def _compound(series: pd.Series) -> float:
    return float((1 + series).prod() - 1)


def _summarize_policy(intervals: pd.DataFrame) -> dict[str, object]:
    if intervals.empty:
        return {}

    first_date = pd.Timestamp(intervals["start_date"].iloc[0])
    last_date = pd.Timestamp(intervals["end_date"].iloc[-1])
    years = max((last_date - first_date).days / 365.25, 1 / 365.25)
    total_return = float(intervals["equity"].iloc[-1] - 1)
    benchmark_total_return = float(intervals["benchmark_equity"].iloc[-1] - 1)
    gross_total_return = float(intervals["gross_equity"].iloc[-1] - 1)
    cagr = (1 + total_return) ** (1 / years) - 1
    benchmark_cagr = (1 + benchmark_total_return) ** (1 / years) - 1

    monthly = intervals.copy()
    monthly["month"] = pd.to_datetime(monthly["end_date"]).dt.to_period("M").astype(str)
    monthly_summary = monthly.groupby("month").agg(
        strategy_return=("net_return", _compound),
        benchmark_return=("benchmark_return", _compound),
        gross_return=("gross_return", _compound),
        turnover=("turnover", "sum"),
        trades=("trades", "sum"),
        transaction_cost_impact=("transaction_cost_impact", "sum"),
    )
    monthly_summary["excess_return"] = monthly_summary["strategy_return"] - monthly_summary["benchmark_return"]
    worst_month = monthly_summary["excess_return"].idxmin()
    best_month = monthly_summary["excess_return"].idxmax()

    return {
        "policy_id": intervals["policy_id"].iloc[0],
        "policy_name": intervals["policy_name"].iloc[0],
        "frequency": intervals["frequency"].iloc[0],
        "portfolio_size": int(intervals["portfolio_size"].iloc[0]),
        "total_return": total_return,
        "benchmark_total_return": benchmark_total_return,
        "cagr": cagr,
        "bist100_cagr": benchmark_cagr,
        "excess_cagr": cagr - benchmark_cagr,
        "monthly_win_rate_vs_bist100": float((monthly_summary["excess_return"] > 0).mean()),
        "average_monthly_excess_return": float(monthly_summary["excess_return"].mean()),
        "max_drawdown": _max_drawdown(intervals["equity"]),
        "average_monthly_turnover": float(monthly_summary["turnover"].mean()),
        "average_trades_per_month": float(monthly_summary["trades"].mean()),
        "transaction_cost_impact": gross_total_return - total_return,
        "worst_underperformance_month": worst_month,
        "worst_underperformance": float(monthly_summary.loc[worst_month, "excess_return"]),
        "best_outperformance_month": best_month,
        "best_outperformance": float(monthly_summary.loc[best_month, "excess_return"]),
        "intervals": len(intervals),
    }


def _load_tracking_state(reports_dir: str) -> dict[str, object] | None:
    path = Path(reports_dir) / "tracking_state.json"
    if not path.exists():
        return None
    with path.open("r", encoding="utf-8") as handle:
        return json.load(handle)


def _fixed_state_counterfactual(
    state: dict[str, object],
    stock_prices: dict[str, pd.DataFrame],
    benchmark_prices: pd.DataFrame,
    end: pd.Timestamp,
    transaction_cost: float,
) -> pd.DataFrame:
    start = pd.Timestamp(state["start_date"])
    symbols = [position["symbol"] for position in state["positions"]]
    returns = []
    for position in state["positions"]:
        symbol = position["symbol"]
        start_price = float(position["start_price"])
        _, end_price = _price_at_or_before(stock_prices[symbol], end)
        returns.append((end_price / start_price) - 1)

    benchmark_start = float(state.get("benchmark", {}).get("start_price", 0.0))
    _, benchmark_end = _price_at_or_before(benchmark_prices, end)
    benchmark_return = (benchmark_end / benchmark_start) - 1 if benchmark_start else 0.0
    gross_return = sum(returns) / len(returns)
    return pd.DataFrame(
        [
            {
                "policy_id": "A",
                "policy_name": "Current fixed follow-up state",
                "frequency": "monthly",
                "portfolio_size": len(symbols),
                "score_mode": "fixed_state",
                "start_date": start,
                "end_date": end,
                "selected_symbols": ", ".join(symbols),
                "selected_sectors": ", ".join(SECTOR_MAP.get(symbol, "Other") for symbol in symbols),
                "gross_return": gross_return,
                "net_return": gross_return - transaction_cost,
                "benchmark_return": benchmark_return,
                "excess_return": gross_return - transaction_cost - benchmark_return,
                "transaction_cost_impact": transaction_cost,
                "turnover": 1.0,
                "trades": len(symbols),
                "equity": 1 + gross_return - transaction_cost,
                "gross_equity": 1 + gross_return,
                "benchmark_equity": 1 + benchmark_return,
            }
        ]
    )


def _diagnose_follow_up(
    state: dict[str, object],
    stock_prices: dict[str, pd.DataFrame],
    benchmark_prices: pd.DataFrame,
    end: pd.Timestamp,
) -> tuple[pd.DataFrame, pd.DataFrame, pd.DataFrame, dict[str, float]]:
    start = pd.Timestamp(state["start_date"])
    rows = []
    for position in state["positions"]:
        symbol = position["symbol"]
        start_price = float(position["start_price"])
        _, current_price = _price_at_or_before(stock_prices[symbol], end)
        stock_return = (current_price / start_price) - 1 if start_price else 0.0
        weight = float(position["weight"])
        rows.append(
            {
                "symbol": symbol,
                "sector": SECTOR_MAP.get(symbol, "Other"),
                "weight": weight,
                "start_price": start_price,
                "current_price": current_price,
                "return": stock_return,
                "portfolio_contribution": weight * stock_return,
            }
        )
    contributions = pd.DataFrame(rows)

    universe_rows = []
    for symbol, prices in stock_prices.items():
        stock_return = _period_return(prices, start, end)
        if stock_return is None:
            continue
        universe_rows.append(
            {
                "symbol": symbol,
                "sector": SECTOR_MAP.get(symbol, "Other"),
                "period_return": stock_return,
            }
        )
    universe = pd.DataFrame(universe_rows).sort_values("period_return", ascending=False)
    sector_leaders = universe.groupby("sector", as_index=False)["period_return"].mean().sort_values(
        "period_return",
        ascending=False,
    )

    portfolio_return = float(contributions["portfolio_contribution"].sum())
    benchmark_return = _period_return(benchmark_prices, start, end) or 0.0
    summary = {
        "portfolio_return": portfolio_return,
        "benchmark_return": benchmark_return,
        "excess_return": portfolio_return - benchmark_return,
    }
    return contributions, universe, sector_leaders, summary


def _decision_text(summary: pd.DataFrame, recent: pd.DataFrame) -> list[str]:
    baseline = summary[summary["policy_id"] == "A"].iloc[0]
    recent_by_policy = recent.groupby("policy_id").tail(1).set_index("policy_id")
    baseline_recent = recent_by_policy.loc["A"]

    lines = []
    for policy_id, question in [
        ("B", "Did weekly rebalance improve excess return?"),
        ("D", "Did relative strength improve excess return?"),
        ("E", "Did benchmark-aware selection improve excess return?"),
    ]:
        row = summary[summary["policy_id"] == policy_id].iloc[0]
        recent_row = recent_by_policy.loc[policy_id]
        improved_history = row["excess_cagr"] > baseline["excess_cagr"]
        improved_recent = recent_row["cumulative_excess_return"] > baseline_recent["cumulative_excess_return"]
        if improved_history and improved_recent:
            answer = "Yes"
        elif improved_recent and not improved_history:
            answer = "Recent yes, historical no, so rejected"
        elif improved_history and not improved_recent:
            answer = "Historical yes, recent no, so rejected"
        else:
            answer = "No"
        lines.append(
            f"- {question} {answer}. Historical excess CAGR delta vs baseline: "
            f"{row['excess_cagr'] - baseline['excess_cagr']:.2%}; recent excess delta: "
            f"{recent_row['cumulative_excess_return'] - baseline_recent['cumulative_excess_return']:.2%}."
        )

    robust = summary[
        (summary["excess_cagr"] > 0)
        & (summary["monthly_win_rate_vs_bist100"] > 0.50)
        & (summary["max_drawdown"] >= baseline["max_drawdown"])
    ]
    lines.append(
        "- Did any policy beat BIST100 robustly? "
        + ("Yes: " + ", ".join(robust["policy_id"]) if not robust.empty else "No under the current acceptance filter.")
    )

    candidates = []
    for _, row in summary.iterrows():
        if row["policy_id"] == "A":
            continue
        recent_row = recent_by_policy.loc[row["policy_id"]]
        if (
            row["excess_cagr"] > baseline["excess_cagr"]
            and recent_row["cumulative_excess_return"] > baseline_recent["cumulative_excess_return"]
        ):
            candidates.append(row)

    if candidates:
        best = max(candidates, key=lambda item: (item["excess_cagr"], item["monthly_win_rate_vs_bist100"]))
        lines.append(f"- Next paper-trading candidate: Policy {best['policy_id']} — {best['policy_name']}.")
        lines.append("- Current one-month fixed hold should be modified after a paper-trading trial, not retired immediately.")
    else:
        lines.append("- Next paper-trading candidate: none. No policy passed both historical and recent acceptance criteria.")
        lines.append("- Current one-month fixed hold should be kept for tracking, while weekly/relative-strength variants remain research-only.")
    return lines


def _format_percent(value: float) -> str:
    return f"{value:.2%}"


def _write_markdown_reports(
    diagnosis_path: Path,
    research_path: Path,
    recent_path: Path,
    state: dict[str, object],
    diagnosis: tuple[pd.DataFrame, pd.DataFrame, pd.DataFrame, dict[str, float]],
    summary: pd.DataFrame,
    recent: pd.DataFrame,
) -> None:
    contributions, universe, sector_leaders, diagnosis_summary = diagnosis
    starting_symbols = ", ".join(position["symbol"] for position in state["positions"])
    top_leaders = universe.head(10)
    selected = set(contributions["symbol"])
    missed_leaders = top_leaders[~top_leaders["symbol"].isin(selected)]

    diagnosis_lines = [
        "# Follow-Up Underperformance Diagnosis",
        "",
        f"- Start date: {state['start_date']}",
        f"- Starting portfolio: {starting_symbols}",
        f"- Current portfolio return: {_format_percent(diagnosis_summary['portfolio_return'])}",
        f"- BIST100 return: {_format_percent(diagnosis_summary['benchmark_return'])}",
        f"- Excess return: {_format_percent(diagnosis_summary['excess_return'])}",
        "",
        "## Per-Stock Contribution",
        "",
        contributions.to_markdown(index=False, floatfmt=".4f"),
        "",
        "## Universe Leaders During Follow-Up",
        "",
        top_leaders.to_markdown(index=False, floatfmt=".4f"),
        "",
        "## Sector/Proxy Group Leaders",
        "",
        sector_leaders.to_markdown(index=False, floatfmt=".4f"),
        "",
        "## Leadership Rotation Finding",
        "",
        (
            "The fixed Top3 basket made money, but the strongest benchmark-relative move came from names outside "
            "the fixed basket. In the available universe, the largest recent winners were concentrated in "
            f"{', '.join(sector_leaders.head(3)['sector'])}. "
            "That is consistent with a leadership rotation the one-month fixed hold did not capture."
        ),
        "",
        "## Missed Leaders",
        "",
        missed_leaders.to_markdown(index=False, floatfmt=".4f") if not missed_leaders.empty else "No missed leaders in universe.",
        "",
    ]
    diagnosis_path.write_text("\n".join(diagnosis_lines), encoding="utf-8")

    display_summary = summary.copy()
    percent_cols = [
        "total_return",
        "benchmark_total_return",
        "cagr",
        "bist100_cagr",
        "excess_cagr",
        "monthly_win_rate_vs_bist100",
        "average_monthly_excess_return",
        "max_drawdown",
        "transaction_cost_impact",
        "worst_underperformance",
        "best_outperformance",
    ]
    for column in percent_cols:
        display_summary[column] = display_summary[column].map(lambda value: f"{value:.2%}")

    decision = _decision_text(summary, recent)
    research_lines = [
        "# Follow-Up Improvement Research",
        "",
        "This is research-only. Production follow-up tracking remains fixed and still reads reports/tracking_state.json.",
        "",
        "## Policy Summary",
        "",
        display_summary.to_markdown(index=False),
        "",
        "## Decision",
        "",
        *decision,
        "",
        "## Acceptance Rule",
        "",
        (
            "A policy is only eligible if it improves both historical walk-forward excess return and the recent "
            "2026-06 counterfactual excess return. Policies that only fix June 2026 are rejected."
        ),
        "",
    ]
    research_path.write_text("\n".join(research_lines), encoding="utf-8")

    recent_display = recent.copy()
    for column in [
        "gross_return",
        "net_return",
        "benchmark_return",
        "excess_return",
        "transaction_cost_impact",
        "turnover",
        "cumulative_return",
        "cumulative_benchmark_return",
        "cumulative_excess_return",
    ]:
        recent_display[column] = recent_display[column].map(lambda value: f"{value:.2%}")
    recent_summary = recent.groupby("policy_id").tail(1).copy()
    for column in ["cumulative_return", "cumulative_benchmark_return", "cumulative_excess_return"]:
        recent_summary[column] = recent_summary[column].map(lambda value: f"{value:.2%}")
    recent_lines = [
        "# Follow-Up Recent Counterfactual",
        "",
        "Period: 2026-06-01 to latest available BIST100 close. Signals use only data available at each rebalance date.",
        "",
        "## Cumulative Results",
        "",
        recent_summary[
            [
                "policy_id",
                "policy_name",
                "cumulative_return",
                "cumulative_benchmark_return",
                "cumulative_excess_return",
                "selected_symbols",
            ]
        ].to_markdown(index=False),
        "",
        "## Rebalance Paths",
        "",
        recent_display[
            [
                "policy_id",
                "policy_name",
                "start_date",
                "end_date",
                "selected_symbols",
                "gross_return",
                "net_return",
                "benchmark_return",
                "excess_return",
                "cumulative_return",
                "cumulative_excess_return",
                "turnover",
                "trades",
            ]
        ].to_markdown(index=False),
        "",
        "## Rotation Check",
        "",
        (
            "Use the selected_symbols column to inspect whether the weekly policies rotated away from the original "
            "EREGL/SISE/BIMAS basket and into the stronger bank or large-cap leadership names."
        ),
        "",
    ]
    recent_path.write_text("\n".join(recent_lines), encoding="utf-8")


def run_follow_up_improvement_research(
    stock_prices: dict[str, pd.DataFrame],
    benchmark_prices: pd.DataFrame,
    factor_models: dict[str, dict[str, float]],
    results_dir: str,
    reports_dir: str = "reports",
    transaction_cost: float = 0.002,
    validation_start: str = "2024-01-01",
) -> dict[str, Path]:
    Path(results_dir).mkdir(exist_ok=True)
    state = _load_tracking_state(reports_dir)
    if state is None:
        raise ValueError("reports/tracking_state.json is required for follow-up diagnosis.")

    benchmark_latest = _clean_close(benchmark_prices).index.max()
    feature_frames = _calculate_research_features(stock_prices, benchmark_prices)

    interval_frames = []
    summary_rows = []
    for policy in POLICIES:
        intervals = _simulate_policy(
            policy=policy,
            stock_prices=stock_prices,
            benchmark_prices=benchmark_prices,
            factor_models=factor_models,
            feature_frames=feature_frames,
            start=validation_start,
            end=benchmark_latest,
            transaction_cost=transaction_cost,
        )
        if intervals.empty:
            continue
        interval_frames.append(intervals)
        summary_rows.append(_summarize_policy(intervals))

    summary = pd.DataFrame(summary_rows).sort_values("policy_id")
    research_csv = Path(results_dir) / "follow_up_improvement_research.csv"
    summary.to_csv(research_csv, index=False)

    recent_frames = [
        _fixed_state_counterfactual(state, stock_prices, benchmark_prices, benchmark_latest, transaction_cost)
    ]
    recent_start = state["start_date"]
    for policy in POLICIES[1:]:
        recent_frames.append(
            _simulate_policy(
                policy=policy,
                stock_prices=stock_prices,
                benchmark_prices=benchmark_prices,
                factor_models=factor_models,
                feature_frames=feature_frames,
                start=recent_start,
                end=benchmark_latest,
                transaction_cost=transaction_cost,
            )
        )
    recent = pd.concat(recent_frames, ignore_index=True)
    recent["cumulative_return"] = recent["equity"] - 1
    recent["cumulative_benchmark_return"] = recent["benchmark_equity"] - 1
    recent["cumulative_excess_return"] = recent["cumulative_return"] - recent["cumulative_benchmark_return"]
    recent_csv = Path(results_dir) / "follow_up_recent_counterfactual.csv"
    recent.to_csv(recent_csv, index=False)

    diagnosis = _diagnose_follow_up(state, stock_prices, benchmark_prices, benchmark_latest)
    diagnosis_path = Path(results_dir) / "follow_up_underperformance_diagnosis.md"
    research_path = Path(results_dir) / "follow_up_improvement_research.md"
    recent_path = Path(results_dir) / "follow_up_recent_counterfactual.md"
    _write_markdown_reports(diagnosis_path, research_path, recent_path, state, diagnosis, summary, recent)

    return {
        "diagnosis": diagnosis_path,
        "research_markdown": research_path,
        "research_csv": research_csv,
        "recent_markdown": recent_path,
        "recent_csv": recent_csv,
    }
