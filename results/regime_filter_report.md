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
| baseline              |             2.1033 |                         0.3816 |            -0.1902 |                     0.5424 |                 0.3124 |                  1 |
| defensive_mode        |             2.0285 |                         0.3068 |            -0.1901 |                     0.4732 |                 0.2302 |                  1 |
| reduced_exposure_mode |             1.8140 |                         0.0923 |            -0.1929 |                     0.4317 |                 0.0177 |                  1 |
| cash_mode             |             1.5854 |                        -0.1363 |            -0.2024 |                     0.3200 |                -0.2968 |                  1 |

## Best Out-Of-Sample Combinations

| policy                | base_model      |   base_portfolio_size | period        |   months |   bear_months |   avg_exposure |   total_return |   bist100_total_return |   excess_return_vs_bist100 |   max_drawdown |   bist100_max_drawdown |   win_rate |   robustness_score |
|:----------------------|:----------------|----------------------:|:--------------|---------:|--------------:|---------------:|---------------:|-----------------------:|---------------------------:|---------------:|-----------------------:|-----------:|-------------------:|
| baseline              | momentum_heavy  |                     3 | out_of_sample |       32 |             7 |         1.0000 |         0.7847 |                 0.7027 |                     0.0820 |        -0.1660 |                -0.1675 |     0.6250 |             0.0624 |
| baseline              | mixed_model     |                    15 | out_of_sample |       32 |             7 |         1.0000 |         0.7338 |                 0.7027 |                     0.0311 |        -0.1644 |                -0.1675 |     0.6250 |             0.0147 |
| baseline              | momentum_heavy  |                    15 | out_of_sample |       32 |             7 |         1.0000 |         0.7304 |                 0.7027 |                     0.0277 |        -0.1680 |                -0.1675 |     0.6250 |             0.0042 |
| baseline              | trend_following |                    15 | out_of_sample |       32 |             7 |         1.0000 |         0.7048 |                 0.7027 |                     0.0021 |        -0.1747 |                -0.1675 |     0.6250 |            -0.0347 |
| baseline              | low_volatility  |                    15 | out_of_sample |       32 |             7 |         1.0000 |         0.6786 |                 0.7027 |                    -0.0241 |        -0.1563 |                -0.1675 |     0.5938 |            -0.0399 |
| defensive_mode        | momentum_heavy  |                     3 | out_of_sample |       32 |             7 |         1.0000 |         0.6650 |                 0.7027 |                    -0.0377 |        -0.1660 |                -0.1675 |     0.5938 |            -0.0729 |
| reduced_exposure_mode | momentum_heavy  |                     3 | out_of_sample |       32 |             7 |         0.8906 |         0.6374 |                 0.7027 |                    -0.0653 |        -0.1660 |                -0.1675 |     0.6250 |            -0.0849 |
| baseline              | volume_heavy    |                    15 | out_of_sample |       32 |             7 |         1.0000 |         0.6503 |                 0.7027 |                    -0.0524 |        -0.1746 |                -0.1675 |     0.6250 |            -0.0890 |
| baseline              | trend_following |                     3 | out_of_sample |       32 |             7 |         1.0000 |         0.6310 |                 0.7027 |                    -0.0717 |        -0.1767 |                -0.1675 |     0.6250 |            -0.1126 |
| defensive_mode        | mixed_model     |                    15 | out_of_sample |       32 |             7 |         1.0000 |         0.6245 |                 0.7027 |                    -0.0782 |        -0.1757 |                -0.1675 |     0.5625 |            -0.1483 |

## Regime Signal Coverage

- Total signal months: 96
- BIST100 below MA200 months: 19
- Below-MA200 rate: 19.79%
