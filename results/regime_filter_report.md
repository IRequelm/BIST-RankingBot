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
| baseline              |             2.0582 |                         0.4249 |            -0.1904 |                     0.4069 |                 0.3504 |                  1 |
| defensive_mode        |             1.9795 |                         0.3462 |            -0.1904 |                     0.3261 |                 0.2606 |                  1 |
| reduced_exposure_mode |             1.7706 |                         0.1373 |            -0.1932 |                     0.3016 |                 0.0572 |                  1 |
| cash_mode             |             1.5441 |                        -0.0892 |            -0.2027 |                     0.1960 |                -0.2580 |                  1 |

## Best Out-Of-Sample Combinations

| policy                | base_model      |   base_portfolio_size | period        |   months |   bear_months |   avg_exposure |   total_return |   bist100_total_return |   excess_return_vs_bist100 |   max_drawdown |   bist100_max_drawdown |   win_rate |   robustness_score |
|:----------------------|:----------------|----------------------:|:--------------|---------:|--------------:|---------------:|---------------:|-----------------------:|---------------------------:|---------------:|-----------------------:|-----------:|-------------------:|
| baseline              | mixed_model     |                    15 | out_of_sample |       33 |             8 |         1.0000 |         0.5959 |                 0.4375 |                     0.1584 |        -0.1644 |                -0.1728 |     0.6061 |             0.1326 |
| baseline              | momentum_heavy  |                    15 | out_of_sample |       33 |             8 |         1.0000 |         0.5702 |                 0.4375 |                     0.1327 |        -0.1680 |                -0.1728 |     0.6061 |             0.0997 |
| baseline              | momentum_heavy  |                     3 | out_of_sample |       33 |             8 |         1.0000 |         0.5828 |                 0.4375 |                     0.1454 |        -0.1660 |                -0.1728 |     0.5455 |             0.0860 |
| baseline              | trend_following |                    15 | out_of_sample |       33 |             8 |         1.0000 |         0.5692 |                 0.4375 |                     0.1317 |        -0.1747 |                -0.1728 |     0.6061 |             0.0854 |
| baseline              | low_volatility  |                    15 | out_of_sample |       33 |             8 |         1.0000 |         0.5457 |                 0.4375 |                     0.1082 |        -0.1563 |                -0.1728 |     0.5758 |             0.0835 |
| baseline              | trend_following |                     3 | out_of_sample |       33 |             8 |         1.0000 |         0.5123 |                 0.4375 |                     0.0748 |        -0.1767 |                -0.1728 |     0.5758 |             0.0093 |
| baseline              | volume_heavy    |                    15 | out_of_sample |       33 |             8 |         1.0000 |         0.4809 |                 0.4375 |                     0.0435 |        -0.1746 |                -0.1728 |     0.6061 |            -0.0026 |
| defensive_mode        | momentum_heavy  |                     3 | out_of_sample |       33 |             8 |         1.0000 |         0.4913 |                 0.4375 |                     0.0538 |        -0.1660 |                -0.1728 |     0.5152 |            -0.0207 |
| reduced_exposure_mode | momentum_heavy  |                     3 | out_of_sample |       33 |             8 |         0.8788 |         0.4642 |                 0.4375 |                     0.0267 |        -0.1660 |                -0.1728 |     0.5455 |            -0.0326 |
| reduced_exposure_mode | mixed_model     |                    15 | out_of_sample |       33 |             8 |         0.8788 |         0.4517 |                 0.4375 |                     0.0142 |        -0.1817 |                -0.1728 |     0.6061 |            -0.0460 |

## Regime Signal Coverage

- Total signal months: 97
- BIST100 below MA200 months: 21
- Below-MA200 rate: 21.65%
