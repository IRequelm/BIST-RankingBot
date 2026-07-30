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
| baseline              |             2.0604 |                         0.3766 |            -0.1902 |                     0.4136 |                 0.3029 |                  1 |
| defensive_mode        |             1.9878 |                         0.3039 |            -0.1901 |                     0.3510 |                 0.2226 |                  1 |
| reduced_exposure_mode |             1.7743 |                         0.0904 |            -0.1929 |                     0.3125 |                 0.0114 |                  1 |
| cash_mode             |             1.5489 |                        -0.1349 |            -0.2024 |                     0.2105 |                -0.3016 |                  1 |

## Best Out-Of-Sample Combinations

| policy                | base_model      |   base_portfolio_size | period        |   months |   bear_months |   avg_exposure |   total_return |   bist100_total_return |   excess_return_vs_bist100 |   max_drawdown |   bist100_max_drawdown |   win_rate |   robustness_score |
|:----------------------|:----------------|----------------------:|:--------------|---------:|--------------:|---------------:|---------------:|-----------------------:|---------------------------:|---------------:|-----------------------:|-----------:|-------------------:|
| baseline              | momentum_heavy  |                    15 | out_of_sample |       30 |             7 |         1.0000 |         0.6204 |                 0.5890 |                     0.0314 |        -0.1680 |                -0.1675 |     0.6000 |            -0.0046 |
| baseline              | mixed_model     |                    15 | out_of_sample |       30 |             7 |         1.0000 |         0.6115 |                 0.5890 |                     0.0225 |        -0.1644 |                -0.1675 |     0.6000 |            -0.0064 |
| baseline              | low_volatility  |                    15 | out_of_sample |       30 |             7 |         1.0000 |         0.5939 |                 0.5890 |                     0.0048 |        -0.1563 |                -0.1675 |     0.5667 |            -0.0245 |
| baseline              | trend_following |                    15 | out_of_sample |       30 |             7 |         1.0000 |         0.5943 |                 0.5890 |                     0.0052 |        -0.1747 |                -0.1675 |     0.6000 |            -0.0441 |
| baseline              | momentum_heavy  |                     3 | out_of_sample |       30 |             7 |         1.0000 |         0.5616 |                 0.5890 |                    -0.0274 |        -0.1660 |                -0.1675 |     0.6000 |            -0.0595 |
| baseline              | volume_heavy    |                    15 | out_of_sample |       30 |             7 |         1.0000 |         0.5339 |                 0.5890 |                    -0.0552 |        -0.1746 |                -0.1675 |     0.6000 |            -0.1043 |
| defensive_mode        | mixed_model     |                    15 | out_of_sample |       30 |             7 |         1.0000 |         0.5099 |                 0.5890 |                    -0.0791 |        -0.1757 |                -0.1675 |     0.5333 |            -0.1638 |
| defensive_mode        | momentum_heavy  |                    15 | out_of_sample |       30 |             7 |         1.0000 |         0.5145 |                 0.5890 |                    -0.0746 |        -0.1792 |                -0.1675 |     0.5333 |            -0.1663 |
| defensive_mode        | low_volatility  |                    15 | out_of_sample |       30 |             7 |         1.0000 |         0.4865 |                 0.5890 |                    -0.1025 |        -0.1661 |                -0.1675 |     0.5333 |            -0.1680 |
| reduced_exposure_mode | mixed_model     |                    15 | out_of_sample |       30 |             7 |         0.8833 |         0.4812 |                 0.5890 |                    -0.1078 |        -0.1817 |                -0.1675 |     0.6000 |            -0.1711 |

## Regime Signal Coverage

- Total signal months: 94
- BIST100 below MA200 months: 19
- Below-MA200 rate: 20.21%
