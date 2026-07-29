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
| baseline              |             2.0614 |                         0.3702 |            -0.1902 |                     0.4165 |                 0.2963 |                  1 |
| defensive_mode        |             1.9887 |                         0.2976 |            -0.1901 |                     0.3537 |                 0.2159 |                  1 |
| reduced_exposure_mode |             1.7752 |                         0.0840 |            -0.1929 |                     0.3152 |                 0.0047 |                  1 |
| cash_mode             |             1.5497 |                        -0.1414 |            -0.2024 |                     0.2130 |                -0.3084 |                  1 |

## Best Out-Of-Sample Combinations

| policy                | base_model      |   base_portfolio_size | period        |   months |   bear_months |   avg_exposure |   total_return |   bist100_total_return |   excess_return_vs_bist100 |   max_drawdown |   bist100_max_drawdown |   win_rate |   robustness_score |
|:----------------------|:----------------|----------------------:|:--------------|---------:|--------------:|---------------:|---------------:|-----------------------:|---------------------------:|---------------:|-----------------------:|-----------:|-------------------:|
| baseline              | momentum_heavy  |                    15 | out_of_sample |       30 |             7 |         1.0000 |         0.6239 |                 0.6110 |                     0.0129 |        -0.1680 |                -0.1675 |     0.6000 |            -0.0231 |
| baseline              | mixed_model     |                    15 | out_of_sample |       30 |             7 |         1.0000 |         0.6165 |                 0.6110 |                     0.0055 |        -0.1644 |                -0.1675 |     0.6000 |            -0.0234 |
| baseline              | low_volatility  |                    15 | out_of_sample |       30 |             7 |         1.0000 |         0.6000 |                 0.6110 |                    -0.0110 |        -0.1563 |                -0.1675 |     0.5667 |            -0.0403 |
| baseline              | trend_following |                    15 | out_of_sample |       30 |             7 |         1.0000 |         0.5977 |                 0.6110 |                    -0.0133 |        -0.1747 |                -0.1675 |     0.6000 |            -0.0626 |
| baseline              | momentum_heavy  |                     3 | out_of_sample |       30 |             7 |         1.0000 |         0.5664 |                 0.6110 |                    -0.0446 |        -0.1660 |                -0.1675 |     0.6000 |            -0.0767 |
| baseline              | volume_heavy    |                    15 | out_of_sample |       30 |             7 |         1.0000 |         0.5386 |                 0.6110 |                    -0.0724 |        -0.1746 |                -0.1675 |     0.6000 |            -0.1215 |
| defensive_mode        | mixed_model     |                    15 | out_of_sample |       30 |             7 |         1.0000 |         0.5146 |                 0.6110 |                    -0.0964 |        -0.1757 |                -0.1675 |     0.5333 |            -0.1811 |
| defensive_mode        | low_volatility  |                    15 | out_of_sample |       30 |             7 |         1.0000 |         0.4922 |                 0.6110 |                    -0.1188 |        -0.1661 |                -0.1675 |     0.5333 |            -0.1842 |
| defensive_mode        | momentum_heavy  |                    15 | out_of_sample |       30 |             7 |         1.0000 |         0.5177 |                 0.6110 |                    -0.0933 |        -0.1792 |                -0.1675 |     0.5333 |            -0.1850 |
| reduced_exposure_mode | mixed_model     |                    15 | out_of_sample |       30 |             7 |         0.8833 |         0.4858 |                 0.6110 |                    -0.1252 |        -0.1817 |                -0.1675 |     0.6000 |            -0.1885 |

## Regime Signal Coverage

- Total signal months: 94
- BIST100 below MA200 months: 19
- Below-MA200 rate: 20.21%
