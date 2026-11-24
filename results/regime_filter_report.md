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
| baseline              |             2.0163 |                         0.4266 |            -0.2005 |                     0.2814 |                 0.3293 |                  1 |
| defensive_mode        |             1.9238 |                         0.3341 |            -0.2066 |                     0.1592 |                 0.2138 |                  1 |
| reduced_exposure_mode |             1.7515 |                         0.1617 |            -0.1942 |                     0.2443 |                 0.0770 |                  1 |
| cash_mode             |             1.5441 |                        -0.0457 |            -0.2027 |                     0.1960 |                -0.2163 |                  1 |

## Best Out-Of-Sample Combinations

| policy                | base_model      |   base_portfolio_size | period        |   months |   bear_months |   avg_exposure |   total_return |   bist100_total_return |   excess_return_vs_bist100 |   max_drawdown |   bist100_max_drawdown |   win_rate |   robustness_score |
|:----------------------|:----------------|----------------------:|:--------------|---------:|--------------:|---------------:|---------------:|-----------------------:|---------------------------:|---------------:|-----------------------:|-----------:|-------------------:|
| baseline              | mixed_model     |                    15 | out_of_sample |       34 |             9 |         1.0000 |         0.5168 |                 0.3069 |                     0.2098 |        -0.1961 |                -0.2550 |     0.5882 |             0.1118 |
| baseline              | trend_following |                    15 | out_of_sample |       34 |             9 |         1.0000 |         0.4606 |                 0.3069 |                     0.1537 |        -0.1926 |                -0.2550 |     0.5882 |             0.0625 |
| baseline              | momentum_heavy  |                    15 | out_of_sample |       34 |             9 |         1.0000 |         0.4615 |                 0.3069 |                     0.1546 |        -0.1948 |                -0.2550 |     0.5882 |             0.0591 |
| reduced_exposure_mode | mixed_model     |                    15 | out_of_sample |       34 |             9 |         0.8676 |         0.4177 |                 0.3069 |                     0.1108 |        -0.1817 |                -0.2550 |     0.5882 |             0.0416 |
| reduced_exposure_mode | momentum_heavy  |                     3 | out_of_sample |       34 |             9 |         0.8676 |         0.3836 |                 0.3069 |                     0.0767 |        -0.1660 |                -0.2550 |     0.5294 |             0.0093 |
| reduced_exposure_mode | momentum_heavy  |                    15 | out_of_sample |       34 |             9 |         0.8676 |         0.3782 |                 0.3069 |                     0.0713 |        -0.1851 |                -0.2550 |     0.5882 |            -0.0048 |
| reduced_exposure_mode | low_volatility  |                    15 | out_of_sample |       34 |             9 |         0.8676 |         0.3655 |                 0.3069 |                     0.0586 |        -0.1737 |                -0.2550 |     0.5588 |            -0.0094 |
| reduced_exposure_mode | trend_following |                    15 | out_of_sample |       34 |             9 |         0.8676 |         0.3774 |                 0.3069 |                     0.0705 |        -0.1882 |                -0.2550 |     0.5882 |            -0.0118 |
| baseline              | low_volatility  |                    15 | out_of_sample |       34 |             9 |         1.0000 |         0.4519 |                 0.3069 |                     0.1450 |        -0.2209 |                -0.2550 |     0.5588 |            -0.0174 |
| baseline              | momentum_heavy  |                     3 | out_of_sample |       34 |             9 |         1.0000 |         0.4084 |                 0.3069 |                     0.1015 |        -0.1950 |                -0.2550 |     0.5294 |            -0.0239 |

## Regime Signal Coverage

- Total signal months: 98
- BIST100 below MA200 months: 22
- Below-MA200 rate: 22.45%
