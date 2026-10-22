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
| baseline              |             2.0482 |                         0.4399 |            -0.1904 |                     0.3769 |                 0.3624 |                  1 |
| defensive_mode        |             1.9680 |                         0.3597 |            -0.1907 |                     0.2917 |                 0.2735 |                  1 |
| reduced_exposure_mode |             1.7660 |                         0.1577 |            -0.1932 |                     0.2877 |                 0.0745 |                  1 |
| cash_mode             |             1.5441 |                        -0.0642 |            -0.2027 |                     0.1960 |                -0.2330 |                  1 |

## Best Out-Of-Sample Combinations

| policy                | base_model      |   base_portfolio_size | period        |   months |   bear_months |   avg_exposure |   total_return |   bist100_total_return |   excess_return_vs_bist100 |   max_drawdown |   bist100_max_drawdown |   win_rate |   robustness_score |
|:----------------------|:----------------|----------------------:|:--------------|---------:|--------------:|---------------:|---------------:|-----------------------:|---------------------------:|---------------:|-----------------------:|-----------:|-------------------:|
| baseline              | mixed_model     |                    15 | out_of_sample |       33 |             8 |         1.0000 |         0.5623 |                 0.3625 |                     0.1997 |        -0.1644 |                -0.1984 |     0.5758 |             0.1587 |
| baseline              | momentum_heavy  |                    15 | out_of_sample |       33 |             8 |         1.0000 |         0.5371 |                 0.3625 |                     0.1746 |        -0.1680 |                -0.1984 |     0.5758 |             0.1265 |
| baseline              | momentum_heavy  |                     3 | out_of_sample |       33 |             8 |         1.0000 |         0.5432 |                 0.3625 |                     0.1807 |        -0.1660 |                -0.1984 |     0.5455 |             0.1213 |
| baseline              | trend_following |                    15 | out_of_sample |       33 |             8 |         1.0000 |         0.5362 |                 0.3625 |                     0.1736 |        -0.1747 |                -0.1984 |     0.5758 |             0.1122 |
| baseline              | low_volatility  |                    15 | out_of_sample |       33 |             8 |         1.0000 |         0.5106 |                 0.3625 |                     0.1481 |        -0.1563 |                -0.1984 |     0.5455 |             0.1081 |
| baseline              | trend_following |                     3 | out_of_sample |       33 |             8 |         1.0000 |         0.4744 |                 0.3625 |                     0.1119 |        -0.1767 |                -0.1984 |     0.5758 |             0.0463 |
| reduced_exposure_mode | momentum_heavy  |                     3 | out_of_sample |       33 |             8 |         0.8788 |         0.4460 |                 0.3625 |                     0.0835 |        -0.1660 |                -0.1984 |     0.5455 |             0.0241 |
| baseline              | volume_heavy    |                    15 | out_of_sample |       33 |             8 |         1.0000 |         0.4471 |                 0.3625 |                     0.0845 |        -0.1746 |                -0.1984 |     0.5758 |             0.0233 |
| defensive_mode        | momentum_heavy  |                     3 | out_of_sample |       33 |             8 |         1.0000 |         0.4526 |                 0.3625 |                     0.0901 |        -0.1660 |                -0.1984 |     0.5152 |             0.0156 |
| reduced_exposure_mode | mixed_model     |                    15 | out_of_sample |       33 |             8 |         0.8788 |         0.4363 |                 0.3625 |                     0.0737 |        -0.1817 |                -0.1984 |     0.5758 |            -0.0017 |

## Regime Signal Coverage

- Total signal months: 97
- BIST100 below MA200 months: 21
- Below-MA200 rate: 21.65%
