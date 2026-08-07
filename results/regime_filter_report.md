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
| baseline              |             2.0597 |                         0.3643 |            -0.1902 |                     0.4116 |                 0.2919 |                  1 |
| defensive_mode        |             1.9871 |                         0.2916 |            -0.1901 |                     0.3490 |                 0.2118 |                  1 |
| reduced_exposure_mode |             1.7736 |                         0.0782 |            -0.1929 |                     0.3106 |                 0.0005 |                  1 |
| cash_mode             |             1.5483 |                        -0.1471 |            -0.2024 |                     0.2088 |                -0.3116 |                  1 |

## Best Out-Of-Sample Combinations

| policy                | base_model      |   base_portfolio_size | period        |   months |   bear_months |   avg_exposure |   total_return |   bist100_total_return |   excess_return_vs_bist100 |   max_drawdown |   bist100_max_drawdown |   win_rate |   robustness_score |
|:----------------------|:----------------|----------------------:|:--------------|---------:|--------------:|---------------:|---------------:|-----------------------:|---------------------------:|---------------:|-----------------------:|-----------:|-------------------:|
| baseline              | mixed_model     |                    15 | out_of_sample |       31 |             7 |         1.0000 |         0.6215 |                 0.6240 |                    -0.0025 |        -0.1644 |                -0.1675 |     0.6129 |            -0.0249 |
| baseline              | momentum_heavy  |                    15 | out_of_sample |       31 |             7 |         1.0000 |         0.6205 |                 0.6240 |                    -0.0035 |        -0.1680 |                -0.1675 |     0.6129 |            -0.0330 |
| baseline              | low_volatility  |                    15 | out_of_sample |       31 |             7 |         1.0000 |         0.6061 |                 0.6240 |                    -0.0180 |        -0.1563 |                -0.1675 |     0.5806 |            -0.0403 |
| baseline              | trend_following |                    15 | out_of_sample |       31 |             7 |         1.0000 |         0.5944 |                 0.6240 |                    -0.0296 |        -0.1747 |                -0.1675 |     0.6129 |            -0.0725 |
| baseline              | momentum_heavy  |                     3 | out_of_sample |       31 |             7 |         1.0000 |         0.5447 |                 0.6240 |                    -0.0794 |        -0.1660 |                -0.1675 |     0.5806 |            -0.1211 |
| baseline              | volume_heavy    |                    15 | out_of_sample |       31 |             7 |         1.0000 |         0.5452 |                 0.6240 |                    -0.0788 |        -0.1746 |                -0.1675 |     0.6129 |            -0.1214 |
| defensive_mode        | mixed_model     |                    15 | out_of_sample |       31 |             7 |         1.0000 |         0.5193 |                 0.6240 |                    -0.1047 |        -0.1757 |                -0.1675 |     0.5484 |            -0.1819 |
| defensive_mode        | low_volatility  |                    15 | out_of_sample |       31 |             7 |         1.0000 |         0.4979 |                 0.6240 |                    -0.1262 |        -0.1661 |                -0.1675 |     0.5484 |            -0.1841 |
| reduced_exposure_mode | mixed_model     |                    15 | out_of_sample |       31 |             7 |         0.8871 |         0.4904 |                 0.6240 |                    -0.1336 |        -0.1817 |                -0.1675 |     0.6129 |            -0.1905 |
| defensive_mode        | momentum_heavy  |                    15 | out_of_sample |       31 |             7 |         1.0000 |         0.5146 |                 0.6240 |                    -0.1094 |        -0.1792 |                -0.1675 |     0.5484 |            -0.1936 |

## Regime Signal Coverage

- Total signal months: 95
- BIST100 below MA200 months: 19
- Below-MA200 rate: 20.00%
