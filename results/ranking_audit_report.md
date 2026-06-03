# Ranking Audit Report

Audit target: current active recommendation snapshot, `volume_heavy` Top20.

## Executive Finding

Factor normalization is now directionally correct in `src/ranking.py` and in the current portfolio contribution logic. The helper uses `rank(pct=True, ascending=higher_is_better)`, so factors where higher values should help receive higher percentile scores. Volatility is configured as lower-is-better and now receives a higher percentile score when raw volatility is lower.

This report supersedes the previous audit that found inverted percentile ranking.

## Required Checks

| Check | Result |
|---|---|
| Factor normalization | **Pass**: percentile direction matches factor intent. |
| Sign direction errors | **Pass**: higher momentum, volume increase, and MA trend improve score. |
| Ranking score construction | Weighted sum uses directionally correct normalized inputs. |
| Lower values accidentally rewarded | **No** for momentum, volume increase, and MA trend. |
| Percentile ranking inverted | **No**. `ascending=higher_is_better` is correct for pandas percentile rank in this scoring convention. |
| Volatility penalty direction | **Pass**: lower volatility receives higher normalized score. |

## Direction Verification

| factor | raw_column | higher_should_help | actual_raw_to_norm_corr | intended_direction |
|:---|:---|:---|---:|:---|
| momentum_1m | momentum_1m | True | 0.8028 | positive |
| momentum_3m | momentum_3m | True | 0.9762 | positive |
| momentum_6m | momentum_6m | True | 0.8946 | positive |
| volume_increase | volume_increase | True | 0.9541 | positive |
| above_ma | above_ma | True | 0.9892 | positive |
| volatility_penalty | volatility | False | -0.9912 | negative |

Interpretation: for higher-is-better factors, actual correlation is positive. For volatility, lower should help, so raw volatility has negative correlation with normalized score.

## Current Recommended Portfolio After Fix

| rank | symbol | score | action | momentum_1m | momentum_3m | momentum_6m | volume_increase | above_ma | volatility |
|---:|:---|---:|:---|---:|---:|---:|---:|---:|---:|
| 1 | EREGL.IS | 0.8735 | HOLD | 0.1862 | 0.2539 | 0.6764 | 0.0413 | 1.0000 | 0.0307 |
| 2 | SISE.IS | 0.7971 | HOLD | 0.0046 | 0.0011 | 0.2350 | 0.1566 | 0.5000 | 0.0299 |
| 3 | BIMAS.IS | 0.6971 | HOLD | 0.0013 | 0.1008 | 0.3633 | -0.1104 | 0.5000 | 0.0236 |
| 4 | TOASO.IS | 0.6265 | HOLD | -0.0025 | -0.0189 | 0.3768 | -0.1761 | 1.0000 | 0.0274 |
| 5 | TCELL.IS | 0.5412 | HOLD | -0.0847 | -0.1507 | 0.1173 | 0.0314 | 0.0000 | 0.0219 |
| 6 | PETKM.IS | 0.5382 | BUY | -0.0709 | 0.3014 | 0.3565 | -0.4659 | 1.0000 | 0.0324 |
| 7 | ASELS.IS | 0.5029 | HOLD | -0.0975 | 0.2347 | 1.0938 | -0.3249 | 0.5000 | 0.0314 |
| 8 | FROTO.IS | 0.5000 | HOLD | -0.1311 | -0.2570 | -0.0073 | 0.4703 | 0.0000 | 0.0233 |
| 9 | ARCLK.IS | 0.4941 | BUY | -0.0739 | -0.1231 | -0.0161 | -0.0887 | 0.0000 | 0.0204 |
| 10 | THYAO.IS | 0.4882 | HOLD | -0.0731 | -0.0642 | 0.0687 | -0.1125 | 0.0000 | 0.0232 |

## Remaining Risk

The factor direction bug is fixed, but model selection still has stability risk. The latest final report shows the validation winner (`trend_following` Top3) differs from the out-of-sample winner (`mixed_model` Top15). That validation-to-out-of-sample transfer gap should be treated as the next improvement-cycle candidate.
