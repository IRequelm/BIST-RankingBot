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
| baseline              |             2.0644 |                         0.3559 |            -0.1903 |                     0.4257 |                 0.2843 |                  1 |
| defensive_mode        |             1.9914 |                         0.2829 |            -0.1903 |                     0.3620 |                 0.2034 |                  1 |
| reduced_exposure_mode |             1.7779 |                         0.0694 |            -0.1931 |                     0.3235 |                -0.0079 |                  1 |
| cash_mode             |             1.5522 |                        -0.1564 |            -0.2026 |                     0.2204 |                -0.3204 |                  1 |

## Best Out-Of-Sample Combinations

| policy                | base_model      |   base_portfolio_size | period        |   months |   bear_months |   avg_exposure |   total_return |   bist100_total_return |   excess_return_vs_bist100 |   max_drawdown |   bist100_max_drawdown |   win_rate |   robustness_score |
|:----------------------|:----------------|----------------------:|:--------------|---------:|--------------:|---------------:|---------------:|-----------------------:|---------------------------:|---------------:|-----------------------:|-----------:|-------------------:|
| baseline              | mixed_model     |                    15 | out_of_sample |       31 |             7 |         1.0000 |         0.6217 |                 0.6633 |                    -0.0416 |        -0.1644 |                -0.1675 |     0.6129 |            -0.0640 |
| baseline              | momentum_heavy  |                    15 | out_of_sample |       31 |             7 |         1.0000 |         0.6248 |                 0.6633 |                    -0.0385 |        -0.1680 |                -0.1675 |     0.6129 |            -0.0680 |
| baseline              | low_volatility  |                    15 | out_of_sample |       31 |             7 |         1.0000 |         0.5983 |                 0.6633 |                    -0.0650 |        -0.1563 |                -0.1675 |     0.5806 |            -0.0873 |
| baseline              | trend_following |                    15 | out_of_sample |       31 |             7 |         1.0000 |         0.5986 |                 0.6633 |                    -0.0647 |        -0.1747 |                -0.1675 |     0.6129 |            -0.1075 |
| baseline              | momentum_heavy  |                     3 | out_of_sample |       31 |             7 |         1.0000 |         0.5750 |                 0.6633 |                    -0.0883 |        -0.1660 |                -0.1675 |     0.6129 |            -0.1139 |
| baseline              | volume_heavy    |                    15 | out_of_sample |       31 |             7 |         1.0000 |         0.5435 |                 0.6633 |                    -0.1197 |        -0.1746 |                -0.1675 |     0.6129 |            -0.1624 |
| defensive_mode        | mixed_model     |                    15 | out_of_sample |       31 |             7 |         1.0000 |         0.5194 |                 0.6633 |                    -0.1438 |        -0.1757 |                -0.1675 |     0.5484 |            -0.2210 |
| defensive_mode        | momentum_heavy  |                    15 | out_of_sample |       31 |             7 |         1.0000 |         0.5186 |                 0.6633 |                    -0.1447 |        -0.1792 |                -0.1675 |     0.5484 |            -0.2289 |
| reduced_exposure_mode | mixed_model     |                    15 | out_of_sample |       31 |             7 |         0.8871 |         0.4906 |                 0.6633 |                    -0.1727 |        -0.1817 |                -0.1675 |     0.6129 |            -0.2296 |
| defensive_mode        | low_volatility  |                    15 | out_of_sample |       31 |             7 |         1.0000 |         0.4906 |                 0.6633 |                    -0.1726 |        -0.1661 |                -0.1675 |     0.5484 |            -0.2306 |

## Regime Signal Coverage

- Total signal months: 95
- BIST100 below MA200 months: 19
- Below-MA200 rate: 20.00%
