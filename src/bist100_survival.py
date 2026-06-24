from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

import pandas as pd

from src.ranking import _cross_sectional_score


@dataclass(frozen=True)
class SurvivalPolicy:
    policy_id: str
    policy_name: str
    mode: str
    portfolio_size: int
    use_regime_cash: bool = True
    use_hard_filters: bool = True


POLICIES = [
    SurvivalPolicy("BENCHMARK", "BIST100 benchmark", "benchmark", 0, False, False),
    SurvivalPolicy("OLD_TOP3", "Old absolute-score Top3", "old_score", 3, True, False),
    SurvivalPolicy("RS_TOP3", "BIST100 relative-strength survival Top3", "survival", 3, True, True),
    SurvivalPolicy("RS_TOP5", "BIST100 relative-strength survival Top5", "survival", 5, True, True),
    SurvivalPolicy("RS_TOP10", "BIST100 relative-strength survival Top10", "survival", 10, True, True),
    SurvivalPolicy("RS_TOP5_NO_CASH", "Survival Top5 without MA200 cash filter", "survival", 5, False, True),
]

SCORE_WEIGHTS = {
    "relative_strength_3m": 0.30,
    "relative_strength_1m": 0.20,
    "relative_strength_6m": 0.15,
    "trend_score": 0.15,
    "volume_increase": 0.10,
    "low_volatility": 0.10,
}

OLD_SCORE_WEIGHTS = {
    "momentum_1m": 0.15,
    "momentum_3m": 0.20,
    "momentum_6m": 0.15,
    "volume_increase": 0.35,
    "trend_score": 0.10,
    "low_volatility": 0.05,
}


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


def _build_features(
    stock_prices: dict[str, pd.DataFrame],
    benchmark_prices: pd.DataFrame,
) -> dict[str, pd.DataFrame]:
    benchmark_close = _clean_close(benchmark_prices)
    feature_frames: dict[str, pd.DataFrame] = {}

    for symbol, prices in stock_prices.items():
        close = _clean_close(prices)
        if close.empty:
            continue

        volume = prices["Volume"].reindex(close.index).fillna(0)
        aligned_benchmark = benchmark_close.reindex(close.index).ffill()

        features = pd.DataFrame(index=close.index)
        features["close"] = close
        features["momentum_1m"] = close.pct_change(21)
        features["momentum_3m"] = close.pct_change(63)
        features["momentum_6m"] = close.pct_change(126)
        features["relative_strength_1m"] = features["momentum_1m"] - aligned_benchmark.pct_change(21)
        features["relative_strength_3m"] = features["momentum_3m"] - aligned_benchmark.pct_change(63)
        features["relative_strength_6m"] = features["momentum_6m"] - aligned_benchmark.pct_change(126)
        features["relative_strength_20d"] = close.pct_change(20) - aligned_benchmark.pct_change(20)

        ma50 = close.rolling(50).mean()
        ma200 = close.rolling(200).mean()
        features["ma50"] = ma50
        features["ma200"] = ma200
        features["above_ma50"] = close > ma50
        features["above_ma200"] = close > ma200
        features["trend_score"] = (features["above_ma50"].astype(int) + features["above_ma200"].astype(int)) / 2

        recent_volume = volume.rolling(21).mean()
        base_volume = volume.rolling(63).mean()
        features["volume_increase"] = recent_volume / base_volume - 1
        features["avg_traded_value"] = (close * volume).rolling(21).mean()
        features["volatility"] = close.pct_change().rolling(63).std()
        feature_frames[symbol] = features

    return feature_frames


def _monthly_rebalance_dates(benchmark_prices: pd.DataFrame, start: pd.Timestamp, end: pd.Timestamp) -> list[pd.Timestamp]:
    dates = _clean_close(benchmark_prices).index
    dates = dates[(dates >= start) & (dates <= end)]
    if dates.empty:
        return []
    grouped = pd.Series(dates, index=dates)
    rebalances = [pd.Timestamp(date) for date in grouped.groupby(dates.to_period("M")).first().tolist()]
    latest = pd.Timestamp(dates[-1])
    if rebalances[-1] < latest:
        rebalances.append(latest)
    return rebalances


def _benchmark_risk_on(benchmark_prices: pd.DataFrame, asof: pd.Timestamp) -> bool:
    close = _clean_close(benchmark_prices)
    available = close[close.index <= asof]
    if len(available) < 200:
        return True
    ma200 = available.rolling(200).mean().iloc[-1]
    return bool(available.iloc[-1] > ma200)


def _snapshot_asof(feature_frames: dict[str, pd.DataFrame], asof: pd.Timestamp) -> pd.DataFrame:
    rows = []
    required = [
        "momentum_1m",
        "momentum_3m",
        "momentum_6m",
        "relative_strength_1m",
        "relative_strength_3m",
        "relative_strength_6m",
        "relative_strength_20d",
        "trend_score",
        "volume_increase",
        "avg_traded_value",
        "volatility",
    ]
    for symbol, features in feature_frames.items():
        valid = features.loc[features.index <= asof].dropna(subset=required)
        if valid.empty:
            continue
        row = valid.iloc[-1].copy()
        row["symbol"] = symbol
        row["signal_date"] = valid.index[-1]
        rows.append(row)
    if not rows:
        return pd.DataFrame()
    return pd.DataFrame(rows).set_index("symbol")


def _survival_score(snapshot: pd.DataFrame) -> pd.Series:
    score = pd.Series(0.0, index=snapshot.index)
    score += SCORE_WEIGHTS["relative_strength_3m"] * _cross_sectional_score(snapshot["relative_strength_3m"]).fillna(0)
    score += SCORE_WEIGHTS["relative_strength_1m"] * _cross_sectional_score(snapshot["relative_strength_1m"]).fillna(0)
    score += SCORE_WEIGHTS["relative_strength_6m"] * _cross_sectional_score(snapshot["relative_strength_6m"]).fillna(0)
    score += SCORE_WEIGHTS["trend_score"] * _cross_sectional_score(snapshot["trend_score"]).fillna(0)
    score += SCORE_WEIGHTS["volume_increase"] * _cross_sectional_score(snapshot["volume_increase"]).fillna(0)
    score += SCORE_WEIGHTS["low_volatility"] * _cross_sectional_score(
        snapshot["volatility"],
        higher_is_better=False,
    ).fillna(0)
    return score


def _old_score(snapshot: pd.DataFrame) -> pd.Series:
    score = pd.Series(0.0, index=snapshot.index)
    score += OLD_SCORE_WEIGHTS["momentum_1m"] * _cross_sectional_score(snapshot["momentum_1m"]).fillna(0)
    score += OLD_SCORE_WEIGHTS["momentum_3m"] * _cross_sectional_score(snapshot["momentum_3m"]).fillna(0)
    score += OLD_SCORE_WEIGHTS["momentum_6m"] * _cross_sectional_score(snapshot["momentum_6m"]).fillna(0)
    score += OLD_SCORE_WEIGHTS["volume_increase"] * _cross_sectional_score(snapshot["volume_increase"]).fillna(0)
    score += OLD_SCORE_WEIGHTS["trend_score"] * _cross_sectional_score(snapshot["trend_score"]).fillna(0)
    score += OLD_SCORE_WEIGHTS["low_volatility"] * _cross_sectional_score(
        snapshot["volatility"],
        higher_is_better=False,
    ).fillna(0)
    return score


def _rank_snapshot(
    snapshot: pd.DataFrame,
    policy: SurvivalPolicy,
    min_avg_traded_value: float,
    max_volatility: float,
) -> pd.DataFrame:
    ranked = snapshot.copy()
    if policy.use_hard_filters:
        ranked = ranked[
            (ranked["above_ma50"])
            & (ranked["relative_strength_20d"] > 0)
            & (ranked["avg_traded_value"] >= min_avg_traded_value)
            & (ranked["volatility"] <= max_volatility)
        ].copy()
    if ranked.empty:
        return pd.DataFrame()

    ranked["score"] = _survival_score(ranked) if policy.mode == "survival" else _old_score(ranked)
    ranked = ranked.sort_values("score", ascending=False).reset_index()
    ranked["rank"] = range(1, len(ranked) + 1)
    return ranked


def _turnover(previous: dict[str, float], current: dict[str, float]) -> tuple[float, int]:
    all_symbols = set(previous) | set(current)
    turnover = float(sum(abs(current.get(symbol, 0.0) - previous.get(symbol, 0.0)) for symbol in all_symbols))
    trades = len(set(current) - set(previous)) + len(set(previous) - set(current))
    return turnover, trades


def _simulate_policy(
    policy: SurvivalPolicy,
    stock_prices: dict[str, pd.DataFrame],
    benchmark_prices: pd.DataFrame,
    feature_frames: dict[str, pd.DataFrame],
    start: pd.Timestamp,
    end: pd.Timestamp,
    transaction_cost: float,
    min_avg_traded_value: float,
    max_volatility: float,
) -> tuple[pd.DataFrame, pd.DataFrame]:
    rebalances = _monthly_rebalance_dates(benchmark_prices, start, end)
    if len(rebalances) < 2:
        return pd.DataFrame(), pd.DataFrame()

    equity = 1.0
    benchmark_equity = 1.0
    previous_weights: dict[str, float] = {}
    result_rows = []
    trade_rows = []

    for start_date, end_date in zip(rebalances[:-1], rebalances[1:]):
        benchmark_return = _period_return(benchmark_prices, start_date, end_date) or 0.0
        selected = pd.DataFrame()
        current_weights: dict[str, float] = {}
        risk_on = _benchmark_risk_on(benchmark_prices, start_date)
        cash_mode = policy.use_regime_cash and not risk_on

        if policy.mode == "benchmark":
            gross_return = benchmark_return
            holdings = 0
        elif cash_mode:
            gross_return = 0.0
            holdings = 0
        else:
            snapshot = _snapshot_asof(feature_frames, start_date)
            ranked = _rank_snapshot(snapshot, policy, min_avg_traded_value, max_volatility)
            selected = ranked.head(policy.portfolio_size).copy()
            holdings = len(selected)
            if selected.empty:
                gross_return = 0.0
            else:
                current_weights = {symbol: 1.0 / holdings for symbol in selected["symbol"]}
                returns = [
                    _period_return(stock_prices[symbol], start_date, end_date)
                    for symbol in selected["symbol"]
                ]
                returns = [value for value in returns if value is not None]
                gross_return = float(sum(returns) / len(returns)) if returns else 0.0

        turnover, trade_count = _turnover(previous_weights, current_weights)
        cost = 0.0 if policy.mode == "benchmark" else transaction_cost * turnover
        net_return = gross_return - cost
        equity *= 1 + net_return
        benchmark_equity *= 1 + benchmark_return

        selected_symbols = ", ".join(selected["symbol"]) if not selected.empty else ""
        result_rows.append(
            {
                "policy_id": policy.policy_id,
                "policy_name": policy.policy_name,
                "start_date": start_date,
                "end_date": end_date,
                "risk_on": risk_on,
                "cash_mode": cash_mode,
                "holdings": holdings,
                "selected_symbols": selected_symbols,
                "gross_return": gross_return,
                "transaction_cost_impact": cost,
                "net_return": net_return,
                "benchmark_return": benchmark_return,
                "excess_return": net_return - benchmark_return,
                "turnover": turnover,
                "trades": trade_count,
                "equity": equity,
                "benchmark_equity": benchmark_equity,
            }
        )

        for _, row in selected.iterrows():
            stock_return = _period_return(stock_prices[row["symbol"]], start_date, end_date)
            trade_rows.append(
                {
                    "policy_id": policy.policy_id,
                    "policy_name": policy.policy_name,
                    "date": start_date,
                    "symbol": row["symbol"],
                    "rank": row["rank"],
                    "score": row["score"],
                    "relative_strength_1m": row["relative_strength_1m"],
                    "relative_strength_3m": row["relative_strength_3m"],
                    "relative_strength_6m": row["relative_strength_6m"],
                    "relative_strength_20d": row["relative_strength_20d"],
                    "trend_score": row["trend_score"],
                    "volume_increase": row["volume_increase"],
                    "volatility": row["volatility"],
                    "avg_traded_value": row["avg_traded_value"],
                    "forward_return": stock_return,
                }
            )

        previous_weights = current_weights

    return pd.DataFrame(result_rows), pd.DataFrame(trade_rows)


def _max_drawdown(equity: pd.Series) -> float:
    if equity.empty:
        return 0.0
    return float((equity / equity.cummax() - 1).min())


def _cagr(total_return: float, start: pd.Timestamp, end: pd.Timestamp) -> float:
    years = max((end - start).days / 365.25, 1 / 365.25)
    return float((1 + total_return) ** (1 / years) - 1)


def _summarize(results: pd.DataFrame) -> dict[str, object]:
    group = results.sort_values("start_date").copy()
    total_return = float(group["equity"].iloc[-1] - 1)
    benchmark_total_return = float(group["benchmark_equity"].iloc[-1] - 1)
    start = pd.Timestamp(group["start_date"].iloc[0])
    end = pd.Timestamp(group["end_date"].iloc[-1])
    cagr = _cagr(total_return, start, end)
    benchmark_cagr = _cagr(benchmark_total_return, start, end)
    worst_idx = group["excess_return"].idxmin()
    best_idx = group["excess_return"].idxmax()
    std = group["net_return"].std()
    sharpe_proxy = 0.0 if std == 0 or pd.isna(std) else float((group["net_return"].mean() / std) * (12 ** 0.5))
    return {
        "policy_id": group["policy_id"].iloc[0],
        "policy_name": group["policy_name"].iloc[0],
        "months": len(group),
        "total_return": total_return,
        "bist100_total_return": benchmark_total_return,
        "cagr": cagr,
        "bist100_cagr": benchmark_cagr,
        "excess_cagr": cagr - benchmark_cagr,
        "max_drawdown": _max_drawdown(group["equity"]),
        "bist100_max_drawdown": _max_drawdown(group["benchmark_equity"]),
        "sharpe_proxy": sharpe_proxy,
        "monthly_win_rate_vs_bist100": float((group["excess_return"] > 0).mean()),
        "average_monthly_excess_return": float(group["excess_return"].mean()),
        "worst_month": pd.Timestamp(group.loc[worst_idx, "start_date"]).strftime("%Y-%m"),
        "worst_month_excess": float(group.loc[worst_idx, "excess_return"]),
        "best_month": pd.Timestamp(group.loc[best_idx, "start_date"]).strftime("%Y-%m"),
        "best_month_excess": float(group.loc[best_idx, "excess_return"]),
        "average_turnover": float(group["turnover"].mean()),
        "average_trades_per_month": float(group["trades"].mean()),
        "cash_months": int(group["cash_mode"].sum()),
        "average_holdings": float(group["holdings"].mean()),
        "transaction_cost_impact": float(group["transaction_cost_impact"].sum()),
    }


def _format_percent(value: float) -> str:
    return f"{value:.2%}"


def _write_report(
    summary: pd.DataFrame,
    detail: pd.DataFrame,
    latest_selection: pd.DataFrame,
    universe: pd.DataFrame,
    path: Path,
    start: pd.Timestamp,
    end: pd.Timestamp,
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
        "worst_month_excess",
        "best_month_excess",
        "average_turnover",
        "transaction_cost_impact",
    ]
    for column in percent_columns:
        display[column] = display[column].map(_format_percent)

    survival = summary[summary["policy_id"].str.startswith("RS_TOP")].copy()
    benchmark_row = summary[summary["policy_id"] == "BENCHMARK"].iloc[0]
    raw_best = survival.sort_values(["excess_cagr", "sharpe_proxy"], ascending=False).head(1)
    survival_eligible = survival[
        (survival["excess_cagr"] > 0)
        & (survival["max_drawdown"] >= benchmark_row["max_drawdown"])
    ].copy()
    best = survival_eligible.sort_values(["excess_cagr", "sharpe_proxy"], ascending=False).head(1)
    if best.empty:
        recommendation = "No live survival candidate passed both excess-return and drawdown tests."
    else:
        row = best.iloc[0]
        recommendation = (
            f"Survival candidate: {row['policy_name']} "
            f"(excess CAGR {row['excess_cagr']:.2%}, max drawdown {row['max_drawdown']:.2%})."
        )
    raw_best_note = ""
    if not raw_best.empty:
        row = raw_best.iloc[0]
        raw_best_note = (
            f"Best raw-return policy was {row['policy_name']} "
            f"(excess CAGR {row['excess_cagr']:.2%}, max drawdown {row['max_drawdown']:.2%}), "
            "but it is not automatically accepted for survival mode if drawdown is worse than BIST100."
        )

    latest_for_report = latest_selection.copy()
    if not latest_for_report.empty:
        latest_for_report = latest_for_report[
            [
                "policy_id",
                "date",
                "symbol",
                "rank",
                "score",
                "relative_strength_1m",
                "relative_strength_3m",
                "relative_strength_6m",
                "trend_score",
                "volatility",
            ]
        ].head(30)

    lines = [
        "# BIST100 Relative Strength Survival Backtest",
        "",
        f"- Period: {start.date()} to {end.date()}",
        f"- Configured BIST100 symbols: {len(universe)}",
        f"- Loaded symbols: {int(universe['loaded'].sum())}",
        f"- Missing/no valid data symbols: {int((~universe['loaded']).sum())}",
        "- Production tracking_state.json was not modified.",
        "",
        "## Policy Summary",
        "",
        display.to_markdown(index=False),
        "",
        "## Decision",
        "",
        recommendation,
        "",
        raw_best_note,
        "",
        (
            "For survival mode, prefer policies that beat BIST100 after transaction costs and do not rely on "
            "one lucky month. The stricter live-readiness test also requires max drawdown no worse than BIST100."
        ),
        "",
        "## Latest Survival Selections",
        "",
        latest_for_report.to_markdown(index=False, floatfmt=".4f") if not latest_for_report.empty else "No latest selection.",
        "",
        "## Notes",
        "",
        "- Strategy uses only data available at each rebalance date.",
        "- Hard filters: stock above MA50, 20-day relative strength above BIST100, liquidity floor, volatility cap.",
        "- Regime cash filter: no stock exposure when BIST100 is below MA200.",
        "- Missing tickers are excluded and never substituted.",
        "",
    ]
    path.write_text("\n".join(lines), encoding="utf-8")


def run_bist100_survival_backtest(
    stock_prices: dict[str, pd.DataFrame],
    benchmark_prices: pd.DataFrame,
    configured_symbols: list[str],
    results_dir: str,
    transaction_cost: float = 0.002,
    years: int = 3,
    min_avg_traded_value: float = 5_000_000,
    max_volatility: float = 0.06,
) -> dict[str, Path]:
    Path(results_dir).mkdir(exist_ok=True)
    benchmark_latest = pd.Timestamp(_clean_close(benchmark_prices).index.max())
    start = benchmark_latest - pd.DateOffset(years=years)

    feature_frames = _build_features(stock_prices, benchmark_prices)
    loaded_symbols = set(feature_frames)
    universe = pd.DataFrame(
        [
            {
                "symbol": symbol,
                "loaded": symbol in loaded_symbols,
                "reason": "" if symbol in loaded_symbols else "no valid OHLCV data returned",
            }
            for symbol in configured_symbols
        ]
    )
    universe_path = Path(results_dir) / "bist100_survival_universe.csv"
    universe.to_csv(universe_path, index=False)

    detail_frames = []
    trade_frames = []
    summary_rows = []
    for policy in POLICIES:
        detail, trades = _simulate_policy(
            policy=policy,
            stock_prices=stock_prices,
            benchmark_prices=benchmark_prices,
            feature_frames=feature_frames,
            start=start,
            end=benchmark_latest,
            transaction_cost=transaction_cost,
            min_avg_traded_value=min_avg_traded_value,
            max_volatility=max_volatility,
        )
        if detail.empty:
            continue
        detail_frames.append(detail)
        if not trades.empty:
            trade_frames.append(trades)
        summary_rows.append(_summarize(detail))

    summary = pd.DataFrame(summary_rows).sort_values("policy_id")
    detail = pd.concat(detail_frames, ignore_index=True) if detail_frames else pd.DataFrame()
    trades = pd.concat(trade_frames, ignore_index=True) if trade_frames else pd.DataFrame()
    if trades.empty:
        latest_selection = pd.DataFrame()
    else:
        dated_trades = trades.copy()
        dated_trades["date"] = pd.to_datetime(dated_trades["date"])
        latest_dates = dated_trades.groupby("policy_id")["date"].transform("max")
        latest_selection = dated_trades[dated_trades["date"] == latest_dates].sort_values(["policy_id", "rank"])

    summary_path = Path(results_dir) / "bist100_survival_backtest.csv"
    detail_path = Path(results_dir) / "bist100_survival_monthly_detail.csv"
    trades_path = Path(results_dir) / "bist100_survival_trades.csv"
    latest_path = Path(results_dir) / "bist100_survival_latest_selection.csv"
    report_path = Path(results_dir) / "bist100_survival_backtest.md"

    summary.to_csv(summary_path, index=False)
    detail.to_csv(detail_path, index=False)
    trades.to_csv(trades_path, index=False)
    latest_selection.to_csv(latest_path, index=False)
    _write_report(summary, detail, latest_selection, universe, report_path, start, benchmark_latest)

    return {
        "report": report_path,
        "summary": summary_path,
        "detail": detail_path,
        "trades": trades_path,
        "latest_selection": latest_path,
        "universe": universe_path,
    }
