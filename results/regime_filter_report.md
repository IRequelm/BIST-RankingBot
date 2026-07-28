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
| baseline              |             2.0647 |                         0.3701 |            -0.1902 |                     0.4264 |                 0.2962 |                  1 |
| defensive_mode        |             1.9918 |                         0.2973 |            -0.1901 |                     0.3631 |                 0.2156 |                  1 |
| reduced_exposure_mode |             1.7782 |                         0.0837 |            -0.1929 |                     0.3244 |                 0.0044 |                  1 |
| cash_mode             |             1.5525 |                        -0.1420 |            -0.2024 |                     0.2214 |                -0.3090 |                  1 |

## Best Out-Of-Sample Combinations

| policy                | base_model      |   base_portfolio_size | period        |   months |   bear_months |   avg_exposure |   total_return |   bist100_total_return |   excess_return_vs_bist100 |   max_drawdown |   bist100_max_drawdown |   win_rate |   robustness_score |
|:----------------------|:----------------|----------------------:|:--------------|---------:|--------------:|---------------:|---------------:|-----------------------:|---------------------------:|---------------:|-----------------------:|-----------:|-------------------:|
| baseline              | momentum_heavy  |                    15 | out_of_sample |       30 |             7 |         1.0000 |         0.6521 |                 0.6212 |                     0.0309 |        -0.1680 |                -0.1675 |     0.6000 |            -0.0051 |
| baseline              | mixed_model     |                    15 | out_of_sample |       30 |             7 |         1.0000 |         0.6350 |                 0.6212 |                     0.0138 |        -0.1644 |                -0.1675 |     0.6000 |            -0.0151 |
| baseline              | low_volatility  |                    15 | out_of_sample |       30 |             7 |         1.0000 |         0.6117 |                 0.6212 |                    -0.0095 |        -0.1563 |                -0.1675 |     0.5667 |            -0.0388 |
| baseline              | trend_following |                    15 | out_of_sample |       30 |             7 |         1.0000 |         0.6254 |                 0.6212 |                     0.0042 |        -0.1747 |                -0.1675 |     0.6000 |            -0.0451 |
| baseline              | momentum_heavy  |                     3 | out_of_sample |       30 |             7 |         1.0000 |         0.5716 |                 0.6212 |                    -0.0496 |        -0.1660 |                -0.1675 |     0.6000 |            -0.0817 |
| baseline              | volume_heavy    |                    15 | out_of_sample |       30 |             7 |         1.0000 |         0.5562 |                 0.6212 |                    -0.0650 |        -0.1746 |                -0.1675 |     0.6000 |            -0.1141 |
| defensive_mode        | momentum_heavy  |                    15 | out_of_sample |       30 |             7 |         1.0000 |         0.5440 |                 0.6212 |                    -0.0772 |        -0.1792 |                -0.1675 |     0.5333 |            -0.1689 |
| defensive_mode        | mixed_model     |                    15 | out_of_sample |       30 |             7 |         1.0000 |         0.5319 |                 0.6212 |                    -0.0893 |        -0.1757 |                -0.1675 |     0.5333 |            -0.1740 |
| reduced_exposure_mode | momentum_heavy  |                    15 | out_of_sample |       30 |             7 |         0.8833 |         0.5165 |                 0.6212 |                    -0.1047 |        -0.1851 |                -0.1675 |     0.6000 |            -0.1749 |
| reduced_exposure_mode | mixed_model     |                    15 | out_of_sample |       30 |             7 |         0.8833 |         0.5028 |                 0.6212 |                    -0.1184 |        -0.1817 |                -0.1675 |     0.6000 |            -0.1817 |

## Regime Signal Coverage

- Total signal months: 94
- BIST100 below MA200 months: 19
- Below-MA200 rate: 20.21%
