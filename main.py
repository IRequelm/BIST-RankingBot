import argparse
from pathlib import Path

import pandas as pd

import config
from src.backtester import run_backtests
from src.cash_allocation import build_cash_allocation_reports, build_opportunity_filter_calibration_report
from src.current_portfolio import generate_current_month_portfolio
from src.data_loader import fetch_price_data, find_missing_tickers
from src.investor_report import generate_investor_report
from src.paper_trading import update_paper_trading
from src.ranking import build_monthly_rankings
from src.real_return_report import save_real_return_report
from src.report_publisher import publish_investor_report, publish_latest_existing_replay, publish_replay_report
from src.replay import run_historical_replay
from src.reporting import (
    assign_periods,
    build_final_report,
    build_model_selection,
    save_charts,
    save_summary_report,
)
from src.regime_filter import (
    run_regime_policy_backtests,
    save_regime_filter_report,
    summarize_regime_results,
)
from src.robustness import (
    random_start_month_tests,
    rolling_out_of_sample_tests,
    transaction_cost_sensitivity,
)
from src.selection_exports import save_selection_exports


def _parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Run BIST-RankingBot research pipeline.")
    parser.add_argument("--replay-date", help="Run historical replay for the requested date, e.g. 2026-05-01.")
    parser.add_argument("--holding-days", type=int, default=30, help="Holding period for historical replay.")
    return parser.parse_args()


def _current_report_date(results_dir: str) -> str:
    current_path = Path(results_dir) / "current_month_portfolio.csv"
    current = pd.read_csv(current_path)
    for column in ["snapshot_date", "benchmark_date"]:
        if column in current and pd.notna(current[column].iloc[0]):
            return pd.Timestamp(current[column].iloc[0]).strftime("%Y-%m-%d")
    return pd.Timestamp.today().strftime("%Y-%m-%d")


def main() -> None:
    args = _parse_args()
    Path(config.DATA_DIR).mkdir(exist_ok=True)
    Path(config.RESULTS_DIR).mkdir(exist_ok=True)

    symbols = config.BIST_SYMBOLS
    benchmark_symbol = config.BENCHMARK_SYMBOL

    print("Fetching price data...")
    prices = fetch_price_data(
        symbols=symbols + [benchmark_symbol, config.USDTRY_SYMBOL],
        start_date=config.START_DATE,
        end_date=config.END_DATE,
        data_dir=config.DATA_DIR,
    )

    stock_prices = {symbol: df for symbol, df in prices.items() if symbol in symbols}
    benchmark_prices = prices.get(benchmark_symbol)
    usdtry_prices = prices.get(config.USDTRY_SYMBOL)
    missing_tickers = find_missing_tickers(symbols, stock_prices)
    missing_tickers.to_csv(Path(config.RESULTS_DIR) / "missing_tickers.csv", index=False)

    if args.replay_date:
        if benchmark_prices is None or benchmark_prices.empty:
            raise ValueError("Benchmark data is required for historical replay mode.")
        print(f"Running historical replay for {args.replay_date}...")
        replay = run_historical_replay(
            stock_prices=stock_prices,
            benchmark_prices=benchmark_prices,
            requested_date=args.replay_date,
            holding_days=args.holding_days,
            results_dir=config.RESULTS_DIR,
            factor_models=config.FACTOR_MODELS,
            portfolio_sizes=config.PORTFOLIO_SIZES,
            transaction_cost=config.TRANSACTION_COST,
            min_buy_expected_return=config.MIN_BUY_EXPECTED_RETURN,
            opportunity_filter_percentile=config.OPPORTUNITY_FILTER_PERCENTILE,
            illiquid_avg_traded_value_threshold=config.ILLIQUID_AVG_TRADED_VALUE_THRESHOLD,
            speculative_daily_volatility_threshold=config.SPECULATIVE_DAILY_VOLATILITY_THRESHOLD,
        )
        replay_publish = publish_replay_report(
            xlsx_path=replay["xlsx_path"],
            markdown_path=replay["report_path"],
            replay_date=replay["replay_date"],
        )
        print(f"Replay report written to: {Path(replay['report_path']).resolve()}")
        print(f"Replay workbook written to: {Path(replay['xlsx_path']).resolve()}")
        print(f"Latest replay report published to: {replay_publish['latest_xlsx'].resolve()}")
        print(f"Portfolio return: {float(replay['portfolio_return']):.2%}")
        print(f"BIST100 return: {float(replay['bist100_return']):.2%}")
        print(f"Excess return: {float(replay['excess_return_vs_bist100']):.2%}")
        return

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

    if benchmark_prices is not None and not benchmark_prices.empty:
        print("Generating current month portfolio recommendation...")
        generate_current_month_portfolio(
            stock_prices=stock_prices,
            benchmark_prices=benchmark_prices,
            factor_models=config.FACTOR_MODELS,
            rankings_by_model=rankings_by_model,
            results_dir=config.RESULTS_DIR,
            base_model="volume_heavy",
            base_portfolio_size=10,
            defensive_model="low_volatility",
            defensive_portfolio_size=5,
            min_buy_expected_return=config.MIN_BUY_EXPECTED_RETURN,
            opportunity_filter_percentile=config.OPPORTUNITY_FILTER_PERCENTILE,
        )

        print("Updating paper trading tracker...")
        update_paper_trading(
            stock_prices=stock_prices,
            benchmark_prices=benchmark_prices,
            results_dir=config.RESULTS_DIR,
            paper_dir=config.PAPER_TRADING_DIR,
            initial_capital=config.PAPER_INITIAL_CAPITAL,
        )

        print("Generating investor report...")
        investor_xlsx, investor_md = generate_investor_report(
            stock_prices=stock_prices,
            results_dir=config.RESULTS_DIR,
        )
        investor_publish = publish_investor_report(
            xlsx_path=investor_xlsx,
            markdown_path=investor_md,
            report_date=_current_report_date(config.RESULTS_DIR),
        )
        replay_publish = publish_latest_existing_replay(config.RESULTS_DIR)
        print(f"Latest investor report published to: {investor_publish['latest_xlsx'].resolve()}")
        if replay_publish:
            print(f"Latest replay report published to: {replay_publish['latest_xlsx'].resolve()}")

        print("Running BIST100 regime filter experiment...")
        regime_results, regime_signal = run_regime_policy_backtests(
            stock_prices=stock_prices,
            rankings_by_model=rankings_by_model,
            benchmark_prices=benchmark_prices,
            portfolio_sizes=config.PORTFOLIO_SIZES,
            transaction_cost=config.TRANSACTION_COST,
            periods=periods,
        )
        regime_detail, regime_policy_summary = summarize_regime_results(
            results=regime_results,
            benchmark_prices=benchmark_prices,
        )
        recommended_regime_policy = save_regime_filter_report(
            results=regime_results,
            detail_summary=regime_detail,
            policy_summary=regime_policy_summary,
            regime_signal=regime_signal,
            results_dir=config.RESULTS_DIR,
        )
    else:
        recommended_regime_policy = "benchmark data unavailable"

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

    print("Generating real return report...")
    build_cash_allocation_reports(
        results_dir=config.RESULTS_DIR,
        summary=summary,
        benchmark_monthly=benchmark_monthly,
        periods=periods,
        transaction_cost=config.TRANSACTION_COST,
        thresholds=config.CASH_ALLOCATION_THRESHOLDS,
    )
    build_opportunity_filter_calibration_report(
        results_dir=config.RESULTS_DIR,
        summary=summary,
        benchmark_monthly=benchmark_monthly,
        periods=periods,
        transaction_cost=config.TRANSACTION_COST,
    )
    save_real_return_report(
        results_dir=config.RESULTS_DIR,
        benchmark_prices=benchmark_prices,
        usdtry_prices=usdtry_prices,
    )

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
    print(f"\nRecommended regime policy: {recommended_regime_policy}")
    print(f"\nResults written to: {Path(config.RESULTS_DIR).resolve()}")
    print(f"Investor reports written to: {Path('reports').resolve()}")


if __name__ == "__main__":
    main()
