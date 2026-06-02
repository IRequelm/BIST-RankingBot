import pandas as pd

from src.backtester import run_backtests
from src.reporting import assign_periods, build_summary


def rolling_out_of_sample_tests(
    backtest_results: pd.DataFrame,
    benchmark_monthly: pd.Series | None,
    window_months: int = 12,
    step_months: int = 6,
) -> pd.DataFrame:
    """Evaluate each model over rolling forward windows."""
    if backtest_results.empty:
        return pd.DataFrame()

    dates = sorted(pd.to_datetime(backtest_results["date"].unique()))
    rows = []
    for start_idx in range(0, max(len(dates) - window_months + 1, 0), step_months):
        start = dates[start_idx]
        end = dates[start_idx + window_months - 1]
        window = backtest_results[
            (pd.to_datetime(backtest_results["date"]) >= start)
            & (pd.to_datetime(backtest_results["date"]) <= end)
        ].copy()
        window["period"] = f"{start:%Y-%m}_to_{end:%Y-%m}"
        rows.append(build_summary(window, benchmark_monthly))

    return pd.concat(rows, ignore_index=True) if rows else pd.DataFrame()


def random_start_month_tests(
    backtest_results: pd.DataFrame,
    benchmark_monthly: pd.Series | None,
    start_offsets: list[int],
) -> pd.DataFrame:
    """Test results after shifting the first eligible month by fixed offsets."""
    if backtest_results.empty:
        return pd.DataFrame()

    dates = sorted(pd.to_datetime(backtest_results["date"].unique()))
    rows = []
    for offset in start_offsets:
        if offset >= len(dates):
            continue
        start = dates[offset]
        sample = backtest_results[pd.to_datetime(backtest_results["date"]) >= start].copy()
        sample["period"] = f"start_offset_{offset}_{start:%Y-%m}"
        rows.append(build_summary(sample, benchmark_monthly))

    return pd.concat(rows, ignore_index=True) if rows else pd.DataFrame()


def transaction_cost_sensitivity(
    stock_prices: dict[str, pd.DataFrame],
    rankings_by_model: dict[str, pd.DataFrame],
    portfolio_sizes: list[int],
    transaction_costs: list[float],
    periods: dict[str, tuple[str, str]],
    benchmark_monthly: pd.Series | None,
) -> tuple[pd.DataFrame, pd.DataFrame]:
    """Rerun model backtests for each transaction cost."""
    result_frames = []
    trade_frames = []

    for cost in transaction_costs:
        for model_name, rankings in rankings_by_model.items():
            results, trades = run_backtests(
                stock_prices=stock_prices,
                rankings=rankings,
                portfolio_sizes=portfolio_sizes,
                transaction_cost=cost,
                model_name=model_name,
            )
            result_frames.append(results)
            trade_frames.append(trades)

    all_results = pd.concat(result_frames, ignore_index=True) if result_frames else pd.DataFrame()
    all_results = assign_periods(all_results, periods)
    summary = build_summary(all_results, benchmark_monthly)

    all_trades = pd.concat(trade_frames, ignore_index=True) if trade_frames else pd.DataFrame()
    return summary, all_trades
