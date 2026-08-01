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
| baseline              |             2.0449 |                         0.3628 |            -0.1903 |                     0.3672 |                 0.2885 |                  1 |
| defensive_mode        |             1.9730 |                         0.2908 |            -0.1903 |                     0.3066 |                 0.2085 |                  1 |
| reduced_exposure_mode |             1.7599 |                         0.0778 |            -0.1931 |                     0.2694 |                -0.0022 |                  1 |
| cash_mode             |             1.5356 |                        -0.1465 |            -0.2026 |                     0.1707 |                -0.3141 |                  1 |

## Best Out-Of-Sample Combinations

| policy                | base_model      |   base_portfolio_size | period        |   months |   bear_months |   avg_exposure |   total_return |   bist100_total_return |   excess_return_vs_bist100 |   max_drawdown |   bist100_max_drawdown |   win_rate |   robustness_score |
|:----------------------|:----------------|----------------------:|:--------------|---------:|--------------:|---------------:|---------------:|-----------------------:|---------------------------:|---------------:|-----------------------:|-----------:|-------------------:|
| baseline              | mixed_model     |                    15 | out_of_sample |       30 |             7 |         1.0000 |         0.5579 |                 0.5839 |                    -0.0260 |        -0.1644 |                -0.1675 |     0.6000 |            -0.0549 |
| baseline              | momentum_heavy  |                    15 | out_of_sample |       30 |             7 |         1.0000 |         0.5609 |                 0.5839 |                    -0.0230 |        -0.1680 |                -0.1675 |     0.6000 |            -0.0590 |
| baseline              | low_volatility  |                    15 | out_of_sample |       30 |             7 |         1.0000 |         0.5465 |                 0.5839 |                    -0.0374 |        -0.1563 |                -0.1675 |     0.5667 |            -0.0667 |
| baseline              | trend_following |                    15 | out_of_sample |       30 |             7 |         1.0000 |         0.5357 |                 0.5839 |                    -0.0482 |        -0.1747 |                -0.1675 |     0.6000 |            -0.0975 |
| baseline              | momentum_heavy  |                     3 | out_of_sample |       30 |             7 |         1.0000 |         0.5181 |                 0.5839 |                    -0.0658 |        -0.1660 |                -0.1675 |     0.6000 |            -0.0979 |
| baseline              | volume_heavy    |                    15 | out_of_sample |       30 |             7 |         1.0000 |         0.4828 |                 0.5839 |                    -0.1011 |        -0.1746 |                -0.1675 |     0.6000 |            -0.1502 |
| defensive_mode        | low_volatility  |                    15 | out_of_sample |       30 |             7 |         1.0000 |         0.4424 |                 0.5839 |                    -0.1416 |        -0.1661 |                -0.1675 |     0.5333 |            -0.2070 |
| defensive_mode        | mixed_model     |                    15 | out_of_sample |       30 |             7 |         1.0000 |         0.4597 |                 0.5839 |                    -0.1242 |        -0.1757 |                -0.1675 |     0.5333 |            -0.2090 |
| reduced_exposure_mode | mixed_model     |                    15 | out_of_sample |       30 |             7 |         0.8833 |         0.4319 |                 0.5839 |                    -0.1520 |        -0.1817 |                -0.1675 |     0.6000 |            -0.2153 |
| defensive_mode        | momentum_heavy  |                     3 | out_of_sample |       30 |             7 |         1.0000 |         0.4163 |                 0.5839 |                    -0.1677 |        -0.1660 |                -0.1675 |     0.5667 |            -0.2164 |

## Regime Signal Coverage

- Total signal months: 94
- BIST100 below MA200 months: 19
- Below-MA200 rate: 20.21%
