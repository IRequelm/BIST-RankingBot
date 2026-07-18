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
| baseline              |             2.0795 |                         0.3769 |            -0.1902 |                     0.4709 |                 0.3057 |                  1 |
| defensive_mode        |             2.0059 |                         0.3033 |            -0.1901 |                     0.4055 |                 0.2244 |                  1 |
| reduced_exposure_mode |             1.7919 |                         0.0893 |            -0.1929 |                     0.3656 |                 0.0128 |                  1 |
| cash_mode             |             1.5652 |                        -0.1374 |            -0.2024 |                     0.2593 |                -0.3016 |                  1 |

## Best Out-Of-Sample Combinations

| policy                | base_model      |   base_portfolio_size | period        |   months |   bear_months |   avg_exposure |   total_return |   bist100_total_return |   excess_return_vs_bist100 |   max_drawdown |   bist100_max_drawdown |   win_rate |   robustness_score |
|:----------------------|:----------------|----------------------:|:--------------|---------:|--------------:|---------------:|---------------:|-----------------------:|---------------------------:|---------------:|-----------------------:|-----------:|-------------------:|
| baseline              | mixed_model     |                    15 | out_of_sample |       30 |             7 |         1.0000 |         0.6701 |                 0.6455 |                     0.0247 |        -0.1644 |                -0.1675 |     0.6333 |             0.0124 |
| baseline              | momentum_heavy  |                    15 | out_of_sample |       30 |             7 |         1.0000 |         0.6719 |                 0.6455 |                     0.0264 |        -0.1680 |                -0.1675 |     0.6333 |             0.0071 |
| baseline              | low_volatility  |                    15 | out_of_sample |       30 |             7 |         1.0000 |         0.6553 |                 0.6455 |                     0.0098 |        -0.1563 |                -0.1675 |     0.6000 |            -0.0028 |
| baseline              | momentum_heavy  |                     3 | out_of_sample |       30 |             7 |         1.0000 |         0.6533 |                 0.6455 |                     0.0078 |        -0.1660 |                -0.1675 |     0.6333 |            -0.0076 |
| baseline              | trend_following |                    15 | out_of_sample |       30 |             7 |         1.0000 |         0.6449 |                 0.6455 |                    -0.0006 |        -0.1747 |                -0.1675 |     0.6333 |            -0.0332 |
| baseline              | volume_heavy    |                    15 | out_of_sample |       30 |             7 |         1.0000 |         0.5896 |                 0.6455 |                    -0.0558 |        -0.1746 |                -0.1675 |     0.6333 |            -0.0883 |
| defensive_mode        | momentum_heavy  |                     3 | out_of_sample |       30 |             7 |         1.0000 |         0.5424 |                 0.6455 |                    -0.1031 |        -0.1660 |                -0.1675 |     0.6000 |            -0.1352 |
| reduced_exposure_mode | momentum_heavy  |                     3 | out_of_sample |       30 |             7 |         0.8833 |         0.5168 |                 0.6455 |                    -0.1287 |        -0.1660 |                -0.1675 |     0.6333 |            -0.1441 |
| defensive_mode        | mixed_model     |                    15 | out_of_sample |       30 |             7 |         1.0000 |         0.5648 |                 0.6455 |                    -0.0807 |        -0.1757 |                -0.1675 |     0.5667 |            -0.1487 |
| defensive_mode        | low_volatility  |                    15 | out_of_sample |       30 |             7 |         1.0000 |         0.5438 |                 0.6455 |                    -0.1017 |        -0.1661 |                -0.1675 |     0.5667 |            -0.1504 |

## Regime Signal Coverage

- Total signal months: 94
- BIST100 below MA200 months: 19
- Below-MA200 rate: 20.21%
