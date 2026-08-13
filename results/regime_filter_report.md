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
| baseline              |             2.0518 |                         0.3441 |            -0.1902 |                     0.3879 |                 0.2699 |                  1 |
| defensive_mode        |             1.9795 |                         0.2718 |            -0.1902 |                     0.3261 |                 0.1899 |                  1 |
| reduced_exposure_mode |             1.7663 |                         0.0586 |            -0.1930 |                     0.2885 |                -0.0212 |                  1 |
| cash_mode             |             1.5415 |                        -0.1662 |            -0.2025 |                     0.1882 |                -0.3327 |                  1 |

## Best Out-Of-Sample Combinations

| policy                | base_model      |   base_portfolio_size | period        |   months |   bear_months |   avg_exposure |   total_return |   bist100_total_return |   excess_return_vs_bist100 |   max_drawdown |   bist100_max_drawdown |   win_rate |   robustness_score |
|:----------------------|:----------------|----------------------:|:--------------|---------:|--------------:|---------------:|---------------:|-----------------------:|---------------------------:|---------------:|-----------------------:|-----------:|-------------------:|
| baseline              | mixed_model     |                    15 | out_of_sample |       31 |             7 |         1.0000 |         0.5887 |                 0.6607 |                    -0.0720 |        -0.1644 |                -0.1675 |     0.6129 |            -0.0945 |
| baseline              | momentum_heavy  |                    15 | out_of_sample |       31 |             7 |         1.0000 |         0.5877 |                 0.6607 |                    -0.0729 |        -0.1680 |                -0.1675 |     0.6129 |            -0.1025 |
| baseline              | low_volatility  |                    15 | out_of_sample |       31 |             7 |         1.0000 |         0.5725 |                 0.6607 |                    -0.0882 |        -0.1563 |                -0.1675 |     0.5806 |            -0.1105 |
| baseline              | trend_following |                    15 | out_of_sample |       31 |             7 |         1.0000 |         0.5621 |                 0.6607 |                    -0.0985 |        -0.1747 |                -0.1675 |     0.6129 |            -0.1414 |
| baseline              | momentum_heavy  |                     3 | out_of_sample |       31 |             7 |         1.0000 |         0.5215 |                 0.6607 |                    -0.1392 |        -0.1660 |                -0.1675 |     0.5806 |            -0.1810 |
| baseline              | volume_heavy    |                    15 | out_of_sample |       31 |             7 |         1.0000 |         0.5143 |                 0.6607 |                    -0.1463 |        -0.1746 |                -0.1675 |     0.6129 |            -0.1890 |
| defensive_mode        | mixed_model     |                    15 | out_of_sample |       31 |             7 |         1.0000 |         0.4885 |                 0.6607 |                    -0.1722 |        -0.1757 |                -0.1675 |     0.5484 |            -0.2494 |
| defensive_mode        | low_volatility  |                    15 | out_of_sample |       31 |             7 |         1.0000 |         0.4665 |                 0.6607 |                    -0.1941 |        -0.1661 |                -0.1675 |     0.5484 |            -0.2520 |
| reduced_exposure_mode | mixed_model     |                    15 | out_of_sample |       31 |             7 |         0.8871 |         0.4602 |                 0.6607 |                    -0.2005 |        -0.1817 |                -0.1675 |     0.6129 |            -0.2573 |
| defensive_mode        | momentum_heavy  |                    15 | out_of_sample |       31 |             7 |         1.0000 |         0.4839 |                 0.6607 |                    -0.1768 |        -0.1792 |                -0.1675 |     0.5484 |            -0.2609 |

## Regime Signal Coverage

- Total signal months: 95
- BIST100 below MA200 months: 19
- Below-MA200 rate: 20.00%
