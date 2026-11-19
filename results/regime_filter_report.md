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
| baseline              |             2.0288 |                         0.4244 |            -0.2002 |                     0.3188 |                 0.3291 |                  1 |
| defensive_mode        |             1.9404 |                         0.3360 |            -0.2051 |                     0.2088 |                 0.2234 |                  1 |
| reduced_exposure_mode |             1.7577 |                         0.1533 |            -0.1942 |                     0.2627 |                 0.0700 |                  1 |
| cash_mode             |             1.5441 |                        -0.0603 |            -0.2027 |                     0.1960 |                -0.2309 |                  1 |

## Best Out-Of-Sample Combinations

| policy                | base_model      |   base_portfolio_size | period        |   months |   bear_months |   avg_exposure |   total_return |   bist100_total_return |   excess_return_vs_bist100 |   max_drawdown |   bist100_max_drawdown |   win_rate |   robustness_score |
|:----------------------|:----------------|----------------------:|:--------------|---------:|--------------:|---------------:|---------------:|-----------------------:|---------------------------:|---------------:|-----------------------:|-----------:|-------------------:|
| baseline              | mixed_model     |                    15 | out_of_sample |       34 |             9 |         1.0000 |         0.5515 |                 0.3508 |                     0.2007 |        -0.1961 |                -0.2550 |     0.5882 |             0.1026 |
| baseline              | trend_following |                    15 | out_of_sample |       34 |             9 |         1.0000 |         0.4977 |                 0.3508 |                     0.1469 |        -0.1926 |                -0.2550 |     0.5882 |             0.0557 |
| baseline              | momentum_heavy  |                    15 | out_of_sample |       34 |             9 |         1.0000 |         0.4987 |                 0.3508 |                     0.1479 |        -0.1948 |                -0.2550 |     0.5882 |             0.0523 |
| baseline              | momentum_heavy  |                     3 | out_of_sample |       34 |             9 |         1.0000 |         0.4597 |                 0.3508 |                     0.1089 |        -0.1839 |                -0.2550 |     0.5588 |             0.0206 |
| reduced_exposure_mode | mixed_model     |                    15 | out_of_sample |       34 |             9 |         0.8676 |         0.4345 |                 0.3508 |                     0.0837 |        -0.1817 |                -0.2550 |     0.5882 |             0.0145 |
| reduced_exposure_mode | momentum_heavy  |                     3 | out_of_sample |       34 |             9 |         0.8676 |         0.4086 |                 0.3508 |                     0.0578 |        -0.1660 |                -0.2550 |     0.5588 |             0.0051 |
| baseline              | trend_following |                     3 | out_of_sample |       34 |             9 |         1.0000 |         0.3946 |                 0.3508 |                     0.0438 |        -0.1767 |                -0.2550 |     0.5882 |            -0.0155 |
| baseline              | low_volatility  |                    15 | out_of_sample |       34 |             9 |         1.0000 |         0.4873 |                 0.3508 |                     0.1364 |        -0.2209 |                -0.2550 |     0.5588 |            -0.0260 |
| reduced_exposure_mode | momentum_heavy  |                    15 | out_of_sample |       34 |             9 |         0.8676 |         0.3962 |                 0.3508 |                     0.0454 |        -0.1851 |                -0.2550 |     0.5882 |            -0.0308 |
| reduced_exposure_mode | low_volatility  |                    15 | out_of_sample |       34 |             9 |         0.8676 |         0.3827 |                 0.3508 |                     0.0319 |        -0.1737 |                -0.2550 |     0.5588 |            -0.0361 |

## Regime Signal Coverage

- Total signal months: 98
- BIST100 below MA200 months: 22
- Below-MA200 rate: 22.45%
