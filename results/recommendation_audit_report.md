# Recommendation Logic Audit Report

Generated after auditing recommendation generation, expected return calculation, action assignment, and the calibrated opportunity filter.

## Executive Finding

The recommendation logic now uses a calibrated opportunity threshold instead of a fixed 5.00% hurdle.

The active rule is:

- Floor: expected return must be at least 0.00%.
- Relative filter: expected return must be at or above the current recommended opportunity set's 50th percentile.
- Current effective BUY threshold: 1.50%.

The investor report still allows `CASH` as an asset. If fewer than 10 attractive opportunities pass the calibrated threshold, unused capital is allocated to `CASH` so portfolio weights always sum to 100%.

## Rule Used

- `BUY`: expected return >= current effective opportunity threshold for active recommended names
- `HOLD`: expected return >= 0.00% and < current effective threshold for active recommended names
- `SELL`: expected return < 0.00%
- `EXCLUDE`: not inside the active recommendation set and not a negative-return sell candidate
- `CASH`: remaining capital when fewer than 10 attractive `BUY` candidates exist

## Current Action Audit

| rank | symbol | recommended | action | expected_return_mid | audit_result |
|---:|:---|:---:|:---|---:|:---|
| 1 | EREGL.IS | True | SELL | -0.0052 | PASS |
| 2 | SISE.IS | True | BUY | 0.0573 | PASS |
| 3 | BIMAS.IS | True | BUY | 0.0150 | PASS |
| 4 | TOASO.IS | True | BUY | 0.0360 | PASS |
| 5 | TCELL.IS | True | SELL | -0.0056 | PASS |
| 6 | PETKM.IS | True | SELL | -0.0293 | PASS |
| 7 | ASELS.IS | True | HOLD | 0.0149 | PASS |
| 8 | FROTO.IS | True | BUY | 0.1135 | PASS |
| 9 | ARCLK.IS | True | BUY | 0.0319 | PASS |
| 10 | THYAO.IS | True | SELL | -0.0071 | PASS |
| 11 | KCHOL.IS | False | EXCLUDE | 0.0070 | PASS |
| 12 | GARAN.IS | False | EXCLUDE | 0.0063 | PASS |
| 13 | TUPRS.IS | False | EXCLUDE | 0.0180 | PASS |
| 14 | SAHOL.IS | False | SELL | -0.0223 | PASS |
| 15 | AKBNK.IS | False | SELL | -0.0047 | PASS |
| 16 | YKBNK.IS | False | SELL | -0.0310 | PASS |
| 17 | PGSUS.IS | False | EXCLUDE | 0.0408 | PASS |

Strict mismatch count: 0.

## YONETICI_OZETI Audit

`YONETICI_OZETI` includes actionable `AL` rows above the calibrated effective threshold, plus a `CASH` row for unused capital.

| rank | stock | action | weight | expected_return_mid |
|---:|:---|:---|---:|---:|
| 1 | SISE.IS | AL | 12.44% | 0.0573 |
| 2 | FROTO.IS | AL | 10.65% | 0.1135 |
| 3 | BIMAS.IS | AL | 9.83% | 0.0150 |
| 4 | TOASO.IS | AL | 9.39% | 0.0360 |
| 5 | ARCLK.IS | AL | 7.68% | 0.0319 |
| 6 | CASH | CASH | 50.00% | 0.0000 |

Weight sum: 100.00%.

## Validation

Command:

```bash
.venv\Scripts\python.exe main.py
```

Result: passed.

Known data warning: Yahoo Finance returned no valid data for `KOZAL.IS`; the project recorded it through the existing missing ticker flow.

## Decision

Accepted.

Reasoning: the calibrated opportunity filter reduced current cash allocation from 80.00% to 50.00% and improved out-of-sample return versus the fixed 5% threshold while keeping drawdown better than the full-invested baseline.
