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
| baseline              |             2.0730 |                         0.3660 |            -0.1902 |                     0.4513 |                 0.2929 |                  1 |
| defensive_mode        |             1.9997 |                         0.2927 |            -0.1901 |                     0.3869 |                 0.2119 |                  1 |
| reduced_exposure_mode |             1.7859 |                         0.0789 |            -0.1929 |                     0.3474 |                 0.0004 |                  1 |
| cash_mode             |             1.5596 |                        -0.1473 |            -0.2024 |                     0.2427 |                -0.3135 |                  1 |

## Best Out-Of-Sample Combinations

| policy                | base_model      |   base_portfolio_size | period        |   months |   bear_months |   avg_exposure |   total_return |   bist100_total_return |   excess_return_vs_bist100 |   max_drawdown |   bist100_max_drawdown |   win_rate |   robustness_score |
|:----------------------|:----------------|----------------------:|:--------------|---------:|--------------:|---------------:|---------------:|-----------------------:|---------------------------:|---------------:|-----------------------:|-----------:|-------------------:|
| baseline              | mixed_model     |                    15 | out_of_sample |       30 |             7 |         1.0000 |         0.6449 |                 0.6585 |                    -0.0136 |        -0.1644 |                -0.1675 |     0.6000 |            -0.0425 |
| baseline              | momentum_heavy  |                     3 | out_of_sample |       30 |             7 |         1.0000 |         0.6247 |                 0.6585 |                    -0.0338 |        -0.1660 |                -0.1675 |     0.6333 |            -0.0492 |
| baseline              | momentum_heavy  |                    15 | out_of_sample |       30 |             7 |         1.0000 |         0.6427 |                 0.6585 |                    -0.0158 |        -0.1680 |                -0.1675 |     0.6000 |            -0.0518 |
| baseline              | low_volatility  |                    15 | out_of_sample |       30 |             7 |         1.0000 |         0.6247 |                 0.6585 |                    -0.0338 |        -0.1563 |                -0.1675 |     0.5667 |            -0.0632 |
| baseline              | trend_following |                    15 | out_of_sample |       30 |             7 |         1.0000 |         0.6162 |                 0.6585 |                    -0.0423 |        -0.1747 |                -0.1675 |     0.6000 |            -0.0916 |
| baseline              | volume_heavy    |                    15 | out_of_sample |       30 |             7 |         1.0000 |         0.5656 |                 0.6585 |                    -0.0929 |        -0.1746 |                -0.1675 |     0.6000 |            -0.1420 |
| defensive_mode        | momentum_heavy  |                     3 | out_of_sample |       30 |             7 |         1.0000 |         0.5158 |                 0.6585 |                    -0.1428 |        -0.1660 |                -0.1675 |     0.6000 |            -0.1749 |
| reduced_exposure_mode | momentum_heavy  |                     3 | out_of_sample |       30 |             7 |         0.8833 |         0.4906 |                 0.6585 |                    -0.1679 |        -0.1660 |                -0.1675 |     0.6333 |            -0.1833 |
| defensive_mode        | mixed_model     |                    15 | out_of_sample |       30 |             7 |         1.0000 |         0.5412 |                 0.6585 |                    -0.1174 |        -0.1757 |                -0.1675 |     0.5333 |            -0.2021 |
| defensive_mode        | low_volatility  |                    15 | out_of_sample |       30 |             7 |         1.0000 |         0.5153 |                 0.6585 |                    -0.1433 |        -0.1661 |                -0.1675 |     0.5333 |            -0.2087 |

## Regime Signal Coverage

- Total signal months: 94
- BIST100 below MA200 months: 19
- Below-MA200 rate: 20.21%
