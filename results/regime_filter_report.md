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
| baseline              |             2.0843 |                         0.4361 |            -0.1902 |                     0.4854 |                 0.3641 |                  1 |
| defensive_mode        |             2.0103 |                         0.3621 |            -0.1901 |                     0.4186 |                 0.2826 |                  1 |
| reduced_exposure_mode |             1.7963 |                         0.1482 |            -0.1929 |                     0.3787 |                 0.0707 |                  1 |
| cash_mode             |             1.5691 |                        -0.0791 |            -0.2024 |                     0.2711 |                -0.2425 |                  1 |

## Best Out-Of-Sample Combinations

| policy                | base_model      |   base_portfolio_size | period        |   months |   bear_months |   avg_exposure |   total_return |   bist100_total_return |   excess_return_vs_bist100 |   max_drawdown |   bist100_max_drawdown |   win_rate |   robustness_score |
|:----------------------|:----------------|----------------------:|:--------------|---------:|--------------:|---------------:|---------------:|-----------------------:|---------------------------:|---------------:|-----------------------:|-----------:|-------------------:|
| baseline              | momentum_heavy  |                     3 | out_of_sample |       32 |             7 |         1.0000 |         0.7451 |                 0.4821 |                     0.2630 |        -0.1660 |                -0.1675 |     0.6250 |             0.2434 |
| baseline              | mixed_model     |                    15 | out_of_sample |       32 |             7 |         1.0000 |         0.6537 |                 0.4821 |                     0.1716 |        -0.1644 |                -0.1675 |     0.6250 |             0.1552 |
| baseline              | momentum_heavy  |                    15 | out_of_sample |       32 |             7 |         1.0000 |         0.6527 |                 0.4821 |                     0.1706 |        -0.1680 |                -0.1675 |     0.6250 |             0.1471 |
| defensive_mode        | momentum_heavy  |                     3 | out_of_sample |       32 |             7 |         1.0000 |         0.6280 |                 0.4821 |                     0.1459 |        -0.1660 |                -0.1675 |     0.5938 |             0.1107 |
| baseline              | trend_following |                    15 | out_of_sample |       32 |             7 |         1.0000 |         0.6260 |                 0.4821 |                     0.1440 |        -0.1747 |                -0.1675 |     0.6250 |             0.1071 |
| reduced_exposure_mode | momentum_heavy  |                     3 | out_of_sample |       32 |             7 |         0.8906 |         0.6010 |                 0.4821 |                     0.1189 |        -0.1660 |                -0.1675 |     0.6250 |             0.0993 |
| baseline              | low_volatility  |                    15 | out_of_sample |       32 |             7 |         1.0000 |         0.6072 |                 0.4821 |                     0.1251 |        -0.1563 |                -0.1675 |     0.5625 |             0.0937 |
| baseline              | trend_following |                     3 | out_of_sample |       32 |             7 |         1.0000 |         0.5948 |                 0.4821 |                     0.1127 |        -0.1767 |                -0.1675 |     0.6250 |             0.0718 |
| baseline              | volume_heavy    |                    15 | out_of_sample |       32 |             7 |         1.0000 |         0.5740 |                 0.4821 |                     0.0919 |        -0.1746 |                -0.1675 |     0.6250 |             0.0553 |
| defensive_mode        | mixed_model     |                    15 | out_of_sample |       32 |             7 |         1.0000 |         0.5494 |                 0.4821 |                     0.0673 |        -0.1757 |                -0.1675 |     0.5625 |            -0.0028 |

## Regime Signal Coverage

- Total signal months: 96
- BIST100 below MA200 months: 20
- Below-MA200 rate: 20.83%
