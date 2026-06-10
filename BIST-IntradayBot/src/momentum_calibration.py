from __future__ import annotations

from dataclasses import dataclass
from itertools import product
from pathlib import Path

import pandas as pd

import config
from src.data_loader import _download_symbol, session_slice
from src.indicators import add_intraday_indicators


OPENING_STRENGTH_THRESHOLDS = [0.002, 0.003, 0.004, 0.005]
VOLUME_RATIO_THRESHOLDS = [1.00, 1.05, 1.10, 1.20]
LOOKBACK_DAYS = 20


@dataclass
class CalibrationDataset:
    interval: str | None
    prices: dict[str, pd.DataFrame]
    benchmark: pd.DataFrame
    session_dates: list[pd.Timestamp]
    warnings: list[str]


def _available_session_count(prices: dict[str, pd.DataFrame], benchmark: pd.DataFrame) -> int:
    if benchmark.empty:
        return 0
    benchmark_dates = set(pd.Series(benchmark.index.date).unique())
    stock_dates = set()
    for frame in prices.values():
        stock_dates.update(pd.Series(frame.index.date).unique())
    return len(benchmark_dates.intersection(stock_dates))


def load_calibration_dataset() -> CalibrationDataset:
    warnings: list[str] = []
    for interval in config.PREFERRED_INTERVALS:
        period = config.YAHOO_PERIOD_BY_INTERVAL[interval]
        prices: dict[str, pd.DataFrame] = {}
        for symbol in config.BIST_SYMBOLS:
            frame = _download_symbol(symbol, interval=interval, period=period)
            if frame.empty:
                warnings.append(f"{symbol}: {interval} intraday data unavailable.")
                continue
            prices[symbol] = frame
        benchmark = _download_symbol(config.BENCHMARK_SYMBOL, interval=interval, period=period)
        session_count = _available_session_count(prices, benchmark)
        if session_count >= LOOKBACK_DAYS:
            session_dates = _latest_session_dates(prices, benchmark, LOOKBACK_DAYS)
            return CalibrationDataset(interval, prices, benchmark, session_dates, warnings)
        warnings.append(
            f"{interval} data had only {session_count} usable sessions; need {LOOKBACK_DAYS}, trying fallback."
        )

    session_dates = _latest_session_dates(prices if "prices" in locals() else {}, benchmark if "benchmark" in locals() else pd.DataFrame(), LOOKBACK_DAYS)
    return CalibrationDataset(None, prices if "prices" in locals() else {}, benchmark if "benchmark" in locals() else pd.DataFrame(), session_dates, warnings)


def _latest_session_dates(
    prices: dict[str, pd.DataFrame],
    benchmark: pd.DataFrame,
    count: int,
) -> list[pd.Timestamp]:
    if benchmark.empty or not prices:
        return []
    benchmark_dates = set(pd.Series(benchmark.index.date).unique())
    stock_dates = set()
    for frame in prices.values():
        stock_dates.update(pd.Series(frame.index.date).unique())
    common_dates = sorted(benchmark_dates.intersection(stock_dates))
    return [pd.Timestamp(day) for day in common_dates[-count:]]


def _score(opening_strength: float, volume_ratio: float, above_vwap: bool, spike_warning: bool, extreme_volatility: bool) -> float:
    score = 0.0
    score += max(opening_strength, 0.0) * 100.0
    score += min(volume_ratio, 3.0) * 0.25
    score += 0.5 if above_vwap else -0.25
    score -= 1.0 if spike_warning else 0.0
    score -= 1.0 if extreme_volatility else 0.0
    return score


def _signal_row(symbol: str, frame: pd.DataFrame, opening_threshold: float, volume_threshold: float) -> dict:
    data = add_intraday_indicators(frame)
    signal_bar = data.iloc[min(3, len(data) - 1)]
    latest_bar = data.iloc[-1]
    opening_strength = float(signal_bar["return_from_open"])
    volume_ratio = float(signal_bar["volume_ratio"]) if pd.notna(signal_bar["volume_ratio"]) else 0.0
    above_vwap = bool(signal_bar["above_vwap"])
    spike_warning = (
        abs(opening_strength) > config.MAX_SPIKE_RETURN
        or float(signal_bar["candle_range_pct"]) > config.MAX_CANDLE_RANGE
    )
    extreme_volatility = float(latest_bar["intraday_volatility"]) > config.MAX_INTRADAY_VOLATILITY
    passes_momentum = opening_strength >= opening_threshold and volume_ratio >= volume_threshold
    passes_vwap = passes_momentum and above_vwap
    passes_mean_reversion = passes_vwap and not spike_warning
    passes_volatility = passes_mean_reversion and not extreme_volatility
    return {
        "symbol": symbol,
        "signal_time": signal_bar.name,
        "entry_price": float(signal_bar["Close"]),
        "opening_strength": opening_strength,
        "volume_ratio": volume_ratio,
        "above_vwap": above_vwap,
        "spike_warning": spike_warning,
        "extreme_volatility": extreme_volatility,
        "passes_momentum": passes_momentum,
        "passes_vwap": passes_vwap,
        "passes_mean_reversion": passes_mean_reversion,
        "passes_volatility": passes_volatility,
        "score": _score(opening_strength, volume_ratio, above_vwap, spike_warning, extreme_volatility),
    }


def _benchmark_return(benchmark_session: pd.DataFrame) -> float:
    if benchmark_session.empty or len(benchmark_session) < 2:
        return 0.0
    return float(benchmark_session["Close"].iloc[-1] / benchmark_session["Open"].iloc[0] - 1.0)


def _simulate_selected(selected: pd.DataFrame, session_prices: dict[str, pd.DataFrame]) -> float:
    if selected.empty:
        return 0.0
    position_size = config.STARTING_CAPITAL / config.MAX_ACTIVE_POSITIONS
    total_pnl = 0.0
    for _, signal in selected.head(config.MAX_ACTIVE_POSITIONS).iterrows():
        frame = session_prices[signal["symbol"]]
        entry_price = float(signal["entry_price"])
        exit_price = float(frame["Close"].iloc[-1])
        gross_return = exit_price / entry_price - 1.0
        cost_drag = 2.0 * (config.TRANSACTION_COST_RATE + config.SLIPPAGE_RATE)
        total_pnl += position_size * (gross_return - cost_drag)
    return total_pnl / config.STARTING_CAPITAL


def evaluate_day(
    session_date: pd.Timestamp,
    dataset: CalibrationDataset,
    opening_threshold: float,
    volume_threshold: float,
) -> dict:
    session_prices = {}
    signal_rows = []
    for symbol in config.BIST_SYMBOLS:
        frame = dataset.prices.get(symbol, pd.DataFrame())
        sliced = session_slice(frame, session_date)
        if sliced.empty or len(sliced) < 3:
            continue
        session_prices[symbol] = sliced
        signal_rows.append(_signal_row(symbol, sliced, opening_threshold, volume_threshold))

    signals = pd.DataFrame(signal_rows)
    if signals.empty:
        after_momentum = after_vwap = after_mean_reversion = final_candidates = 0
        selected = pd.DataFrame()
    else:
        after_momentum = int(signals["passes_momentum"].eq(True).sum())
        after_vwap = int(signals["passes_vwap"].eq(True).sum())
        after_mean_reversion = int(signals["passes_mean_reversion"].eq(True).sum())
        final_candidates = int(signals["passes_volatility"].eq(True).sum())
        selected = signals[signals["passes_volatility"].eq(True)].sort_values("score", ascending=False).head(
            config.MAX_ACTIVE_POSITIONS
        )

    benchmark_session = session_slice(dataset.benchmark, session_date)
    daily_return = _simulate_selected(selected, session_prices)
    benchmark_return = _benchmark_return(benchmark_session)
    return {
        "date": session_date.date().isoformat(),
        "interval": dataset.interval or "N/A",
        "opening_strength_threshold": opening_threshold,
        "volume_ratio_threshold": volume_threshold,
        "starting_universe": len(config.BIST_SYMBOLS),
        "data_available": len(session_prices),
        "after_momentum_filter": after_momentum,
        "after_vwap_filter": after_vwap,
        "after_mean_reversion_filter": after_mean_reversion,
        "after_volatility_filter": final_candidates,
        "final_candidates": final_candidates,
        "trades_taken": min(final_candidates, config.MAX_ACTIVE_POSITIONS),
        "selected_symbols": ", ".join(selected["symbol"].tolist()) if not selected.empty else "",
        "daily_return": daily_return,
        "bist100_return": benchmark_return,
        "excess_return": daily_return - benchmark_return,
    }


def _max_drawdown(returns: pd.Series) -> float:
    if returns.empty:
        return 0.0
    equity = (1.0 + returns).cumprod()
    drawdown = equity / equity.cummax() - 1.0
    return float(drawdown.min())


def summarize_results(results: pd.DataFrame) -> pd.DataFrame:
    rows = []
    for (opening_threshold, volume_threshold), group in results.groupby(
        ["opening_strength_threshold", "volume_ratio_threshold"]
    ):
        rows.append(
            {
                "opening_strength_threshold": opening_threshold,
                "volume_ratio_threshold": volume_threshold,
                "avg_trades_per_day": group["trades_taken"].mean(),
                "avg_candidates_per_day": group["final_candidates"].mean(),
                "win_rate": (group["daily_return"] > 0).mean(),
                "avg_daily_return": group["daily_return"].mean(),
                "avg_bist100_return": group["bist100_return"].mean(),
                "avg_excess_return": group["excess_return"].mean(),
                "worst_day": group["daily_return"].min(),
                "max_daily_drawdown": _max_drawdown(group["daily_return"]),
                "no_trade_days": int((group["trades_taken"] == 0).sum()),
            }
        )
    return pd.DataFrame(rows).sort_values(
        ["avg_excess_return", "avg_trades_per_day"],
        ascending=[False, False],
    )


def _format_percent(value: float) -> str:
    return f"{value:.2%}"


def _write_report(
    dataset: CalibrationDataset,
    results: pd.DataFrame,
    summary: pd.DataFrame,
    report_path: Path,
) -> None:
    current = results[
        (results["opening_strength_threshold"] == config.MIN_OPENING_STRENGTH)
        & (results["volume_ratio_threshold"] == config.MIN_VOLUME_RATIO)
    ].copy()
    best_excess = summary.iloc[0]
    trade_band = summary[
        (summary["avg_candidates_per_day"] >= 3.0)
        & (summary["avg_candidates_per_day"] <= 10.0)
    ].sort_values("avg_excess_return", ascending=False)

    if trade_band.empty:
        trade_band_text = "No tested combination produced 3-10 final candidates per day on average."
        trade_band_table = ""
    else:
        best_band = trade_band.iloc[0]
        trade_band_text = (
            f"{best_band['opening_strength_threshold']:.2%} opening strength and "
            f"{best_band['volume_ratio_threshold']:.2f} volume ratio produced "
            f"{best_band['avg_candidates_per_day']:.2f} candidates/day with the best excess return inside the 3-10 band."
        )
        trade_band_table = trade_band.head(8).to_markdown(index=False)

    current_summary = summary[
        (summary["opening_strength_threshold"] == config.MIN_OPENING_STRENGTH)
        & (summary["volume_ratio_threshold"] == config.MIN_VOLUME_RATIO)
    ].iloc[0]
    too_strict = current_summary["avg_trades_per_day"] < 1.5 or current_summary["no_trade_days"] >= len(current) / 2
    recommendation = (
        "Research suggests the current filter is too strict for trade frequency, but production should not be changed yet without a longer out-of-sample test."
        if too_strict
        else "Research does not show enough evidence that the current filter is too strict."
    )

    display_summary = summary.copy()
    for column in [
        "opening_strength_threshold",
        "win_rate",
        "avg_daily_return",
        "avg_bist100_return",
        "avg_excess_return",
        "worst_day",
        "max_daily_drawdown",
    ]:
        display_summary[column] = display_summary[column].map(_format_percent)
    display_summary["volume_ratio_threshold"] = display_summary["volume_ratio_threshold"].map(lambda value: f"{value:.2f}")

    current_display = current[
        [
            "date",
            "starting_universe",
            "data_available",
            "after_momentum_filter",
            "after_vwap_filter",
            "after_mean_reversion_filter",
            "after_volatility_filter",
            "final_candidates",
            "trades_taken",
            "daily_return",
            "bist100_return",
            "excess_return",
            "selected_symbols",
        ]
    ].copy()
    for column in ["daily_return", "bist100_return", "excess_return"]:
        current_display[column] = current_display[column].map(_format_percent)

    warnings_md = "\n".join(f"- {warning}" for warning in dataset.warnings) if dataset.warnings else "- No warnings."
    report = f"""# Momentum Filter Calibration

- Research only: production strategy thresholds were not changed.
- Universe source: same ticker list as BIST-RankingBot monthly bot.
- Universe size: {len(config.BIST_SYMBOLS)}
- Data interval used: {dataset.interval or "N/A"}
- Trading days tested: {len(dataset.session_dates)}
- Opening strength thresholds tested: {", ".join(_format_percent(value) for value in OPENING_STRENGTH_THRESHOLDS)}
- Volume ratio thresholds tested: {", ".join(f"{value:.2f}" for value in VOLUME_RATIO_THRESHOLDS)}
- Max trades per day remains capped at {config.MAX_ACTIVE_POSITIONS}; candidate counts can exceed actual trades taken.

## Clear Answers

- Is the current filter too strict? **{"Yes" if too_strict else "No"}**. Current thresholds average {current_summary['avg_trades_per_day']:.2f} trades/day and {current_summary['avg_candidates_per_day']:.2f} candidates/day, with {int(current_summary['no_trade_days'])} no-trade days.
- Which threshold combination gives 3-10 trades per day? Because paper trading is capped at {config.MAX_ACTIVE_POSITIONS} trades/day, no setting can average more than 3 actual trades/day without changing the trading rule. By candidate count: {trade_band_text}
- Which threshold combination has the best excess return? **{best_excess['opening_strength_threshold']:.2%} opening strength / {best_excess['volume_ratio_threshold']:.2f} volume ratio**, average excess return **{best_excess['avg_excess_return']:.2%}** per tested day.
- Should production thresholds be changed? **Not yet.** {recommendation}

## Current Production Threshold Daily Funnel

{current_display.to_markdown(index=False)}

## Threshold Combination Summary

{display_summary.to_markdown(index=False)}

## 3-10 Candidate Band

{trade_band_table or trade_band_text}

## Warnings

{warnings_md}
"""
    report_path.write_text(report, encoding="utf-8")


def run_calibration() -> tuple[Path, Path]:
    config.REPORTS_DIR.mkdir(exist_ok=True)
    dataset = load_calibration_dataset()
    rows = []
    for opening_threshold, volume_threshold in product(OPENING_STRENGTH_THRESHOLDS, VOLUME_RATIO_THRESHOLDS):
        for session_date in dataset.session_dates:
            rows.append(evaluate_day(session_date, dataset, opening_threshold, volume_threshold))

    results = pd.DataFrame(rows)
    csv_path = config.REPORTS_DIR / "momentum_filter_calibration.csv"
    report_path = config.REPORTS_DIR / "momentum_filter_calibration.md"
    if results.empty:
        csv_path.write_text("", encoding="utf-8")
        report_path.write_text("No usable intraday calibration data was available.\n", encoding="utf-8")
        return report_path, csv_path

    summary = summarize_results(results)
    results.to_csv(csv_path, index=False)
    _write_report(dataset, results, summary, report_path)
    return report_path, csv_path


if __name__ == "__main__":
    report, csv = run_calibration()
    print(report.resolve())
    print(csv.resolve())
