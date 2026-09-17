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
| baseline              |             2.0864 |                         0.4175 |            -0.1902 |                     0.4917 |                 0.3470 |                  1 |
| defensive_mode        |             2.0123 |                         0.3433 |            -0.1901 |                     0.4245 |                 0.2654 |                  1 |
| reduced_exposure_mode |             1.7983 |                         0.1293 |            -0.1929 |                     0.3845 |                 0.0534 |                  1 |
| cash_mode             |             1.5709 |                        -0.0981 |            -0.2024 |                     0.2764 |                -0.2599 |                  1 |

## Best Out-Of-Sample Combinations

| policy                | base_model      |   base_portfolio_size | period        |   months |   bear_months |   avg_exposure |   total_return |   bist100_total_return |   excess_return_vs_bist100 |   max_drawdown |   bist100_max_drawdown |   win_rate |   robustness_score |
|:----------------------|:----------------|----------------------:|:--------------|---------:|--------------:|---------------:|---------------:|-----------------------:|---------------------------:|---------------:|-----------------------:|-----------:|-------------------:|
| baseline              | momentum_heavy  |                     3 | out_of_sample |       32 |             7 |         1.0000 |         0.7441 |                 0.5444 |                     0.1997 |        -0.1660 |                -0.1675 |     0.6250 |             0.1801 |
| baseline              | mixed_model     |                    15 | out_of_sample |       32 |             7 |         1.0000 |         0.6667 |                 0.5444 |                     0.1223 |        -0.1644 |                -0.1675 |     0.6250 |             0.1059 |
| baseline              | momentum_heavy  |                    15 | out_of_sample |       32 |             7 |         1.0000 |         0.6659 |                 0.5444 |                     0.1214 |        -0.1680 |                -0.1675 |     0.6250 |             0.0979 |
| baseline              | trend_following |                    15 | out_of_sample |       32 |             7 |         1.0000 |         0.6388 |                 0.5444 |                     0.0944 |        -0.1747 |                -0.1675 |     0.6250 |             0.0576 |
| defensive_mode        | momentum_heavy  |                     3 | out_of_sample |       32 |             7 |         1.0000 |         0.6272 |                 0.5444 |                     0.0827 |        -0.1660 |                -0.1675 |     0.5938 |             0.0475 |
| baseline              | low_volatility  |                    15 | out_of_sample |       32 |             7 |         1.0000 |         0.6208 |                 0.5444 |                     0.0763 |        -0.1563 |                -0.1675 |     0.5625 |             0.0449 |
| reduced_exposure_mode | momentum_heavy  |                     3 | out_of_sample |       32 |             7 |         0.8906 |         0.6002 |                 0.5444 |                     0.0557 |        -0.1660 |                -0.1675 |     0.6250 |             0.0361 |
| baseline              | trend_following |                     3 | out_of_sample |       32 |             7 |         1.0000 |         0.5940 |                 0.5444 |                     0.0495 |        -0.1767 |                -0.1675 |     0.6250 |             0.0086 |
| baseline              | volume_heavy    |                    15 | out_of_sample |       32 |             7 |         1.0000 |         0.5864 |                 0.5444 |                     0.0420 |        -0.1746 |                -0.1675 |     0.6250 |             0.0053 |
| defensive_mode        | mixed_model     |                    15 | out_of_sample |       32 |             7 |         1.0000 |         0.5616 |                 0.5444 |                     0.0172 |        -0.1757 |                -0.1675 |     0.5625 |            -0.0530 |

## Regime Signal Coverage

- Total signal months: 96
- BIST100 below MA200 months: 20
- Below-MA200 rate: 20.83%
