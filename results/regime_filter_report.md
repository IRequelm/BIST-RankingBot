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
| baseline              |             2.0787 |                         0.3780 |            -0.1902 |                     0.4685 |                 0.3036 |                  1 |
| defensive_mode        |             2.0050 |                         0.3043 |            -0.1901 |                     0.4028 |                 0.2225 |                  1 |
| reduced_exposure_mode |             1.7911 |                         0.0904 |            -0.1929 |                     0.3632 |                 0.0106 |                  1 |
| cash_mode             |             1.5644 |                        -0.1363 |            -0.2024 |                     0.2569 |                -0.3021 |                  1 |

## Best Out-Of-Sample Combinations

| policy                | base_model      |   base_portfolio_size | period        |   months |   bear_months |   avg_exposure |   total_return |   bist100_total_return |   excess_return_vs_bist100 |   max_drawdown |   bist100_max_drawdown |   win_rate |   robustness_score |
|:----------------------|:----------------|----------------------:|:--------------|---------:|--------------:|---------------:|---------------:|-----------------------:|---------------------------:|---------------:|-----------------------:|-----------:|-------------------:|
| baseline              | momentum_heavy  |                     3 | out_of_sample |       32 |             7 |         1.0000 |         0.6867 |                 0.6398 |                     0.0470 |        -0.1660 |                -0.1675 |     0.5938 |             0.0118 |
| baseline              | mixed_model     |                    15 | out_of_sample |       32 |             7 |         1.0000 |         0.6310 |                 0.6398 |                    -0.0088 |        -0.1644 |                -0.1675 |     0.5938 |            -0.0408 |
| baseline              | momentum_heavy  |                    15 | out_of_sample |       32 |             7 |         1.0000 |         0.6325 |                 0.6398 |                    -0.0073 |        -0.1680 |                -0.1675 |     0.5938 |            -0.0464 |
| baseline              | low_volatility  |                    15 | out_of_sample |       32 |             7 |         1.0000 |         0.6010 |                 0.6398 |                    -0.0387 |        -0.1563 |                -0.1675 |     0.5625 |            -0.0702 |
| baseline              | trend_following |                    15 | out_of_sample |       32 |             7 |         1.0000 |         0.6037 |                 0.6398 |                    -0.0361 |        -0.1747 |                -0.1675 |     0.5938 |            -0.0885 |
| defensive_mode        | momentum_heavy  |                     3 | out_of_sample |       32 |             7 |         1.0000 |         0.5736 |                 0.6398 |                    -0.0662 |        -0.1660 |                -0.1675 |     0.5625 |            -0.1170 |
| reduced_exposure_mode | momentum_heavy  |                     3 | out_of_sample |       32 |             7 |         0.8906 |         0.5475 |                 0.6398 |                    -0.0923 |        -0.1660 |                -0.1675 |     0.5938 |            -0.1275 |
| baseline              | volume_heavy    |                    15 | out_of_sample |       32 |             7 |         1.0000 |         0.5524 |                 0.6398 |                    -0.0874 |        -0.1746 |                -0.1675 |     0.5938 |            -0.1396 |
| baseline              | trend_following |                     3 | out_of_sample |       32 |             7 |         1.0000 |         0.5415 |                 0.6398 |                    -0.0983 |        -0.1767 |                -0.1675 |     0.5938 |            -0.1548 |
| defensive_mode        | mixed_model     |                    15 | out_of_sample |       32 |             7 |         1.0000 |         0.5281 |                 0.6398 |                    -0.1117 |        -0.1757 |                -0.1675 |     0.5312 |            -0.1974 |

## Regime Signal Coverage

- Total signal months: 96
- BIST100 below MA200 months: 19
- Below-MA200 rate: 19.79%
