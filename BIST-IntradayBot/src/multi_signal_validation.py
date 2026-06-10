from __future__ import annotations

from pathlib import Path

import pandas as pd

import config
from src.data_loader import session_slice
from src.indicators import add_intraday_indicators
from src.momentum_calibration import (
    _benchmark_return,
    _max_drawdown,
    _simulate_selected,
    evaluate_day,
    load_calibration_dataset,
)


def _previous_session(frame: pd.DataFrame, session_date: pd.Timestamp) -> pd.DataFrame:
    if frame.empty:
        return pd.DataFrame()
    dates = sorted(pd.Series(frame.index.date).unique())
    previous_dates = [day for day in dates if day < session_date.date()]
    if not previous_dates:
        return pd.DataFrame()
    return session_slice(frame, pd.Timestamp(previous_dates[-1]))


def _safe_return(numerator: float, denominator: float) -> float:
    if denominator == 0:
        return 0.0
    return numerator / denominator - 1.0


def _first_vwap_reclaim(data: pd.DataFrame) -> pd.Series | None:
    if len(data) < 3:
        return None
    below_before = data["Close"].shift(1) <= data["vwap"].shift(1)
    above_now = data["Close"] > data["vwap"]
    reclaim = data[below_before & above_now & (data["volume_ratio"] >= 1.0)]
    if reclaim.empty:
        return None
    return reclaim.iloc[0]


def _multi_signal_row(
    symbol: str,
    frame: pd.DataFrame,
    previous_frame: pd.DataFrame,
    benchmark_session: pd.DataFrame,
) -> dict | None:
    data = add_intraday_indicators(frame)
    if len(data) < 3:
        return None

    signal_bar = data.iloc[min(3, len(data) - 1)]
    latest_bar = data.iloc[-1]
    previous_high = float(previous_frame["High"].max()) if not previous_frame.empty else float("nan")
    previous_close = float(previous_frame["Close"].iloc[-1]) if not previous_frame.empty else float("nan")

    benchmark_signal_return = 0.0
    if not benchmark_session.empty and len(benchmark_session) >= 3:
        benchmark_bar = benchmark_session.iloc[min(3, len(benchmark_session) - 1)]
        benchmark_signal_return = _safe_return(float(benchmark_bar["Close"]), float(benchmark_session["Open"].iloc[0]))

    opening_strength = float(signal_bar["return_from_open"])
    volume_ratio = float(signal_bar["volume_ratio"]) if pd.notna(signal_bar["volume_ratio"]) else 0.0
    above_vwap = bool(signal_bar["above_vwap"])
    spike_warning = (
        abs(opening_strength) > config.MAX_SPIKE_RETURN
        or float(signal_bar["candle_range_pct"]) > config.MAX_CANDLE_RANGE
    )
    extreme_volatility = float(latest_bar["intraday_volatility"]) > config.MAX_INTRADAY_VOLATILITY

    momentum_score = 0.0
    if opening_strength >= config.MIN_OPENING_STRENGTH and volume_ratio >= config.MIN_VOLUME_RATIO and above_vwap:
        momentum_score = max(opening_strength, 0.0) * 100.0 + min(volume_ratio, 3.0) * 0.25 + 0.50

    relative_momentum = opening_strength - benchmark_signal_return
    relative_strength_score = 0.0
    if opening_strength > 0 and relative_momentum > 0.002:
        relative_strength_score = relative_momentum * 120.0 + min(volume_ratio, 2.0) * 0.15

    breakout_score = 0.0
    if pd.notna(previous_high) and float(signal_bar["Close"]) > previous_high and volume_ratio >= 1.0:
        breakout_pct = _safe_return(float(signal_bar["Close"]), previous_high)
        breakout_score = breakout_pct * 140.0 + min(volume_ratio, 2.5) * 0.20

    vwap_score = 0.0
    reclaim_bar = _first_vwap_reclaim(data)
    entry_bar = signal_bar
    signal_family = []
    if reclaim_bar is not None:
        reclaim_strength = _safe_return(float(reclaim_bar["Close"]), float(reclaim_bar["vwap"]))
        vwap_score = 0.40 + reclaim_strength * 100.0 + min(float(reclaim_bar["volume_ratio"]), 2.5) * 0.15
        entry_bar = reclaim_bar
        signal_family.append("VWAP_RECLAIM")

    gap_score = 0.0
    if pd.notna(previous_close):
        gap = _safe_return(float(data["Open"].iloc[0]), previous_close)
        continuation = float(signal_bar["Close"]) > float(data["Open"].iloc[0]) and above_vwap
        if gap > 0.002 and continuation:
            gap_score = gap * 100.0 + max(opening_strength, 0.0) * 50.0 + min(volume_ratio, 2.0) * 0.10

    if momentum_score > 0:
        signal_family.append("MOMENTUM")
    if relative_strength_score > 0:
        signal_family.append("RELATIVE_STRENGTH")
    if breakout_score > 0:
        signal_family.append("PREVIOUS_DAY_BREAKOUT")
    if gap_score > 0:
        signal_family.append("GAP_CONTINUATION")

    final_score = momentum_score + relative_strength_score + breakout_score + vwap_score + gap_score
    risk_pass = not spike_warning and not extreme_volatility
    if final_score <= 0 or not risk_pass:
        return None

    return {
        "symbol": symbol,
        "signal_time": entry_bar.name,
        "entry_price": float(entry_bar["Close"]),
        "momentum_score": momentum_score,
        "relative_strength_score": relative_strength_score,
        "breakout_score": breakout_score,
        "vwap_score": vwap_score,
        "gap_score": gap_score,
        "final_score": final_score,
        "families": ", ".join(signal_family),
        "opening_strength": opening_strength,
        "relative_momentum": relative_momentum,
        "volume_ratio": volume_ratio,
        "spike_warning": spike_warning,
        "extreme_volatility": extreme_volatility,
    }


def evaluate_multi_signal_day(session_date: pd.Timestamp, dataset) -> dict:
    session_prices = {}
    rows = []
    benchmark_session = session_slice(dataset.benchmark, session_date)

    for symbol in config.BIST_SYMBOLS:
        frame = dataset.prices.get(symbol, pd.DataFrame())
        sliced = session_slice(frame, session_date)
        if sliced.empty or len(sliced) < 3:
            continue
        previous_frame = _previous_session(frame, session_date)
        session_prices[symbol] = sliced
        row = _multi_signal_row(symbol, sliced, previous_frame, benchmark_session)
        if row:
            rows.append(row)

    signals = pd.DataFrame(rows)
    if signals.empty:
        selected = pd.DataFrame()
        family_counts = {}
    else:
        selected = signals.sort_values("final_score", ascending=False).head(config.MAX_ACTIVE_POSITIONS)
        family_counts = {
            "momentum_candidates": int((signals["momentum_score"] > 0).sum()),
            "relative_strength_candidates": int((signals["relative_strength_score"] > 0).sum()),
            "breakout_candidates": int((signals["breakout_score"] > 0).sum()),
            "vwap_candidates": int((signals["vwap_score"] > 0).sum()),
            "gap_candidates": int((signals["gap_score"] > 0).sum()),
        }

    daily_return = _simulate_selected(selected, session_prices)
    benchmark_return = _benchmark_return(benchmark_session)
    return {
        "date": session_date.date().isoformat(),
        "strategy": "New Multi-Signal",
        "interval": dataset.interval or "N/A",
        "starting_universe": len(config.BIST_SYMBOLS),
        "data_available": len(session_prices),
        "final_candidates": len(signals),
        "trades_taken": min(len(signals), config.MAX_ACTIVE_POSITIONS),
        "selected_symbols": ", ".join(selected["symbol"].tolist()) if not selected.empty else "",
        "selected_families": " ; ".join(selected["families"].tolist()) if not selected.empty else "",
        "daily_return": daily_return,
        "bist100_return": benchmark_return,
        "excess_return": daily_return - benchmark_return,
        **family_counts,
    }


def _old_strategy_row(session_date: pd.Timestamp, dataset) -> dict:
    old = evaluate_day(
        session_date,
        dataset,
        opening_threshold=config.MIN_OPENING_STRENGTH,
        volume_threshold=config.MIN_VOLUME_RATIO,
    )
    return {
        "date": old["date"],
        "strategy": "Old Momentum-Only",
        "interval": old["interval"],
        "starting_universe": old["starting_universe"],
        "data_available": old["data_available"],
        "final_candidates": old["final_candidates"],
        "trades_taken": old["trades_taken"],
        "selected_symbols": old["selected_symbols"],
        "selected_families": "MOMENTUM",
        "daily_return": old["daily_return"],
        "bist100_return": old["bist100_return"],
        "excess_return": old["excess_return"],
        "momentum_candidates": old["final_candidates"],
        "relative_strength_candidates": 0,
        "breakout_candidates": 0,
        "vwap_candidates": 0,
        "gap_candidates": 0,
    }


def summarize(results: pd.DataFrame) -> pd.DataFrame:
    rows = []
    for strategy, group in results.groupby("strategy"):
        rows.append(
            {
                "strategy": strategy,
                "days": len(group),
                "trades_per_day": group["trades_taken"].mean(),
                "avg_candidates_per_day": group["final_candidates"].mean(),
                "no_trade_days": int((group["trades_taken"] == 0).sum()),
                "win_rate": (group["daily_return"] > 0).mean(),
                "avg_daily_return": group["daily_return"].mean(),
                "avg_bist100_return": group["bist100_return"].mean(),
                "avg_excess_return": group["excess_return"].mean(),
                "worst_day": group["daily_return"].min(),
                "drawdown": _max_drawdown(group["daily_return"]),
            }
        )
    return pd.DataFrame(rows).sort_values("strategy")


def _pct(value: float) -> str:
    return f"{value:.2%}"


def _write_report(results: pd.DataFrame, summary: pd.DataFrame, dataset, report_path: Path) -> None:
    old = summary[summary["strategy"] == "Old Momentum-Only"].iloc[0]
    new = summary[summary["strategy"] == "New Multi-Signal"].iloc[0]
    frequency_improved = new["trades_per_day"] > old["trades_per_day"] and new["no_trade_days"] < old["no_trade_days"]
    excess_improved = new["avg_excess_return"] > old["avg_excess_return"]
    replacement = frequency_improved and excess_improved and new["drawdown"] >= old["drawdown"]

    display_summary = summary.copy()
    for column in ["win_rate", "avg_daily_return", "avg_bist100_return", "avg_excess_return", "worst_day", "drawdown"]:
        display_summary[column] = display_summary[column].map(_pct)

    display_daily = results.copy()
    for column in ["daily_return", "bist100_return", "excess_return"]:
        display_daily[column] = display_daily[column].map(_pct)

    family_cols = [
        "momentum_candidates",
        "relative_strength_candidates",
        "breakout_candidates",
        "vwap_candidates",
        "gap_candidates",
    ]
    family_summary = (
        results[results["strategy"] == "New Multi-Signal"][family_cols]
        .mean()
        .rename_axis("signal_family")
        .reset_index(name="avg_candidates_per_day")
    )

    warnings_md = "\n".join(f"- {warning}" for warning in dataset.warnings) if dataset.warnings else "- No warnings."
    report = f"""# Multi-Signal Validation

- Research only: production signal engine was not changed.
- Data interval used: {dataset.interval or "N/A"}
- Trading days tested: {len(dataset.session_dates)}
- Universe size: {len(config.BIST_SYMBOLS)}
- Old strategy: existing momentum-only rules.
- New strategy: unified score = Momentum + Relative Strength + Breakout + VWAP Reclaim + Gap Continuation.
- Risk controls retained: mean-reversion spike warning and extreme intraday volatility filter.

## Clear Answers

- Did trade frequency improve? **{"Yes" if frequency_improved else "No"}**. Trades/day changed from **{old['trades_per_day']:.2f}** to **{new['trades_per_day']:.2f}**; no-trade days changed from **{int(old['no_trade_days'])}** to **{int(new['no_trade_days'])}**.
- Did excess return improve? **{"Yes" if excess_improved else "No"}**. Average excess return changed from **{old['avg_excess_return']:.2%}** to **{new['avg_excess_return']:.2%}**.
- Should multi-signal replace momentum-only? **{"Yes" if replacement else "Not yet"}**. The architecture should only replace production if frequency and excess return improve without worse drawdown.

## Strategy Comparison

{display_summary.to_markdown(index=False)}

## Signal Family Candidate Contribution

{family_summary.to_markdown(index=False)}

## Daily Replay Results

{display_daily.to_markdown(index=False)}

## Warnings

{warnings_md}
"""
    report_path.write_text(report, encoding="utf-8")


def run_validation() -> tuple[Path, Path]:
    config.REPORTS_DIR.mkdir(exist_ok=True)
    dataset = load_calibration_dataset()
    rows = []
    for session_date in dataset.session_dates:
        rows.append(_old_strategy_row(session_date, dataset))
        rows.append(evaluate_multi_signal_day(session_date, dataset))

    results = pd.DataFrame(rows)
    csv_path = config.REPORTS_DIR / "multi_signal_validation.csv"
    report_path = config.REPORTS_DIR / "multi_signal_validation.md"
    if results.empty:
        csv_path.write_text("", encoding="utf-8")
        report_path.write_text("No usable intraday validation data was available.\n", encoding="utf-8")
        return report_path, csv_path

    summary = summarize(results)
    results.to_csv(csv_path, index=False)
    _write_report(results, summary, dataset, report_path)
    return report_path, csv_path


if __name__ == "__main__":
    report, csv = run_validation()
    print(report.resolve())
    print(csv.resolve())
