# Signal Funnel Report

- Latest trading session: 2026-06-10
- Data interval: 15m
- Starting universe size: 18
- Final candidates: 1
- Final candidate symbols: ASELS.IS

## Funnel Counts

| Stage | Count |
|---|---:|
| Starting universe size | 18 |
| After data availability filter | 17 |
| After momentum filter | 1 |
| After VWAP filter | 1 |
| After mean reversion filter | 1 |
| After volatility filter | 1 |
| Final candidates | 1 |

## Rejections By Stage

| Stage | Rejected |
|---|---:|
| After data availability filter | 1 |
| After momentum filter | 16 |
| After VWAP filter | 0 |
| After mean reversion filter | 0 |
| After volatility filter | 0 |

## Most Restrictive Filter

The most restrictive step was **After momentum filter**, which rejected **16** symbols from the previous stage.

## Why Did Only 1 Trade Survive?

Only **1** symbol passed every rule. The funnel shows that most symbols were removed before the final risk checks, mainly because they did not satisfy the combined opening momentum requirement: opening strength of at least **0.40%** and volume ratio of at least **1.05**. After that, the VWAP rule removed symbols whose signal candle was not above VWAP. Mean reversion and volatility did not create the main bottleneck in this session unless shown in the stage counts above.

## Failure Stage Summary

| Failure Stage     |   Count |
|:------------------|--------:|
| Momentum          |      16 |
| Survived          |       1 |
| Data availability |       1 |

## Symbol Diagnostics

| symbol   | has_data   | opening_strength   |   volume_ratio |   above_vwap |   spike_warning |   extreme_volatility | failure_stage     | reason                                           |
|:---------|:-----------|:-------------------|---------------:|-------------:|----------------:|---------------------:|:------------------|:-------------------------------------------------|
| AKBNK.IS | True       | 0.07%              |           0.84 |            0 |               0 |                    0 | Momentum          | Opening strength and volume confirmation failed. |
| ARCLK.IS | True       | 0.00%              |           0.78 |            0 |               0 |                    0 | Momentum          | Opening strength and volume confirmation failed. |
| ASELS.IS | True       | 1.96%              |           1.26 |            1 |               0 |                    0 | Survived          | Passed all filters.                              |
| BIMAS.IS | True       | 0.07%              |           0.34 |            0 |               0 |                    0 | Momentum          | Opening strength and volume confirmation failed. |
| EREGL.IS | True       | 0.05%              |           0.91 |            0 |               0 |                    0 | Momentum          | Opening strength and volume confirmation failed. |
| FROTO.IS | True       | 0.06%              |           0.69 |            0 |               0 |                    0 | Momentum          | Opening strength and volume confirmation failed. |
| GARAN.IS | True       | 0.31%              |           0.89 |            1 |               0 |                    0 | Momentum          | Opening strength and volume confirmation failed. |
| KCHOL.IS | True       | 0.32%              |           0.85 |            1 |               0 |                    0 | Momentum          | Opening strength and volume confirmation failed. |
| KOZAL.IS | False      |                    |                |          nan |             nan |                  nan | Data availability | No usable latest-session intraday candles.       |
| PETKM.IS | True       | 0.79%              |           1    |            1 |               0 |                    0 | Momentum          | Volume confirmation below threshold.             |
| PGSUS.IS | True       | 0.24%              |           0.88 |            0 |               0 |                    0 | Momentum          | Opening strength and volume confirmation failed. |
| SAHOL.IS | True       | 0.33%              |           0.61 |            1 |               0 |                    0 | Momentum          | Opening strength and volume confirmation failed. |
| SISE.IS  | True       | 0.18%              |           0.59 |            0 |               0 |                    0 | Momentum          | Opening strength and volume confirmation failed. |
| TCELL.IS | True       | 0.19%              |           1.49 |            0 |               0 |                    0 | Momentum          | Opening momentum below threshold.                |
| THYAO.IS | True       | 0.25%              |           0.78 |            0 |               0 |                    0 | Momentum          | Opening strength and volume confirmation failed. |
| TOASO.IS | True       | 0.00%              |           1.6  |            0 |               0 |                    0 | Momentum          | Opening momentum below threshold.                |
| TUPRS.IS | True       | 3.04%              |           0.83 |            1 |               0 |                    0 | Momentum          | Volume confirmation below threshold.             |
| YKBNK.IS | True       | 0.11%              |           0.71 |            0 |               0 |                    0 | Momentum          | Opening strength and volume confirmation failed. |

## Warnings

- KOZAL.IS: 15m intraday data unavailable.
