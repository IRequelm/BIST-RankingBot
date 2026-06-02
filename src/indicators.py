import pandas as pd


def calculate_features(df: pd.DataFrame) -> pd.DataFrame:
    """Create ranking features from daily price data."""
    features = pd.DataFrame(index=df.index)
    close = df["Close"]
    volume = df["Volume"]

    features["momentum_1m"] = close.pct_change(21)
    features["momentum_3m"] = close.pct_change(63)
    features["momentum_6m"] = close.pct_change(126)

    recent_volume = volume.rolling(21).mean()
    base_volume = volume.rolling(63).mean()
    features["volume_increase"] = recent_volume / base_volume - 1

    ma50 = close.rolling(50).mean()
    ma200 = close.rolling(200).mean()
    features["above_ma"] = ((close > ma50).astype(int) + (close > ma200).astype(int)) / 2

    daily_returns = close.pct_change()
    features["volatility"] = daily_returns.rolling(63).std()

    return features


def get_forward_month_return(df: pd.DataFrame, ranking_date: pd.Timestamp) -> float | None:
    """Return next month performance from one month-end close to the next."""
    monthly_close = df["Close"].resample("ME").last()
    if ranking_date not in monthly_close.index:
        return None

    current_position = monthly_close.index.get_loc(ranking_date)
    next_position = current_position + 1
    if next_position >= len(monthly_close):
        return None

    current_close = monthly_close.iloc[current_position]
    next_close = monthly_close.iloc[next_position]
    if current_close <= 0:
        return None

    return (next_close / current_close) - 1
