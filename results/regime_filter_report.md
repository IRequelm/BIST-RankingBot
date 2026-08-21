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
| baseline              |             2.0850 |                         0.3661 |            -0.1903 |                     0.4876 |                 0.2942 |                  1 |
| defensive_mode        |             2.0111 |                         0.2921 |            -0.1903 |                     0.4209 |                 0.2124 |                  1 |
| reduced_exposure_mode |             1.7970 |                         0.0781 |            -0.1931 |                     0.3808 |                 0.0006 |                  1 |
| cash_mode             |             1.5698 |                        -0.1491 |            -0.2026 |                     0.2732 |                -0.3134 |                  1 |

## Best Out-Of-Sample Combinations

| policy                | base_model      |   base_portfolio_size | period        |   months |   bear_months |   avg_exposure |   total_return |   bist100_total_return |   excess_return_vs_bist100 |   max_drawdown |   bist100_max_drawdown |   win_rate |   robustness_score |
|:----------------------|:----------------|----------------------:|:--------------|---------:|--------------:|---------------:|---------------:|-----------------------:|---------------------------:|---------------:|-----------------------:|-----------:|-------------------:|
| baseline              | momentum_heavy  |                     3 | out_of_sample |       31 |             7 |         1.0000 |         0.6928 |                 0.6944 |                    -0.0015 |        -0.1660 |                -0.1675 |     0.6129 |            -0.0272 |
| baseline              | mixed_model     |                    15 | out_of_sample |       31 |             7 |         1.0000 |         0.6571 |                 0.6944 |                    -0.0373 |        -0.1644 |                -0.1675 |     0.6129 |            -0.0598 |
| baseline              | momentum_heavy  |                    15 | out_of_sample |       31 |             7 |         1.0000 |         0.6602 |                 0.6944 |                    -0.0341 |        -0.1680 |                -0.1675 |     0.6129 |            -0.0637 |
| baseline              | low_volatility  |                    15 | out_of_sample |       31 |             7 |         1.0000 |         0.6331 |                 0.6944 |                    -0.0612 |        -0.1563 |                -0.1675 |     0.5806 |            -0.0836 |
| baseline              | trend_following |                    15 | out_of_sample |       31 |             7 |         1.0000 |         0.6335 |                 0.6944 |                    -0.0609 |        -0.1747 |                -0.1675 |     0.6129 |            -0.1038 |
| defensive_mode        | momentum_heavy  |                     3 | out_of_sample |       31 |             7 |         1.0000 |         0.5793 |                 0.6944 |                    -0.1151 |        -0.1660 |                -0.1675 |     0.5806 |            -0.1568 |
| baseline              | volume_heavy    |                    15 | out_of_sample |       31 |             7 |         1.0000 |         0.5772 |                 0.6944 |                    -0.1172 |        -0.1746 |                -0.1675 |     0.6129 |            -0.1598 |
| reduced_exposure_mode | momentum_heavy  |                     3 | out_of_sample |       31 |             7 |         0.8871 |         0.5531 |                 0.6944 |                    -0.1413 |        -0.1660 |                -0.1675 |     0.6129 |            -0.1669 |
| baseline              | trend_following |                     3 | out_of_sample |       31 |             7 |         1.0000 |         0.5471 |                 0.6944 |                    -0.1473 |        -0.1767 |                -0.1675 |     0.6129 |            -0.1942 |
| defensive_mode        | mixed_model     |                    15 | out_of_sample |       31 |             7 |         1.0000 |         0.5526 |                 0.6944 |                    -0.1418 |        -0.1757 |                -0.1675 |     0.5484 |            -0.2190 |

## Regime Signal Coverage

- Total signal months: 95
- BIST100 below MA200 months: 19
- Below-MA200 rate: 20.00%
