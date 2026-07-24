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
| baseline              |             2.0735 |                         0.3670 |            -0.1902 |                     0.4528 |                 0.2939 |                  1 |
| defensive_mode        |             2.0001 |                         0.2937 |            -0.1901 |                     0.3881 |                 0.2129 |                  1 |
| reduced_exposure_mode |             1.7863 |                         0.0799 |            -0.1929 |                     0.3488 |                 0.0014 |                  1 |
| cash_mode             |             1.5600 |                        -0.1464 |            -0.2024 |                     0.2438 |                -0.3125 |                  1 |

## Best Out-Of-Sample Combinations

| policy                | base_model      |   base_portfolio_size | period        |   months |   bear_months |   avg_exposure |   total_return |   bist100_total_return |   excess_return_vs_bist100 |   max_drawdown |   bist100_max_drawdown |   win_rate |   robustness_score |
|:----------------------|:----------------|----------------------:|:--------------|---------:|--------------:|---------------:|---------------:|-----------------------:|---------------------------:|---------------:|-----------------------:|-----------:|-------------------:|
| baseline              | momentum_heavy  |                    15 | out_of_sample |       30 |             7 |         1.0000 |         0.6794 |                 0.6569 |                     0.0225 |        -0.1680 |                -0.1675 |     0.6333 |             0.0032 |
| baseline              | mixed_model     |                    15 | out_of_sample |       30 |             7 |         1.0000 |         0.6645 |                 0.6569 |                     0.0076 |        -0.1644 |                -0.1675 |     0.6000 |            -0.0212 |
| baseline              | trend_following |                    15 | out_of_sample |       30 |             7 |         1.0000 |         0.6523 |                 0.6569 |                    -0.0045 |        -0.1747 |                -0.1675 |     0.6333 |            -0.0372 |
| baseline              | low_volatility  |                    15 | out_of_sample |       30 |             7 |         1.0000 |         0.6438 |                 0.6569 |                    -0.0131 |        -0.1563 |                -0.1675 |     0.5667 |            -0.0424 |
| baseline              | momentum_heavy  |                     3 | out_of_sample |       30 |             7 |         1.0000 |         0.6013 |                 0.6569 |                    -0.0555 |        -0.1660 |                -0.1675 |     0.6000 |            -0.0876 |
| baseline              | volume_heavy    |                    15 | out_of_sample |       30 |             7 |         1.0000 |         0.5843 |                 0.6569 |                    -0.0726 |        -0.1746 |                -0.1675 |     0.6000 |            -0.1217 |
| defensive_mode        | momentum_heavy  |                    15 | out_of_sample |       30 |             7 |         1.0000 |         0.5696 |                 0.6569 |                    -0.0873 |        -0.1792 |                -0.1675 |     0.5667 |            -0.1623 |
| reduced_exposure_mode | momentum_heavy  |                    15 | out_of_sample |       30 |             7 |         0.8833 |         0.5416 |                 0.6569 |                    -0.1152 |        -0.1851 |                -0.1675 |     0.6333 |            -0.1688 |
| defensive_mode        | mixed_model     |                    15 | out_of_sample |       30 |             7 |         1.0000 |         0.5595 |                 0.6569 |                    -0.0973 |        -0.1757 |                -0.1675 |     0.5333 |            -0.1820 |
| defensive_mode        | low_volatility  |                    15 | out_of_sample |       30 |             7 |         1.0000 |         0.5331 |                 0.6569 |                    -0.1238 |        -0.1661 |                -0.1675 |     0.5333 |            -0.1892 |

## Regime Signal Coverage

- Total signal months: 94
- BIST100 below MA200 months: 19
- Below-MA200 rate: 20.21%
