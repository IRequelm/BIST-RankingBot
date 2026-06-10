from __future__ import annotations

import pandas as pd


def add_intraday_indicators(frame: pd.DataFrame) -> pd.DataFrame:
    if frame.empty:
        return frame.copy()

    data = frame.copy()
    volume = data["Volume"].astype(float)
    safe_volume = volume.replace(0, float("nan"))
    typical_price = (data["High"] + data["Low"] + data["Close"]) / 3.0
    cumulative_volume = safe_volume.cumsum()
    data["vwap"] = (typical_price * volume).cumsum() / cumulative_volume
    data["return_from_open"] = data["Close"] / data["Open"].iloc[0] - 1.0
    data["bar_return"] = data["Close"].pct_change().fillna(0.0)
    data["candle_range_pct"] = ((data["High"] - data["Low"]) / data["Open"].replace(0, float("nan"))).fillna(0.0)
    data["intraday_volatility"] = (data["High"].cummax() - data["Low"].cummin()) / data["Open"].iloc[0]
    data["volume_ratio"] = (volume / volume.rolling(4, min_periods=1).mean().replace(0, float("nan"))).fillna(0.0)
    data["above_vwap"] = data["Close"] > data["vwap"]
    return data
