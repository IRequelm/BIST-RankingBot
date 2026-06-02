# Ranking Audit Report

Audit target: current active recommendation snapshot, `volume_heavy` Top20.

## Executive Finding

The ranking normalization is inverted in `src/ranking.py` and in the current portfolio contribution logic. The current helper uses `rank(pct=True, ascending=not higher_is_better)`. In pandas, `ascending=False` gives the highest raw value the lowest percentile rank, so factors where higher should be better are accidentally penalized. Conversely, volatility is configured as lower-is-better but is accidentally rewarded when volatility is higher.

Impact: high-ranked stocks can have negative 1m, 3m, and 6m momentum because lower momentum receives a higher normalized score under the current code. The same inversion rewards lower volume increase and higher volatility.

## Required Checks

| Check | Result |
|---|---|
| Factor normalization | **Fail**: percentile direction is inverted. |
| Sign direction errors | **Fail**: higher momentum/volume/trend should improve score, but current normalization makes lower values score higher. |
| Ranking score construction | Weighted sum is structurally simple, but it sums inverted normalized inputs. |
| Lower values accidentally rewarded | **Yes** for momentum, volume increase, and MA trend. |
| Percentile ranking inverted | **Yes**. `ascending=not higher_is_better` is backwards for pandas percentile rank. |
| Volume overpowering momentum | Volume has the largest configured weight in `volume_heavy` at 35%, but the bigger problem is direction: low/negative volume increase is rewarded. |

## Direction Verification

| factor             | raw_column      | higher_should_help   |   actual_raw_to_norm_corr |   intended_raw_to_norm_corr |
|:-------------------|:----------------|:---------------------|--------------------------:|----------------------------:|
| momentum_1m        | momentum_1m     | True                 |                   -0.8028 |                      0.8028 |
| momentum_3m        | momentum_3m     | True                 |                   -0.9762 |                      0.9762 |
| momentum_6m        | momentum_6m     | True                 |                   -0.8946 |                      0.8946 |
| volume_increase    | volume_increase | True                 |                   -0.9541 |                      0.9541 |
| above_ma           | above_ma        | True                 |                   -0.9892 |                      0.9892 |
| volatility_penalty | volatility      | False                |                    0.9912 |                     -0.9912 |

Interpretation: for higher-is-better factors, actual correlation should be positive but is negative. For volatility, lower should help, so raw volatility should have negative correlation with normalized score; actual correlation is positive.

## Current Top 20 Raw Factor Values

|   rank | symbol   |   score |   momentum_1m |   momentum_3m |   momentum_6m |   volume_increase |   above_ma |   volatility |
|-------:|:---------|--------:|--------------:|--------------:|--------------:|------------------:|-----------:|-------------:|
|      1 | PGSUS.IS |  0.7206 |       -0.0597 |       -0.1672 |       -0.1622 |           -0.2601 |     0.0000 |       0.0216 |
|      2 | YKBNK.IS |  0.6824 |       -0.0859 |       -0.2408 |       -0.0533 |           -0.0415 |     0.0000 |       0.0306 |
|      3 | AKBNK.IS |  0.6412 |       -0.1357 |       -0.2831 |        0.0153 |            0.1238 |     0.0000 |       0.0317 |
|      4 | SAHOL.IS |  0.6353 |       -0.0744 |       -0.1388 |        0.1041 |           -0.1380 |     0.0000 |       0.0262 |
|      5 | TUPRS.IS |  0.6206 |       -0.1111 |        0.1808 |        0.3087 |           -0.4372 |     0.5000 |       0.0254 |
|      6 | GARAN.IS |  0.6000 |       -0.0723 |       -0.2186 |       -0.0779 |           -0.0070 |     0.0000 |       0.0280 |
|      7 | THYAO.IS |  0.5706 |       -0.0731 |       -0.0642 |        0.0687 |           -0.1125 |     0.0000 |       0.0232 |
|      8 | KCHOL.IS |  0.5706 |       -0.0806 |       -0.0597 |        0.1458 |           -0.2600 |     0.5000 |       0.0210 |
|      9 | ARCLK.IS |  0.5647 |       -0.0739 |       -0.1231 |       -0.0161 |           -0.0887 |     0.0000 |       0.0204 |
|     10 | FROTO.IS |  0.5588 |       -0.1311 |       -0.2570 |       -0.0073 |            0.4703 |     0.0000 |       0.0233 |
|     11 | ASELS.IS |  0.5559 |       -0.0975 |        0.2347 |        1.0938 |           -0.3249 |     0.5000 |       0.0314 |
|     12 | PETKM.IS |  0.5206 |       -0.0709 |        0.3014 |        0.3565 |           -0.4659 |     1.0000 |       0.0324 |
|     13 | TCELL.IS |  0.5176 |       -0.0847 |       -0.1507 |        0.1173 |            0.0314 |     0.0000 |       0.0219 |
|     14 | TOASO.IS |  0.4324 |       -0.0025 |       -0.0189 |        0.3768 |           -0.1761 |     1.0000 |       0.0274 |
|     15 | BIMAS.IS |  0.3618 |        0.0013 |        0.1008 |        0.3633 |           -0.1104 |     0.5000 |       0.0236 |
|     16 | SISE.IS  |  0.2618 |        0.0046 |        0.0011 |        0.2350 |            0.1566 |     0.5000 |       0.0299 |
|     17 | EREGL.IS |  0.1853 |        0.1862 |        0.2539 |        0.6764 |            0.0413 |     1.0000 |       0.0307 |

## Current Top 20 Normalized Values: Actual vs Intended

|   rank | symbol   |   momentum_1m_actual_norm |   momentum_3m_actual_norm |   momentum_6m_actual_norm |   volume_increase_actual_norm |   above_ma_actual_norm |   volatility_penalty_actual_norm |   momentum_1m_intended_norm |   momentum_3m_intended_norm |   momentum_6m_intended_norm |   volume_increase_intended_norm |   above_ma_intended_norm |   volatility_penalty_intended_norm |
|-------:|:---------|--------------------------:|--------------------------:|--------------------------:|------------------------------:|-----------------------:|---------------------------------:|----------------------------:|----------------------------:|----------------------------:|--------------------------------:|-------------------------:|-----------------------------------:|
|      1 | PGSUS.IS |                    0.2941 |                    0.7647 |                    1.0000 |                        0.8235 |                 0.7647 |                           0.1765 |                      0.7647 |                      0.2941 |                      0.0588 |                          0.2353 |                   0.2941 |                             0.8824 |
|      2 | YKBNK.IS |                    0.7647 |                    0.8824 |                    0.8824 |                        0.4118 |                 0.7647 |                           0.7647 |                      0.2941 |                      0.1765 |                      0.1765 |                          0.6471 |                   0.2941 |                             0.2941 |
|      3 | AKBNK.IS |                    1.0000 |                    1.0000 |                    0.7059 |                        0.1765 |                 0.7647 |                           0.9412 |                      0.0588 |                      0.0588 |                      0.3529 |                          0.8824 |                   0.2941 |                             0.1176 |
|      4 | SAHOL.IS |                    0.5882 |                    0.6471 |                    0.5882 |                        0.6471 |                 0.7647 |                           0.5294 |                      0.4706 |                      0.4118 |                      0.4706 |                          0.4118 |                   0.2941 |                             0.5294 |
|      5 | TUPRS.IS |                    0.8824 |                    0.2353 |                    0.3529 |                        0.9412 |                 0.3529 |                           0.4706 |                      0.1765 |                      0.8235 |                      0.7059 |                          0.1176 |                   0.7059 |                             0.5882 |
|      6 | GARAN.IS |                    0.4118 |                    0.8235 |                    0.9412 |                        0.3529 |                 0.7647 |                           0.6471 |                      0.6471 |                      0.2353 |                      0.1176 |                          0.7059 |                   0.2941 |                             0.4118 |
|      7 | THYAO.IS |                    0.4706 |                    0.5294 |                    0.6471 |                        0.5882 |                 0.7647 |                           0.2941 |                      0.5882 |                      0.5294 |                      0.4118 |                          0.4706 |                   0.2941 |                             0.7647 |
|      8 | KCHOL.IS |                    0.6471 |                    0.4706 |                    0.4706 |                        0.7647 |                 0.3529 |                           0.1176 |                      0.4118 |                      0.5882 |                      0.5882 |                          0.2941 |                   0.7059 |                             0.9412 |
|      9 | ARCLK.IS |                    0.5294 |                    0.5882 |                    0.8235 |                        0.4706 |                 0.7647 |                           0.0588 |                      0.5294 |                      0.4706 |                      0.2353 |                          0.5882 |                   0.2941 |                             1.0000 |
|     10 | FROTO.IS |                    0.9412 |                    0.9412 |                    0.7647 |                        0.0588 |                 0.7647 |                           0.3529 |                      0.1176 |                      0.1176 |                      0.2941 |                          1.0000 |                   0.2941 |                             0.7059 |
|     11 | ASELS.IS |                    0.8235 |                    0.1765 |                    0.0588 |                        0.8824 |                 0.3529 |                           0.8824 |                      0.2353 |                      0.8824 |                      1.0000 |                          0.1765 |                   0.7059 |                             0.1765 |
|     12 | PETKM.IS |                    0.3529 |                    0.0588 |                    0.2941 |                        1.0000 |                 0.1176 |                           1.0000 |                      0.7059 |                      1.0000 |                      0.7647 |                          0.0588 |                   0.9412 |                             0.0588 |
|     13 | TCELL.IS |                    0.7059 |                    0.7059 |                    0.5294 |                        0.2941 |                 0.7647 |                           0.2353 |                      0.3529 |                      0.3529 |                      0.5294 |                          0.7647 |                   0.2941 |                             0.8235 |
|     14 | TOASO.IS |                    0.2353 |                    0.4118 |                    0.1765 |                        0.7059 |                 0.1176 |                           0.5882 |                      0.8235 |                      0.6471 |                      0.8824 |                          0.3529 |                   0.9412 |                             0.4706 |
|     15 | BIMAS.IS |                    0.1765 |                    0.2941 |                    0.2353 |                        0.5294 |                 0.3529 |                           0.4118 |                      0.8824 |                      0.7647 |                      0.8235 |                          0.5294 |                   0.7059 |                             0.6471 |
|     16 | SISE.IS  |                    0.1176 |                    0.3529 |                    0.4118 |                        0.1176 |                 0.3529 |                           0.7059 |                      0.9412 |                      0.7059 |                      0.6471 |                          0.9412 |                   0.7059 |                             0.3529 |
|     17 | EREGL.IS |                    0.0588 |                    0.1176 |                    0.1176 |                        0.2353 |                 0.1176 |                           0.8235 |                      1.0000 |                      0.9412 |                      0.9412 |                          0.8235 |                   0.9412 |                             0.2353 |

## Current Top 20 Weighted Contributions

|   rank | symbol   |   score |   actual_recalc_score_top20 |   intended_recalc_score_top20 |   momentum_1m_actual_weighted |   momentum_3m_actual_weighted |   momentum_6m_actual_weighted |   volume_increase_actual_weighted |   above_ma_actual_weighted |   volatility_penalty_actual_weighted |
|-------:|:---------|--------:|----------------------------:|------------------------------:|------------------------------:|------------------------------:|------------------------------:|----------------------------------:|---------------------------:|-------------------------------------:|
|      1 | PGSUS.IS |  0.7206 |                      0.7206 |                        0.3382 |                        0.0441 |                        0.1529 |                        0.1500 |                            0.2882 |                     0.0765 |                               0.0088 |
|      2 | YKBNK.IS |  0.6824 |                      0.6824 |                        0.3765 |                        0.1147 |                        0.1765 |                        0.1324 |                            0.1441 |                     0.0765 |                               0.0382 |
|      3 | AKBNK.IS |  0.6412 |                      0.6412 |                        0.4176 |                        0.1500 |                        0.2000 |                        0.1059 |                            0.0618 |                     0.0765 |                               0.0471 |
|      4 | SAHOL.IS |  0.6353 |                      0.6353 |                        0.4235 |                        0.0882 |                        0.1294 |                        0.0882 |                            0.2265 |                     0.0765 |                               0.0265 |
|      5 | TUPRS.IS |  0.6206 |                      0.6206 |                        0.4382 |                        0.1324 |                        0.0471 |                        0.0529 |                            0.3294 |                     0.0353 |                               0.0235 |
|      6 | GARAN.IS |  0.6000 |                      0.6000 |                        0.4588 |                        0.0618 |                        0.1647 |                        0.1412 |                            0.1235 |                     0.0765 |                               0.0324 |
|      7 | THYAO.IS |  0.5706 |                      0.5706 |                        0.4882 |                        0.0706 |                        0.1059 |                        0.0971 |                            0.2059 |                     0.0765 |                               0.0147 |
|      8 | KCHOL.IS |  0.5706 |                      0.5706 |                        0.4882 |                        0.0971 |                        0.0941 |                        0.0706 |                            0.2676 |                     0.0353 |                               0.0059 |
|      9 | ARCLK.IS |  0.5647 |                      0.5647 |                        0.4941 |                        0.0794 |                        0.1176 |                        0.1235 |                            0.1647 |                     0.0765 |                               0.0029 |
|     10 | FROTO.IS |  0.5588 |                      0.5588 |                        0.5000 |                        0.1412 |                        0.1882 |                        0.1147 |                            0.0206 |                     0.0765 |                               0.0176 |
|     11 | ASELS.IS |  0.5559 |                      0.5559 |                        0.5029 |                        0.1235 |                        0.0353 |                        0.0088 |                            0.3088 |                     0.0353 |                               0.0441 |
|     12 | PETKM.IS |  0.5206 |                      0.5206 |                        0.5382 |                        0.0529 |                        0.0118 |                        0.0441 |                            0.3500 |                     0.0118 |                               0.0500 |
|     13 | TCELL.IS |  0.5176 |                      0.5176 |                        0.5412 |                        0.1059 |                        0.1412 |                        0.0794 |                            0.1029 |                     0.0765 |                               0.0118 |
|     14 | TOASO.IS |  0.4324 |                      0.4324 |                        0.6265 |                        0.0353 |                        0.0824 |                        0.0265 |                            0.2471 |                     0.0118 |                               0.0294 |
|     15 | BIMAS.IS |  0.3618 |                      0.3618 |                        0.6971 |                        0.0265 |                        0.0588 |                        0.0353 |                            0.1853 |                     0.0353 |                               0.0206 |
|     16 | SISE.IS  |  0.2618 |                      0.2618 |                        0.7971 |                        0.0176 |                        0.0706 |                        0.0618 |                            0.0412 |                     0.0353 |                               0.0353 |
|     17 | EREGL.IS |  0.1853 |                      0.1853 |                        0.8735 |                        0.0088 |                        0.0235 |                        0.0176 |                            0.0824 |                     0.0118 |                               0.0412 |

## Negative Momentum In Current Top 10

| symbol   |   momentum_1m |   momentum_3m |   momentum_6m |   score |
|:---------|--------------:|--------------:|--------------:|--------:|
| PGSUS.IS |       -0.0597 |       -0.1672 |       -0.1622 |  0.7206 |
| YKBNK.IS |       -0.0859 |       -0.2408 |       -0.0533 |  0.6824 |
| AKBNK.IS |       -0.1357 |       -0.2831 |        0.0153 |  0.6412 |
| SAHOL.IS |       -0.0744 |       -0.1388 |        0.1041 |  0.6353 |
| TUPRS.IS |       -0.1111 |        0.1808 |        0.3087 |  0.6206 |
| GARAN.IS |       -0.0723 |       -0.2186 |       -0.0779 |  0.6000 |
| THYAO.IS |       -0.0731 |       -0.0642 |        0.0687 |  0.5706 |
| KCHOL.IS |       -0.0806 |       -0.0597 |        0.1458 |  0.5706 |
| ARCLK.IS |       -0.0739 |       -0.1231 |       -0.0161 |  0.5647 |
| FROTO.IS |       -0.1311 |       -0.2570 |       -0.0073 |  0.5588 |

## Volume Factor Influence In Current Top 10

| symbol   |   score |   volume_increase_actual_weighted |   volume_contribution_share |
|:---------|--------:|----------------------------------:|----------------------------:|
| PGSUS.IS |  0.7206 |                            0.2882 |                      0.4000 |
| YKBNK.IS |  0.6824 |                            0.1441 |                      0.2112 |
| AKBNK.IS |  0.6412 |                            0.0618 |                      0.0963 |
| SAHOL.IS |  0.6353 |                            0.2265 |                      0.3565 |
| TUPRS.IS |  0.6206 |                            0.3294 |                      0.5308 |
| GARAN.IS |  0.6000 |                            0.1235 |                      0.2059 |
| THYAO.IS |  0.5706 |                            0.2059 |                      0.3608 |
| KCHOL.IS |  0.5706 |                            0.2676 |                      0.4691 |
| ARCLK.IS |  0.5647 |                            0.1647 |                      0.2917 |
| FROTO.IS |  0.5588 |                            0.0206 |                      0.0368 |

The `volume_heavy` model gives volume increase a 35% weight. That is intentionally large, but because normalization is inverted, stocks with weaker or more negative volume increase receive larger volume contributions. This makes the model defensive in practice, but unintentionally so.

## Anomalies

- Higher momentum does **not** improve score in the current implementation; it lowers the percentile contribution.
- Lower volatility does **not** improve score in the current implementation; higher volatility receives a larger percentile contribution.
- Higher volume increase does **not** improve score in the current implementation; lower volume increase receives a larger contribution.
- Current top-ranked names with broadly negative momentum are a direct consequence of the inverted percentile rank direction.
- `above_ma` is also inverted: weaker MA trend receives higher normalized contribution.

## Recommended Fix

Change `_cross_sectional_score` to:

```python
return clean.rank(pct=True, ascending=higher_is_better)
```

With this change: higher momentum, higher volume increase, and stronger MA trend receive higher percentiles; lower volatility receives a higher percentile when `higher_is_better=False`. After fixing, rerun all backtests and invalidate prior ranking/backtest reports because historical results were based on inverted factor signs.
