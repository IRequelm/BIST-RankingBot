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
| baseline              |             2.0609 |                         0.4301 |            -0.1904 |                     0.4152 |                 0.3562 |                  1 |
| defensive_mode        |             1.9851 |                         0.3543 |            -0.1904 |                     0.3429 |                 0.2738 |                  1 |
| reduced_exposure_mode |             1.7719 |                         0.1411 |            -0.1932 |                     0.3054 |                 0.0615 |                  1 |
| cash_mode             |             1.5441 |                        -0.0867 |            -0.2027 |                     0.1960 |                -0.2555 |                  1 |

## Best Out-Of-Sample Combinations

| policy                | base_model      |   base_portfolio_size | period        |   months |   bear_months |   avg_exposure |   total_return |   bist100_total_return |   excess_return_vs_bist100 |   max_drawdown |   bist100_max_drawdown |   win_rate |   robustness_score |
|:----------------------|:----------------|----------------------:|:--------------|---------:|--------------:|---------------:|---------------:|-----------------------:|---------------------------:|---------------:|-----------------------:|-----------:|-------------------:|
| baseline              | mixed_model     |                    15 | out_of_sample |       33 |             8 |         1.0000 |         0.5964 |                 0.4301 |                     0.1663 |        -0.1644 |                -0.1728 |     0.6061 |             0.1405 |
| baseline              | momentum_heavy  |                     3 | out_of_sample |       33 |             8 |         1.0000 |         0.5989 |                 0.4301 |                     0.1688 |        -0.1660 |                -0.1728 |     0.5455 |             0.1094 |
| baseline              | momentum_heavy  |                    15 | out_of_sample |       33 |             8 |         1.0000 |         0.5707 |                 0.4301 |                     0.1406 |        -0.1680 |                -0.1728 |     0.6061 |             0.1076 |
| baseline              | trend_following |                    15 | out_of_sample |       33 |             8 |         1.0000 |         0.5697 |                 0.4301 |                     0.1396 |        -0.1747 |                -0.1728 |     0.6061 |             0.0933 |
| baseline              | low_volatility  |                    15 | out_of_sample |       33 |             8 |         1.0000 |         0.5434 |                 0.4301 |                     0.1133 |        -0.1563 |                -0.1728 |     0.5758 |             0.0885 |
| baseline              | trend_following |                     3 | out_of_sample |       33 |             8 |         1.0000 |         0.5276 |                 0.4301 |                     0.0975 |        -0.1767 |                -0.1728 |     0.5758 |             0.0320 |
| defensive_mode        | momentum_heavy  |                     3 | out_of_sample |       33 |             8 |         1.0000 |         0.5102 |                 0.4301 |                     0.0802 |        -0.1660 |                -0.1728 |     0.5455 |             0.0208 |
| baseline              | volume_heavy    |                    15 | out_of_sample |       33 |             8 |         1.0000 |         0.4815 |                 0.4301 |                     0.0514 |        -0.1746 |                -0.1728 |     0.6061 |             0.0053 |
| reduced_exposure_mode | momentum_heavy  |                     3 | out_of_sample |       33 |             8 |         0.8788 |         0.4715 |                 0.4301 |                     0.0415 |        -0.1660 |                -0.1728 |     0.5455 |            -0.0179 |
| defensive_mode        | mixed_model     |                    15 | out_of_sample |       33 |             8 |         1.0000 |         0.4733 |                 0.4301 |                     0.0433 |        -0.1757 |                -0.1728 |     0.5455 |            -0.0354 |

## Regime Signal Coverage

- Total signal months: 97
- BIST100 below MA200 months: 21
- Below-MA200 rate: 21.65%
