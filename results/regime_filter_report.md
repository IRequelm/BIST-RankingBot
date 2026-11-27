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
| baseline              |             2.0004 |                         0.4248 |            -0.2040 |                     0.2336 |                 0.3188 |                  1 |
| defensive_mode        |             1.9125 |                         0.3369 |            -0.2129 |                     0.1253 |                 0.2041 |                  1 |
| reduced_exposure_mode |             1.7437 |                         0.1681 |            -0.1949 |                     0.2208 |                 0.0802 |                  1 |
| cash_mode             |             1.5441 |                        -0.0315 |            -0.2027 |                     0.1960 |                -0.2021 |                  1 |

## Best Out-Of-Sample Combinations

| policy                | base_model      |   base_portfolio_size | period        |   months |   bear_months |   avg_exposure |   total_return |   bist100_total_return |   excess_return_vs_bist100 |   max_drawdown |   bist100_max_drawdown |   win_rate |   robustness_score |
|:----------------------|:----------------|----------------------:|:--------------|---------:|--------------:|---------------:|---------------:|-----------------------:|---------------------------:|---------------:|-----------------------:|-----------:|-------------------:|
| baseline              | mixed_model     |                    15 | out_of_sample |       34 |             9 |         1.0000 |         0.4702 |                 0.2644 |                     0.2058 |        -0.1961 |                -0.2562 |     0.5882 |             0.1077 |
| reduced_exposure_mode | mixed_model     |                    15 | out_of_sample |       34 |             9 |         0.8676 |         0.3952 |                 0.2644 |                     0.1308 |        -0.1817 |                -0.2562 |     0.5882 |             0.0616 |
| baseline              | trend_following |                    15 | out_of_sample |       34 |             9 |         1.0000 |         0.4140 |                 0.2644 |                     0.1496 |        -0.1926 |                -0.2562 |     0.5882 |             0.0584 |
| baseline              | momentum_heavy  |                    15 | out_of_sample |       34 |             9 |         1.0000 |         0.4149 |                 0.2644 |                     0.1505 |        -0.1948 |                -0.2562 |     0.5882 |             0.0549 |
| reduced_exposure_mode | momentum_heavy  |                     3 | out_of_sample |       34 |             9 |         0.8676 |         0.3539 |                 0.2644 |                     0.0895 |        -0.1660 |                -0.2562 |     0.5294 |             0.0222 |
| reduced_exposure_mode | momentum_heavy  |                    15 | out_of_sample |       34 |             9 |         0.8676 |         0.3557 |                 0.2644 |                     0.0913 |        -0.1851 |                -0.2562 |     0.5882 |             0.0152 |
| reduced_exposure_mode | low_volatility  |                    15 | out_of_sample |       34 |             9 |         0.8676 |         0.3424 |                 0.2644 |                     0.0780 |        -0.1737 |                -0.2562 |     0.5588 |             0.0100 |
| reduced_exposure_mode | trend_following |                    15 | out_of_sample |       34 |             9 |         0.8676 |         0.3549 |                 0.2644 |                     0.0905 |        -0.1882 |                -0.2562 |     0.5882 |             0.0083 |
| baseline              | low_volatility  |                    15 | out_of_sample |       34 |             9 |         1.0000 |         0.4043 |                 0.2644 |                     0.1399 |        -0.2209 |                -0.2562 |     0.5588 |            -0.0224 |
| reduced_exposure_mode | trend_following |                     3 | out_of_sample |       34 |             9 |         0.8676 |         0.2936 |                 0.2644 |                     0.0292 |        -0.1767 |                -0.2562 |     0.5588 |            -0.0448 |

## Regime Signal Coverage

- Total signal months: 98
- BIST100 below MA200 months: 22
- Below-MA200 rate: 22.45%
