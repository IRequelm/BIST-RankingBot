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
| baseline              |             2.0646 |                         0.4350 |            -0.1904 |                     0.4262 |                 0.3618 |                  1 |
| defensive_mode        |             1.9861 |                         0.3566 |            -0.1904 |                     0.3461 |                 0.2761 |                  1 |
| reduced_exposure_mode |             1.7736 |                         0.1440 |            -0.1932 |                     0.3105 |                 0.0652 |                  1 |
| cash_mode             |             1.5441 |                        -0.0855 |            -0.2027 |                     0.1960 |                -0.2542 |                  1 |

## Best Out-Of-Sample Combinations

| policy                | base_model      |   base_portfolio_size | period        |   months |   bear_months |   avg_exposure |   total_return |   bist100_total_return |   excess_return_vs_bist100 |   max_drawdown |   bist100_max_drawdown |   win_rate |   robustness_score |
|:----------------------|:----------------|----------------------:|:--------------|---------:|--------------:|---------------:|---------------:|-----------------------:|---------------------------:|---------------:|-----------------------:|-----------:|-------------------:|
| baseline              | mixed_model     |                    15 | out_of_sample |       33 |             8 |         1.0000 |         0.6062 |                 0.4262 |                     0.1800 |        -0.1644 |                -0.1728 |     0.6061 |             0.1541 |
| baseline              | momentum_heavy  |                     3 | out_of_sample |       33 |             8 |         1.0000 |         0.6206 |                 0.4262 |                     0.1944 |        -0.1660 |                -0.1728 |     0.5758 |             0.1502 |
| baseline              | momentum_heavy  |                    15 | out_of_sample |       33 |             8 |         1.0000 |         0.5803 |                 0.4262 |                     0.1541 |        -0.1680 |                -0.1728 |     0.6061 |             0.1211 |
| baseline              | trend_following |                    15 | out_of_sample |       33 |             8 |         1.0000 |         0.5793 |                 0.4262 |                     0.1531 |        -0.1747 |                -0.1728 |     0.6061 |             0.1068 |
| baseline              | low_volatility  |                    15 | out_of_sample |       33 |             8 |         1.0000 |         0.5492 |                 0.4262 |                     0.1230 |        -0.1563 |                -0.1728 |     0.5758 |             0.0982 |
| baseline              | trend_following |                     3 | out_of_sample |       33 |             8 |         1.0000 |         0.5484 |                 0.4262 |                     0.1221 |        -0.1767 |                -0.1728 |     0.6061 |             0.0718 |
| defensive_mode        | momentum_heavy  |                     3 | out_of_sample |       33 |             8 |         1.0000 |         0.5137 |                 0.4262 |                     0.0875 |        -0.1660 |                -0.1728 |     0.5455 |             0.0282 |
| baseline              | volume_heavy    |                    15 | out_of_sample |       33 |             8 |         1.0000 |         0.4879 |                 0.4262 |                     0.0617 |        -0.1746 |                -0.1728 |     0.6061 |             0.0156 |
| reduced_exposure_mode | momentum_heavy  |                     3 | out_of_sample |       33 |             8 |         0.8788 |         0.4815 |                 0.4262 |                     0.0553 |        -0.1660 |                -0.1728 |     0.5758 |             0.0111 |
| defensive_mode        | mixed_model     |                    15 | out_of_sample |       33 |             8 |         1.0000 |         0.4767 |                 0.4262 |                     0.0505 |        -0.1757 |                -0.1728 |     0.5455 |            -0.0281 |

## Regime Signal Coverage

- Total signal months: 97
- BIST100 below MA200 months: 21
- Below-MA200 rate: 21.65%
