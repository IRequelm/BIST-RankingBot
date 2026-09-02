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
| baseline              |             2.0846 |                         0.3722 |            -0.1902 |                     0.4862 |                 0.3007 |                  1 |
| defensive_mode        |             2.0106 |                         0.2983 |            -0.1901 |                     0.4196 |                 0.2192 |                  1 |
| reduced_exposure_mode |             1.7966 |                         0.0843 |            -0.1929 |                     0.3796 |                 0.0074 |                  1 |
| cash_mode             |             1.5694 |                        -0.1429 |            -0.2024 |                     0.2720 |                -0.3066 |                  1 |

## Best Out-Of-Sample Combinations

| policy                | base_model      |   base_portfolio_size | period        |   months |   bear_months |   avg_exposure |   total_return |   bist100_total_return |   excess_return_vs_bist100 |   max_drawdown |   bist100_max_drawdown |   win_rate |   robustness_score |
|:----------------------|:----------------|----------------------:|:--------------|---------:|--------------:|---------------:|---------------:|-----------------------:|---------------------------:|---------------:|-----------------------:|-----------:|-------------------:|
| baseline              | momentum_heavy  |                     3 | out_of_sample |       32 |             7 |         1.0000 |         0.7055 |                 0.6747 |                     0.0308 |        -0.1660 |                -0.1675 |     0.6129 |             0.0052 |
| baseline              | mixed_model     |                    15 | out_of_sample |       32 |             7 |         1.0000 |         0.6528 |                 0.6747 |                    -0.0219 |        -0.1644 |                -0.1675 |     0.6129 |            -0.0443 |
| baseline              | momentum_heavy  |                    15 | out_of_sample |       32 |             7 |         1.0000 |         0.6518 |                 0.6747 |                    -0.0229 |        -0.1680 |                -0.1675 |     0.6129 |            -0.0524 |
| baseline              | low_volatility  |                    15 | out_of_sample |       32 |             7 |         1.0000 |         0.6233 |                 0.6747 |                    -0.0514 |        -0.1563 |                -0.1675 |     0.5806 |            -0.0737 |
| baseline              | trend_following |                    15 | out_of_sample |       32 |             7 |         1.0000 |         0.6251 |                 0.6747 |                    -0.0495 |        -0.1747 |                -0.1675 |     0.6129 |            -0.0924 |
| defensive_mode        | momentum_heavy  |                     3 | out_of_sample |       32 |             7 |         1.0000 |         0.5911 |                 0.6747 |                    -0.0836 |        -0.1660 |                -0.1675 |     0.5806 |            -0.1253 |
| reduced_exposure_mode | momentum_heavy  |                     3 | out_of_sample |       32 |             7 |         0.8906 |         0.5647 |                 0.6747 |                    -0.1100 |        -0.1660 |                -0.1675 |     0.6129 |            -0.1356 |
| baseline              | volume_heavy    |                    15 | out_of_sample |       32 |             7 |         1.0000 |         0.5731 |                 0.6747 |                    -0.1015 |        -0.1746 |                -0.1675 |     0.6129 |            -0.1442 |
| baseline              | trend_following |                     3 | out_of_sample |       32 |             7 |         1.0000 |         0.5586 |                 0.6747 |                    -0.1160 |        -0.1767 |                -0.1675 |     0.6129 |            -0.1630 |
| defensive_mode        | mixed_model     |                    15 | out_of_sample |       32 |             7 |         1.0000 |         0.5485 |                 0.6747 |                    -0.1261 |        -0.1757 |                -0.1675 |     0.5484 |            -0.2033 |

## Regime Signal Coverage

- Total signal months: 96
- BIST100 below MA200 months: 19
- Below-MA200 rate: 19.79%
