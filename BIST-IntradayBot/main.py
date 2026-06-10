from __future__ import annotations

import argparse

import pandas as pd

from src.data_loader import fetch_intraday_data, latest_common_session, session_slice
from src.paper_trader import simulate_day
from src.reporting import write_reports
from src.signal_engine import SignalResult, generate_signals


def run_intraday_paper_session() -> tuple:
    dataset = fetch_intraday_data()
    session_date = latest_common_session(dataset)
    warnings = list(dataset.warnings)

    if session_date is None:
        empty_result = SignalResult(pd.DataFrame(), pd.DataFrame(), pd.DataFrame(), "NO_INTRADAY_DATA")
        trade_result = simulate_day(pd.DataFrame(), {}, pd.DataFrame())
        return write_reports(None, dataset.interval, empty_result, trade_result, warnings)

    session_prices = {
        symbol: session_slice(frame, session_date)
        for symbol, frame in dataset.prices.items()
        if not session_slice(frame, session_date).empty
    }
    benchmark_session = session_slice(dataset.benchmark, session_date)

    signal_result = generate_signals(session_prices)
    trade_result = simulate_day(signal_result.selected, session_prices, benchmark_session)
    return write_reports(session_date, dataset.interval, signal_result, trade_result, warnings)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="BIST intraday research-only paper trading assistant.")
    parser.add_argument("--run-paper-session", action="store_true", help="Run the latest available intraday paper session.")
    parser.add_argument("--generate-eod-report", action="store_true", help="Generate the end-of-day paper trading report.")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    if not args.run_paper_session and not args.generate_eod_report:
        print("No action requested. Use --run-paper-session or --generate-eod-report.")
        return

    latest_md, latest_xlsx = run_intraday_paper_session()
    print(f"Intraday markdown report: {latest_md.resolve()}")
    print(f"Intraday Excel report: {latest_xlsx.resolve()}")


if __name__ == "__main__":
    main()
