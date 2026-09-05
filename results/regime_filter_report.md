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
| baseline              |             2.0803 |                         0.3765 |            -0.1902 |                     0.4733 |                 0.3023 |                  1 |
| defensive_mode        |             2.0065 |                         0.3027 |            -0.1901 |                     0.4073 |                 0.2211 |                  1 |
| reduced_exposure_mode |             1.7926 |                         0.0888 |            -0.1929 |                     0.3676 |                 0.0093 |                  1 |
| cash_mode             |             1.5657 |                        -0.1381 |            -0.2024 |                     0.2610 |                -0.3036 |                  1 |

## Best Out-Of-Sample Combinations

| policy                | base_model      |   base_portfolio_size | period        |   months |   bear_months |   avg_exposure |   total_return |   bist100_total_return |   excess_return_vs_bist100 |   max_drawdown |   bist100_max_drawdown |   win_rate |   robustness_score |
|:----------------------|:----------------|----------------------:|:--------------|---------:|--------------:|---------------:|---------------:|-----------------------:|---------------------------:|---------------:|-----------------------:|-----------:|-------------------:|
| baseline              | momentum_heavy  |                     3 | out_of_sample |       32 |             7 |         1.0000 |         0.7031 |                 0.6492 |                     0.0539 |        -0.1660 |                -0.1675 |     0.5938 |             0.0187 |
| baseline              | mixed_model     |                    15 | out_of_sample |       32 |             7 |         1.0000 |         0.6295 |                 0.6492 |                    -0.0197 |        -0.1644 |                -0.1675 |     0.5938 |            -0.0517 |
| baseline              | momentum_heavy  |                    15 | out_of_sample |       32 |             7 |         1.0000 |         0.6312 |                 0.6492 |                    -0.0179 |        -0.1680 |                -0.1675 |     0.5938 |            -0.0571 |
| baseline              | low_volatility  |                    15 | out_of_sample |       32 |             7 |         1.0000 |         0.5965 |                 0.6492 |                    -0.0526 |        -0.1563 |                -0.1675 |     0.5625 |            -0.0841 |
| baseline              | trend_following |                    15 | out_of_sample |       32 |             7 |         1.0000 |         0.6022 |                 0.6492 |                    -0.0470 |        -0.1747 |                -0.1675 |     0.5938 |            -0.0994 |
| defensive_mode        | momentum_heavy  |                     3 | out_of_sample |       32 |             7 |         1.0000 |         0.5888 |                 0.6492 |                    -0.0603 |        -0.1660 |                -0.1675 |     0.5625 |            -0.1112 |
| reduced_exposure_mode | momentum_heavy  |                     3 | out_of_sample |       32 |             7 |         0.8906 |         0.5625 |                 0.6492 |                    -0.0867 |        -0.1660 |                -0.1675 |     0.5938 |            -0.1219 |
| baseline              | trend_following |                     3 | out_of_sample |       32 |             7 |         1.0000 |         0.5564 |                 0.6492 |                    -0.0927 |        -0.1767 |                -0.1675 |     0.5938 |            -0.1493 |
| baseline              | volume_heavy    |                    15 | out_of_sample |       32 |             7 |         1.0000 |         0.5509 |                 0.6492 |                    -0.0982 |        -0.1746 |                -0.1675 |     0.5938 |            -0.1505 |
| defensive_mode        | mixed_model     |                    15 | out_of_sample |       32 |             7 |         1.0000 |         0.5267 |                 0.6492 |                    -0.1225 |        -0.1757 |                -0.1675 |     0.5312 |            -0.2082 |

## Regime Signal Coverage

- Total signal months: 96
- BIST100 below MA200 months: 19
- Below-MA200 rate: 19.79%
