# BIST-IntradayBot

Research-only intraday paper trading assistant for BIST symbols.

This side project does not place broker orders, does not trade live, and should not be treated as financial advice. It is only a paper trading research tool for observing how simple intraday signals behave during or after a BIST session.

## What It Does

- Downloads intraday Yahoo Finance candles when available.
- Tries 15-minute data first, then 30-minute, then hourly fallback.
- Uses the same initial BIST symbol universe as the monthly ranking bot.
- Generates simple paper-only intraday BUY candidates.
- Simulates max 3 equal-weight paper positions with transaction cost and slippage assumptions.
- Closes all paper positions at the final available candle of the day.
- Produces latest and archived end-of-day reports.

## Strategy MVP

The MVP combines four simple research rules:

- Opening momentum: first 30/60 minute strength.
- VWAP trend: price above VWAP with volume confirmation.
- Mean reversion warning: avoid large spike candles.
- Risk filter: avoid extreme intraday volatility.

## Paper Trading Rules

- Starting capital: 100,000 TL
- Max active positions: 3
- Equal weight per selected position
- No overnight holding
- Transaction cost and slippage assumptions are included
- No real broker integration

## Commands

```bash
python main.py --run-paper-session
python main.py --generate-eod-report
```

Both commands currently run the same latest available intraday simulation and write the reports.

## Outputs

```text
reports/latest_intraday_report.md
reports/latest_intraday_report.xlsx
reports/archive/intraday_report_YYYY-MM-DD.md
reports/archive/intraday_report_YYYY-MM-DD.xlsx
```

## Data Limitations

Yahoo Finance intraday coverage for BIST symbols can be delayed, incomplete, or unavailable. If intraday data cannot be downloaded, the bot still produces a clear fallback warning report instead of silently failing.

## Research Only

This project is intentionally paper-only. Do not connect it to a broker without a separate review, validation process, and explicit production risk controls.
