# BIST-RankingBot

Monthly stock ranking and backtesting MVP for BIST stocks.

## What It Does

- Fetches historical BIST stock prices from Yahoo Finance.
- Logs missing tickers to `results/missing_tickers.csv` and excludes them without substitution.
- Calculates monthly ranking scores using:
  - 1 month momentum
  - 3 month momentum
  - 6 month momentum
  - volume increase
  - price above 50/200 day moving averages
  - volatility penalty
- Ranks all stocks at each month-end.
- Backtests equal-weight portfolios for top 3, top 5, top 10, and top 15 stocks.
- Compares predefined factor models:
  - momentum-heavy
  - volume-heavy
  - low-volatility
  - trend-following
  - mixed model
- Uses train, validation, and out-of-sample periods.
- Compares each strategy with BIST100 for each period.
- Uses this benchmark-relative selection score:
  `excess_return - abs(max_drawdown) * 2 + win_rate * 0.5`.
- Runs robustness checks:
  - rolling out-of-sample windows
  - random start month test
  - portfolio size sensitivity
  - transaction cost sensitivity
- Holds each portfolio for one month.
- Reports whether selected stocks are frequently illiquid or speculative using
  configurable traded-value and volatility thresholds.
- Exports CSV files, charts, and Markdown reports.

## Project Structure

```text
BIST-RankingBot/
|-- main.py
|-- config.py
|-- data/
|-- paper_trading/
|-- src/
|   |-- data_loader.py
|   |-- indicators.py
|   |-- ranking.py
|   |-- backtester.py
|   |-- robustness.py
|   `-- reporting.py
|-- results/
|-- requirements.txt
`-- README.md
```

## Setup

```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
```

## Run

```bash
python main.py
```

Outputs are written to `results/`:

- `monthly_rankings.csv`
- `current_month_portfolio.csv`
- `current_month_portfolio.md`
- `paper_portfolio_history.csv`
- `paper_trade_log.csv`
- `paper_performance_report.md`
- `monthly_investor_report.xlsx` - latest human-readable investor Excel report
- `monthly_investor_report.md` - latest human-readable investor Markdown report
- `monthly_investor_report_YYYY-MM-DD.xlsx` - archived dated Excel investor report
- `monthly_investor_report_YYYY-MM-DD.md` - archived dated Markdown investor report
- `monthly_selections.csv`
- `factor_breakdown.csv`
- `ticker_selection_stats.csv`
- `backtest_results.csv`
- `trades.csv`
- `missing_tickers.csv`
- `summary_report.csv`
- `summary_report.md`
- `final_report.csv`
- `final_report.md`
- `model_selection.csv`
- `portfolio_size_sensitivity.csv`
- `rolling_out_of_sample_tests.csv`
- `random_start_month_tests.csv`
- `transaction_cost_sensitivity.csv`
- `regime_filter_report.md`
- `regime_filter_policy_summary.csv`
- `regime_filter_detail.csv`
- `regime_filter_results.csv`
- `bist100_regime_signal.csv`
- `selection_report.md`
- `selected_ticker_counts.csv`
- `selected_ticker_average_returns.csv`
- `factor_importance_by_model.csv`
- `best_worst_selected_stocks.csv`
- `best_model.csv`
- `best_model_results.csv`
- `all_models_equity_curve.png`
- `all_models_monthly_returns.png`
- `best_model_equity_curve.png`
- `best_model_monthly_returns.png`

Downloaded price data is cached in `data/`.

## Historical Replay Mode

Historical replay mode answers: if the bot had been run on a past date, what would it have recommended and what actually happened afterward?

Example commands:

```bash
python main.py --replay-date 2026-05-01
python main.py --replay-date 2026-05-01 --holding-days 30
```

Replay mode:

- uses only data available up to the replay date for recommendation generation
- uses the first available trading day on or after the requested date
- evaluates the realized performance after the replay date
- writes `results/replay_YYYY-MM-DD_report.md`
- writes `results/replay_YYYY-MM-DD_portfolio.xlsx`
- appends/updates `results/replay_summary.csv`

## Configuration

Edit `config.py` to change:

- BIST stock list
- benchmark symbol
- date range
- factor model weights
- train/validation/out-of-sample dates
- portfolio sizes
- transaction costs

Yahoo Finance uses `.IS` symbols for Borsa Istanbul stocks, for example `THYAO.IS`.

## Automated Research Workflow

The repository includes a GitHub Actions workflow at `.github/workflows/nightly_research.yml`.

It runs every day at 02:00 UTC and can also be started manually from the GitHub Actions tab. The workflow:

- checks out the repository
- installs Python dependencies from `requirements.txt`
- runs `python main.py`
- saves generated files under `results/`
- uploads `results/` as a workflow artifact
- commits and pushes changed `results/`, `paper_trading/`, and cached `data/` files back to the repository

This workflow is research-only. It does not place trades, does not call broker APIs, and only runs ranking, backtesting, paper trading, reporting, and portfolio recommendation generation.

## Telegram Notifications

The nightly workflow can send a concise Telegram summary after research and paper trading reports are updated.

To enable it, add these GitHub Actions repository secrets:

- `TELEGRAM_BOT_TOKEN`
- `TELEGRAM_CHAT_ID`

The message includes regime status, confidence score, buy/sell/hold lists, portfolio value, total return, BIST100 return, and unrealized PnL. It does not send full reports.

Telegram notifications are optional. If either secret is missing, the workflow prints `Telegram secrets not configured.` and continues successfully.

## Paper Trading

The paper trading engine tracks real-world performance of generated monthly recommendations over time. It reads `results/current_month_portfolio.csv`, opens paper positions for new buy signals, closes paper positions for sell signals, keeps hold positions, and marks active positions to market with latest available prices.

Generated paper trading files:

- `results/paper_portfolio_history.csv`
- `results/paper_trade_log.csv`
- `results/paper_performance_report.md`
- `paper_trading/recommendation_snapshots.csv`

This is paper trading only. No broker API integration exists in this project.

## Notes

This is a working MVP, not investment advice. It is designed to be simple and easy to extend.
