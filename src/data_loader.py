from pathlib import Path

import pandas as pd
import yfinance as yf


def _cache_path(data_dir: str, symbol: str) -> Path:
    safe_symbol = symbol.replace(".", "_")
    return Path(data_dir) / f"{safe_symbol}.csv"


def fetch_price_data(
    symbols: list[str],
    start_date: str,
    end_date: str,
    data_dir: str,
    refresh: bool = False,
) -> dict[str, pd.DataFrame]:
    """Fetch daily OHLCV data from Yahoo Finance and cache it as CSV files."""
    Path(data_dir).mkdir(exist_ok=True)
    data: dict[str, pd.DataFrame] = {}

    for symbol in symbols:
        cache_file = _cache_path(data_dir, symbol)
        if cache_file.exists() and not refresh:
            df = pd.read_csv(cache_file, parse_dates=["Date"], index_col="Date")
        else:
            df = yf.download(
                symbol,
                start=start_date,
                end=end_date,
                auto_adjust=True,
                progress=False,
                group_by="column",
            )
            if df.empty:
                print(f"Warning: no data returned for {symbol}")
                continue

            # yfinance may return a MultiIndex when only one ticker is requested.
            if isinstance(df.columns, pd.MultiIndex):
                df.columns = df.columns.get_level_values(0)

            df.index.name = "Date"
            df.to_csv(cache_file)

        required_columns = {"Open", "High", "Low", "Close", "Volume"}
        if not required_columns.issubset(df.columns):
            print(f"Warning: missing required columns for {symbol}")
            continue

        data[symbol] = df.sort_index()

    return data


def find_missing_tickers(requested_symbols: list[str], loaded_data: dict[str, pd.DataFrame]) -> pd.DataFrame:
    """Return requested tickers that were excluded because no valid data loaded."""
    rows = []
    for symbol in requested_symbols:
        if symbol not in loaded_data:
            rows.append(
                {
                    "symbol": symbol,
                    "reason": "no valid OHLCV data returned",
                }
            )
    return pd.DataFrame(rows)
