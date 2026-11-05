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
| baseline              |             2.0263 |                         0.4219 |            -0.2002 |                     0.3113 |                 0.3266 |                  1 |
| defensive_mode        |             1.9437 |                         0.3393 |            -0.2051 |                     0.2189 |                 0.2268 |                  1 |
| reduced_exposure_mode |             1.7564 |                         0.1520 |            -0.1942 |                     0.2590 |                 0.0688 |                  1 |
| cash_mode             |             1.5441 |                        -0.0603 |            -0.2027 |                     0.1960 |                -0.2310 |                  1 |

## Best Out-Of-Sample Combinations

| policy                | base_model      |   base_portfolio_size | period        |   months |   bear_months |   avg_exposure |   total_return |   bist100_total_return |   excess_return_vs_bist100 |   max_drawdown |   bist100_max_drawdown |   win_rate |   robustness_score |
|:----------------------|:----------------|----------------------:|:--------------|---------:|--------------:|---------------:|---------------:|-----------------------:|---------------------------:|---------------:|-----------------------:|-----------:|-------------------:|
| baseline              | mixed_model     |                    15 | out_of_sample |       34 |             9 |         1.0000 |         0.5226 |                 0.3509 |                     0.1717 |        -0.1961 |                -0.2550 |     0.5882 |             0.0737 |
| baseline              | trend_following |                    15 | out_of_sample |       34 |             9 |         1.0000 |         0.4917 |                 0.3509 |                     0.1408 |        -0.1926 |                -0.2550 |     0.5882 |             0.0496 |
| baseline              | momentum_heavy  |                    15 | out_of_sample |       34 |             9 |         1.0000 |         0.4926 |                 0.3509 |                     0.1417 |        -0.1948 |                -0.2550 |     0.5882 |             0.0462 |
| baseline              | momentum_heavy  |                     3 | out_of_sample |       34 |             9 |         1.0000 |         0.4610 |                 0.3509 |                     0.1101 |        -0.1839 |                -0.2550 |     0.5588 |             0.0218 |
| reduced_exposure_mode | momentum_heavy  |                     3 | out_of_sample |       34 |             9 |         0.8676 |         0.4092 |                 0.3509 |                     0.0583 |        -0.1660 |                -0.2550 |     0.5588 |             0.0057 |
| reduced_exposure_mode | mixed_model     |                    15 | out_of_sample |       34 |             9 |         0.8676 |         0.4206 |                 0.3509 |                     0.0697 |        -0.1817 |                -0.2550 |     0.5882 |             0.0005 |
| baseline              | trend_following |                     3 | out_of_sample |       34 |             9 |         1.0000 |         0.3958 |                 0.3509 |                     0.0449 |        -0.1767 |                -0.2550 |     0.5882 |            -0.0144 |
| reduced_exposure_mode | momentum_heavy  |                    15 | out_of_sample |       34 |             9 |         0.8676 |         0.3932 |                 0.3509 |                     0.0423 |        -0.1851 |                -0.2550 |     0.5882 |            -0.0338 |
| reduced_exposure_mode | trend_following |                    15 | out_of_sample |       34 |             9 |         0.8676 |         0.3924 |                 0.3509 |                     0.0415 |        -0.1882 |                -0.2550 |     0.5882 |            -0.0407 |
| reduced_exposure_mode | low_volatility  |                    15 | out_of_sample |       34 |             9 |         0.8676 |         0.3650 |                 0.3509 |                     0.0141 |        -0.1737 |                -0.2550 |     0.5588 |            -0.0540 |

## Regime Signal Coverage

- Total signal months: 98
- BIST100 below MA200 months: 22
- Below-MA200 rate: 22.45%
