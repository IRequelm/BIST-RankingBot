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
| baseline              |             2.0957 |                         0.4359 |            -0.1902 |                     0.5195 |                 0.3667 |                  1 |
| defensive_mode        |             2.0212 |                         0.3614 |            -0.1901 |                     0.4513 |                 0.2848 |                  1 |
| reduced_exposure_mode |             1.8069 |                         0.1471 |            -0.1929 |                     0.4104 |                 0.0726 |                  1 |
| cash_mode             |             1.5789 |                        -0.0809 |            -0.2024 |                     0.3004 |                -0.2414 |                  1 |

## Best Out-Of-Sample Combinations

| policy                | base_model      |   base_portfolio_size | period        |   months |   bear_months |   avg_exposure |   total_return |   bist100_total_return |   excess_return_vs_bist100 |   max_drawdown |   bist100_max_drawdown |   win_rate |   robustness_score |
|:----------------------|:----------------|----------------------:|:--------------|---------:|--------------:|---------------:|---------------:|-----------------------:|---------------------------:|---------------:|-----------------------:|-----------:|-------------------:|
| baseline              | momentum_heavy  |                     3 | out_of_sample |       32 |             7 |         1.0000 |         0.7770 |                 0.5169 |                     0.2601 |        -0.1660 |                -0.1675 |     0.6250 |             0.2406 |
| baseline              | mixed_model     |                    15 | out_of_sample |       32 |             7 |         1.0000 |         0.6937 |                 0.5169 |                     0.1768 |        -0.1644 |                -0.1675 |     0.6250 |             0.1604 |
| baseline              | momentum_heavy  |                    15 | out_of_sample |       32 |             7 |         1.0000 |         0.6929 |                 0.5169 |                     0.1760 |        -0.1680 |                -0.1675 |     0.6250 |             0.1525 |
| baseline              | trend_following |                    15 | out_of_sample |       32 |             7 |         1.0000 |         0.6653 |                 0.5169 |                     0.1485 |        -0.1747 |                -0.1675 |     0.6250 |             0.1117 |
| baseline              | low_volatility  |                    15 | out_of_sample |       32 |             7 |         1.0000 |         0.6407 |                 0.5169 |                     0.1238 |        -0.1563 |                -0.1675 |     0.5938 |             0.1080 |
| defensive_mode        | momentum_heavy  |                     3 | out_of_sample |       32 |             7 |         1.0000 |         0.6578 |                 0.5169 |                     0.1410 |        -0.1660 |                -0.1675 |     0.5938 |             0.1058 |
| reduced_exposure_mode | momentum_heavy  |                     3 | out_of_sample |       32 |             7 |         0.8906 |         0.6303 |                 0.5169 |                     0.1135 |        -0.1660 |                -0.1675 |     0.6250 |             0.0939 |
| baseline              | trend_following |                     3 | out_of_sample |       32 |             7 |         1.0000 |         0.6240 |                 0.5169 |                     0.1071 |        -0.1767 |                -0.1675 |     0.6250 |             0.0662 |
| baseline              | volume_heavy    |                    15 | out_of_sample |       32 |             7 |         1.0000 |         0.6121 |                 0.5169 |                     0.0952 |        -0.1746 |                -0.1675 |     0.6250 |             0.0586 |
| defensive_mode        | mixed_model     |                    15 | out_of_sample |       32 |             7 |         1.0000 |         0.5869 |                 0.5169 |                     0.0700 |        -0.1757 |                -0.1675 |     0.5625 |            -0.0001 |

## Regime Signal Coverage

- Total signal months: 96
- BIST100 below MA200 months: 20
- Below-MA200 rate: 20.83%
