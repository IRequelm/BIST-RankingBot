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
| baseline              |             2.0596 |                         0.3649 |            -0.1902 |                     0.4113 |                 0.2934 |                  1 |
| defensive_mode        |             1.9870 |                         0.2922 |            -0.1901 |                     0.3486 |                 0.2132 |                  1 |
| reduced_exposure_mode |             1.7735 |                         0.0788 |            -0.1929 |                     0.3103 |                 0.0019 |                  1 |
| cash_mode             |             1.5482 |                        -0.1465 |            -0.2024 |                     0.2084 |                -0.3102 |                  1 |

## Best Out-Of-Sample Combinations

| policy                | base_model      |   base_portfolio_size | period        |   months |   bear_months |   avg_exposure |   total_return |   bist100_total_return |   excess_return_vs_bist100 |   max_drawdown |   bist100_max_drawdown |   win_rate |   robustness_score |
|:----------------------|:----------------|----------------------:|:--------------|---------:|--------------:|---------------:|---------------:|-----------------------:|---------------------------:|---------------:|-----------------------:|-----------:|-------------------:|
| baseline              | mixed_model     |                    15 | out_of_sample |       31 |             7 |         1.0000 |         0.6093 |                 0.6217 |                    -0.0124 |        -0.1644 |                -0.1675 |     0.6129 |            -0.0349 |
| baseline              | momentum_heavy  |                    15 | out_of_sample |       31 |             7 |         1.0000 |         0.6083 |                 0.6217 |                    -0.0134 |        -0.1680 |                -0.1675 |     0.6129 |            -0.0430 |
| baseline              | low_volatility  |                    15 | out_of_sample |       31 |             7 |         1.0000 |         0.5935 |                 0.6217 |                    -0.0283 |        -0.1563 |                -0.1675 |     0.5806 |            -0.0506 |
| baseline              | momentum_heavy  |                     3 | out_of_sample |       31 |             7 |         1.0000 |         0.5706 |                 0.6217 |                    -0.0511 |        -0.1660 |                -0.1675 |     0.6129 |            -0.0767 |
| baseline              | trend_following |                    15 | out_of_sample |       31 |             7 |         1.0000 |         0.5824 |                 0.6217 |                    -0.0394 |        -0.1747 |                -0.1675 |     0.6129 |            -0.0822 |
| baseline              | volume_heavy    |                    15 | out_of_sample |       31 |             7 |         1.0000 |         0.5348 |                 0.6217 |                    -0.0870 |        -0.1746 |                -0.1675 |     0.6129 |            -0.1297 |
| defensive_mode        | mixed_model     |                    15 | out_of_sample |       31 |             7 |         1.0000 |         0.5078 |                 0.6217 |                    -0.1139 |        -0.1757 |                -0.1675 |     0.5484 |            -0.1911 |
| defensive_mode        | low_volatility  |                    15 | out_of_sample |       31 |             7 |         1.0000 |         0.4861 |                 0.6217 |                    -0.1356 |        -0.1661 |                -0.1675 |     0.5484 |            -0.1935 |
| defensive_mode        | momentum_heavy  |                     3 | out_of_sample |       31 |             7 |         1.0000 |         0.4653 |                 0.6217 |                    -0.1565 |        -0.1660 |                -0.1675 |     0.5806 |            -0.1982 |
| reduced_exposure_mode | mixed_model     |                    15 | out_of_sample |       31 |             7 |         0.8871 |         0.4792 |                 0.6217 |                    -0.1426 |        -0.1817 |                -0.1675 |     0.6129 |            -0.1994 |

## Regime Signal Coverage

- Total signal months: 95
- BIST100 below MA200 months: 19
- Below-MA200 rate: 20.00%
