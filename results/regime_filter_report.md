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
| baseline              |             2.0852 |                         0.3567 |            -0.1902 |                     0.4880 |                 0.2852 |                  1 |
| defensive_mode        |             2.0113 |                         0.2827 |            -0.1901 |                     0.4215 |                 0.2037 |                  1 |
| reduced_exposure_mode |             1.7972 |                         0.0687 |            -0.1929 |                     0.3813 |                -0.0082 |                  1 |
| cash_mode             |             1.5700 |                        -0.1586 |            -0.2024 |                     0.2737 |                -0.3222 |                  1 |

## Best Out-Of-Sample Combinations

| policy                | base_model      |   base_portfolio_size | period        |   months |   bear_months |   avg_exposure |   total_return |   bist100_total_return |   excess_return_vs_bist100 |   max_drawdown |   bist100_max_drawdown |   win_rate |   robustness_score |
|:----------------------|:----------------|----------------------:|:--------------|---------:|--------------:|---------------:|---------------:|-----------------------:|---------------------------:|---------------:|-----------------------:|-----------:|-------------------:|
| baseline              | momentum_heavy  |                     3 | out_of_sample |       31 |             7 |         1.0000 |         0.6801 |                 0.7232 |                    -0.0431 |        -0.1660 |                -0.1675 |     0.6129 |            -0.0688 |
| baseline              | mixed_model     |                    15 | out_of_sample |       31 |             7 |         1.0000 |         0.6727 |                 0.7232 |                    -0.0506 |        -0.1644 |                -0.1675 |     0.6129 |            -0.0730 |
| baseline              | momentum_heavy  |                    15 | out_of_sample |       31 |             7 |         1.0000 |         0.6716 |                 0.7232 |                    -0.0516 |        -0.1680 |                -0.1675 |     0.6129 |            -0.0811 |
| baseline              | low_volatility  |                    15 | out_of_sample |       31 |             7 |         1.0000 |         0.6450 |                 0.7232 |                    -0.0782 |        -0.1563 |                -0.1675 |     0.5806 |            -0.1005 |
| baseline              | trend_following |                    15 | out_of_sample |       31 |             7 |         1.0000 |         0.6447 |                 0.7232 |                    -0.0785 |        -0.1747 |                -0.1675 |     0.6129 |            -0.1214 |
| baseline              | volume_heavy    |                    15 | out_of_sample |       31 |             7 |         1.0000 |         0.5931 |                 0.7232 |                    -0.1301 |        -0.1746 |                -0.1675 |     0.6129 |            -0.1728 |
| defensive_mode        | momentum_heavy  |                     3 | out_of_sample |       31 |             7 |         1.0000 |         0.5674 |                 0.7232 |                    -0.1558 |        -0.1660 |                -0.1675 |     0.5806 |            -0.1976 |
| reduced_exposure_mode | momentum_heavy  |                     3 | out_of_sample |       31 |             7 |         0.8871 |         0.5414 |                 0.7232 |                    -0.1818 |        -0.1660 |                -0.1675 |     0.6129 |            -0.2075 |
| defensive_mode        | mixed_model     |                    15 | out_of_sample |       31 |             7 |         1.0000 |         0.5672 |                 0.7232 |                    -0.1560 |        -0.1757 |                -0.1675 |     0.5484 |            -0.2332 |
| baseline              | trend_following |                     3 | out_of_sample |       31 |             7 |         1.0000 |         0.5354 |                 0.7232 |                    -0.1878 |        -0.1767 |                -0.1675 |     0.6129 |            -0.2347 |

## Regime Signal Coverage

- Total signal months: 95
- BIST100 below MA200 months: 19
- Below-MA200 rate: 20.00%
