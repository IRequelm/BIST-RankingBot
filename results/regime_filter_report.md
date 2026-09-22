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
| baseline              |             2.0835 |                         0.4062 |            -0.1902 |                     0.4830 |                 0.3328 |                  1 |
| defensive_mode        |             2.0096 |                         0.3322 |            -0.1901 |                     0.4164 |                 0.2514 |                  1 |
| reduced_exposure_mode |             1.7956 |                         0.1182 |            -0.1929 |                     0.3766 |                 0.0395 |                  1 |
| cash_mode             |             1.5684 |                        -0.1089 |            -0.2024 |                     0.2691 |                -0.2736 |                  1 |

## Best Out-Of-Sample Combinations

| policy                | base_model      |   base_portfolio_size | period        |   months |   bear_months |   avg_exposure |   total_return |   bist100_total_return |   excess_return_vs_bist100 |   max_drawdown |   bist100_max_drawdown |   win_rate |   robustness_score |
|:----------------------|:----------------|----------------------:|:--------------|---------:|--------------:|---------------:|---------------:|-----------------------:|---------------------------:|---------------:|-----------------------:|-----------:|-------------------:|
| baseline              | momentum_heavy  |                     3 | out_of_sample |       32 |             7 |         1.0000 |         0.7492 |                 0.5698 |                     0.1795 |        -0.1660 |                -0.1675 |     0.6250 |             0.1599 |
| baseline              | mixed_model     |                    15 | out_of_sample |       32 |             7 |         1.0000 |         0.6465 |                 0.5698 |                     0.0767 |        -0.1644 |                -0.1675 |     0.5938 |             0.0447 |
| baseline              | momentum_heavy  |                    15 | out_of_sample |       32 |             7 |         1.0000 |         0.6473 |                 0.5698 |                     0.0775 |        -0.1680 |                -0.1675 |     0.5938 |             0.0384 |
| defensive_mode        | momentum_heavy  |                     3 | out_of_sample |       32 |             7 |         1.0000 |         0.6319 |                 0.5698 |                     0.0621 |        -0.1660 |                -0.1675 |     0.5938 |             0.0269 |
| reduced_exposure_mode | momentum_heavy  |                     3 | out_of_sample |       32 |             7 |         0.8906 |         0.6048 |                 0.5698 |                     0.0351 |        -0.1660 |                -0.1675 |     0.6250 |             0.0155 |
| baseline              | low_volatility  |                    15 | out_of_sample |       32 |             7 |         1.0000 |         0.6035 |                 0.5698 |                     0.0338 |        -0.1563 |                -0.1675 |     0.5625 |             0.0023 |
| baseline              | trend_following |                    15 | out_of_sample |       32 |             7 |         1.0000 |         0.6190 |                 0.5698 |                     0.0492 |        -0.1747 |                -0.1675 |     0.5938 |            -0.0032 |
| baseline              | trend_following |                     3 | out_of_sample |       32 |             7 |         1.0000 |         0.5986 |                 0.5698 |                     0.0289 |        -0.1767 |                -0.1675 |     0.6250 |            -0.0121 |
| baseline              | volume_heavy    |                    15 | out_of_sample |       32 |             7 |         1.0000 |         0.5672 |                 0.5698 |                    -0.0026 |        -0.1746 |                -0.1675 |     0.5938 |            -0.0548 |
| defensive_mode        | mixed_model     |                    15 | out_of_sample |       32 |             7 |         1.0000 |         0.5427 |                 0.5698 |                    -0.0271 |        -0.1757 |                -0.1675 |     0.5312 |            -0.1128 |

## Regime Signal Coverage

- Total signal months: 96
- BIST100 below MA200 months: 20
- Below-MA200 rate: 20.83%
