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
| baseline              |             2.0764 |                         0.3741 |            -0.1902 |                     0.4618 |                 0.3021 |                  1 |
| defensive_mode        |             2.0030 |                         0.3006 |            -0.1901 |                     0.3967 |                 0.2209 |                  1 |
| reduced_exposure_mode |             1.7891 |                         0.0868 |            -0.1929 |                     0.3571 |                 0.0094 |                  1 |
| cash_mode             |             1.5626 |                        -0.1398 |            -0.2024 |                     0.2515 |                -0.3048 |                  1 |

## Best Out-Of-Sample Combinations

| policy                | base_model      |   base_portfolio_size | period        |   months |   bear_months |   avg_exposure |   total_return |   bist100_total_return |   excess_return_vs_bist100 |   max_drawdown |   bist100_max_drawdown |   win_rate |   robustness_score |
|:----------------------|:----------------|----------------------:|:--------------|---------:|--------------:|---------------:|---------------:|-----------------------:|---------------------------:|---------------:|-----------------------:|-----------:|-------------------:|
| baseline              | momentum_heavy  |                    15 | out_of_sample |       30 |             7 |         1.0000 |         0.6795 |                 0.6447 |                     0.0348 |        -0.1680 |                -0.1675 |     0.6333 |             0.0155 |
| baseline              | mixed_model     |                    15 | out_of_sample |       30 |             7 |         1.0000 |         0.6634 |                 0.6447 |                     0.0187 |        -0.1644 |                -0.1675 |     0.6000 |            -0.0102 |
| baseline              | momentum_heavy  |                     3 | out_of_sample |       30 |             7 |         1.0000 |         0.6382 |                 0.6447 |                    -0.0064 |        -0.1660 |                -0.1675 |     0.6333 |            -0.0218 |
| baseline              | trend_following |                    15 | out_of_sample |       30 |             7 |         1.0000 |         0.6524 |                 0.6447 |                     0.0077 |        -0.1747 |                -0.1675 |     0.6333 |            -0.0249 |
| baseline              | low_volatility  |                    15 | out_of_sample |       30 |             7 |         1.0000 |         0.6475 |                 0.6447 |                     0.0029 |        -0.1563 |                -0.1675 |     0.5667 |            -0.0265 |
| baseline              | volume_heavy    |                    15 | out_of_sample |       30 |             7 |         1.0000 |         0.5832 |                 0.6447 |                    -0.0614 |        -0.1746 |                -0.1675 |     0.6000 |            -0.1106 |
| defensive_mode        | momentum_heavy  |                     3 | out_of_sample |       30 |             7 |         1.0000 |         0.5283 |                 0.6447 |                    -0.1163 |        -0.1660 |                -0.1675 |     0.6000 |            -0.1484 |
| defensive_mode        | momentum_heavy  |                    15 | out_of_sample |       30 |             7 |         1.0000 |         0.5697 |                 0.6447 |                    -0.0750 |        -0.1792 |                -0.1675 |     0.5667 |            -0.1500 |
| reduced_exposure_mode | momentum_heavy  |                    15 | out_of_sample |       30 |             7 |         0.8833 |         0.5417 |                 0.6447 |                    -0.1030 |        -0.1851 |                -0.1675 |     0.6333 |            -0.1565 |
| reduced_exposure_mode | momentum_heavy  |                     3 | out_of_sample |       30 |             7 |         0.8833 |         0.5030 |                 0.6447 |                    -0.1417 |        -0.1660 |                -0.1675 |     0.6333 |            -0.1571 |

## Regime Signal Coverage

- Total signal months: 94
- BIST100 below MA200 months: 19
- Below-MA200 rate: 20.21%
