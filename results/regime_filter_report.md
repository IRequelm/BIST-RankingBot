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
| baseline              |             2.0940 |                         0.4166 |            -0.1902 |                     0.5143 |                 0.3474 |                  1 |
| defensive_mode        |             2.0195 |                         0.3421 |            -0.1901 |                     0.4462 |                 0.2655 |                  1 |
| reduced_exposure_mode |             1.8053 |                         0.1279 |            -0.1929 |                     0.4056 |                 0.0533 |                  1 |
| cash_mode             |             1.5774 |                        -0.1000 |            -0.2024 |                     0.2959 |                -0.2606 |                  1 |

## Best Out-Of-Sample Combinations

| policy                | base_model      |   base_portfolio_size | period        |   months |   bear_months |   avg_exposure |   total_return |   bist100_total_return |   excess_return_vs_bist100 |   max_drawdown |   bist100_max_drawdown |   win_rate |   robustness_score |
|:----------------------|:----------------|----------------------:|:--------------|---------:|--------------:|---------------:|---------------:|-----------------------:|---------------------------:|---------------:|-----------------------:|-----------:|-------------------:|
| baseline              | momentum_heavy  |                     3 | out_of_sample |       32 |             7 |         1.0000 |         0.7845 |                 0.5698 |                     0.2147 |        -0.1660 |                -0.1675 |     0.6250 |             0.1951 |
| baseline              | mixed_model     |                    15 | out_of_sample |       32 |             7 |         1.0000 |         0.6791 |                 0.5698 |                     0.1094 |        -0.1644 |                -0.1675 |     0.6250 |             0.0930 |
| baseline              | momentum_heavy  |                    15 | out_of_sample |       32 |             7 |         1.0000 |         0.6800 |                 0.5698 |                     0.1102 |        -0.1680 |                -0.1675 |     0.6250 |             0.0867 |
| defensive_mode        | momentum_heavy  |                     3 | out_of_sample |       32 |             7 |         1.0000 |         0.6648 |                 0.5698 |                     0.0950 |        -0.1660 |                -0.1675 |     0.5938 |             0.0598 |
| baseline              | low_volatility  |                    15 | out_of_sample |       32 |             7 |         1.0000 |         0.6356 |                 0.5698 |                     0.0658 |        -0.1563 |                -0.1675 |     0.5938 |             0.0501 |
| reduced_exposure_mode | momentum_heavy  |                     3 | out_of_sample |       32 |             7 |         0.8906 |         0.6371 |                 0.5698 |                     0.0674 |        -0.1660 |                -0.1675 |     0.6250 |             0.0478 |
| baseline              | trend_following |                    15 | out_of_sample |       32 |             7 |         1.0000 |         0.6510 |                 0.5698 |                     0.0813 |        -0.1747 |                -0.1675 |     0.6250 |             0.0445 |
| baseline              | trend_following |                     3 | out_of_sample |       32 |             7 |         1.0000 |         0.6308 |                 0.5698 |                     0.0611 |        -0.1767 |                -0.1675 |     0.6250 |             0.0202 |
| baseline              | volume_heavy    |                    15 | out_of_sample |       32 |             7 |         1.0000 |         0.5982 |                 0.5698 |                     0.0285 |        -0.1746 |                -0.1675 |     0.6250 |            -0.0082 |
| defensive_mode        | mixed_model     |                    15 | out_of_sample |       32 |             7 |         1.0000 |         0.5732 |                 0.5698 |                     0.0035 |        -0.1757 |                -0.1675 |     0.5625 |            -0.0666 |

## Regime Signal Coverage

- Total signal months: 96
- BIST100 below MA200 months: 20
- Below-MA200 rate: 20.83%
