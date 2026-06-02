import pandas as pd

from src.indicators import get_forward_month_return


def run_backtests(
    stock_prices: dict[str, pd.DataFrame],
    rankings: pd.DataFrame,
    portfolio_sizes: list[int],
    transaction_cost: float,
    model_name: str | None = None,
) -> tuple[pd.DataFrame, pd.DataFrame]:
    """Simulate buying top N stocks at month-end and holding for one month."""
    if rankings.empty:
        return pd.DataFrame(), pd.DataFrame()

    result_rows = []
    trade_rows = []

    for portfolio_size in portfolio_sizes:
        equity = 1.0
        for ranking_date, month_rankings in rankings.groupby("date"):
            selected = month_rankings.sort_values("rank").head(portfolio_size)
            returns = []

            for _, row in selected.iterrows():
                symbol = row["symbol"]
                stock_return = get_forward_month_return(stock_prices[symbol], pd.Timestamp(ranking_date))
                if stock_return is None:
                    continue

                returns.append(stock_return)
                trade_rows.append(
                    {
                        "date": ranking_date,
                        "model": model_name,
                        "portfolio_size": portfolio_size,
                        "symbol": symbol,
                        "rank": row["rank"],
                        "score": row["score"],
                        "forward_return": stock_return,
                    }
                )

            if not returns:
                continue

            gross_return = sum(returns) / len(returns)
            net_return = gross_return - transaction_cost
            equity *= 1 + net_return

            result_rows.append(
                {
                    "date": ranking_date,
                    "model": model_name,
                    "portfolio_size": portfolio_size,
                    "holdings": len(returns),
                    "gross_return": gross_return,
                    "transaction_cost": transaction_cost,
                    "net_return": net_return,
                    "equity": equity,
                }
            )

    return pd.DataFrame(result_rows), pd.DataFrame(trade_rows)
