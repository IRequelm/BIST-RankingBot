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
| baseline              |             2.0393 |                         0.4218 |            -0.2002 |                     0.3503 |                 0.3265 |                  1 |
| defensive_mode        |             1.9476 |                         0.3301 |            -0.2051 |                     0.2304 |                 0.2175 |                  1 |
| reduced_exposure_mode |             1.7628 |                         0.1453 |            -0.1942 |                     0.2782 |                 0.0621 |                  1 |
| cash_mode             |             1.5441 |                        -0.0734 |            -0.2027 |                     0.1960 |                -0.2440 |                  1 |

## Best Out-Of-Sample Combinations

| policy                | base_model      |   base_portfolio_size | period        |   months |   bear_months |   avg_exposure |   total_return |   bist100_total_return |   excess_return_vs_bist100 |   max_drawdown |   bist100_max_drawdown |   win_rate |   robustness_score |
|:----------------------|:----------------|----------------------:|:--------------|---------:|--------------:|---------------:|---------------:|-----------------------:|---------------------------:|---------------:|-----------------------:|-----------:|-------------------:|
| baseline              | mixed_model     |                    15 | out_of_sample |       34 |             9 |         1.0000 |         0.5795 |                 0.3901 |                     0.1894 |        -0.1961 |                -0.2550 |     0.5882 |             0.0913 |
| baseline              | trend_following |                    15 | out_of_sample |       34 |             9 |         1.0000 |         0.5302 |                 0.3901 |                     0.1401 |        -0.1926 |                -0.2550 |     0.5882 |             0.0489 |
| baseline              | momentum_heavy  |                    15 | out_of_sample |       34 |             9 |         1.0000 |         0.5312 |                 0.3901 |                     0.1411 |        -0.1948 |                -0.2550 |     0.5882 |             0.0455 |
| baseline              | momentum_heavy  |                     3 | out_of_sample |       34 |             9 |         1.0000 |         0.4897 |                 0.3901 |                     0.0996 |        -0.1839 |                -0.2550 |     0.5588 |             0.0113 |
| reduced_exposure_mode | mixed_model     |                    15 | out_of_sample |       34 |             9 |         0.8676 |         0.4480 |                 0.3901 |                     0.0579 |        -0.1817 |                -0.2550 |     0.5882 |            -0.0113 |
| reduced_exposure_mode | momentum_heavy  |                     3 | out_of_sample |       34 |             9 |         0.8676 |         0.4233 |                 0.3901 |                     0.0332 |        -0.1660 |                -0.2550 |     0.5588 |            -0.0195 |
| baseline              | trend_following |                     3 | out_of_sample |       34 |             9 |         1.0000 |         0.4233 |                 0.3901 |                     0.0332 |        -0.1767 |                -0.2550 |     0.5882 |            -0.0261 |
| baseline              | low_volatility  |                    15 | out_of_sample |       34 |             9 |         1.0000 |         0.5105 |                 0.3901 |                     0.1204 |        -0.2209 |                -0.2550 |     0.5588 |            -0.0420 |
| reduced_exposure_mode | momentum_heavy  |                    15 | out_of_sample |       34 |             9 |         0.8676 |         0.4118 |                 0.3901 |                     0.0217 |        -0.1851 |                -0.2550 |     0.5882 |            -0.0544 |
| reduced_exposure_mode | trend_following |                    15 | out_of_sample |       34 |             9 |         0.8676 |         0.4110 |                 0.3901 |                     0.0209 |        -0.1882 |                -0.2550 |     0.5882 |            -0.0613 |

## Regime Signal Coverage

- Total signal months: 98
- BIST100 below MA200 months: 22
- Below-MA200 rate: 22.45%
