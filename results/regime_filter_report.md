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
| baseline              |             2.0383 |                         0.4247 |            -0.2002 |                     0.3475 |                 0.3294 |                  1 |
| defensive_mode        |             1.9476 |                         0.3339 |            -0.2051 |                     0.2304 |                 0.2214 |                  1 |
| reduced_exposure_mode |             1.7623 |                         0.1487 |            -0.1942 |                     0.2768 |                 0.0655 |                  1 |
| cash_mode             |             1.5441 |                        -0.0695 |            -0.2027 |                     0.1960 |                -0.2402 |                  1 |

## Best Out-Of-Sample Combinations

| policy                | base_model      |   base_portfolio_size | period        |   months |   bear_months |   avg_exposure |   total_return |   bist100_total_return |   excess_return_vs_bist100 |   max_drawdown |   bist100_max_drawdown |   win_rate |   robustness_score |
|:----------------------|:----------------|----------------------:|:--------------|---------:|--------------:|---------------:|---------------:|-----------------------:|---------------------------:|---------------:|-----------------------:|-----------:|-------------------:|
| baseline              | mixed_model     |                    15 | out_of_sample |       34 |             9 |         1.0000 |         0.5811 |                 0.3785 |                     0.2026 |        -0.1961 |                -0.2550 |     0.5882 |             0.1045 |
| baseline              | trend_following |                    15 | out_of_sample |       34 |             9 |         1.0000 |         0.5392 |                 0.3785 |                     0.1607 |        -0.1926 |                -0.2550 |     0.5882 |             0.0695 |
| baseline              | momentum_heavy  |                    15 | out_of_sample |       34 |             9 |         1.0000 |         0.5402 |                 0.3785 |                     0.1617 |        -0.1948 |                -0.2550 |     0.5882 |             0.0662 |
| reduced_exposure_mode | mixed_model     |                    15 | out_of_sample |       34 |             9 |         0.8676 |         0.4488 |                 0.3785 |                     0.0703 |        -0.1817 |                -0.2550 |     0.5882 |             0.0011 |
| baseline              | momentum_heavy  |                     3 | out_of_sample |       34 |             9 |         1.0000 |         0.4638 |                 0.3785 |                     0.0853 |        -0.1839 |                -0.2550 |     0.5588 |            -0.0030 |
| reduced_exposure_mode | momentum_heavy  |                     3 | out_of_sample |       34 |             9 |         0.8676 |         0.4106 |                 0.3785 |                     0.0321 |        -0.1660 |                -0.2550 |     0.5588 |            -0.0205 |
| baseline              | low_volatility  |                    15 | out_of_sample |       34 |             9 |         1.0000 |         0.5140 |                 0.3785 |                     0.1355 |        -0.2209 |                -0.2550 |     0.5588 |            -0.0269 |
| reduced_exposure_mode | momentum_heavy  |                    15 | out_of_sample |       34 |             9 |         0.8676 |         0.4162 |                 0.3785 |                     0.0377 |        -0.1851 |                -0.2550 |     0.5882 |            -0.0384 |
| baseline              | trend_following |                     3 | out_of_sample |       34 |             9 |         1.0000 |         0.3986 |                 0.3785 |                     0.0201 |        -0.1767 |                -0.2550 |     0.5882 |            -0.0392 |
| reduced_exposure_mode | trend_following |                    15 | out_of_sample |       34 |             9 |         0.8676 |         0.4153 |                 0.3785 |                     0.0368 |        -0.1882 |                -0.2550 |     0.5882 |            -0.0454 |

## Regime Signal Coverage

- Total signal months: 98
- BIST100 below MA200 months: 22
- Below-MA200 rate: 22.45%
