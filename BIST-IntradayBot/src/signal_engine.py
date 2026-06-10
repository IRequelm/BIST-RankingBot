from __future__ import annotations

from dataclasses import dataclass

import pandas as pd

import config
from src.indicators import add_intraday_indicators


@dataclass
class SignalResult:
    selected: pd.DataFrame
    all_signals: pd.DataFrame
    missed_signals: pd.DataFrame
    market_status: str


def _signal_for_symbol(symbol: str, frame: pd.DataFrame) -> dict | None:
    data = add_intraday_indicators(frame)
    if len(data) < 3:
        return None

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

    score = 0.0
    score += max(opening_strength, 0.0) * 100.0
    score += min(volume_ratio, 3.0) * 0.25
    score += 0.5 if above_vwap else -0.25
    score -= 1.0 if spike_warning else 0.0
    score -= 1.0 if extreme_volatility else 0.0

    is_buy = (
        opening_strength >= config.MIN_OPENING_STRENGTH
        and volume_ratio >= config.MIN_VOLUME_RATIO
        and above_vwap
        and not spike_warning
        and not extreme_volatility
    )

    reasons = []
    reasons.append(f"opening_strength={opening_strength:.2%}")
    reasons.append(f"volume_ratio={volume_ratio:.2f}")
    reasons.append("above_vwap" if above_vwap else "below_vwap")
    if spike_warning:
        reasons.append("mean_reversion_warning")
    if extreme_volatility:
        reasons.append("extreme_intraday_volatility")

    return {
        "symbol": symbol,
        "signal_time": signal_bar.name,
        "entry_price": float(signal_bar["Close"]),
        "latest_price": float(latest_bar["Close"]),
        "opening_strength": opening_strength,
        "volume_ratio": volume_ratio,
        "above_vwap": above_vwap,
        "spike_warning": spike_warning,
        "extreme_volatility": extreme_volatility,
        "score": score,
        "signal": "BUY" if is_buy else "WATCH",
        "reason": "; ".join(reasons),
    }


def generate_signals(session_prices: dict[str, pd.DataFrame]) -> SignalResult:
    rows = []
    for symbol, frame in session_prices.items():
        row = _signal_for_symbol(symbol, frame)
        if row:
            rows.append(row)

    if not rows:
        empty = pd.DataFrame()
        return SignalResult(empty, empty, empty, "NO_INTRADAY_SIGNALS")

    all_signals = pd.DataFrame(rows).sort_values("score", ascending=False).reset_index(drop=True)
    buy_signals = all_signals[all_signals["signal"] == "BUY"].copy()
    selected = buy_signals.head(config.MAX_ACTIVE_POSITIONS).copy()
    missed = buy_signals.iloc[config.MAX_ACTIVE_POSITIONS :].copy()
    status = "SIGNALS_FOUND" if not selected.empty else "NO_BUY_SIGNALS"
    return SignalResult(selected, all_signals, missed, status)
