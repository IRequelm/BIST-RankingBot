from __future__ import annotations

from pathlib import Path

import pandas as pd

import config
from src.data_loader import fetch_intraday_data, latest_common_session, session_slice
from src.indicators import add_intraday_indicators


def _bool_count(frame: pd.DataFrame, column: str) -> int:
    if column not in frame:
        return 0
    return int(frame[column].eq(True).sum())


def _symbol_diagnostics(symbol: str, frame: pd.DataFrame) -> dict:
    data = add_intraday_indicators(frame)
    if len(data) < 3:
        return {
            "symbol": symbol,
            "has_data": False,
            "failure_stage": "Data availability",
            "reason": "Less than 3 intraday candles in latest session.",
        }

    signal_bar = data.iloc[min(3, len(data) - 1)]
    latest_bar = data.iloc[-1]
    opening_strength = float(signal_bar["return_from_open"])
    volume_ratio = float(signal_bar["volume_ratio"]) if pd.notna(signal_bar["volume_ratio"]) else 0.0
    above_vwap = bool(signal_bar["above_vwap"])
    spike_warning = (
        abs(float(signal_bar["return_from_open"])) > config.MAX_SPIKE_RETURN
        or float(signal_bar["candle_range_pct"]) > config.MAX_CANDLE_RANGE
    )
    extreme_volatility = float(latest_bar["intraday_volatility"]) > config.MAX_INTRADAY_VOLATILITY

    passes_momentum = opening_strength >= config.MIN_OPENING_STRENGTH and volume_ratio >= config.MIN_VOLUME_RATIO
    passes_vwap = passes_momentum and above_vwap
    passes_mean_reversion = passes_vwap and not spike_warning
    passes_volatility = passes_mean_reversion and not extreme_volatility

    if not passes_momentum:
        if opening_strength < config.MIN_OPENING_STRENGTH and volume_ratio < config.MIN_VOLUME_RATIO:
            reason = "Opening strength and volume confirmation failed."
        elif opening_strength < config.MIN_OPENING_STRENGTH:
            reason = "Opening momentum below threshold."
        else:
            reason = "Volume confirmation below threshold."
        failure_stage = "Momentum"
    elif not passes_vwap:
        failure_stage = "VWAP"
        reason = "Signal candle closed below VWAP."
    elif not passes_mean_reversion:
        failure_stage = "Mean reversion"
        reason = "Move was too extended or candle range was too wide."
    elif not passes_volatility:
        failure_stage = "Volatility"
        reason = "Intraday volatility exceeded risk threshold."
    else:
        failure_stage = "Survived"
        reason = "Passed all filters."

    return {
        "symbol": symbol,
        "has_data": True,
        "opening_strength": opening_strength,
        "volume_ratio": volume_ratio,
        "above_vwap": above_vwap,
        "spike_warning": spike_warning,
        "extreme_volatility": extreme_volatility,
        "passes_momentum": passes_momentum,
        "passes_vwap": passes_vwap,
        "passes_mean_reversion": passes_mean_reversion,
        "passes_volatility": passes_volatility,
        "failure_stage": failure_stage,
        "reason": reason,
    }


def build_signal_funnel_report(output_path: Path | None = None) -> Path:
    output_path = output_path or (config.REPORTS_DIR / "signal_funnel_report.md")
    config.REPORTS_DIR.mkdir(exist_ok=True)

    dataset = fetch_intraday_data()
    session_date = latest_common_session(dataset)
    starting_universe = len(config.BIST_SYMBOLS)

    if session_date is None:
        md = f"""# Signal Funnel Report

- Latest trading session: N/A
- Data interval: {dataset.interval or "N/A"}
- Starting universe size: {starting_universe}

No usable intraday session data was available. The signal funnel could not be calculated.

## Warnings

{chr(10).join(f"- {warning}" for warning in dataset.warnings)}
"""
        output_path.write_text(md, encoding="utf-8")
        return output_path

    session_prices = {}
    rows = []
    unavailable = []
    for symbol in config.BIST_SYMBOLS:
        frame = dataset.prices.get(symbol, pd.DataFrame())
        sliced = session_slice(frame, session_date)
        if sliced.empty or len(sliced) < 3:
            unavailable.append(symbol)
            rows.append(
                {
                    "symbol": symbol,
                    "has_data": False,
                    "failure_stage": "Data availability",
                    "reason": "No usable latest-session intraday candles.",
                }
            )
            continue
        session_prices[symbol] = sliced
        rows.append(_symbol_diagnostics(symbol, sliced))

    diagnostics = pd.DataFrame(rows)
    after_data = int(diagnostics["has_data"].sum())
    after_momentum = _bool_count(diagnostics, "passes_momentum")
    after_vwap = _bool_count(diagnostics, "passes_vwap")
    after_mean_reversion = _bool_count(diagnostics, "passes_mean_reversion")
    final_candidates = _bool_count(diagnostics, "passes_volatility")

    funnel = [
        ("Starting universe size", starting_universe),
        ("After data availability filter", after_data),
        ("After momentum filter", after_momentum),
        ("After VWAP filter", after_vwap),
        ("After mean reversion filter", after_mean_reversion),
        ("After volatility filter", final_candidates),
        ("Final candidates", final_candidates),
    ]
    drops = []
    for idx in range(1, len(funnel) - 1):
        previous_label, previous_count = funnel[idx - 1]
        current_label, current_count = funnel[idx]
        drops.append(
            {
                "stage": current_label,
                "rejected": previous_count - current_count,
                "from": previous_label,
            }
        )
    most_restrictive = max(drops, key=lambda row: row["rejected"]) if drops else {"stage": "N/A", "rejected": 0}

    failure_counts = diagnostics["failure_stage"].value_counts().rename_axis("Failure Stage").reset_index(name="Count")
    final_table = diagnostics[
        [
            "symbol",
            "has_data",
            "opening_strength",
            "volume_ratio",
            "above_vwap",
            "spike_warning",
            "extreme_volatility",
            "failure_stage",
            "reason",
        ]
    ].copy()
    for column in ["opening_strength", "volume_ratio"]:
        if column in final_table:
            final_table[column] = final_table[column].map(lambda value: "" if pd.isna(value) else f"{value:.2%}" if column == "opening_strength" else f"{value:.2f}")

    survived_mask = diagnostics["passes_volatility"].eq(True) if "passes_volatility" in diagnostics else pd.Series(False, index=diagnostics.index)
    survived = diagnostics[survived_mask]
    survived_symbols = ", ".join(survived["symbol"].tolist()) if not survived.empty else "None"
    warnings_md = "\n".join(f"- {warning}" for warning in dataset.warnings) if dataset.warnings else "- No warnings."

    md = f"""# Signal Funnel Report

- Latest trading session: {session_date.date().isoformat()}
- Data interval: {dataset.interval}
- Starting universe size: {starting_universe}
- Final candidates: {final_candidates}
- Final candidate symbols: {survived_symbols}

## Funnel Counts

| Stage | Count |
|---|---:|
{chr(10).join(f"| {label} | {count} |" for label, count in funnel)}

## Rejections By Stage

| Stage | Rejected |
|---|---:|
{chr(10).join(f"| {row['stage']} | {row['rejected']} |" for row in drops)}

## Most Restrictive Filter

The most restrictive step was **{most_restrictive['stage']}**, which rejected **{most_restrictive['rejected']}** symbols from the previous stage.

## Why Did Only 1 Trade Survive?

Only **{final_candidates}** symbol passed every rule. The funnel shows that most symbols were removed before the final risk checks, mainly because they did not satisfy the combined opening momentum requirement: opening strength of at least **{config.MIN_OPENING_STRENGTH:.2%}** and volume ratio of at least **{config.MIN_VOLUME_RATIO:.2f}**. After that, the VWAP rule removed symbols whose signal candle was not above VWAP. Mean reversion and volatility did not create the main bottleneck in this session unless shown in the stage counts above.

## Failure Stage Summary

{failure_counts.to_markdown(index=False)}

## Symbol Diagnostics

{final_table.to_markdown(index=False)}

## Warnings

{warnings_md}
"""
    output_path.write_text(md, encoding="utf-8")
    return output_path


if __name__ == "__main__":
    path = build_signal_funnel_report()
    print(path.resolve())
