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
| baseline              |             2.0902 |                         0.3683 |            -0.1902 |                     0.5030 |                 0.2968 |                  1 |
| defensive_mode        |             2.0160 |                         0.2941 |            -0.1901 |                     0.4357 |                 0.2150 |                  1 |
| reduced_exposure_mode |             1.8018 |                         0.0799 |            -0.1929 |                     0.3952 |                 0.0030 |                  1 |
| cash_mode             |             1.5742 |                        -0.1477 |            -0.2024 |                     0.2864 |                -0.3114 |                  1 |

## Best Out-Of-Sample Combinations

| policy                | base_model      |   base_portfolio_size | period        |   months |   bear_months |   avg_exposure |   total_return |   bist100_total_return |   excess_return_vs_bist100 |   max_drawdown |   bist100_max_drawdown |   win_rate |   robustness_score |
|:----------------------|:----------------|----------------------:|:--------------|---------:|--------------:|---------------:|---------------:|-----------------------:|---------------------------:|---------------:|-----------------------:|-----------:|-------------------:|
| baseline              | momentum_heavy  |                     3 | out_of_sample |       31 |             7 |         1.0000 |         0.7076 |                 0.7034 |                     0.0041 |        -0.1660 |                -0.1675 |     0.6129 |            -0.0215 |
| baseline              | mixed_model     |                    15 | out_of_sample |       31 |             7 |         1.0000 |         0.6827 |                 0.7034 |                    -0.0207 |        -0.1644 |                -0.1675 |     0.6129 |            -0.0432 |
| baseline              | momentum_heavy  |                    15 | out_of_sample |       31 |             7 |         1.0000 |         0.6817 |                 0.7034 |                    -0.0218 |        -0.1680 |                -0.1675 |     0.6129 |            -0.0513 |
| baseline              | low_volatility  |                    15 | out_of_sample |       31 |             7 |         1.0000 |         0.6548 |                 0.7034 |                    -0.0487 |        -0.1563 |                -0.1675 |     0.5806 |            -0.0710 |
| baseline              | trend_following |                    15 | out_of_sample |       31 |             7 |         1.0000 |         0.6545 |                 0.7034 |                    -0.0489 |        -0.1747 |                -0.1675 |     0.6129 |            -0.0917 |
| baseline              | volume_heavy    |                    15 | out_of_sample |       31 |             7 |         1.0000 |         0.5993 |                 0.7034 |                    -0.1041 |        -0.1746 |                -0.1675 |     0.6129 |            -0.1467 |
| defensive_mode        | momentum_heavy  |                     3 | out_of_sample |       31 |             7 |         1.0000 |         0.5930 |                 0.7034 |                    -0.1104 |        -0.1660 |                -0.1675 |     0.5806 |            -0.1521 |
| reduced_exposure_mode | momentum_heavy  |                     3 | out_of_sample |       31 |             7 |         0.8871 |         0.5666 |                 0.7034 |                    -0.1368 |        -0.1660 |                -0.1675 |     0.6129 |            -0.1624 |
| baseline              | trend_following |                     3 | out_of_sample |       31 |             7 |         1.0000 |         0.5605 |                 0.7034 |                    -0.1429 |        -0.1767 |                -0.1675 |     0.6129 |            -0.1898 |
| defensive_mode        | mixed_model     |                    15 | out_of_sample |       31 |             7 |         1.0000 |         0.5766 |                 0.7034 |                    -0.1268 |        -0.1757 |                -0.1675 |     0.5484 |            -0.2040 |

## Regime Signal Coverage

- Total signal months: 95
- BIST100 below MA200 months: 19
- Below-MA200 rate: 20.00%
