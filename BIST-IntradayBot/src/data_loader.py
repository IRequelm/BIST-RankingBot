from __future__ import annotations

from dataclasses import dataclass

import pandas as pd

import config


@dataclass
class IntradayDataset:
    interval: str | None
    prices: dict[str, pd.DataFrame]
    benchmark: pd.DataFrame
    warnings: list[str]


def _normalize_frame(frame: pd.DataFrame) -> pd.DataFrame:
    if frame.empty:
        return pd.DataFrame()

    if isinstance(frame.columns, pd.MultiIndex):
        frame.columns = frame.columns.get_level_values(0)

    frame = frame.rename(columns={col: str(col).title() for col in frame.columns})
    required = ["Open", "High", "Low", "Close", "Volume"]
    missing = [col for col in required if col not in frame.columns]
    if missing:
        return pd.DataFrame()

    frame = frame[required].dropna(subset=["Open", "High", "Low", "Close"]).copy()
    frame = frame[~frame.index.duplicated(keep="last")].sort_index()
    if hasattr(frame.index, "tz") and frame.index.tz is not None:
        frame.index = frame.index.tz_convert("Europe/Istanbul").tz_localize(None)
    return frame


def _download_symbol(symbol: str, interval: str, period: str) -> pd.DataFrame:
    try:
        import yfinance as yf
    except ImportError:
        return pd.DataFrame()

    try:
        cache_dir = config.DATA_DIR / "yfinance_cache"
        cache_dir.mkdir(parents=True, exist_ok=True)
        if hasattr(yf, "set_tz_cache_location"):
            yf.set_tz_cache_location(str(cache_dir))
        raw = yf.download(
            symbol,
            period=period,
            interval=interval,
            auto_adjust=False,
            progress=False,
            threads=False,
        )
    except Exception:
        return pd.DataFrame()
    return _normalize_frame(raw)


def fetch_intraday_data(
    symbols: list[str] | None = None,
    benchmark_symbol: str = config.BENCHMARK_SYMBOL,
) -> IntradayDataset:
    symbols = symbols or config.BIST_SYMBOLS
    warnings: list[str] = []

    for interval in config.PREFERRED_INTERVALS:
        period = config.YAHOO_PERIOD_BY_INTERVAL[interval]
        prices: dict[str, pd.DataFrame] = {}
        for symbol in symbols:
            frame = _download_symbol(symbol, interval=interval, period=period)
            if frame.empty:
                warnings.append(f"{symbol}: {interval} intraday data unavailable.")
                continue
            prices[symbol] = frame

        benchmark = _download_symbol(benchmark_symbol, interval=interval, period=period)
        if prices and not benchmark.empty:
            return IntradayDataset(interval=interval, prices=prices, benchmark=benchmark, warnings=warnings)

        warnings.append(f"{interval} data did not produce a usable intraday dataset; trying fallback.")

    return IntradayDataset(
        interval=None,
        prices={},
        benchmark=pd.DataFrame(),
        warnings=warnings + ["No usable Yahoo Finance intraday data found. Generated fallback warning report."],
    )


def latest_common_session(dataset: IntradayDataset) -> pd.Timestamp | None:
    if not dataset.prices or dataset.benchmark.empty:
        return None

    benchmark_dates = set(pd.Series(dataset.benchmark.index.date).unique())
    stock_dates: set = set()
    for frame in dataset.prices.values():
        stock_dates.update(pd.Series(frame.index.date).unique())

    common_dates = sorted(benchmark_dates.intersection(stock_dates))
    if not common_dates:
        return None
    return pd.Timestamp(common_dates[-1])


def session_slice(frame: pd.DataFrame, session_date: pd.Timestamp) -> pd.DataFrame:
    if frame.empty:
        return pd.DataFrame()
    mask = pd.Series(frame.index.date, index=frame.index) == session_date.date()
    return frame.loc[mask].copy()
