from pathlib import Path

import pandas as pd

import config
from src.backtester import run_backtests
from src.data_loader import fetch_price_data, find_missing_tickers
from src.ranking import build_monthly_rankings
from src.reporting import (
    assign_periods,
    build_final_report,
    build_model_selection,
    save_charts,
    save_summary_report,
)
from src.robustness import (
    random_start_month_tests,
    rolling_out_of_sample_tests,
    transaction_cost_sensitivity,
)
from src.selection_exports import save_selection_exports


def main() -> None:
    Path(config.DATA_DIR).mkdir(exist_ok=True)
    Path(config.RESULTS_DIR).mkdir(exist_ok=True)

    symbols = config.BIST_SYMBOLS
    benchmark_symbol = config.BENCHMARK_SYMBOL

    print("Fetching price data...")
    prices = fetch_price_data(
        symbols=symbols + [benchmark_symbol],
        start_date=config.START_DATE,
        end_date=config.END_DATE,
        data_dir=config.DATA_DIR,
    )

    stock_prices = {symbol: df for symbol, df in prices.items() if symbol in symbols}
    benchmark_prices = prices.get(benchmark_symbol)
    missing_tickers = find_missing_tickers(symbols, stock_prices)
    missing_tickers.to_csv(Path(config.RESULTS_DIR) / "missing_tickers.csv", index=False)

    all_rankings = []
    all_backtests = []
    all_trades = []
    rankings_by_model = {}

    print("Building monthly rankings and running model backtests...")
    for model_name, weights in config.FACTOR_MODELS.items():
        rankings = build_monthly_rankings(stock_prices, weights)
        if rankings.empty:
            print(f"Warning: no rankings generated for {model_name}")
            continue

        rankings["model"] = model_name
        all_rankings.append(rankings)
        rankings_by_model[model_name] = rankings

        backtest_results, trades = run_backtests(
            stock_prices=stock_prices,
            rankings=rankings,
            portfolio_sizes=config.PORTFOLIO_SIZES,
            transaction_cost=config.TRANSACTION_COST,
            model_name=model_name,
        )
        all_backtests.append(backtest_results)
        all_trades.append(trades)

    rankings = pd.concat(all_rankings, ignore_index=True) if all_rankings else pd.DataFrame()
    rankings_path = Path(config.RESULTS_DIR) / "monthly_rankings.csv"
    rankings.to_csv(rankings_path, index=False)

    backtest_results = pd.concat(all_backtests, ignore_index=True) if all_backtests else pd.DataFrame()
    trades = pd.concat(all_trades, ignore_index=True) if all_trades else pd.DataFrame()

    periods = {
        "train": (config.TRAIN_START, config.TRAIN_END),
        "validation": (config.VALIDATION_START, config.VALIDATION_END),
        "out_of_sample": (config.OUT_OF_SAMPLE_START, config.OUT_OF_SAMPLE_END),
    }
    backtest_results = assign_periods(backtest_results, periods)

    backtest_path = Path(config.RESULTS_DIR) / "backtest_results.csv"
    trades_path = Path(config.RESULTS_DIR) / "trades.csv"
    backtest_results.to_csv(backtest_path, index=False)
    trades.to_csv(trades_path, index=False)

    benchmark_monthly = None
    if benchmark_prices is not None and not benchmark_prices.empty:
        benchmark_close = benchmark_prices["Close"].resample("ME").last()
        benchmark_monthly = ((benchmark_close.shift(-1) / benchmark_close) - 1).rename("BIST100").dropna()

    print("Saving monthly selection exports...")
    monthly_selections, factor_breakdown = save_selection_exports(
        trades=trades,
        rankings=rankings,
        backtest_results=backtest_results,
        stock_prices=stock_prices,
        benchmark_prices=benchmark_prices,
        factor_models=config.FACTOR_MODELS,
        illiquid_avg_traded_value_threshold=config.ILLIQUID_AVG_TRADED_VALUE_THRESHOLD,
        speculative_daily_volatility_threshold=config.SPECULATIVE_DAILY_VOLATILITY_THRESHOLD,
        results_dir=config.RESULTS_DIR,
    )

    print("Writing reports and charts...")
    summary = save_summary_report(
        backtest_results=backtest_results,
        benchmark_monthly=benchmark_monthly,
        results_dir=config.RESULTS_DIR,
    )

    model_selection = build_model_selection(summary)
    model_selection.to_csv(Path(config.RESULTS_DIR) / "model_selection.csv", index=False)

    final_report, final_report_md = build_final_report(summary, model_selection)
    final_report.to_csv(Path(config.RESULTS_DIR) / "final_report.csv", index=False)
    (Path(config.RESULTS_DIR) / "final_report.md").write_text(final_report_md, encoding="utf-8")

    best_model = final_report[final_report["category"] == "best_model_by_validation"].head(1)
    best_model_path = Path(config.RESULTS_DIR) / "best_model.csv"
    best_results_path = Path(config.RESULTS_DIR) / "best_model_results.csv"

    if not best_model.empty:
        best_model.to_csv(best_model_path, index=False)
        best_row = best_model.iloc[0]
        best_results = backtest_results[
            (backtest_results["model"] == best_row["model"])
            & (backtest_results["portfolio_size"] == best_row["portfolio_size"])
        ].copy()
        best_results.to_csv(best_results_path, index=False)
    else:
        pd.DataFrame().to_csv(best_model_path, index=False)
        pd.DataFrame().to_csv(best_results_path, index=False)

    save_charts(
        backtest_results=backtest_results,
        benchmark_monthly=benchmark_monthly,
        results_dir=config.RESULTS_DIR,
        filename_prefix="all_models_",
    )
    if not best_model.empty:
        save_charts(
            backtest_results=best_results,
            benchmark_monthly=benchmark_monthly,
            results_dir=config.RESULTS_DIR,
            filename_prefix="best_model_",
        )

    portfolio_sensitivity = summary[
        ["model", "period", "portfolio_size", "transaction_cost", "selection_score",
         "strategy_total_return", "bist100_total_return", "excess_return_over_benchmark",
         "strategy_max_drawdown", "bist100_max_drawdown", "win_rate"]
    ].copy()
    portfolio_sensitivity.to_csv(Path(config.RESULTS_DIR) / "portfolio_size_sensitivity.csv", index=False)

    rolling = rolling_out_of_sample_tests(
        backtest_results=backtest_results,
        benchmark_monthly=benchmark_monthly,
    )
    rolling.to_csv(Path(config.RESULTS_DIR) / "rolling_out_of_sample_tests.csv", index=False)

    random_starts = random_start_month_tests(
        backtest_results=backtest_results,
        benchmark_monthly=benchmark_monthly,
        start_offsets=[0, 1, 2, 3, 6, 9, 12],
    )
    random_starts.to_csv(Path(config.RESULTS_DIR) / "random_start_month_tests.csv", index=False)

    cost_summary, cost_trades = transaction_cost_sensitivity(
        stock_prices=stock_prices,
        rankings_by_model=rankings_by_model,
        portfolio_sizes=config.PORTFOLIO_SIZES,
        transaction_costs=config.TRANSACTION_COSTS,
        periods=periods,
        benchmark_monthly=benchmark_monthly,
    )
    cost_summary.to_csv(Path(config.RESULTS_DIR) / "transaction_cost_sensitivity.csv", index=False)
    cost_trades.to_csv(Path(config.RESULTS_DIR) / "transaction_cost_sensitivity_trades.csv", index=False)

    pd.set_option("display.max_columns", 20)
    print("\nSummary:")
    print(summary)
    if not best_model.empty:
        print("\nBest validation model:")
        print(best_model)
    if not missing_tickers.empty:
        print("\nMissing tickers:")
        print(missing_tickers)
    print(f"\nResults written to: {Path(config.RESULTS_DIR).resolve()}")


if __name__ == "__main__":
    main()
