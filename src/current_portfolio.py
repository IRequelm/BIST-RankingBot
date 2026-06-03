from pathlib import Path

import pandas as pd

from src.indicators import calculate_features
from src.ranking import _cross_sectional_score


FACTOR_MAP = {
    "momentum_1m": ("momentum_1m", True),
    "momentum_3m": ("momentum_3m", True),
    "momentum_6m": ("momentum_6m", True),
    "volume_increase": ("volume_increase", True),
    "above_ma": ("above_ma", True),
    "volatility_penalty": ("volatility", False),
}

def _latest_feature_snapshot(stock_prices: dict[str, pd.DataFrame]) -> tuple[pd.DataFrame, pd.Timestamp]:
    rows = []
    latest_dates = []

    for symbol, prices in stock_prices.items():
        if prices.empty:
            continue
        features = calculate_features(prices)
        valid = features.dropna()
        if valid.empty:
            continue
        latest_date = valid.index.max()
        latest_dates.append(latest_date)
        row = valid.loc[latest_date].copy()
        row["symbol"] = symbol
        rows.append(row)

    if not rows:
        return pd.DataFrame(), pd.NaT

    snapshot_date = max(latest_dates)
    snapshot = pd.DataFrame(rows).set_index("symbol")
    return snapshot, pd.Timestamp(snapshot_date)


def _rank_snapshot(snapshot: pd.DataFrame, weights: dict[str, float], model: str) -> pd.DataFrame:
    ranked = snapshot.copy()
    score = pd.Series(0.0, index=ranked.index)

    for factor_name, weight in weights.items():
        source_column, higher_is_better = FACTOR_MAP[factor_name]
        percentile = _cross_sectional_score(ranked[source_column], higher_is_better=higher_is_better)
        contribution_column = f"{factor_name}_contribution"
        ranked[contribution_column] = weight * percentile
        score += ranked[contribution_column].fillna(0)

    ranked["score"] = score
    ranked = ranked.sort_values("score", ascending=False)
    ranked["rank"] = range(1, len(ranked) + 1)
    ranked["model"] = model

    contribution_columns = [f"{factor}_contribution" for factor in weights]
    for column in contribution_columns:
        relative_column = column.replace("_contribution", "_relative_contribution")
        ranked[relative_column] = ranked[column] / ranked["score"].replace(0, pd.NA)

    ranked = ranked.reset_index()
    return ranked


def _current_regime(benchmark_prices: pd.DataFrame) -> dict[str, object]:
    close = benchmark_prices["Close"].dropna().sort_index()
    ma200 = close.rolling(200).mean()
    latest_date = close.index.max()
    latest_close = close.loc[latest_date]
    latest_ma200 = ma200.loc[latest_date]
    below_ma200 = bool(latest_close < latest_ma200)

    return {
        "benchmark_date": pd.Timestamp(latest_date),
        "bist100_close": float(latest_close),
        "bist100_ma200": float(latest_ma200),
        "bist100_below_ma200": below_ma200,
        "regime_status": "BELOW_MA200_DEFENSIVE" if below_ma200 else "ABOVE_MA200_RISK_ON",
        "distance_to_ma200": float((latest_close / latest_ma200) - 1),
    }


def _previous_holdings(
    rankings_by_model: dict[str, pd.DataFrame],
    model: str,
    portfolio_size: int,
    snapshot_date: pd.Timestamp,
) -> set[str]:
    rankings = rankings_by_model.get(model)
    if rankings is None or rankings.empty:
        return set()

    dated = rankings.copy()
    dated["date"] = pd.to_datetime(dated["date"])
    previous_dates = sorted(dated.loc[dated["date"] < snapshot_date, "date"].unique())
    if not previous_dates:
        return set()

    previous_date = previous_dates[-1]
    previous = dated[dated["date"] == previous_date].sort_values("rank").head(portfolio_size)
    return set(previous["symbol"])


def _expected_return_band(
    symbol: str,
    model: str,
    score: float,
    factor_breakdown: pd.DataFrame | None,
) -> dict[str, float | None]:
    if factor_breakdown is None or factor_breakdown.empty:
        return {"expected_return_low": None, "expected_return_mid": None, "expected_return_high": None}

    history = factor_breakdown[
        (factor_breakdown["model"] == model)
        & (factor_breakdown["symbol"] == symbol)
        & (factor_breakdown["score"].between(score - 0.05, score + 0.05))
    ]

    if len(history) < 5:
        history = factor_breakdown[
            (factor_breakdown["model"] == model)
            & (factor_breakdown["score"].between(score - 0.05, score + 0.05))
        ]

    if history.empty:
        return {"expected_return_low": None, "expected_return_mid": None, "expected_return_high": None}

    returns = history["next_month_return"].dropna()
    return {
        "expected_return_low": returns.quantile(0.25),
        "expected_return_mid": returns.median(),
        "expected_return_high": returns.quantile(0.75),
    }


def _expected_return_action(
    expected_return_mid: float | None,
    in_recommended: bool,
    min_buy_expected_return: float,
) -> str:
    if expected_return_mid is None or pd.isna(expected_return_mid):
        return "HOLD" if in_recommended else "EXCLUDE"

    if expected_return_mid >= min_buy_expected_return:
        return "BUY" if in_recommended else "EXCLUDE"
    if expected_return_mid < 0:
        return "SELL"
    return "HOLD" if in_recommended else "EXCLUDE"


def _confidence_score(recommended: pd.DataFrame, regime: dict[str, object]) -> float:
    if recommended.empty:
        return 0.0

    score_component = min(float(recommended["score"].mean()), 1.0) * 60
    regime_component = min(abs(float(regime["distance_to_ma200"])) / 0.10, 1.0) * 20
    breadth_component = float((recommended["score"] > 0.60).mean()) * 20
    return round(score_component + regime_component + breadth_component, 2)


def generate_current_month_portfolio(
    stock_prices: dict[str, pd.DataFrame],
    benchmark_prices: pd.DataFrame,
    factor_models: dict[str, dict[str, float]],
    rankings_by_model: dict[str, pd.DataFrame],
    results_dir: str,
    base_model: str = "volume_heavy",
    base_portfolio_size: int = 10,
    defensive_model: str = "low_volatility",
    defensive_portfolio_size: int = 5,
    min_buy_expected_return: float = 0.10,
) -> tuple[pd.DataFrame, str]:
    """Generate current portfolio recommendation from existing regime/ranking framework."""
    Path(results_dir).mkdir(exist_ok=True)
    regime = _current_regime(benchmark_prices)

    snapshot, snapshot_date = _latest_feature_snapshot(stock_prices)
    if snapshot.empty:
        raise ValueError("No valid stock features available for current portfolio recommendation.")

    active_model = defensive_model if regime["bist100_below_ma200"] else base_model
    active_portfolio_size = defensive_portfolio_size if regime["bist100_below_ma200"] else base_portfolio_size

    top20 = _rank_snapshot(snapshot, factor_models[active_model], active_model).head(20)
    recommended_symbols = set(top20.head(active_portfolio_size)["symbol"])
    previous_symbols = _previous_holdings(rankings_by_model, active_model, active_portfolio_size, snapshot_date)

    factor_breakdown_path = Path(results_dir) / "factor_breakdown.csv"
    factor_breakdown = None
    if factor_breakdown_path.exists():
        factor_breakdown = pd.read_csv(factor_breakdown_path, parse_dates=["date"])

    rows = []
    for _, row in top20.iterrows():
        symbol = row["symbol"]
        in_recommended = symbol in recommended_symbols
        expected = _expected_return_band(symbol, active_model, row["score"], factor_breakdown)
        action = _expected_return_action(expected["expected_return_mid"], in_recommended, min_buy_expected_return)
        output = row.to_dict()
        output.update(expected)
        output.update(
            {
                "snapshot_date": snapshot_date,
                "benchmark_date": regime["benchmark_date"],
                "policy": "defensive_mode",
                "regime_status": regime["regime_status"],
                "bist100_close": regime["bist100_close"],
                "bist100_ma200": regime["bist100_ma200"],
                "bist100_below_ma200": regime["bist100_below_ma200"],
                "active_model": active_model,
                "active_portfolio_size": active_portfolio_size,
                "min_buy_expected_return": min_buy_expected_return,
                "recommended": in_recommended,
                "action": action,
            }
        )
        rows.append(output)

    report_df = pd.DataFrame(rows)
    confidence = _confidence_score(report_df[report_df["recommended"]], regime)
    report_df["confidence_score"] = confidence

    csv_path = Path(results_dir) / "current_month_portfolio.csv"
    report_df.to_csv(csv_path, index=False)

    buy_list = report_df[report_df["action"] == "BUY"]["symbol"].tolist()
    hold_list = report_df[report_df["action"] == "HOLD"]["symbol"].tolist()
    sell_list = report_df[report_df["action"] == "SELL"]["symbol"].tolist()
    excluded = report_df[~report_df["recommended"]].head(10)

    factor_columns = [
        "momentum_1m",
        "momentum_3m",
        "momentum_6m",
        "volume_increase",
        "above_ma",
        "volatility",
        "score",
    ]
    contribution_columns = [column for column in report_df.columns if column.endswith("_relative_contribution")]

    lines = [
        "# Current Month Portfolio Recommendation",
        "",
        f"- Policy: defensive_mode",
        f"- Base model: {base_model} Top{base_portfolio_size}",
        f"- Active model: {active_model} Top{active_portfolio_size}",
        f"- Snapshot date: {snapshot_date.date()}",
        f"- BIST100 date: {regime['benchmark_date'].date()}",
        f"- Regime status: {regime['regime_status']}",
        f"- BIST100 close: {regime['bist100_close']:.2f}",
        f"- BIST100 MA200: {regime['bist100_ma200']:.2f}",
        f"- BIST100 below MA200: {regime['bist100_below_ma200']}",
        f"- Confidence score: {confidence:.2f}/100",
        f"- Minimum BUY expected return: {min_buy_expected_return:.2%}",
        "",
        "## Recommended Portfolio",
        "",
        report_df[report_df["recommended"]][
            [
                "rank",
                "symbol",
                "score",
                "action",
                "expected_return_low",
                "expected_return_mid",
                "expected_return_high",
                *factor_columns[:-1],
            ]
        ].to_markdown(index=False, floatfmt=".4f"),
        "",
        "## Top 20 Ranked Stocks",
        "",
        report_df[
            ["rank", "symbol", "score", "recommended", "action", *factor_columns[:-1]]
        ].to_markdown(index=False, floatfmt=".4f"),
        "",
        "## Factor Contribution Breakdown",
        "",
        report_df[report_df["recommended"]][
            ["rank", "symbol", "score", *contribution_columns]
        ].to_markdown(index=False, floatfmt=".4f"),
        "",
        "## Buy List",
        "",
        ", ".join(buy_list) if buy_list else "No new buys.",
        "",
        "## Hold List",
        "",
        ", ".join(hold_list) if hold_list else "No holds from the previous rebalance.",
        "",
        "## Sell List",
        "",
        ", ".join(sell_list) if sell_list else "No sells from the previous rebalance.",
        "",
        "## Why These Stocks Were Selected",
        "",
        (
            "The selected stocks are the highest-ranked names under the active existing model. "
            "The score combines cross-sectional momentum, volume increase, MA trend, and volatility penalty factors "
            "using the configured model weights."
        ),
        "",
        "## Why Excluded Stocks Were Removed",
        "",
        (
            "Excluded top-20 names did not rank inside the active portfolio size. "
            "They may still have positive factor values, but their combined weighted score was lower than the selected list."
        ),
        "",
        excluded[["rank", "symbol", "score", "action"]].to_markdown(index=False, floatfmt=".4f"),
        "",
        "## Main Risks This Month",
        "",
        "- BIST100 regime can change quickly around MA200, creating whipsaw risk.",
        "- Expected return bands are historical score-neighborhood estimates, not forecasts.",
        "- Concentration risk remains because Top10 is a concentrated monthly portfolio.",
        "- Liquidity and gap risk can matter for BIST stocks, especially around earnings or macro news.",
        "",
    ]

    markdown = "\n".join(lines)
    markdown_path = Path(results_dir) / "current_month_portfolio.md"
    markdown_path.write_text(markdown, encoding="utf-8")
    return report_df, markdown
