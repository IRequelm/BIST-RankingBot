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
| baseline              |             2.0678 |                         0.3608 |            -0.1902 |                     0.4358 |                 0.2877 |                  1 |
| defensive_mode        |             1.9948 |                         0.2878 |            -0.1901 |                     0.3720 |                 0.2069 |                  1 |
| reduced_exposure_mode |             1.7811 |                         0.0741 |            -0.1929 |                     0.3330 |                -0.0044 |                  1 |
| cash_mode             |             1.5552 |                        -0.1518 |            -0.2024 |                     0.2293 |                -0.3179 |                  1 |

## Best Out-Of-Sample Combinations

| policy                | base_model      |   base_portfolio_size | period        |   months |   bear_months |   avg_exposure |   total_return |   bist100_total_return |   excess_return_vs_bist100 |   max_drawdown |   bist100_max_drawdown |   win_rate |   robustness_score |
|:----------------------|:----------------|----------------------:|:--------------|---------:|--------------:|---------------:|---------------:|-----------------------:|---------------------------:|---------------:|-----------------------:|-----------:|-------------------:|
| baseline              | mixed_model     |                    15 | out_of_sample |       30 |             7 |         1.0000 |         0.6269 |                 0.6585 |                    -0.0317 |        -0.1644 |                -0.1675 |     0.6000 |            -0.0606 |
| baseline              | momentum_heavy  |                     3 | out_of_sample |       30 |             7 |         1.0000 |         0.6106 |                 0.6585 |                    -0.0480 |        -0.1660 |                -0.1675 |     0.6333 |            -0.0634 |
| baseline              | momentum_heavy  |                    15 | out_of_sample |       30 |             7 |         1.0000 |         0.6278 |                 0.6585 |                    -0.0307 |        -0.1680 |                -0.1675 |     0.6000 |            -0.0667 |
| baseline              | low_volatility  |                    15 | out_of_sample |       30 |             7 |         1.0000 |         0.6109 |                 0.6585 |                    -0.0477 |        -0.1563 |                -0.1675 |     0.5667 |            -0.0770 |
| baseline              | trend_following |                    15 | out_of_sample |       30 |             7 |         1.0000 |         0.6015 |                 0.6585 |                    -0.0570 |        -0.1747 |                -0.1675 |     0.6000 |            -0.1063 |
| baseline              | volume_heavy    |                    15 | out_of_sample |       30 |             7 |         1.0000 |         0.5485 |                 0.6585 |                    -0.1101 |        -0.1746 |                -0.1675 |     0.6000 |            -0.1592 |
| defensive_mode        | momentum_heavy  |                     3 | out_of_sample |       30 |             7 |         1.0000 |         0.5025 |                 0.6585 |                    -0.1560 |        -0.1660 |                -0.1675 |     0.6000 |            -0.1881 |
| reduced_exposure_mode | momentum_heavy  |                     3 | out_of_sample |       30 |             7 |         0.8833 |         0.4776 |                 0.6585 |                    -0.1809 |        -0.1660 |                -0.1675 |     0.6333 |            -0.1963 |
| defensive_mode        | mixed_model     |                    15 | out_of_sample |       30 |             7 |         1.0000 |         0.5243 |                 0.6585 |                    -0.1343 |        -0.1757 |                -0.1675 |     0.5333 |            -0.2190 |
| defensive_mode        | low_volatility  |                    15 | out_of_sample |       30 |             7 |         1.0000 |         0.5024 |                 0.6585 |                    -0.1562 |        -0.1661 |                -0.1675 |     0.5333 |            -0.2216 |

## Regime Signal Coverage

- Total signal months: 94
- BIST100 below MA200 months: 19
- Below-MA200 rate: 20.21%
