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
| baseline              |             2.1008 |                         0.4017 |            -0.1902 |                     0.5348 |                 0.3324 |                  1 |
| defensive_mode        |             2.0260 |                         0.3269 |            -0.1901 |                     0.4658 |                 0.2502 |                  1 |
| reduced_exposure_mode |             1.8116 |                         0.1125 |            -0.1929 |                     0.4246 |                 0.0379 |                  1 |
| cash_mode             |             1.5832 |                        -0.1160 |            -0.2024 |                     0.3133 |                -0.2765 |                  1 |

## Best Out-Of-Sample Combinations

| policy                | base_model      |   base_portfolio_size | period        |   months |   bear_months |   avg_exposure |   total_return |   bist100_total_return |   excess_return_vs_bist100 |   max_drawdown |   bist100_max_drawdown |   win_rate |   robustness_score |
|:----------------------|:----------------|----------------------:|:--------------|---------:|--------------:|---------------:|---------------:|-----------------------:|---------------------------:|---------------:|-----------------------:|-----------:|-------------------:|
| baseline              | momentum_heavy  |                     3 | out_of_sample |       32 |             7 |         1.0000 |         0.7861 |                 0.6350 |                     0.1511 |        -0.1660 |                -0.1675 |     0.6250 |             0.1315 |
| baseline              | mixed_model     |                    15 | out_of_sample |       32 |             7 |         1.0000 |         0.7169 |                 0.6350 |                     0.0819 |        -0.1644 |                -0.1675 |     0.6250 |             0.0655 |
| baseline              | momentum_heavy  |                    15 | out_of_sample |       32 |             7 |         1.0000 |         0.7162 |                 0.6350 |                     0.0812 |        -0.1680 |                -0.1675 |     0.6250 |             0.0577 |
| baseline              | low_volatility  |                    15 | out_of_sample |       32 |             7 |         1.0000 |         0.6700 |                 0.6350 |                     0.0350 |        -0.1563 |                -0.1675 |     0.5938 |             0.0192 |
| baseline              | trend_following |                    15 | out_of_sample |       32 |             7 |         1.0000 |         0.6882 |                 0.6350 |                     0.0532 |        -0.1747 |                -0.1675 |     0.6250 |             0.0164 |
| defensive_mode        | momentum_heavy  |                     3 | out_of_sample |       32 |             7 |         1.0000 |         0.6663 |                 0.6350 |                     0.0313 |        -0.1660 |                -0.1675 |     0.5938 |            -0.0039 |
| reduced_exposure_mode | momentum_heavy  |                     3 | out_of_sample |       32 |             7 |         0.8906 |         0.6387 |                 0.6350 |                     0.0036 |        -0.1660 |                -0.1675 |     0.6250 |            -0.0159 |
| baseline              | volume_heavy    |                    15 | out_of_sample |       32 |             7 |         1.0000 |         0.6342 |                 0.6350 |                    -0.0008 |        -0.1746 |                -0.1675 |     0.6250 |            -0.0375 |
| baseline              | trend_following |                     3 | out_of_sample |       32 |             7 |         1.0000 |         0.6323 |                 0.6350 |                    -0.0027 |        -0.1767 |                -0.1675 |     0.6250 |            -0.0436 |
| defensive_mode        | mixed_model     |                    15 | out_of_sample |       32 |             7 |         1.0000 |         0.6087 |                 0.6350 |                    -0.0264 |        -0.1757 |                -0.1675 |     0.5625 |            -0.0965 |

## Regime Signal Coverage

- Total signal months: 96
- BIST100 below MA200 months: 19
- Below-MA200 rate: 19.79%
