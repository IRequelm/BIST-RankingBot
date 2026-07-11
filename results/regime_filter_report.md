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
| baseline              |             2.0666 |                         0.3506 |            -0.1902 |                     0.4322 |                 0.2764 |                  1 |
| defensive_mode        |             1.9937 |                         0.2777 |            -0.1901 |                     0.3687 |                 0.1958 |                  1 |
| reduced_exposure_mode |             1.7800 |                         0.0640 |            -0.1929 |                     0.3298 |                -0.0156 |                  1 |
| cash_mode             |             1.5542 |                        -0.1618 |            -0.2024 |                     0.2264 |                -0.3290 |                  1 |

## Best Out-Of-Sample Combinations

| policy                | base_model      |   base_portfolio_size | period        |   months |   bear_months |   avg_exposure |   total_return |   bist100_total_return |   excess_return_vs_bist100 |   max_drawdown |   bist100_max_drawdown |   win_rate |   robustness_score |
|:----------------------|:----------------|----------------------:|:--------------|---------:|--------------:|---------------:|---------------:|-----------------------:|---------------------------:|---------------:|-----------------------:|-----------:|-------------------:|
| baseline              | mixed_model     |                    15 | out_of_sample |       30 |             7 |         1.0000 |         0.6225 |                 0.6855 |                    -0.0630 |        -0.1644 |                -0.1675 |     0.6000 |            -0.0919 |
| baseline              | momentum_heavy  |                    15 | out_of_sample |       30 |             7 |         1.0000 |         0.6198 |                 0.6855 |                    -0.0657 |        -0.1680 |                -0.1675 |     0.6000 |            -0.1017 |
| baseline              | low_volatility  |                    15 | out_of_sample |       30 |             7 |         1.0000 |         0.6034 |                 0.6855 |                    -0.0821 |        -0.1563 |                -0.1675 |     0.5667 |            -0.1114 |
| baseline              | momentum_heavy  |                     3 | out_of_sample |       30 |             7 |         1.0000 |         0.5965 |                 0.6855 |                    -0.0891 |        -0.1660 |                -0.1675 |     0.6000 |            -0.1211 |
| baseline              | trend_following |                    15 | out_of_sample |       30 |             7 |         1.0000 |         0.5937 |                 0.6855 |                    -0.0918 |        -0.1747 |                -0.1675 |     0.6000 |            -0.1411 |
| baseline              | volume_heavy    |                    15 | out_of_sample |       30 |             7 |         1.0000 |         0.5443 |                 0.6855 |                    -0.1412 |        -0.1746 |                -0.1675 |     0.6000 |            -0.1903 |
| defensive_mode        | momentum_heavy  |                     3 | out_of_sample |       30 |             7 |         1.0000 |         0.4894 |                 0.6855 |                    -0.1961 |        -0.1660 |                -0.1675 |     0.5667 |            -0.2449 |
| defensive_mode        | mixed_model     |                    15 | out_of_sample |       30 |             7 |         1.0000 |         0.5202 |                 0.6855 |                    -0.1653 |        -0.1757 |                -0.1675 |     0.5333 |            -0.2500 |
| reduced_exposure_mode | momentum_heavy  |                     3 | out_of_sample |       30 |             7 |         0.8833 |         0.4647 |                 0.6855 |                    -0.2208 |        -0.1660 |                -0.1675 |     0.6000 |            -0.2529 |
| defensive_mode        | low_volatility  |                    15 | out_of_sample |       30 |             7 |         1.0000 |         0.4954 |                 0.6855 |                    -0.1901 |        -0.1661 |                -0.1675 |     0.5333 |            -0.2556 |

## Regime Signal Coverage

- Total signal months: 94
- BIST100 below MA200 months: 19
- Below-MA200 rate: 20.21%
