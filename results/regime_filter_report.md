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
| baseline              |             2.1057 |                         0.3931 |            -0.1902 |                     0.5495 |                 0.3239 |                  1 |
| defensive_mode        |             2.0307 |                         0.3181 |            -0.1901 |                     0.4799 |                 0.2415 |                  1 |
| reduced_exposure_mode |             1.8162 |                         0.1036 |            -0.1929 |                     0.4383 |                 0.0290 |                  1 |
| cash_mode             |             1.5874 |                        -0.1252 |            -0.2024 |                     0.3260 |                -0.2857 |                  1 |

## Best Out-Of-Sample Combinations

| policy                | base_model      |   base_portfolio_size | period        |   months |   bear_months |   avg_exposure |   total_return |   bist100_total_return |   excess_return_vs_bist100 |   max_drawdown |   bist100_max_drawdown |   win_rate |   robustness_score |
|:----------------------|:----------------|----------------------:|:--------------|---------:|--------------:|---------------:|---------------:|-----------------------:|---------------------------:|---------------:|-----------------------:|-----------:|-------------------:|
| baseline              | momentum_heavy  |                     3 | out_of_sample |       32 |             7 |         1.0000 |         0.7899 |                 0.6755 |                     0.1145 |        -0.1660 |                -0.1675 |     0.6250 |             0.0949 |
| baseline              | mixed_model     |                    15 | out_of_sample |       32 |             7 |         1.0000 |         0.7471 |                 0.6755 |                     0.0716 |        -0.1644 |                -0.1675 |     0.6250 |             0.0553 |
| baseline              | momentum_heavy  |                    15 | out_of_sample |       32 |             7 |         1.0000 |         0.7430 |                 0.6755 |                     0.0675 |        -0.1680 |                -0.1675 |     0.6250 |             0.0440 |
| baseline              | trend_following |                    15 | out_of_sample |       32 |             7 |         1.0000 |         0.7179 |                 0.6755 |                     0.0424 |        -0.1747 |                -0.1675 |     0.6250 |             0.0056 |
| baseline              | low_volatility  |                    15 | out_of_sample |       32 |             7 |         1.0000 |         0.6926 |                 0.6755 |                     0.0172 |        -0.1563 |                -0.1675 |     0.5938 |             0.0014 |
| defensive_mode        | momentum_heavy  |                     3 | out_of_sample |       32 |             7 |         1.0000 |         0.6699 |                 0.6755 |                    -0.0056 |        -0.1660 |                -0.1675 |     0.5938 |            -0.0408 |
| baseline              | volume_heavy    |                    15 | out_of_sample |       32 |             7 |         1.0000 |         0.6629 |                 0.6755 |                    -0.0125 |        -0.1746 |                -0.1675 |     0.6250 |            -0.0492 |
| reduced_exposure_mode | momentum_heavy  |                     3 | out_of_sample |       32 |             7 |         0.8906 |         0.6422 |                 0.6755 |                    -0.0333 |        -0.1660 |                -0.1675 |     0.6250 |            -0.0529 |
| baseline              | trend_following |                     3 | out_of_sample |       32 |             7 |         1.0000 |         0.6358 |                 0.6755 |                    -0.0396 |        -0.1767 |                -0.1675 |     0.6250 |            -0.0805 |
| defensive_mode        | mixed_model     |                    15 | out_of_sample |       32 |             7 |         1.0000 |         0.6369 |                 0.6755 |                    -0.0385 |        -0.1757 |                -0.1675 |     0.5625 |            -0.1086 |

## Regime Signal Coverage

- Total signal months: 96
- BIST100 below MA200 months: 19
- Below-MA200 rate: 19.79%
