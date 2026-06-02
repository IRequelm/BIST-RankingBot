from pathlib import Path

import pandas as pd

from src.indicators import calculate_features


FACTOR_COLUMNS = [
    "momentum_1m",
    "momentum_3m",
    "momentum_6m",
    "volume_change",
    "volatility",
    "ma_trend_signal",
    "relative_strength_vs_bist100",
]


def _benchmark_momentum_1m(benchmark_prices: pd.DataFrame | None) -> pd.Series:
    if benchmark_prices is None or benchmark_prices.empty:
        return pd.Series(dtype=float)

    features = calculate_features(benchmark_prices).resample("ME").last()
    return features["momentum_1m"].rename("benchmark_momentum_1m")


def _liquidity_frame(stock_prices: dict[str, pd.DataFrame]) -> pd.DataFrame:
    rows = []
    for symbol, prices in stock_prices.items():
        frame = pd.DataFrame(index=prices.index)
        frame["symbol"] = symbol
        frame["avg_daily_volume_21"] = prices["Volume"].rolling(21).mean()
        frame["avg_daily_traded_value_21"] = (prices["Close"] * prices["Volume"]).rolling(21).mean()
        frame = frame.resample("ME").last()
        frame["date"] = frame.index
        rows.append(frame.reset_index(drop=True))

    if not rows:
        return pd.DataFrame()

    return pd.concat(rows, ignore_index=True)


def build_factor_breakdown(
    trades: pd.DataFrame,
    rankings: pd.DataFrame,
    backtest_results: pd.DataFrame,
    stock_prices: dict[str, pd.DataFrame],
    benchmark_prices: pd.DataFrame | None,
    illiquid_avg_traded_value_threshold: float,
    speculative_daily_volatility_threshold: float,
) -> pd.DataFrame:
    """Join selected trades with ranking factors and portfolio returns."""
    if trades.empty or rankings.empty:
        return pd.DataFrame()

    rank_cols = [
        "date",
        "model",
        "symbol",
        "score",
        "momentum_1m",
        "momentum_3m",
        "momentum_6m",
        "volume_increase",
        "above_ma",
        "volatility",
    ]
    selected = trades.merge(
        rankings[rank_cols],
        on=["date", "model", "symbol", "score"],
        how="left",
    )

    portfolio_returns = backtest_results[
        ["date", "model", "portfolio_size", "gross_return", "net_return", "transaction_cost"]
    ].rename(columns={"gross_return": "portfolio_gross_return", "net_return": "portfolio_return"})

    selected = selected.merge(
        portfolio_returns,
        on=["date", "model", "portfolio_size"],
        how="left",
    )

    benchmark_1m = _benchmark_momentum_1m(benchmark_prices)
    if not benchmark_1m.empty:
        selected = selected.merge(
            benchmark_1m.reset_index().rename(columns={"Date": "date", "index": "date"}),
            on="date",
            how="left",
        )
    else:
        selected["benchmark_momentum_1m"] = pd.NA

    selected["volume_change"] = selected["volume_increase"]
    selected["ma_trend_signal"] = selected["above_ma"]
    selected["relative_strength_vs_bist100"] = selected["momentum_1m"] - selected["benchmark_momentum_1m"]
    selected["next_month_return"] = selected["forward_return"]

    liquidity = _liquidity_frame(stock_prices)
    if not liquidity.empty:
        selected = selected.merge(liquidity, on=["date", "symbol"], how="left")
    else:
        selected["avg_daily_volume_21"] = pd.NA
        selected["avg_daily_traded_value_21"] = pd.NA

    selected["is_illiquid"] = selected["avg_daily_traded_value_21"] < illiquid_avg_traded_value_threshold
    selected["is_speculative"] = selected["volatility"] > speculative_daily_volatility_threshold

    columns = [
        "date",
        "model",
        "portfolio_size",
        "symbol",
        "rank",
        "score",
        *FACTOR_COLUMNS,
        "avg_daily_volume_21",
        "avg_daily_traded_value_21",
        "is_illiquid",
        "is_speculative",
        "next_month_return",
        "portfolio_gross_return",
        "transaction_cost",
        "portfolio_return",
    ]
    return selected[columns].sort_values(["date", "model", "portfolio_size", "rank"])


def build_monthly_selections(factor_breakdown: pd.DataFrame) -> pd.DataFrame:
    """Create one row per rebalance month, model, and portfolio size."""
    if factor_breakdown.empty:
        return pd.DataFrame()

    rows = []
    for keys, group in factor_breakdown.groupby(["date", "model", "portfolio_size"], dropna=False):
        date, model, portfolio_size = keys
        group = group.sort_values("rank")
        rows.append(
            {
                "date": date,
                "model": model,
                "portfolio_size": portfolio_size,
                "selected_tickers": ", ".join(group["symbol"].astype(str)),
                "ticker_scores": ", ".join(
                    f"{row.symbol}:{row.score:.4f}" for row in group.itertuples(index=False)
                ),
                "portfolio_return": group["portfolio_return"].iloc[0],
            }
        )

    return pd.DataFrame(rows).sort_values(["date", "model", "portfolio_size"])


def build_selection_report(
    factor_breakdown: pd.DataFrame,
    factor_models: dict[str, dict[str, float]],
) -> tuple[pd.DataFrame, pd.DataFrame, pd.DataFrame, pd.DataFrame, pd.DataFrame, str]:
    """Build ticker frequency, ticker return, factor importance, and best/worst reports."""
    if factor_breakdown.empty:
        empty = pd.DataFrame()
        return empty, empty, empty, empty, empty, "# Monthly Selection Report\n\nNo selections were generated.\n"

    selected_counts = (
        factor_breakdown.groupby("symbol")
        .size()
        .reset_index(name="selection_count")
        .sort_values(["selection_count", "symbol"], ascending=[False, True])
    )

    avg_return_by_ticker = (
        factor_breakdown.groupby("symbol")["next_month_return"]
        .agg(["count", "mean", "median", "min", "max"])
        .reset_index()
        .rename(
            columns={
                "count": "selection_count",
                "mean": "avg_next_month_return",
                "median": "median_next_month_return",
                "min": "worst_next_month_return",
                "max": "best_next_month_return",
            }
        )
        .sort_values("avg_next_month_return", ascending=False)
    )

    ticker_selection_stats = (
        factor_breakdown.groupby("symbol")
        .agg(
            selection_count=("symbol", "size"),
            avg_next_month_return=("next_month_return", "mean"),
            median_next_month_return=("next_month_return", "median"),
            best_next_month_return=("next_month_return", "max"),
            worst_next_month_return=("next_month_return", "min"),
            avg_score=("score", "mean"),
            avg_momentum_1m=("momentum_1m", "mean"),
            avg_momentum_3m=("momentum_3m", "mean"),
            avg_momentum_6m=("momentum_6m", "mean"),
            avg_volume_change=("volume_change", "mean"),
            avg_volatility=("volatility", "mean"),
            avg_ma_trend_signal=("ma_trend_signal", "mean"),
            avg_relative_strength_vs_bist100=("relative_strength_vs_bist100", "mean"),
            avg_daily_traded_value_21=("avg_daily_traded_value_21", "mean"),
            illiquid_selection_rate=("is_illiquid", "mean"),
            speculative_selection_rate=("is_speculative", "mean"),
        )
        .reset_index()
        .sort_values(["selection_count", "avg_next_month_return"], ascending=[False, False])
    )

    importance_rows = []
    for model, weights in factor_models.items():
        total = sum(abs(value) for value in weights.values())
        for factor, weight in weights.items():
            display_factor = "volatility" if factor == "volatility_penalty" else factor
            importance_rows.append(
                {
                    "model": model,
                    "factor": display_factor,
                    "weight": weight,
                    "normalized_importance": abs(weight) / total if total else 0,
                }
            )
    factor_importance = pd.DataFrame(importance_rows).sort_values(
        ["model", "normalized_importance"],
        ascending=[True, False],
    )

    best_worst = pd.concat(
        [
            factor_breakdown.nlargest(10, "next_month_return").assign(result_group="best_selected_stocks"),
            factor_breakdown.nsmallest(10, "next_month_return").assign(result_group="worst_selected_stocks"),
        ],
        ignore_index=True,
    )[
        [
            "result_group",
            "date",
            "model",
            "portfolio_size",
            "symbol",
            "score",
            "next_month_return",
            "portfolio_return",
        ]
    ]

    markdown = "# Monthly Selection Report\n\n"
    markdown += "## Most Frequently Selected Tickers\n\n"
    markdown += selected_counts.head(20).to_markdown(index=False, floatfmt=".4f")
    markdown += "\n\n## Average Return After Selection\n\n"
    markdown += avg_return_by_ticker.head(20).to_markdown(index=False, floatfmt=".4f")
    markdown += "\n\n## Factor Importance By Model\n\n"
    markdown += factor_importance.to_markdown(index=False, floatfmt=".4f")
    markdown += "\n\n## Best And Worst Selected Stocks\n\n"
    markdown += best_worst.to_markdown(index=False, floatfmt=".4f")
    markdown += "\n\n## Illiquid Or Speculative Selection Check\n\n"
    illiquid_rate = factor_breakdown["is_illiquid"].mean()
    speculative_rate = factor_breakdown["is_speculative"].mean()
    combined_rate = (factor_breakdown["is_illiquid"] | factor_breakdown["is_speculative"]).mean()
    markdown += (
        f"- Illiquid selection rate: {illiquid_rate:.2%}\n"
        f"- Speculative selection rate: {speculative_rate:.2%}\n"
        f"- Illiquid or speculative selection rate: {combined_rate:.2%}\n\n"
    )
    markdown += "Highest risk tickers by combined illiquid/speculative rate:\n\n"
    risk_table = ticker_selection_stats.assign(
        combined_risk_rate=lambda df: df["illiquid_selection_rate"] + df["speculative_selection_rate"]
    ).sort_values("combined_risk_rate", ascending=False)
    markdown += risk_table[
        [
            "symbol",
            "selection_count",
            "illiquid_selection_rate",
            "speculative_selection_rate",
            "avg_daily_traded_value_21",
            "avg_volatility",
            "avg_next_month_return",
        ]
    ].head(15).to_markdown(index=False, floatfmt=".4f")
    markdown += "\n"

    return selected_counts, avg_return_by_ticker, ticker_selection_stats, factor_importance, best_worst, markdown


def save_selection_exports(
    trades: pd.DataFrame,
    rankings: pd.DataFrame,
    backtest_results: pd.DataFrame,
    stock_prices: dict[str, pd.DataFrame],
    benchmark_prices: pd.DataFrame | None,
    factor_models: dict[str, dict[str, float]],
    illiquid_avg_traded_value_threshold: float,
    speculative_daily_volatility_threshold: float,
    results_dir: str,
) -> tuple[pd.DataFrame, pd.DataFrame]:
    """Save monthly selections, factor breakdown, and supporting selection reports."""
    Path(results_dir).mkdir(exist_ok=True)

    factor_breakdown = build_factor_breakdown(
        trades=trades,
        rankings=rankings,
        backtest_results=backtest_results,
        stock_prices=stock_prices,
        benchmark_prices=benchmark_prices,
        illiquid_avg_traded_value_threshold=illiquid_avg_traded_value_threshold,
        speculative_daily_volatility_threshold=speculative_daily_volatility_threshold,
    )
    monthly_selections = build_monthly_selections(factor_breakdown)

    factor_breakdown.to_csv(Path(results_dir) / "factor_breakdown.csv", index=False)
    monthly_selections.to_csv(Path(results_dir) / "monthly_selections.csv", index=False)

    selected_counts, avg_returns, ticker_selection_stats, factor_importance, best_worst, markdown = build_selection_report(
        factor_breakdown=factor_breakdown,
        factor_models=factor_models,
    )
    selected_counts.to_csv(Path(results_dir) / "selected_ticker_counts.csv", index=False)
    avg_returns.to_csv(Path(results_dir) / "selected_ticker_average_returns.csv", index=False)
    ticker_selection_stats.to_csv(Path(results_dir) / "ticker_selection_stats.csv", index=False)
    factor_importance.to_csv(Path(results_dir) / "factor_importance_by_model.csv", index=False)
    best_worst.to_csv(Path(results_dir) / "best_worst_selected_stocks.csv", index=False)
    (Path(results_dir) / "selection_report.md").write_text(markdown, encoding="utf-8")

    return monthly_selections, factor_breakdown
