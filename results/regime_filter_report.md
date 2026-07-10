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
| baseline              |             2.0682 |                         0.3607 |            -0.1902 |                     0.4370 |                 0.2865 |                  1 |
| defensive_mode        |             1.9952 |                         0.2877 |            -0.1901 |                     0.3733 |                 0.2058 |                  1 |
| reduced_exposure_mode |             1.7815 |                         0.0740 |            -0.1929 |                     0.3342 |                -0.0056 |                  1 |
| cash_mode             |             1.5556 |                        -0.1519 |            -0.2024 |                     0.2305 |                -0.3192 |                  1 |

## Best Out-Of-Sample Combinations

| policy                | base_model      |   base_portfolio_size | period        |   months |   bear_months |   avg_exposure |   total_return |   bist100_total_return |   excess_return_vs_bist100 |   max_drawdown |   bist100_max_drawdown |   win_rate |   robustness_score |
|:----------------------|:----------------|----------------------:|:--------------|---------:|--------------:|---------------:|---------------:|-----------------------:|---------------------------:|---------------:|-----------------------:|-----------:|-------------------:|
| baseline              | mixed_model     |                    15 | out_of_sample |       30 |             7 |         1.0000 |         0.6267 |                 0.6601 |                    -0.0334 |        -0.1644 |                -0.1675 |     0.6000 |            -0.0623 |
| baseline              | momentum_heavy  |                    15 | out_of_sample |       30 |             7 |         1.0000 |         0.6253 |                 0.6601 |                    -0.0348 |        -0.1680 |                -0.1675 |     0.6000 |            -0.0708 |
| baseline              | low_volatility  |                    15 | out_of_sample |       30 |             7 |         1.0000 |         0.6021 |                 0.6601 |                    -0.0580 |        -0.1563 |                -0.1675 |     0.5667 |            -0.0873 |
| baseline              | momentum_heavy  |                     3 | out_of_sample |       30 |             7 |         1.0000 |         0.5894 |                 0.6601 |                    -0.0707 |        -0.1660 |                -0.1675 |     0.6000 |            -0.1028 |
| baseline              | trend_following |                    15 | out_of_sample |       30 |             7 |         1.0000 |         0.5991 |                 0.6601 |                    -0.0610 |        -0.1747 |                -0.1675 |     0.6000 |            -0.1104 |
| baseline              | volume_heavy    |                    15 | out_of_sample |       30 |             7 |         1.0000 |         0.5483 |                 0.6601 |                    -0.1118 |        -0.1746 |                -0.1675 |     0.6000 |            -0.1609 |
| defensive_mode        | mixed_model     |                    15 | out_of_sample |       30 |             7 |         1.0000 |         0.5241 |                 0.6601 |                    -0.1360 |        -0.1757 |                -0.1675 |     0.5333 |            -0.2207 |
| defensive_mode        | momentum_heavy  |                     3 | out_of_sample |       30 |             7 |         1.0000 |         0.4828 |                 0.6601 |                    -0.1773 |        -0.1660 |                -0.1675 |     0.5667 |            -0.2261 |
| reduced_exposure_mode | mixed_model     |                    15 | out_of_sample |       30 |             7 |         0.8833 |         0.4952 |                 0.6601 |                    -0.1649 |        -0.1817 |                -0.1675 |     0.6000 |            -0.2282 |
| defensive_mode        | low_volatility  |                    15 | out_of_sample |       30 |             7 |         1.0000 |         0.4942 |                 0.6601 |                    -0.1659 |        -0.1661 |                -0.1675 |     0.5333 |            -0.2314 |

## Regime Signal Coverage

- Total signal months: 94
- BIST100 below MA200 months: 19
- Below-MA200 rate: 20.21%
