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
| baseline              |             2.0755 |                         0.3555 |            -0.1902 |                     0.4590 |                 0.2813 |                  1 |
| defensive_mode        |             2.0023 |                         0.2822 |            -0.1901 |                     0.3945 |                 0.2003 |                  1 |
| reduced_exposure_mode |             1.7883 |                         0.0683 |            -0.1929 |                     0.3547 |                -0.0113 |                  1 |
| cash_mode             |             1.5619 |                        -0.1581 |            -0.2024 |                     0.2495 |                -0.3254 |                  1 |

## Best Out-Of-Sample Combinations

| policy                | base_model      |   base_portfolio_size | period        |   months |   bear_months |   avg_exposure |   total_return |   bist100_total_return |   excess_return_vs_bist100 |   max_drawdown |   bist100_max_drawdown |   win_rate |   robustness_score |
|:----------------------|:----------------|----------------------:|:--------------|---------:|--------------:|---------------:|---------------:|-----------------------:|---------------------------:|---------------:|-----------------------:|-----------:|-------------------:|
| baseline              | mixed_model     |                    15 | out_of_sample |       30 |             7 |         1.0000 |         0.6648 |                 0.6977 |                    -0.0328 |        -0.1644 |                -0.1675 |     0.6000 |            -0.0617 |
| baseline              | momentum_heavy  |                    15 | out_of_sample |       30 |             7 |         1.0000 |         0.6577 |                 0.6977 |                    -0.0400 |        -0.1680 |                -0.1675 |     0.6000 |            -0.0760 |
| baseline              | low_volatility  |                    15 | out_of_sample |       30 |             7 |         1.0000 |         0.6365 |                 0.6977 |                    -0.0611 |        -0.1563 |                -0.1675 |     0.5667 |            -0.0905 |
| baseline              | trend_following |                    15 | out_of_sample |       30 |             7 |         1.0000 |         0.6309 |                 0.6977 |                    -0.0667 |        -0.1747 |                -0.1675 |     0.6000 |            -0.1160 |
| baseline              | momentum_heavy  |                     3 | out_of_sample |       30 |             7 |         1.0000 |         0.6022 |                 0.6977 |                    -0.0955 |        -0.1660 |                -0.1675 |     0.6000 |            -0.1276 |
| baseline              | volume_heavy    |                    15 | out_of_sample |       30 |             7 |         1.0000 |         0.5846 |                 0.6977 |                    -0.1131 |        -0.1746 |                -0.1675 |     0.6000 |            -0.1622 |
| defensive_mode        | mixed_model     |                    15 | out_of_sample |       30 |             7 |         1.0000 |         0.5598 |                 0.6977 |                    -0.1378 |        -0.1757 |                -0.1675 |     0.5333 |            -0.2225 |
| reduced_exposure_mode | mixed_model     |                    15 | out_of_sample |       30 |             7 |         0.8833 |         0.5302 |                 0.6977 |                    -0.1675 |        -0.1817 |                -0.1675 |     0.6000 |            -0.2308 |
| defensive_mode        | low_volatility  |                    15 | out_of_sample |       30 |             7 |         1.0000 |         0.5263 |                 0.6977 |                    -0.1714 |        -0.1661 |                -0.1675 |     0.5333 |            -0.2368 |
| defensive_mode        | momentum_heavy  |                    15 | out_of_sample |       30 |             7 |         1.0000 |         0.5493 |                 0.6977 |                    -0.1484 |        -0.1792 |                -0.1675 |     0.5333 |            -0.2401 |

## Regime Signal Coverage

- Total signal months: 94
- BIST100 below MA200 months: 19
- Below-MA200 rate: 20.21%
