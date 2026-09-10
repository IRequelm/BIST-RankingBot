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
| baseline              |             2.1010 |                         0.3778 |            -0.1902 |                     0.5356 |                 0.3086 |                  1 |
| defensive_mode        |             2.0263 |                         0.3031 |            -0.1901 |                     0.4666 |                 0.2265 |                  1 |
| reduced_exposure_mode |             1.8119 |                         0.0887 |            -0.1929 |                     0.4253 |                 0.0141 |                  1 |
| cash_mode             |             1.5835 |                        -0.1397 |            -0.2024 |                     0.3141 |                -0.3003 |                  1 |

## Best Out-Of-Sample Combinations

| policy                | base_model      |   base_portfolio_size | period        |   months |   bear_months |   avg_exposure |   total_return |   bist100_total_return |   excess_return_vs_bist100 |   max_drawdown |   bist100_max_drawdown |   win_rate |   robustness_score |
|:----------------------|:----------------|----------------------:|:--------------|---------:|--------------:|---------------:|---------------:|-----------------------:|---------------------------:|---------------:|-----------------------:|-----------:|-------------------:|
| baseline              | mixed_model     |                    15 | out_of_sample |       32 |             7 |         1.0000 |         0.7432 |                 0.7072 |                     0.0360 |        -0.1644 |                -0.1675 |     0.6250 |             0.0196 |
| baseline              | momentum_heavy  |                     3 | out_of_sample |       32 |             7 |         1.0000 |         0.7411 |                 0.7072 |                     0.0339 |        -0.1660 |                -0.1675 |     0.6250 |             0.0143 |
| baseline              | momentum_heavy  |                    15 | out_of_sample |       32 |             7 |         1.0000 |         0.7402 |                 0.7072 |                     0.0330 |        -0.1680 |                -0.1675 |     0.6250 |             0.0095 |
| baseline              | low_volatility  |                    15 | out_of_sample |       32 |             7 |         1.0000 |         0.6935 |                 0.7072 |                    -0.0137 |        -0.1563 |                -0.1675 |     0.5938 |            -0.0295 |
| baseline              | trend_following |                    15 | out_of_sample |       32 |             7 |         1.0000 |         0.7141 |                 0.7072 |                     0.0069 |        -0.1747 |                -0.1675 |     0.6250 |            -0.0300 |
| baseline              | volume_heavy    |                    15 | out_of_sample |       32 |             7 |         1.0000 |         0.6592 |                 0.7072 |                    -0.0480 |        -0.1746 |                -0.1675 |     0.6250 |            -0.0846 |
| defensive_mode        | momentum_heavy  |                     3 | out_of_sample |       32 |             7 |         1.0000 |         0.6243 |                 0.7072 |                    -0.0829 |        -0.1660 |                -0.1675 |     0.5938 |            -0.1181 |
| reduced_exposure_mode | momentum_heavy  |                     3 | out_of_sample |       32 |             7 |         0.8906 |         0.5974 |                 0.7072 |                    -0.1098 |        -0.1660 |                -0.1675 |     0.6250 |            -0.1294 |
| defensive_mode        | mixed_model     |                    15 | out_of_sample |       32 |             7 |         1.0000 |         0.6333 |                 0.7072 |                    -0.0739 |        -0.1757 |                -0.1675 |     0.5625 |            -0.1440 |
| reduced_exposure_mode | mixed_model     |                    15 | out_of_sample |       32 |             7 |         0.8906 |         0.6022 |                 0.7072 |                    -0.1050 |        -0.1817 |                -0.1675 |     0.6250 |            -0.1558 |

## Regime Signal Coverage

- Total signal months: 96
- BIST100 below MA200 months: 19
- Below-MA200 rate: 19.79%
