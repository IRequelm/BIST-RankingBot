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
| baseline              |             2.0638 |                         0.4285 |            -0.1904 |                     0.4239 |                 0.3553 |                  1 |
| defensive_mode        |             1.9859 |                         0.3506 |            -0.1904 |                     0.3455 |                 0.2701 |                  1 |
| reduced_exposure_mode |             1.7732 |                         0.1379 |            -0.1932 |                     0.3094 |                 0.0590 |                  1 |
| cash_mode             |             1.5441 |                        -0.0913 |            -0.2027 |                     0.1960 |                -0.2600 |                  1 |

## Best Out-Of-Sample Combinations

| policy                | base_model      |   base_portfolio_size | period        |   months |   bear_months |   avg_exposure |   total_return |   bist100_total_return |   excess_return_vs_bist100 |   max_drawdown |   bist100_max_drawdown |   win_rate |   robustness_score |
|:----------------------|:----------------|----------------------:|:--------------|---------:|--------------:|---------------:|---------------:|-----------------------:|---------------------------:|---------------:|-----------------------:|-----------:|-------------------:|
| baseline              | mixed_model     |                    15 | out_of_sample |       33 |             8 |         1.0000 |         0.6055 |                 0.4436 |                     0.1619 |        -0.1644 |                -0.1728 |     0.6061 |             0.1360 |
| baseline              | momentum_heavy  |                     3 | out_of_sample |       33 |             8 |         1.0000 |         0.6165 |                 0.4436 |                     0.1729 |        -0.1660 |                -0.1728 |     0.5758 |             0.1287 |
| baseline              | momentum_heavy  |                    15 | out_of_sample |       33 |             8 |         1.0000 |         0.5796 |                 0.4436 |                     0.1360 |        -0.1680 |                -0.1728 |     0.6061 |             0.1030 |
| baseline              | trend_following |                    15 | out_of_sample |       33 |             8 |         1.0000 |         0.5786 |                 0.4436 |                     0.1350 |        -0.1747 |                -0.1728 |     0.6061 |             0.0887 |
| baseline              | low_volatility  |                    15 | out_of_sample |       33 |             8 |         1.0000 |         0.5542 |                 0.4436 |                     0.1105 |        -0.1563 |                -0.1728 |     0.5758 |             0.0858 |
| baseline              | trend_following |                     3 | out_of_sample |       33 |             8 |         1.0000 |         0.5444 |                 0.4436 |                     0.1008 |        -0.1767 |                -0.1728 |     0.6061 |             0.0504 |
| defensive_mode        | momentum_heavy  |                     3 | out_of_sample |       33 |             8 |         1.0000 |         0.5131 |                 0.4436 |                     0.0694 |        -0.1660 |                -0.1728 |     0.5455 |             0.0101 |
| baseline              | volume_heavy    |                    15 | out_of_sample |       33 |             8 |         1.0000 |         0.4904 |                 0.4436 |                     0.0467 |        -0.1746 |                -0.1728 |     0.6061 |             0.0007 |
| reduced_exposure_mode | momentum_heavy  |                     3 | out_of_sample |       33 |             8 |         0.8788 |         0.4796 |                 0.4436 |                     0.0360 |        -0.1660 |                -0.1728 |     0.5758 |            -0.0082 |
| defensive_mode        | mixed_model     |                    15 | out_of_sample |       33 |             8 |         1.0000 |         0.4761 |                 0.4436 |                     0.0325 |        -0.1757 |                -0.1728 |     0.5455 |            -0.0462 |

## Regime Signal Coverage

- Total signal months: 97
- BIST100 below MA200 months: 21
- Below-MA200 rate: 21.65%
