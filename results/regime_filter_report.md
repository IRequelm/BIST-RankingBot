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
| baseline              |             2.0267 |                         0.4351 |            -0.1924 |                     0.3126 |                 0.3531 |                  1 |
| defensive_mode        |             1.9467 |                         0.3551 |            -0.1954 |                     0.2277 |                 0.2595 |                  1 |
| reduced_exposure_mode |             1.7560 |                         0.1644 |            -0.1933 |                     0.2578 |                 0.0805 |                  1 |
| cash_mode             |             1.5441 |                        -0.0475 |            -0.2027 |                     0.1960 |                -0.2163 |                  1 |

## Best Out-Of-Sample Combinations

| policy                | base_model      |   base_portfolio_size | period        |   months |   bear_months |   avg_exposure |   total_return |   bist100_total_return |   excess_return_vs_bist100 |   max_drawdown |   bist100_max_drawdown |   win_rate |   robustness_score |
|:----------------------|:----------------|----------------------:|:--------------|---------:|--------------:|---------------:|---------------:|-----------------------:|---------------------------:|---------------:|-----------------------:|-----------:|-------------------:|
| baseline              | momentum_heavy  |                     3 | out_of_sample |       33 |             8 |         1.0000 |         0.5126 |                 0.3124 |                     0.2002 |        -0.1660 |                -0.2279 |     0.5455 |             0.1409 |
| baseline              | mixed_model     |                    15 | out_of_sample |       33 |             8 |         1.0000 |         0.4839 |                 0.3124 |                     0.1715 |        -0.1644 |                -0.2279 |     0.5758 |             0.1305 |
| baseline              | momentum_heavy  |                    15 | out_of_sample |       33 |             8 |         1.0000 |         0.4600 |                 0.3124 |                     0.1476 |        -0.1680 |                -0.2279 |     0.5758 |             0.0995 |
| baseline              | trend_following |                    15 | out_of_sample |       33 |             8 |         1.0000 |         0.4591 |                 0.3124 |                     0.1467 |        -0.1747 |                -0.2279 |     0.5758 |             0.0852 |
| baseline              | trend_following |                     3 | out_of_sample |       33 |             8 |         1.0000 |         0.4452 |                 0.3124 |                     0.1328 |        -0.1767 |                -0.2279 |     0.5758 |             0.0672 |
| reduced_exposure_mode | momentum_heavy  |                     3 | out_of_sample |       33 |             8 |         0.8788 |         0.4320 |                 0.3124 |                     0.1196 |        -0.1660 |                -0.2279 |     0.5455 |             0.0602 |
| baseline              | low_volatility  |                    15 | out_of_sample |       33 |             8 |         1.0000 |         0.4271 |                 0.3124 |                     0.1147 |        -0.1801 |                -0.2279 |     0.5455 |             0.0273 |
| reduced_exposure_mode | mixed_model     |                    15 | out_of_sample |       33 |             8 |         0.8788 |         0.4002 |                 0.3124 |                     0.0878 |        -0.1817 |                -0.2279 |     0.5758 |             0.0124 |
| defensive_mode        | momentum_heavy  |                     3 | out_of_sample |       33 |             8 |         1.0000 |         0.3806 |                 0.3124 |                     0.0682 |        -0.1660 |                -0.2279 |     0.5152 |            -0.0063 |
| baseline              | volume_heavy    |                    15 | out_of_sample |       33 |             8 |         1.0000 |         0.3676 |                 0.3124 |                     0.0552 |        -0.1763 |                -0.2279 |     0.5758 |            -0.0095 |

## Regime Signal Coverage

- Total signal months: 97
- BIST100 below MA200 months: 21
- Below-MA200 rate: 21.65%
