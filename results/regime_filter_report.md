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
| baseline              |             2.0393 |                         0.4275 |            -0.2002 |                     0.3503 |                 0.3322 |                  1 |
| defensive_mode        |             1.9476 |                         0.3357 |            -0.2051 |                     0.2304 |                 0.2232 |                  1 |
| reduced_exposure_mode |             1.7628 |                         0.1510 |            -0.1942 |                     0.2782 |                 0.0678 |                  1 |
| cash_mode             |             1.5441 |                        -0.0677 |            -0.2027 |                     0.1960 |                -0.2383 |                  1 |

## Best Out-Of-Sample Combinations

| policy                | base_model      |   base_portfolio_size | period        |   months |   bear_months |   avg_exposure |   total_return |   bist100_total_return |   excess_return_vs_bist100 |   max_drawdown |   bist100_max_drawdown |   win_rate |   robustness_score |
|:----------------------|:----------------|----------------------:|:--------------|---------:|--------------:|---------------:|---------------:|-----------------------:|---------------------------:|---------------:|-----------------------:|-----------:|-------------------:|
| baseline              | mixed_model     |                    15 | out_of_sample |       34 |             9 |         1.0000 |         0.5795 |                 0.3731 |                     0.2064 |        -0.1961 |                -0.2550 |     0.5882 |             0.1083 |
| baseline              | trend_following |                    15 | out_of_sample |       34 |             9 |         1.0000 |         0.5302 |                 0.3731 |                     0.1571 |        -0.1926 |                -0.2550 |     0.5882 |             0.0660 |
| baseline              | momentum_heavy  |                    15 | out_of_sample |       34 |             9 |         1.0000 |         0.5312 |                 0.3731 |                     0.1581 |        -0.1948 |                -0.2550 |     0.5882 |             0.0626 |
| baseline              | momentum_heavy  |                     3 | out_of_sample |       34 |             9 |         1.0000 |         0.4897 |                 0.3731 |                     0.1166 |        -0.1839 |                -0.2550 |     0.5588 |             0.0284 |
| reduced_exposure_mode | mixed_model     |                    15 | out_of_sample |       34 |             9 |         0.8676 |         0.4480 |                 0.3731 |                     0.0750 |        -0.1817 |                -0.2550 |     0.5882 |             0.0058 |
| reduced_exposure_mode | momentum_heavy  |                     3 | out_of_sample |       34 |             9 |         0.8676 |         0.4233 |                 0.3731 |                     0.0502 |        -0.1660 |                -0.2550 |     0.5588 |            -0.0025 |
| baseline              | trend_following |                     3 | out_of_sample |       34 |             9 |         1.0000 |         0.4233 |                 0.3731 |                     0.0502 |        -0.1767 |                -0.2550 |     0.5882 |            -0.0090 |
| baseline              | low_volatility  |                    15 | out_of_sample |       34 |             9 |         1.0000 |         0.5105 |                 0.3731 |                     0.1375 |        -0.2209 |                -0.2550 |     0.5588 |            -0.0249 |
| reduced_exposure_mode | momentum_heavy  |                    15 | out_of_sample |       34 |             9 |         0.8676 |         0.4118 |                 0.3731 |                     0.0388 |        -0.1851 |                -0.2550 |     0.5882 |            -0.0373 |
| reduced_exposure_mode | trend_following |                    15 | out_of_sample |       34 |             9 |         0.8676 |         0.4110 |                 0.3731 |                     0.0379 |        -0.1882 |                -0.2550 |     0.5882 |            -0.0443 |

## Regime Signal Coverage

- Total signal months: 98
- BIST100 below MA200 months: 22
- Below-MA200 rate: 22.45%
