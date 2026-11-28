# Regime Filter Report

Policies tested:
- baseline: current ranking/backtest system
- cash_mode: hold cash when BIST100 is below MA200
- defensive_mode: switch to low_volatility Top 5 when BIST100 is below MA200
- reduced_exposure_mode: invest 50% when BIST100 is below MA200

Recommended policy: **baseline**

Recommendation is based on average robustness score across model and portfolio combinations.

## Policy Summary

| policy                |   avg_total_return |   avg_excess_return_vs_bist100 |   avg_max_drawdown |   avg_out_of_sample_return |   avg_robustness_score |   best_combo_count |
|:----------------------|-------------------:|-------------------------------:|-------------------:|---------------------------:|-----------------------:|-------------------:|
| baseline              |             2.0071 |                         0.4224 |            -0.2019 |                     0.2539 |                 0.3212 |                  1 |
| defensive_mode        |             1.9207 |                         0.3360 |            -0.2082 |                     0.1499 |                 0.2125 |                  1 |
| reduced_exposure_mode |             1.7470 |                         0.1622 |            -0.1946 |                     0.2307 |                 0.0757 |                  1 |
| cash_mode             |             1.5441 |                        -0.0407 |            -0.2027 |                     0.1960 |                -0.2113 |                  1 |

## Best Out-Of-Sample Combinations

| policy                | base_model      |   base_portfolio_size | period        |   months |   bear_months |   avg_exposure |   total_return |   bist100_total_return |   excess_return_vs_bist100 |   max_drawdown |   bist100_max_drawdown |   win_rate |   robustness_score |
|:----------------------|:----------------|----------------------:|:--------------|---------:|--------------:|---------------:|---------------:|-----------------------:|---------------------------:|---------------:|-----------------------:|-----------:|-------------------:|
| baseline              | mixed_model     |                    15 | out_of_sample |       34 |             9 |         1.0000 |         0.4953 |                 0.2919 |                     0.2034 |        -0.1961 |                -0.2550 |     0.5882 |             0.1053 |
| baseline              | trend_following |                    15 | out_of_sample |       34 |             9 |         1.0000 |         0.4395 |                 0.2919 |                     0.1476 |        -0.1926 |                -0.2550 |     0.5882 |             0.0564 |
| baseline              | momentum_heavy  |                    15 | out_of_sample |       34 |             9 |         1.0000 |         0.4404 |                 0.2919 |                     0.1485 |        -0.1948 |                -0.2550 |     0.5882 |             0.0530 |
| reduced_exposure_mode | mixed_model     |                    15 | out_of_sample |       34 |             9 |         0.8676 |         0.4073 |                 0.2919 |                     0.1154 |        -0.1817 |                -0.2550 |     0.5882 |             0.0462 |
| reduced_exposure_mode | momentum_heavy  |                     3 | out_of_sample |       34 |             9 |         0.8676 |         0.3658 |                 0.2919 |                     0.0739 |        -0.1660 |                -0.2550 |     0.5294 |             0.0065 |
| reduced_exposure_mode | momentum_heavy  |                    15 | out_of_sample |       34 |             9 |         0.8676 |         0.3680 |                 0.2919 |                     0.0761 |        -0.1851 |                -0.2550 |     0.5882 |            -0.0000 |
| reduced_exposure_mode | low_volatility  |                    15 | out_of_sample |       34 |             9 |         0.8676 |         0.3547 |                 0.2919 |                     0.0628 |        -0.1737 |                -0.2550 |     0.5588 |            -0.0053 |
| reduced_exposure_mode | trend_following |                    15 | out_of_sample |       34 |             9 |         0.8676 |         0.3672 |                 0.2919 |                     0.0753 |        -0.1882 |                -0.2550 |     0.5882 |            -0.0069 |
| baseline              | low_volatility  |                    15 | out_of_sample |       34 |             9 |         1.0000 |         0.4295 |                 0.2919 |                     0.1376 |        -0.2209 |                -0.2550 |     0.5588 |            -0.0248 |
| reduced_exposure_mode | trend_following |                     3 | out_of_sample |       34 |             9 |         0.8676 |         0.3049 |                 0.2919 |                     0.0130 |        -0.1767 |                -0.2550 |     0.5588 |            -0.0610 |

## Regime Signal Coverage

- Total signal months: 98
- BIST100 below MA200 months: 22
- Below-MA200 rate: 22.45%
