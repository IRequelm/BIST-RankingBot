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
| baseline              |             2.0416 |                         0.4229 |            -0.2002 |                     0.3571 |                 0.3276 |                  1 |
| defensive_mode        |             1.9529 |                         0.3342 |            -0.2051 |                     0.2464 |                 0.2217 |                  1 |
| reduced_exposure_mode |             1.7639 |                         0.1452 |            -0.1942 |                     0.2815 |                 0.0620 |                  1 |
| cash_mode             |             1.5441 |                        -0.0746 |            -0.2027 |                     0.1960 |                -0.2452 |                  1 |

## Best Out-Of-Sample Combinations

| policy                | base_model      |   base_portfolio_size | period        |   months |   bear_months |   avg_exposure |   total_return |   bist100_total_return |   excess_return_vs_bist100 |   max_drawdown |   bist100_max_drawdown |   win_rate |   robustness_score |
|:----------------------|:----------------|----------------------:|:--------------|---------:|--------------:|---------------:|---------------:|-----------------------:|---------------------------:|---------------:|-----------------------:|-----------:|-------------------:|
| baseline              | mixed_model     |                    15 | out_of_sample |       34 |             9 |         1.0000 |         0.5935 |                 0.3937 |                     0.1998 |        -0.1961 |                -0.2550 |     0.5882 |             0.1017 |
| baseline              | trend_following |                    15 | out_of_sample |       34 |             9 |         1.0000 |         0.5406 |                 0.3937 |                     0.1469 |        -0.1926 |                -0.2550 |     0.5882 |             0.0558 |
| baseline              | momentum_heavy  |                    15 | out_of_sample |       34 |             9 |         1.0000 |         0.5416 |                 0.3937 |                     0.1479 |        -0.1948 |                -0.2550 |     0.5882 |             0.0524 |
| baseline              | momentum_heavy  |                     3 | out_of_sample |       34 |             9 |         1.0000 |         0.5000 |                 0.3937 |                     0.1063 |        -0.1839 |                -0.2550 |     0.5588 |             0.0180 |
| reduced_exposure_mode | mixed_model     |                    15 | out_of_sample |       34 |             9 |         0.8676 |         0.4548 |                 0.3937 |                     0.0611 |        -0.1817 |                -0.2550 |     0.5882 |            -0.0081 |
| reduced_exposure_mode | momentum_heavy  |                     3 | out_of_sample |       34 |             9 |         0.8676 |         0.4283 |                 0.3937 |                     0.0346 |        -0.1660 |                -0.2550 |     0.5588 |            -0.0181 |
| baseline              | trend_following |                     3 | out_of_sample |       34 |             9 |         1.0000 |         0.4331 |                 0.3937 |                     0.0394 |        -0.1767 |                -0.2550 |     0.5882 |            -0.0198 |
| baseline              | low_volatility  |                    15 | out_of_sample |       34 |             9 |         1.0000 |         0.5241 |                 0.3937 |                     0.1304 |        -0.2209 |                -0.2550 |     0.5588 |            -0.0320 |
| reduced_exposure_mode | momentum_heavy  |                    15 | out_of_sample |       34 |             9 |         0.8676 |         0.4169 |                 0.3937 |                     0.0232 |        -0.1851 |                -0.2550 |     0.5882 |            -0.0529 |
| reduced_exposure_mode | trend_following |                    15 | out_of_sample |       34 |             9 |         0.8676 |         0.4160 |                 0.3937 |                     0.0223 |        -0.1882 |                -0.2550 |     0.5882 |            -0.0599 |

## Regime Signal Coverage

- Total signal months: 98
- BIST100 below MA200 months: 22
- Below-MA200 rate: 22.45%
