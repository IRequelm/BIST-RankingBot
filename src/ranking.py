import pandas as pd

from src.indicators import calculate_features


def _cross_sectional_score(values: pd.Series, higher_is_better: bool = True) -> pd.Series:
    """Rank values from 0 to 1 across stocks for one month-end."""
    clean = values.replace([float("inf"), float("-inf")], pd.NA).dropna()
    if clean.empty:
        return pd.Series(dtype=float)

    return clean.rank(pct=True, ascending=higher_is_better)


def build_monthly_rankings(
    stock_prices: dict[str, pd.DataFrame],
    weights: dict[str, float],
) -> pd.DataFrame:
    """Rank all stocks at each month-end using weighted factor scores."""
    monthly_rows = []

    feature_frames = {
        symbol: calculate_features(df).resample("ME").last()
        for symbol, df in stock_prices.items()
    }

    all_dates = sorted(set().union(*(frame.index for frame in feature_frames.values())))

    for ranking_date in all_dates:
        raw_rows = []
        for symbol, features in feature_frames.items():
            if ranking_date not in features.index:
                continue
            row = features.loc[ranking_date].copy()
            row["symbol"] = symbol
            row["date"] = ranking_date
            raw_rows.append(row)

        if not raw_rows:
            continue

        month_df = pd.DataFrame(raw_rows).set_index("symbol")
        required = ["momentum_1m", "momentum_3m", "momentum_6m", "volume_increase", "above_ma", "volatility"]
        month_df = month_df.dropna(subset=required)
        if month_df.empty:
            continue

        score = pd.Series(0.0, index=month_df.index)
        score += weights["momentum_1m"] * _cross_sectional_score(month_df["momentum_1m"])
        score += weights["momentum_3m"] * _cross_sectional_score(month_df["momentum_3m"])
        score += weights["momentum_6m"] * _cross_sectional_score(month_df["momentum_6m"])
        score += weights["volume_increase"] * _cross_sectional_score(month_df["volume_increase"])
        score += weights["above_ma"] * _cross_sectional_score(month_df["above_ma"])
        score += weights["volatility_penalty"] * _cross_sectional_score(
            month_df["volatility"],
            higher_is_better=False,
        )

        month_df["score"] = score
        month_df = month_df.sort_values("score", ascending=False)
        month_df["rank"] = range(1, len(month_df) + 1)
        month_df["date"] = ranking_date
        monthly_rows.append(month_df.reset_index())

    if not monthly_rows:
        return pd.DataFrame()

    columns = [
        "date",
        "rank",
        "symbol",
        "score",
        "momentum_1m",
        "momentum_3m",
        "momentum_6m",
        "volume_increase",
        "above_ma",
        "volatility",
    ]
    return pd.concat(monthly_rows, ignore_index=True)[columns]
