# Recommendation Logic Audit Report

Generated after auditing recommendation generation, expected return calculation, and action assignment.

## Executive Finding

The previous recommendation logic could show `BUY` / `AL` even when `expected_return_mid` was negative.

Root causes:

1. `src/current_portfolio.py` assigned `BUY`, `HOLD`, and `SELL` primarily from portfolio membership changes versus the previous rebalance, not from expected return.
2. `src/investor_report.py` forced every row in `YONETICI_OZETI` to `AL`, even when the source row had negative expected return.

Both issues are now fixed.

## Rule Used

A small near-zero band is used so very small expected returns are not over-traded:

- `BUY`: expected return > +0.50%
- `HOLD`: expected return between -0.50% and +0.50%
- `SELL`: expected return < -0.50%
- `EXCLUDE`: not inside the active recommendation set and not a negative-return sell candidate

This implements the requested rule while giving `HOLD` a practical "near zero" definition.

## Current Action Audit

| rank | symbol | recommended | action | expected_return_mid | audit_result |
|---:|:---|:---:|:---|---:|:---|
| 1 | EREGL.IS | True | SELL | -0.0052 | PASS |
| 2 | SISE.IS | True | BUY | 0.0573 | PASS |
| 3 | BIMAS.IS | True | BUY | 0.0150 | PASS |
| 4 | TOASO.IS | True | BUY | 0.0360 | PASS |
| 5 | TCELL.IS | True | SELL | -0.0056 | PASS |
| 6 | PETKM.IS | True | SELL | -0.0293 | PASS |
| 7 | ASELS.IS | True | BUY | 0.0149 | PASS |
| 8 | FROTO.IS | True | BUY | 0.1135 | PASS |
| 9 | ARCLK.IS | True | BUY | 0.0319 | PASS |
| 10 | THYAO.IS | True | SELL | -0.0071 | PASS |
| 11 | KCHOL.IS | False | EXCLUDE | 0.0070 | PASS |
| 12 | GARAN.IS | False | EXCLUDE | 0.0063 | PASS |
| 13 | TUPRS.IS | False | EXCLUDE | 0.0180 | PASS |
| 14 | SAHOL.IS | False | SELL | -0.0223 | PASS |
| 15 | AKBNK.IS | False | EXCLUDE | -0.0047 | PASS |
| 16 | YKBNK.IS | False | SELL | -0.0310 | PASS |
| 17 | PGSUS.IS | False | EXCLUDE | 0.0408 | PASS |

## YONETICI_OZETI Audit

`YONETICI_OZETI` now includes only actionable `BUY` rows with positive expected return.

| rank | stock | action | expected_return_mid |
|---:|:---|:---|---:|
| 1 | SISE.IS | AL | 0.0573 |
| 2 | FROTO.IS | AL | 0.1135 |
| 3 | BIMAS.IS | AL | 0.0150 |
| 4 | TOASO.IS | AL | 0.0360 |
| 5 | ARCLK.IS | AL | 0.0319 |
| 6 | ASELS.IS | AL | 0.0149 |

All `AL` rows have expected return above +0.50%.

## Fixes Implemented

- `src/current_portfolio.py`
  - Added expected-return based action assignment.
  - `BUY`, `HOLD`, and `SELL` are now assigned from `expected_return_mid`.
  - The markdown buy/hold/sell lists now follow the same action field.

- `src/investor_report.py`
  - `YONETICI_OZETI` now uses only source rows whose action is `BUY`.
  - It no longer converts all recommended holdings to `AL`.

## Validation

Command:

```bash
.venv\Scripts\python.exe main.py
```

Result: passed.

Known data warning: Yahoo Finance returned no valid data for `KOZAL.IS`; the project recorded it through the existing missing ticker flow.

## Decision

Accepted.

Reasoning: the previous mismatch was a real logic bug. The generated investor report now answers "what should I buy today?" using only positive expected-return candidates, while negative expected-return names are no longer shown as `BUY` / `AL`.
