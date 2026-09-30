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
| baseline              |             2.0787 |                         0.4423 |            -0.1902 |                     0.4684 |                 0.3687 |                  1 |
| defensive_mode        |             2.0049 |                         0.3686 |            -0.1901 |                     0.4024 |                 0.2875 |                  1 |
| reduced_exposure_mode |             1.7911 |                         0.1548 |            -0.1929 |                     0.3630 |                 0.0758 |                  1 |
| cash_mode             |             1.5643 |                        -0.0720 |            -0.2024 |                     0.2566 |                -0.2390 |                  1 |

## Best Out-Of-Sample Combinations

| policy                | base_model      |   base_portfolio_size | period        |   months |   bear_months |   avg_exposure |   total_return |   bist100_total_return |   excess_return_vs_bist100 |   max_drawdown |   bist100_max_drawdown |   win_rate |   robustness_score |
|:----------------------|:----------------|----------------------:|:--------------|---------:|--------------:|---------------:|---------------:|-----------------------:|---------------------------:|---------------:|-----------------------:|-----------:|-------------------:|
| baseline              | momentum_heavy  |                     3 | out_of_sample |       32 |             7 |         1.0000 |         0.7299 |                 0.4465 |                     0.2834 |        -0.1660 |                -0.1675 |     0.6250 |             0.2638 |
| baseline              | mixed_model     |                    15 | out_of_sample |       32 |             7 |         1.0000 |         0.6271 |                 0.4465 |                     0.1806 |        -0.1644 |                -0.1675 |     0.5938 |             0.1486 |
| baseline              | momentum_heavy  |                    15 | out_of_sample |       32 |             7 |         1.0000 |         0.6265 |                 0.4465 |                     0.1800 |        -0.1680 |                -0.1675 |     0.5938 |             0.1409 |
| defensive_mode        | momentum_heavy  |                     3 | out_of_sample |       32 |             7 |         1.0000 |         0.6139 |                 0.4465 |                     0.1674 |        -0.1660 |                -0.1675 |     0.5938 |             0.1322 |
| reduced_exposure_mode | momentum_heavy  |                     3 | out_of_sample |       32 |             7 |         0.8906 |         0.5871 |                 0.4465 |                     0.1406 |        -0.1660 |                -0.1675 |     0.6250 |             0.1210 |
| baseline              | low_volatility  |                    15 | out_of_sample |       32 |             7 |         1.0000 |         0.5866 |                 0.4465 |                     0.1400 |        -0.1563 |                -0.1675 |     0.5625 |             0.1086 |
| baseline              | trend_following |                    15 | out_of_sample |       32 |             7 |         1.0000 |         0.5999 |                 0.4465 |                     0.1534 |        -0.1747 |                -0.1675 |     0.5938 |             0.1009 |
| baseline              | trend_following |                     3 | out_of_sample |       32 |             7 |         1.0000 |         0.5810 |                 0.4465 |                     0.1344 |        -0.1767 |                -0.1675 |     0.6250 |             0.0935 |
| baseline              | volume_heavy    |                    15 | out_of_sample |       32 |             7 |         1.0000 |         0.5487 |                 0.4465 |                     0.1022 |        -0.1746 |                -0.1675 |     0.5938 |             0.0499 |
| defensive_mode        | mixed_model     |                    15 | out_of_sample |       32 |             7 |         1.0000 |         0.5245 |                 0.4465 |                     0.0780 |        -0.1757 |                -0.1675 |     0.5312 |            -0.0078 |

## Regime Signal Coverage

- Total signal months: 96
- BIST100 below MA200 months: 20
- Below-MA200 rate: 20.83%
