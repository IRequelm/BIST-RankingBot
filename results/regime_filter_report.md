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
| baseline              |             2.0934 |                         0.3704 |            -0.1902 |                     0.5127 |                 0.2989 |                  1 |
| defensive_mode        |             2.0191 |                         0.2960 |            -0.1901 |                     0.4450 |                 0.2170 |                  1 |
| reduced_exposure_mode |             1.8048 |                         0.0818 |            -0.1929 |                     0.4042 |                 0.0049 |                  1 |
| cash_mode             |             1.5770 |                        -0.1461 |            -0.2024 |                     0.2947 |                -0.3097 |                  1 |

## Best Out-Of-Sample Combinations

| policy                | base_model      |   base_portfolio_size | period        |   months |   bear_months |   avg_exposure |   total_return |   bist100_total_return |   excess_return_vs_bist100 |   max_drawdown |   bist100_max_drawdown |   win_rate |   robustness_score |
|:----------------------|:----------------|----------------------:|:--------------|---------:|--------------:|---------------:|---------------:|-----------------------:|---------------------------:|---------------:|-----------------------:|-----------:|-------------------:|
| baseline              | momentum_heavy  |                     3 | out_of_sample |       31 |             7 |         1.0000 |         0.7236 |                 0.7067 |                     0.0169 |        -0.1660 |                -0.1675 |     0.6129 |            -0.0087 |
| baseline              | mixed_model     |                    15 | out_of_sample |       31 |             7 |         1.0000 |         0.6826 |                 0.7067 |                    -0.0242 |        -0.1644 |                -0.1675 |     0.6129 |            -0.0466 |
| baseline              | momentum_heavy  |                    15 | out_of_sample |       31 |             7 |         1.0000 |         0.6815 |                 0.7067 |                    -0.0252 |        -0.1680 |                -0.1675 |     0.6129 |            -0.0547 |
| baseline              | low_volatility  |                    15 | out_of_sample |       31 |             7 |         1.0000 |         0.6591 |                 0.7067 |                    -0.0476 |        -0.1563 |                -0.1675 |     0.5806 |            -0.0699 |
| baseline              | trend_following |                    15 | out_of_sample |       31 |             7 |         1.0000 |         0.6544 |                 0.7067 |                    -0.0523 |        -0.1747 |                -0.1675 |     0.6129 |            -0.0952 |
| defensive_mode        | momentum_heavy  |                     3 | out_of_sample |       31 |             7 |         1.0000 |         0.6080 |                 0.7067 |                    -0.0987 |        -0.1660 |                -0.1675 |     0.5806 |            -0.1404 |
| baseline              | volume_heavy    |                    15 | out_of_sample |       31 |             7 |         1.0000 |         0.5990 |                 0.7067 |                    -0.1077 |        -0.1746 |                -0.1675 |     0.6129 |            -0.1504 |
| reduced_exposure_mode | momentum_heavy  |                     3 | out_of_sample |       31 |             7 |         0.8871 |         0.5813 |                 0.7067 |                    -0.1254 |        -0.1660 |                -0.1675 |     0.6129 |            -0.1510 |
| baseline              | trend_following |                     3 | out_of_sample |       31 |             7 |         1.0000 |         0.5752 |                 0.7067 |                    -0.1315 |        -0.1767 |                -0.1675 |     0.6129 |            -0.1784 |
| defensive_mode        | mixed_model     |                    15 | out_of_sample |       31 |             7 |         1.0000 |         0.5765 |                 0.7067 |                    -0.1303 |        -0.1757 |                -0.1675 |     0.5484 |            -0.2074 |

## Regime Signal Coverage

- Total signal months: 95
- BIST100 below MA200 months: 19
- Below-MA200 rate: 20.00%
