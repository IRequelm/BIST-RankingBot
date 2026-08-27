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
| baseline              |             2.0868 |                         0.3594 |            -0.1902 |                     0.4928 |                 0.2879 |                  1 |
| defensive_mode        |             2.0128 |                         0.2854 |            -0.1901 |                     0.4260 |                 0.2064 |                  1 |
| reduced_exposure_mode |             1.7987 |                         0.0713 |            -0.1929 |                     0.3857 |                -0.0055 |                  1 |
| cash_mode             |             1.5713 |                        -0.1560 |            -0.2024 |                     0.2777 |                -0.3197 |                  1 |

## Best Out-Of-Sample Combinations

| policy                | base_model      |   base_portfolio_size | period        |   months |   bear_months |   avg_exposure |   total_return |   bist100_total_return |   excess_return_vs_bist100 |   max_drawdown |   bist100_max_drawdown |   win_rate |   robustness_score |
|:----------------------|:----------------|----------------------:|:--------------|---------:|--------------:|---------------:|---------------:|-----------------------:|---------------------------:|---------------:|-----------------------:|-----------:|-------------------:|
| baseline              | momentum_heavy  |                     3 | out_of_sample |       31 |             7 |         1.0000 |         0.6859 |                 0.7196 |                    -0.0337 |        -0.1660 |                -0.1675 |     0.6129 |            -0.0593 |
| baseline              | mixed_model     |                    15 | out_of_sample |       31 |             7 |         1.0000 |         0.6784 |                 0.7196 |                    -0.0412 |        -0.1644 |                -0.1675 |     0.6129 |            -0.0636 |
| baseline              | momentum_heavy  |                    15 | out_of_sample |       31 |             7 |         1.0000 |         0.6774 |                 0.7196 |                    -0.0422 |        -0.1680 |                -0.1675 |     0.6129 |            -0.0717 |
| baseline              | low_volatility  |                    15 | out_of_sample |       31 |             7 |         1.0000 |         0.6513 |                 0.7196 |                    -0.0683 |        -0.1563 |                -0.1675 |     0.5806 |            -0.0907 |
| baseline              | trend_following |                    15 | out_of_sample |       31 |             7 |         1.0000 |         0.6503 |                 0.7196 |                    -0.0693 |        -0.1747 |                -0.1675 |     0.6129 |            -0.1121 |
| baseline              | volume_heavy    |                    15 | out_of_sample |       31 |             7 |         1.0000 |         0.5984 |                 0.7196 |                    -0.1212 |        -0.1746 |                -0.1675 |     0.6129 |            -0.1639 |
| defensive_mode        | momentum_heavy  |                     3 | out_of_sample |       31 |             7 |         1.0000 |         0.5729 |                 0.7196 |                    -0.1467 |        -0.1660 |                -0.1675 |     0.5806 |            -0.1885 |
| reduced_exposure_mode | momentum_heavy  |                     3 | out_of_sample |       31 |             7 |         0.8871 |         0.5468 |                 0.7196 |                    -0.1728 |        -0.1660 |                -0.1675 |     0.6129 |            -0.1985 |
| defensive_mode        | mixed_model     |                    15 | out_of_sample |       31 |             7 |         1.0000 |         0.5726 |                 0.7196 |                    -0.1470 |        -0.1757 |                -0.1675 |     0.5484 |            -0.2242 |
| baseline              | trend_following |                     3 | out_of_sample |       31 |             7 |         1.0000 |         0.5408 |                 0.7196 |                    -0.1788 |        -0.1767 |                -0.1675 |     0.6129 |            -0.2258 |

## Regime Signal Coverage

- Total signal months: 95
- BIST100 below MA200 months: 19
- Below-MA200 rate: 20.00%
