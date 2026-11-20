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
| baseline              |             2.0250 |                         0.4237 |            -0.2002 |                     0.3075 |                 0.3284 |                  1 |
| defensive_mode        |             1.9341 |                         0.3327 |            -0.2051 |                     0.1900 |                 0.2202 |                  1 |
| reduced_exposure_mode |             1.7558 |                         0.1544 |            -0.1942 |                     0.2571 |                 0.0712 |                  1 |
| cash_mode             |             1.5441 |                        -0.0573 |            -0.2027 |                     0.1960 |                -0.2279 |                  1 |

## Best Out-Of-Sample Combinations

| policy                | base_model      |   base_portfolio_size | period        |   months |   bear_months |   avg_exposure |   total_return |   bist100_total_return |   excess_return_vs_bist100 |   max_drawdown |   bist100_max_drawdown |   win_rate |   robustness_score |
|:----------------------|:----------------|----------------------:|:--------------|---------:|--------------:|---------------:|---------------:|-----------------------:|---------------------------:|---------------:|-----------------------:|-----------:|-------------------:|
| baseline              | mixed_model     |                    15 | out_of_sample |       34 |             9 |         1.0000 |         0.5482 |                 0.3417 |                     0.2065 |        -0.1961 |                -0.2550 |     0.5882 |             0.1085 |
| baseline              | trend_following |                    15 | out_of_sample |       34 |             9 |         1.0000 |         0.4925 |                 0.3417 |                     0.1508 |        -0.1926 |                -0.2550 |     0.5882 |             0.0596 |
| baseline              | momentum_heavy  |                    15 | out_of_sample |       34 |             9 |         1.0000 |         0.4934 |                 0.3417 |                     0.1517 |        -0.1948 |                -0.2550 |     0.5882 |             0.0562 |
| reduced_exposure_mode | mixed_model     |                    15 | out_of_sample |       34 |             9 |         0.8676 |         0.4329 |                 0.3417 |                     0.0912 |        -0.1817 |                -0.2550 |     0.5882 |             0.0220 |
| baseline              | momentum_heavy  |                     3 | out_of_sample |       34 |             9 |         1.0000 |         0.4385 |                 0.3417 |                     0.0968 |        -0.1839 |                -0.2550 |     0.5588 |             0.0085 |
| reduced_exposure_mode | momentum_heavy  |                     3 | out_of_sample |       34 |             9 |         0.8676 |         0.3983 |                 0.3417 |                     0.0566 |        -0.1660 |                -0.2550 |     0.5588 |             0.0039 |
| baseline              | low_volatility  |                    15 | out_of_sample |       34 |             9 |         1.0000 |         0.4830 |                 0.3417 |                     0.1413 |        -0.2209 |                -0.2550 |     0.5588 |            -0.0211 |
| reduced_exposure_mode | momentum_heavy  |                    15 | out_of_sample |       34 |             9 |         0.8676 |         0.3936 |                 0.3417 |                     0.0519 |        -0.1851 |                -0.2550 |     0.5882 |            -0.0242 |
| baseline              | trend_following |                     3 | out_of_sample |       34 |             9 |         1.0000 |         0.3744 |                 0.3417 |                     0.0327 |        -0.1767 |                -0.2550 |     0.5882 |            -0.0266 |
| reduced_exposure_mode | low_volatility  |                    15 | out_of_sample |       34 |             9 |         0.8676 |         0.3807 |                 0.3417 |                     0.0390 |        -0.1737 |                -0.2550 |     0.5588 |            -0.0291 |

## Regime Signal Coverage

- Total signal months: 98
- BIST100 below MA200 months: 22
- Below-MA200 rate: 22.45%
