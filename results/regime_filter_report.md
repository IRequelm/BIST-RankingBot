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
| baseline              |             2.0614 |                         0.4338 |            -0.1904 |                     0.4167 |                 0.3606 |                  1 |
| defensive_mode        |             1.9847 |                         0.3571 |            -0.1904 |                     0.3420 |                 0.2766 |                  1 |
| reduced_exposure_mode |             1.7721 |                         0.1445 |            -0.1932 |                     0.3061 |                 0.0656 |                  1 |
| cash_mode             |             1.5441 |                        -0.0836 |            -0.2027 |                     0.1960 |                -0.2523 |                  1 |

## Best Out-Of-Sample Combinations

| policy                | base_model      |   base_portfolio_size | period        |   months |   bear_months |   avg_exposure |   total_return |   bist100_total_return |   excess_return_vs_bist100 |   max_drawdown |   bist100_max_drawdown |   win_rate |   robustness_score |
|:----------------------|:----------------|----------------------:|:--------------|---------:|--------------:|---------------:|---------------:|-----------------------:|---------------------------:|---------------:|-----------------------:|-----------:|-------------------:|
| baseline              | momentum_heavy  |                     3 | out_of_sample |       33 |             8 |         1.0000 |         0.6206 |                 0.4206 |                     0.2000 |        -0.1660 |                -0.1728 |     0.5758 |             0.1558 |
| baseline              | mixed_model     |                    15 | out_of_sample |       33 |             8 |         1.0000 |         0.5882 |                 0.4206 |                     0.1676 |        -0.1644 |                -0.1728 |     0.6061 |             0.1417 |
| baseline              | momentum_heavy  |                    15 | out_of_sample |       33 |             8 |         1.0000 |         0.5626 |                 0.4206 |                     0.1420 |        -0.1680 |                -0.1728 |     0.6061 |             0.1091 |
| baseline              | trend_following |                    15 | out_of_sample |       33 |             8 |         1.0000 |         0.5616 |                 0.4206 |                     0.1410 |        -0.1747 |                -0.1728 |     0.6061 |             0.0948 |
| baseline              | low_volatility  |                    15 | out_of_sample |       33 |             8 |         1.0000 |         0.5293 |                 0.4206 |                     0.1087 |        -0.1563 |                -0.1728 |     0.5758 |             0.0839 |
| baseline              | trend_following |                     3 | out_of_sample |       33 |             8 |         1.0000 |         0.5483 |                 0.4206 |                     0.1278 |        -0.1767 |                -0.1728 |     0.6061 |             0.0774 |
| defensive_mode        | momentum_heavy  |                     3 | out_of_sample |       33 |             8 |         1.0000 |         0.5091 |                 0.4206 |                     0.0886 |        -0.1660 |                -0.1728 |     0.5455 |             0.0292 |
| reduced_exposure_mode | momentum_heavy  |                     3 | out_of_sample |       33 |             8 |         0.8788 |         0.4815 |                 0.4206 |                     0.0609 |        -0.1660 |                -0.1728 |     0.5758 |             0.0167 |
| baseline              | volume_heavy    |                    15 | out_of_sample |       33 |             8 |         1.0000 |         0.4697 |                 0.4206 |                     0.0491 |        -0.1746 |                -0.1728 |     0.6061 |             0.0031 |
| defensive_mode        | mixed_model     |                    15 | out_of_sample |       33 |             8 |         1.0000 |         0.4722 |                 0.4206 |                     0.0517 |        -0.1757 |                -0.1728 |     0.5455 |            -0.0270 |

## Regime Signal Coverage

- Total signal months: 97
- BIST100 below MA200 months: 21
- Below-MA200 rate: 21.65%
