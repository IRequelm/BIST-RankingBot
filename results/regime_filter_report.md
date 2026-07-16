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
| baseline              |             2.0688 |                         0.3623 |            -0.1902 |                     0.4388 |                 0.2883 |                  1 |
| defensive_mode        |             1.9957 |                         0.2892 |            -0.1901 |                     0.3749 |                 0.2076 |                  1 |
| reduced_exposure_mode |             1.7820 |                         0.0755 |            -0.1929 |                     0.3358 |                -0.0038 |                  1 |
| cash_mode             |             1.5561 |                        -0.1505 |            -0.2024 |                     0.2319 |                -0.3174 |                  1 |

## Best Out-Of-Sample Combinations

| policy                | base_model      |   base_portfolio_size | period        |   months |   bear_months |   avg_exposure |   total_return |   bist100_total_return |   excess_return_vs_bist100 |   max_drawdown |   bist100_max_drawdown |   win_rate |   robustness_score |
|:----------------------|:----------------|----------------------:|:--------------|---------:|--------------:|---------------:|---------------:|-----------------------:|---------------------------:|---------------:|-----------------------:|-----------:|-------------------:|
| baseline              | mixed_model     |                    15 | out_of_sample |       30 |             7 |         1.0000 |         0.6335 |                 0.6571 |                    -0.0237 |        -0.1644 |                -0.1675 |     0.6000 |            -0.0526 |
| baseline              | momentum_heavy  |                    15 | out_of_sample |       30 |             7 |         1.0000 |         0.6339 |                 0.6571 |                    -0.0233 |        -0.1680 |                -0.1675 |     0.6000 |            -0.0593 |
| baseline              | low_volatility  |                    15 | out_of_sample |       30 |             7 |         1.0000 |         0.6192 |                 0.6571 |                    -0.0379 |        -0.1563 |                -0.1675 |     0.5667 |            -0.0673 |
| baseline              | momentum_heavy  |                     3 | out_of_sample |       30 |             7 |         1.0000 |         0.6004 |                 0.6571 |                    -0.0567 |        -0.1660 |                -0.1675 |     0.6000 |            -0.0888 |
| baseline              | trend_following |                    15 | out_of_sample |       30 |             7 |         1.0000 |         0.6075 |                 0.6571 |                    -0.0496 |        -0.1747 |                -0.1675 |     0.6000 |            -0.0989 |
| baseline              | volume_heavy    |                    15 | out_of_sample |       30 |             7 |         1.0000 |         0.5547 |                 0.6571 |                    -0.1024 |        -0.1746 |                -0.1675 |     0.6000 |            -0.1515 |
| defensive_mode        | mixed_model     |                    15 | out_of_sample |       30 |             7 |         1.0000 |         0.5305 |                 0.6571 |                    -0.1267 |        -0.1757 |                -0.1675 |     0.5333 |            -0.2114 |
| defensive_mode        | low_volatility  |                    15 | out_of_sample |       30 |             7 |         1.0000 |         0.5101 |                 0.6571 |                    -0.1470 |        -0.1661 |                -0.1675 |     0.5333 |            -0.2125 |
| defensive_mode        | momentum_heavy  |                     3 | out_of_sample |       30 |             7 |         1.0000 |         0.4931 |                 0.6571 |                    -0.1640 |        -0.1660 |                -0.1675 |     0.5667 |            -0.2128 |
| reduced_exposure_mode | mixed_model     |                    15 | out_of_sample |       30 |             7 |         0.8833 |         0.5014 |                 0.6571 |                    -0.1558 |        -0.1817 |                -0.1675 |     0.6000 |            -0.2191 |

## Regime Signal Coverage

- Total signal months: 94
- BIST100 below MA200 months: 19
- Below-MA200 rate: 20.21%
