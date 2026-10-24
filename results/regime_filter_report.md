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
| baseline              |             2.0270 |                         0.4368 |            -0.1916 |                     0.3136 |                 0.3564 |                  1 |
| defensive_mode        |             1.9495 |                         0.3592 |            -0.1943 |                     0.2361 |                 0.2658 |                  1 |
| reduced_exposure_mode |             1.7562 |                         0.1659 |            -0.1933 |                     0.2583 |                 0.0821 |                  1 |
| cash_mode             |             1.5441 |                        -0.0462 |            -0.2027 |                     0.1960 |                -0.2150 |                  1 |

## Best Out-Of-Sample Combinations

| policy                | base_model      |   base_portfolio_size | period        |   months |   bear_months |   avg_exposure |   total_return |   bist100_total_return |   excess_return_vs_bist100 |   max_drawdown |   bist100_max_drawdown |   win_rate |   robustness_score |
|:----------------------|:----------------|----------------------:|:--------------|---------:|--------------:|---------------:|---------------:|-----------------------:|---------------------------:|---------------:|-----------------------:|-----------:|-------------------:|
| baseline              | mixed_model     |                    15 | out_of_sample |       33 |             8 |         1.0000 |         0.4932 |                 0.3084 |                     0.1849 |        -0.1644 |                -0.2303 |     0.5758 |             0.1438 |
| baseline              | momentum_heavy  |                    15 | out_of_sample |       33 |             8 |         1.0000 |         0.4692 |                 0.3084 |                     0.1608 |        -0.1680 |                -0.2303 |     0.5758 |             0.1127 |
| baseline              | momentum_heavy  |                     3 | out_of_sample |       33 |             8 |         1.0000 |         0.4765 |                 0.3084 |                     0.1681 |        -0.1660 |                -0.2303 |     0.5455 |             0.1088 |
| baseline              | trend_following |                    15 | out_of_sample |       33 |             8 |         1.0000 |         0.4683 |                 0.3084 |                     0.1599 |        -0.1747 |                -0.2303 |     0.5758 |             0.0984 |
| baseline              | low_volatility  |                    15 | out_of_sample |       33 |             8 |         1.0000 |         0.4402 |                 0.3084 |                     0.1318 |        -0.1725 |                -0.2303 |     0.5455 |             0.0595 |
| reduced_exposure_mode | momentum_heavy  |                     3 | out_of_sample |       33 |             8 |         0.8788 |         0.4154 |                 0.3084 |                     0.1070 |        -0.1660 |                -0.2303 |     0.5455 |             0.0477 |
| baseline              | trend_following |                     3 | out_of_sample |       33 |             8 |         1.0000 |         0.4107 |                 0.3084 |                     0.1023 |        -0.1767 |                -0.2303 |     0.5758 |             0.0368 |
| reduced_exposure_mode | mixed_model     |                    15 | out_of_sample |       33 |             8 |         0.8788 |         0.4045 |                 0.3084 |                     0.0961 |        -0.1817 |                -0.2303 |     0.5758 |             0.0207 |
| baseline              | volume_heavy    |                    15 | out_of_sample |       33 |             8 |         1.0000 |         0.3780 |                 0.3084 |                     0.0696 |        -0.1746 |                -0.2303 |     0.5758 |             0.0084 |
| defensive_mode        | momentum_heavy  |                     3 | out_of_sample |       33 |             8 |         1.0000 |         0.3901 |                 0.3084 |                     0.0817 |        -0.1660 |                -0.2303 |     0.5152 |             0.0072 |

## Regime Signal Coverage

- Total signal months: 97
- BIST100 below MA200 months: 21
- Below-MA200 rate: 21.65%
