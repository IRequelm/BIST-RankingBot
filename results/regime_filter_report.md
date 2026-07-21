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
| baseline              |             2.0729 |                         0.3668 |            -0.1902 |                     0.4512 |                 0.2939 |                  1 |
| defensive_mode        |             1.9996 |                         0.2935 |            -0.1901 |                     0.3866 |                 0.2129 |                  1 |
| reduced_exposure_mode |             1.7858 |                         0.0797 |            -0.1929 |                     0.3472 |                 0.0015 |                  1 |
| cash_mode             |             1.5595 |                        -0.1466 |            -0.2024 |                     0.2424 |                -0.3125 |                  1 |

## Best Out-Of-Sample Combinations

| policy                | base_model      |   base_portfolio_size | period        |   months |   bear_months |   avg_exposure |   total_return |   bist100_total_return |   excess_return_vs_bist100 |   max_drawdown |   bist100_max_drawdown |   win_rate |   robustness_score |
|:----------------------|:----------------|----------------------:|:--------------|---------:|--------------:|---------------:|---------------:|-----------------------:|---------------------------:|---------------:|-----------------------:|-----------:|-------------------:|
| baseline              | mixed_model     |                    15 | out_of_sample |       30 |             7 |         1.0000 |         0.6491 |                 0.6561 |                    -0.0070 |        -0.1644 |                -0.1675 |     0.6000 |            -0.0359 |
| baseline              | momentum_heavy  |                     3 | out_of_sample |       30 |             7 |         1.0000 |         0.6344 |                 0.6561 |                    -0.0216 |        -0.1660 |                -0.1675 |     0.6333 |            -0.0370 |
| baseline              | momentum_heavy  |                    15 | out_of_sample |       30 |             7 |         1.0000 |         0.6538 |                 0.6561 |                    -0.0022 |        -0.1680 |                -0.1675 |     0.6000 |            -0.0382 |
| baseline              | low_volatility  |                    15 | out_of_sample |       30 |             7 |         1.0000 |         0.6333 |                 0.6561 |                    -0.0227 |        -0.1563 |                -0.1675 |     0.5667 |            -0.0521 |
| baseline              | trend_following |                    15 | out_of_sample |       30 |             7 |         1.0000 |         0.6271 |                 0.6561 |                    -0.0289 |        -0.1747 |                -0.1675 |     0.6000 |            -0.0782 |
| baseline              | volume_heavy    |                    15 | out_of_sample |       30 |             7 |         1.0000 |         0.5696 |                 0.6561 |                    -0.0865 |        -0.1746 |                -0.1675 |     0.6000 |            -0.1356 |
| defensive_mode        | momentum_heavy  |                     3 | out_of_sample |       30 |             7 |         1.0000 |         0.5248 |                 0.6561 |                    -0.1312 |        -0.1660 |                -0.1675 |     0.6000 |            -0.1633 |
| reduced_exposure_mode | momentum_heavy  |                     3 | out_of_sample |       30 |             7 |         0.8833 |         0.4995 |                 0.6561 |                    -0.1565 |        -0.1660 |                -0.1675 |     0.6333 |            -0.1720 |
| defensive_mode        | mixed_model     |                    15 | out_of_sample |       30 |             7 |         1.0000 |         0.5451 |                 0.6561 |                    -0.1110 |        -0.1757 |                -0.1675 |     0.5333 |            -0.1957 |
| defensive_mode        | low_volatility  |                    15 | out_of_sample |       30 |             7 |         1.0000 |         0.5233 |                 0.6561 |                    -0.1327 |        -0.1661 |                -0.1675 |     0.5333 |            -0.1982 |

## Regime Signal Coverage

- Total signal months: 94
- BIST100 below MA200 months: 19
- Below-MA200 rate: 20.21%
