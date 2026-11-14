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
| baseline              |             2.0418 |                         0.4230 |            -0.2002 |                     0.3578 |                 0.3277 |                  1 |
| defensive_mode        |             1.9529 |                         0.3342 |            -0.2051 |                     0.2465 |                 0.2217 |                  1 |
| reduced_exposure_mode |             1.7640 |                         0.1453 |            -0.1942 |                     0.2819 |                 0.0621 |                  1 |
| cash_mode             |             1.5441 |                        -0.0747 |            -0.2027 |                     0.1960 |                -0.2453 |                  1 |

## Best Out-Of-Sample Combinations

| policy                | base_model      |   base_portfolio_size | period        |   months |   bear_months |   avg_exposure |   total_return |   bist100_total_return |   excess_return_vs_bist100 |   max_drawdown |   bist100_max_drawdown |   win_rate |   robustness_score |
|:----------------------|:----------------|----------------------:|:--------------|---------:|--------------:|---------------:|---------------:|-----------------------:|---------------------------:|---------------:|-----------------------:|-----------:|-------------------:|
| baseline              | mixed_model     |                    15 | out_of_sample |       34 |             9 |         1.0000 |         0.5918 |                 0.3938 |                     0.1980 |        -0.1961 |                -0.2550 |     0.5882 |             0.0999 |
| baseline              | trend_following |                    15 | out_of_sample |       34 |             9 |         1.0000 |         0.5418 |                 0.3938 |                     0.1480 |        -0.1926 |                -0.2550 |     0.5882 |             0.0568 |
| baseline              | momentum_heavy  |                    15 | out_of_sample |       34 |             9 |         1.0000 |         0.5428 |                 0.3938 |                     0.1490 |        -0.1948 |                -0.2550 |     0.5882 |             0.0534 |
| baseline              | momentum_heavy  |                     3 | out_of_sample |       34 |             9 |         1.0000 |         0.4960 |                 0.3938 |                     0.1022 |        -0.1839 |                -0.2550 |     0.5588 |             0.0139 |
| reduced_exposure_mode | mixed_model     |                    15 | out_of_sample |       34 |             9 |         0.8676 |         0.4540 |                 0.3938 |                     0.0602 |        -0.1817 |                -0.2550 |     0.5882 |            -0.0090 |
| reduced_exposure_mode | momentum_heavy  |                     3 | out_of_sample |       34 |             9 |         0.8676 |         0.4263 |                 0.3938 |                     0.0325 |        -0.1660 |                -0.2550 |     0.5588 |            -0.0202 |
| baseline              | trend_following |                     3 | out_of_sample |       34 |             9 |         1.0000 |         0.4293 |                 0.3938 |                     0.0355 |        -0.1767 |                -0.2550 |     0.5882 |            -0.0238 |
| baseline              | low_volatility  |                    15 | out_of_sample |       34 |             9 |         1.0000 |         0.5226 |                 0.3938 |                     0.1288 |        -0.2209 |                -0.2550 |     0.5588 |            -0.0336 |
| reduced_exposure_mode | momentum_heavy  |                    15 | out_of_sample |       34 |             9 |         0.8676 |         0.4175 |                 0.3938 |                     0.0236 |        -0.1851 |                -0.2550 |     0.5882 |            -0.0525 |
| reduced_exposure_mode | trend_following |                    15 | out_of_sample |       34 |             9 |         0.8676 |         0.4166 |                 0.3938 |                     0.0227 |        -0.1882 |                -0.2550 |     0.5882 |            -0.0595 |

## Regime Signal Coverage

- Total signal months: 98
- BIST100 below MA200 months: 22
- Below-MA200 rate: 22.45%
