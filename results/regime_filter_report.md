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
| baseline              |             2.0580 |                         0.4233 |            -0.1904 |                     0.4064 |                 0.3493 |                  1 |
| defensive_mode        |             1.9826 |                         0.3479 |            -0.1904 |                     0.3356 |                 0.2674 |                  1 |
| reduced_exposure_mode |             1.7705 |                         0.1358 |            -0.1932 |                     0.3014 |                 0.0562 |                  1 |
| cash_mode             |             1.5441 |                        -0.0907 |            -0.2027 |                     0.1960 |                -0.2594 |                  1 |

## Best Out-Of-Sample Combinations

| policy                | base_model      |   base_portfolio_size | period        |   months |   bear_months |   avg_exposure |   total_return |   bist100_total_return |   excess_return_vs_bist100 |   max_drawdown |   bist100_max_drawdown |   win_rate |   robustness_score |
|:----------------------|:----------------|----------------------:|:--------------|---------:|--------------:|---------------:|---------------:|-----------------------:|---------------------------:|---------------:|-----------------------:|-----------:|-------------------:|
| baseline              | mixed_model     |                    15 | out_of_sample |       33 |             8 |         1.0000 |         0.5865 |                 0.4418 |                     0.1447 |        -0.1644 |                -0.1728 |     0.6061 |             0.1188 |
| baseline              | momentum_heavy  |                    15 | out_of_sample |       33 |             8 |         1.0000 |         0.5609 |                 0.4418 |                     0.1191 |        -0.1680 |                -0.1728 |     0.6061 |             0.0862 |
| baseline              | momentum_heavy  |                     3 | out_of_sample |       33 |             8 |         1.0000 |         0.5859 |                 0.4418 |                     0.1440 |        -0.1660 |                -0.1728 |     0.5455 |             0.0847 |
| baseline              | trend_following |                    15 | out_of_sample |       33 |             8 |         1.0000 |         0.5600 |                 0.4418 |                     0.1181 |        -0.1747 |                -0.1728 |     0.6061 |             0.0719 |
| baseline              | low_volatility  |                    15 | out_of_sample |       33 |             8 |         1.0000 |         0.5354 |                 0.4418 |                     0.0936 |        -0.1563 |                -0.1728 |     0.5758 |             0.0688 |
| baseline              | trend_following |                     3 | out_of_sample |       33 |             8 |         1.0000 |         0.5152 |                 0.4418 |                     0.0733 |        -0.1767 |                -0.1728 |     0.5758 |             0.0078 |
| defensive_mode        | momentum_heavy  |                     3 | out_of_sample |       33 |             8 |         1.0000 |         0.5020 |                 0.4418 |                     0.0602 |        -0.1660 |                -0.1728 |     0.5455 |             0.0009 |
| baseline              | volume_heavy    |                    15 | out_of_sample |       33 |             8 |         1.0000 |         0.4737 |                 0.4418 |                     0.0319 |        -0.1746 |                -0.1728 |     0.6061 |            -0.0142 |
| reduced_exposure_mode | momentum_heavy  |                     3 | out_of_sample |       33 |             8 |         0.8788 |         0.4656 |                 0.4418 |                     0.0238 |        -0.1660 |                -0.1728 |     0.5455 |            -0.0356 |
| reduced_exposure_mode | mixed_model     |                    15 | out_of_sample |       33 |             8 |         0.8788 |         0.4474 |                 0.4418 |                     0.0056 |        -0.1817 |                -0.1728 |     0.6061 |            -0.0547 |

## Regime Signal Coverage

- Total signal months: 97
- BIST100 below MA200 months: 21
- Below-MA200 rate: 21.65%
