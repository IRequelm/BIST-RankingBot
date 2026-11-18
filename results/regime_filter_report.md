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
| baseline              |             2.0348 |                         0.4232 |            -0.2002 |                     0.3368 |                 0.3279 |                  1 |
| defensive_mode        |             1.9474 |                         0.3358 |            -0.2051 |                     0.2299 |                 0.2232 |                  1 |
| reduced_exposure_mode |             1.7606 |                         0.1490 |            -0.1942 |                     0.2716 |                 0.0658 |                  1 |
| cash_mode             |             1.5441 |                        -0.0675 |            -0.2027 |                     0.1960 |                -0.2381 |                  1 |

## Best Out-Of-Sample Combinations

| policy                | base_model      |   base_portfolio_size | period        |   months |   bear_months |   avg_exposure |   total_return |   bist100_total_return |   excess_return_vs_bist100 |   max_drawdown |   bist100_max_drawdown |   win_rate |   robustness_score |
|:----------------------|:----------------|----------------------:|:--------------|---------:|--------------:|---------------:|---------------:|-----------------------:|---------------------------:|---------------:|-----------------------:|-----------:|-------------------:|
| baseline              | mixed_model     |                    15 | out_of_sample |       34 |             9 |         1.0000 |         0.5766 |                 0.3724 |                     0.2042 |        -0.1961 |                -0.2550 |     0.5882 |             0.1061 |
| baseline              | trend_following |                    15 | out_of_sample |       34 |             9 |         1.0000 |         0.5214 |                 0.3724 |                     0.1490 |        -0.1926 |                -0.2550 |     0.5882 |             0.0578 |
| baseline              | momentum_heavy  |                    15 | out_of_sample |       34 |             9 |         1.0000 |         0.5224 |                 0.3724 |                     0.1499 |        -0.1948 |                -0.2550 |     0.5882 |             0.0544 |
| baseline              | momentum_heavy  |                     3 | out_of_sample |       34 |             9 |         1.0000 |         0.4677 |                 0.3724 |                     0.0952 |        -0.1839 |                -0.2550 |     0.5588 |             0.0069 |
| reduced_exposure_mode | mixed_model     |                    15 | out_of_sample |       34 |             9 |         0.8676 |         0.4466 |                 0.3724 |                     0.0742 |        -0.1817 |                -0.2550 |     0.5882 |             0.0050 |
| reduced_exposure_mode | momentum_heavy  |                     3 | out_of_sample |       34 |             9 |         0.8676 |         0.4125 |                 0.3724 |                     0.0401 |        -0.1660 |                -0.2550 |     0.5588 |            -0.0126 |
| baseline              | low_volatility  |                    15 | out_of_sample |       34 |             9 |         1.0000 |         0.5083 |                 0.3724 |                     0.1359 |        -0.2209 |                -0.2550 |     0.5588 |            -0.0265 |
| baseline              | trend_following |                     3 | out_of_sample |       34 |             9 |         1.0000 |         0.4022 |                 0.3724 |                     0.0298 |        -0.1767 |                -0.2550 |     0.5882 |            -0.0295 |
| reduced_exposure_mode | momentum_heavy  |                    15 | out_of_sample |       34 |             9 |         0.8676 |         0.4076 |                 0.3724 |                     0.0352 |        -0.1851 |                -0.2550 |     0.5882 |            -0.0410 |
| reduced_exposure_mode | low_volatility  |                    15 | out_of_sample |       34 |             9 |         0.8676 |         0.3930 |                 0.3724 |                     0.0205 |        -0.1737 |                -0.2550 |     0.5588 |            -0.0475 |

## Regime Signal Coverage

- Total signal months: 98
- BIST100 below MA200 months: 22
- Below-MA200 rate: 22.45%
