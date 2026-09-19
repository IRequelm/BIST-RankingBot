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
| baseline              |             2.0624 |                         0.3871 |            -0.1902 |                     0.4198 |                 0.3127 |                  1 |
| defensive_mode        |             1.9894 |                         0.3141 |            -0.1901 |                     0.3559 |                 0.2323 |                  1 |
| reduced_exposure_mode |             1.7760 |                         0.1007 |            -0.1929 |                     0.3178 |                 0.0209 |                  1 |
| cash_mode             |             1.5504 |                        -0.1249 |            -0.2024 |                     0.2149 |                -0.2907 |                  1 |

## Best Out-Of-Sample Combinations

| policy                | base_model      |   base_portfolio_size | period        |   months |   bear_months |   avg_exposure |   total_return |   bist100_total_return |   excess_return_vs_bist100 |   max_drawdown |   bist100_max_drawdown |   win_rate |   robustness_score |
|:----------------------|:----------------|----------------------:|:--------------|---------:|--------------:|---------------:|---------------:|-----------------------:|---------------------------:|---------------:|-----------------------:|-----------:|-------------------:|
| baseline              | momentum_heavy  |                     3 | out_of_sample |       32 |             7 |         1.0000 |         0.6854 |                 0.5635 |                     0.1219 |        -0.1660 |                -0.1675 |     0.5938 |             0.0867 |
| baseline              | mixed_model     |                    15 | out_of_sample |       32 |             7 |         1.0000 |         0.5734 |                 0.5635 |                     0.0099 |        -0.1644 |                -0.1675 |     0.5938 |            -0.0221 |
| baseline              | momentum_heavy  |                    15 | out_of_sample |       32 |             7 |         1.0000 |         0.5744 |                 0.5635 |                     0.0109 |        -0.1680 |                -0.1675 |     0.5938 |            -0.0282 |
| defensive_mode        | momentum_heavy  |                     3 | out_of_sample |       32 |             7 |         1.0000 |         0.5724 |                 0.5635 |                     0.0089 |        -0.1660 |                -0.1675 |     0.5625 |            -0.0419 |
| reduced_exposure_mode | momentum_heavy  |                     3 | out_of_sample |       32 |             7 |         0.8906 |         0.5463 |                 0.5635 |                    -0.0172 |        -0.1660 |                -0.1675 |     0.5938 |            -0.0524 |
| baseline              | low_volatility  |                    15 | out_of_sample |       32 |             7 |         1.0000 |         0.5337 |                 0.5635 |                    -0.0298 |        -0.1563 |                -0.1675 |     0.5625 |            -0.0612 |
| baseline              | trend_following |                    15 | out_of_sample |       32 |             7 |         1.0000 |         0.5471 |                 0.5635 |                    -0.0164 |        -0.1747 |                -0.1675 |     0.5938 |            -0.0689 |
| baseline              | trend_following |                     3 | out_of_sample |       32 |             7 |         1.0000 |         0.5403 |                 0.5635 |                    -0.0232 |        -0.1767 |                -0.1675 |     0.5938 |            -0.0797 |
| baseline              | volume_heavy    |                    15 | out_of_sample |       32 |             7 |         1.0000 |         0.4976 |                 0.5635 |                    -0.0659 |        -0.1746 |                -0.1675 |     0.5938 |            -0.1182 |
| defensive_mode        | mixed_model     |                    15 | out_of_sample |       32 |             7 |         1.0000 |         0.4742 |                 0.5635 |                    -0.0893 |        -0.1757 |                -0.1675 |     0.5312 |            -0.1751 |

## Regime Signal Coverage

- Total signal months: 96
- BIST100 below MA200 months: 20
- Below-MA200 rate: 20.83%
