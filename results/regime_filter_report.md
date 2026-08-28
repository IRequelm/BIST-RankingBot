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
| baseline              |             2.0852 |                         0.3593 |            -0.1902 |                     0.4880 |                 0.2878 |                  1 |
| defensive_mode        |             2.0113 |                         0.2853 |            -0.1901 |                     0.4215 |                 0.2062 |                  1 |
| reduced_exposure_mode |             1.7972 |                         0.0713 |            -0.1929 |                     0.3813 |                -0.0056 |                  1 |
| cash_mode             |             1.5700 |                        -0.1560 |            -0.2024 |                     0.2737 |                -0.3196 |                  1 |

## Best Out-Of-Sample Combinations

| policy                | base_model      |   base_portfolio_size | period        |   months |   bear_months |   avg_exposure |   total_return |   bist100_total_return |   excess_return_vs_bist100 |   max_drawdown |   bist100_max_drawdown |   win_rate |   robustness_score |
|:----------------------|:----------------|----------------------:|:--------------|---------:|--------------:|---------------:|---------------:|-----------------------:|---------------------------:|---------------:|-----------------------:|-----------:|-------------------:|
| baseline              | momentum_heavy  |                     3 | out_of_sample |       31 |             7 |         1.0000 |         0.6801 |                 0.7154 |                    -0.0354 |        -0.1660 |                -0.1675 |     0.6129 |            -0.0610 |
| baseline              | mixed_model     |                    15 | out_of_sample |       31 |             7 |         1.0000 |         0.6727 |                 0.7154 |                    -0.0428 |        -0.1644 |                -0.1675 |     0.6129 |            -0.0652 |
| baseline              | momentum_heavy  |                    15 | out_of_sample |       31 |             7 |         1.0000 |         0.6716 |                 0.7154 |                    -0.0438 |        -0.1680 |                -0.1675 |     0.6129 |            -0.0733 |
| baseline              | low_volatility  |                    15 | out_of_sample |       31 |             7 |         1.0000 |         0.6450 |                 0.7154 |                    -0.0704 |        -0.1563 |                -0.1675 |     0.5806 |            -0.0927 |
| baseline              | trend_following |                    15 | out_of_sample |       31 |             7 |         1.0000 |         0.6447 |                 0.7154 |                    -0.0708 |        -0.1747 |                -0.1675 |     0.6129 |            -0.1136 |
| baseline              | volume_heavy    |                    15 | out_of_sample |       31 |             7 |         1.0000 |         0.5931 |                 0.7154 |                    -0.1223 |        -0.1746 |                -0.1675 |     0.6129 |            -0.1650 |
| defensive_mode        | momentum_heavy  |                     3 | out_of_sample |       31 |             7 |         1.0000 |         0.5674 |                 0.7154 |                    -0.1480 |        -0.1660 |                -0.1675 |     0.5806 |            -0.1898 |
| reduced_exposure_mode | momentum_heavy  |                     3 | out_of_sample |       31 |             7 |         0.8871 |         0.5414 |                 0.7154 |                    -0.1741 |        -0.1660 |                -0.1675 |     0.6129 |            -0.1997 |
| defensive_mode        | mixed_model     |                    15 | out_of_sample |       31 |             7 |         1.0000 |         0.5672 |                 0.7154 |                    -0.1483 |        -0.1757 |                -0.1675 |     0.5484 |            -0.2254 |
| baseline              | trend_following |                     3 | out_of_sample |       31 |             7 |         1.0000 |         0.5354 |                 0.7154 |                    -0.1800 |        -0.1767 |                -0.1675 |     0.6129 |            -0.2270 |

## Regime Signal Coverage

- Total signal months: 95
- BIST100 below MA200 months: 19
- Below-MA200 rate: 20.00%
