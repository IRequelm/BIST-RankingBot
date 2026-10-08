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
| baseline              |             2.0707 |                         0.4410 |            -0.1902 |                     0.4446 |                 0.3689 |                  1 |
| defensive_mode        |             1.9926 |                         0.3629 |            -0.1901 |                     0.3656 |                 0.2835 |                  1 |
| reduced_exposure_mode |             1.7794 |                         0.1497 |            -0.1929 |                     0.3279 |                 0.0722 |                  1 |
| cash_mode             |             1.5495 |                        -0.0802 |            -0.2024 |                     0.2122 |                -0.2480 |                  1 |

## Best Out-Of-Sample Combinations

| policy                | base_model      |   base_portfolio_size | period        |   months |   bear_months |   avg_exposure |   total_return |   bist100_total_return |   excess_return_vs_bist100 |   max_drawdown |   bist100_max_drawdown |   win_rate |   robustness_score |
|:----------------------|:----------------|----------------------:|:--------------|---------:|--------------:|---------------:|---------------:|-----------------------:|---------------------------:|---------------:|-----------------------:|-----------:|-------------------:|
| baseline              | momentum_heavy  |                     3 | out_of_sample |       33 |             8 |         1.0000 |         0.6848 |                 0.4268 |                     0.2580 |        -0.1660 |                -0.1728 |     0.6061 |             0.2290 |
| baseline              | mixed_model     |                    15 | out_of_sample |       33 |             8 |         1.0000 |         0.6211 |                 0.4268 |                     0.1943 |        -0.1644 |                -0.1728 |     0.6061 |             0.1684 |
| baseline              | momentum_heavy  |                    15 | out_of_sample |       33 |             8 |         1.0000 |         0.6167 |                 0.4268 |                     0.1899 |        -0.1680 |                -0.1728 |     0.6061 |             0.1569 |
| baseline              | trend_following |                    15 | out_of_sample |       33 |             8 |         1.0000 |         0.5940 |                 0.4268 |                     0.1672 |        -0.1747 |                -0.1728 |     0.6061 |             0.1209 |
| defensive_mode        | momentum_heavy  |                     3 | out_of_sample |       33 |             8 |         1.0000 |         0.5840 |                 0.4268 |                     0.1572 |        -0.1660 |                -0.1728 |     0.5758 |             0.1130 |
| baseline              | low_volatility  |                    15 | out_of_sample |       33 |             8 |         1.0000 |         0.5644 |                 0.4268 |                     0.1376 |        -0.1563 |                -0.1728 |     0.5758 |             0.1129 |
| reduced_exposure_mode | momentum_heavy  |                     3 | out_of_sample |       33 |             8 |         0.8788 |         0.5445 |                 0.4268 |                     0.1177 |        -0.1660 |                -0.1728 |     0.6061 |             0.0887 |
| baseline              | trend_following |                     3 | out_of_sample |       33 |             8 |         1.0000 |         0.5398 |                 0.4268 |                     0.1130 |        -0.1767 |                -0.1728 |     0.6061 |             0.0626 |
| baseline              | volume_heavy    |                    15 | out_of_sample |       33 |             8 |         1.0000 |         0.5314 |                 0.4268 |                     0.1046 |        -0.1746 |                -0.1728 |     0.6061 |             0.0586 |
| reduced_exposure_mode | mixed_model     |                    15 | out_of_sample |       33 |             8 |         0.8788 |         0.4633 |                 0.4268 |                     0.0365 |        -0.1817 |                -0.1728 |     0.6061 |            -0.0238 |

## Regime Signal Coverage

- Total signal months: 97
- BIST100 below MA200 months: 21
- Below-MA200 rate: 21.65%
