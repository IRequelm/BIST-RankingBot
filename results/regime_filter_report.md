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
| baseline              |             2.0624 |                         0.3783 |            -0.1902 |                     0.4198 |                 0.3039 |                  1 |
| defensive_mode        |             1.9894 |                         0.3053 |            -0.1901 |                     0.3559 |                 0.2234 |                  1 |
| reduced_exposure_mode |             1.7760 |                         0.0919 |            -0.1929 |                     0.3178 |                 0.0121 |                  1 |
| cash_mode             |             1.5504 |                        -0.1338 |            -0.2024 |                     0.2149 |                -0.2995 |                  1 |

## Best Out-Of-Sample Combinations

| policy                | base_model      |   base_portfolio_size | period        |   months |   bear_months |   avg_exposure |   total_return |   bist100_total_return |   excess_return_vs_bist100 |   max_drawdown |   bist100_max_drawdown |   win_rate |   robustness_score |
|:----------------------|:----------------|----------------------:|:--------------|---------:|--------------:|---------------:|---------------:|-----------------------:|---------------------------:|---------------:|-----------------------:|-----------:|-------------------:|
| baseline              | momentum_heavy  |                     3 | out_of_sample |       32 |             7 |         1.0000 |         0.6854 |                 0.5900 |                     0.0954 |        -0.1660 |                -0.1675 |     0.5938 |             0.0602 |
| baseline              | mixed_model     |                    15 | out_of_sample |       32 |             7 |         1.0000 |         0.5734 |                 0.5900 |                    -0.0166 |        -0.1644 |                -0.1675 |     0.5938 |            -0.0486 |
| baseline              | momentum_heavy  |                    15 | out_of_sample |       32 |             7 |         1.0000 |         0.5744 |                 0.5900 |                    -0.0156 |        -0.1680 |                -0.1675 |     0.5938 |            -0.0548 |
| defensive_mode        | momentum_heavy  |                     3 | out_of_sample |       32 |             7 |         1.0000 |         0.5724 |                 0.5900 |                    -0.0176 |        -0.1660 |                -0.1675 |     0.5625 |            -0.0685 |
| reduced_exposure_mode | momentum_heavy  |                     3 | out_of_sample |       32 |             7 |         0.8906 |         0.5463 |                 0.5900 |                    -0.0437 |        -0.1660 |                -0.1675 |     0.5938 |            -0.0789 |
| baseline              | low_volatility  |                    15 | out_of_sample |       32 |             7 |         1.0000 |         0.5337 |                 0.5900 |                    -0.0563 |        -0.1563 |                -0.1675 |     0.5625 |            -0.0877 |
| baseline              | trend_following |                    15 | out_of_sample |       32 |             7 |         1.0000 |         0.5471 |                 0.5900 |                    -0.0429 |        -0.1747 |                -0.1675 |     0.5938 |            -0.0954 |
| baseline              | trend_following |                     3 | out_of_sample |       32 |             7 |         1.0000 |         0.5403 |                 0.5900 |                    -0.0497 |        -0.1767 |                -0.1675 |     0.5938 |            -0.1062 |
| baseline              | volume_heavy    |                    15 | out_of_sample |       32 |             7 |         1.0000 |         0.4976 |                 0.5900 |                    -0.0924 |        -0.1746 |                -0.1675 |     0.5938 |            -0.1447 |
| defensive_mode        | mixed_model     |                    15 | out_of_sample |       32 |             7 |         1.0000 |         0.4742 |                 0.5900 |                    -0.1158 |        -0.1757 |                -0.1675 |     0.5312 |            -0.2016 |

## Regime Signal Coverage

- Total signal months: 96
- BIST100 below MA200 months: 19
- Below-MA200 rate: 19.79%
