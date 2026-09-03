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
| baseline              |             2.0846 |                         0.3793 |            -0.1902 |                     0.4863 |                 0.3067 |                  1 |
| defensive_mode        |             2.0106 |                         0.3053 |            -0.1901 |                     0.4197 |                 0.2253 |                  1 |
| reduced_exposure_mode |             1.7966 |                         0.0913 |            -0.1929 |                     0.3796 |                 0.0133 |                  1 |
| cash_mode             |             1.5694 |                        -0.1359 |            -0.2024 |                     0.2720 |                -0.2999 |                  1 |

## Best Out-Of-Sample Combinations

| policy                | base_model      |   base_portfolio_size | period        |   months |   bear_months |   avg_exposure |   total_return |   bist100_total_return |   excess_return_vs_bist100 |   max_drawdown |   bist100_max_drawdown |   win_rate |   robustness_score |
|:----------------------|:----------------|----------------------:|:--------------|---------:|--------------:|---------------:|---------------:|-----------------------:|---------------------------:|---------------:|-----------------------:|-----------:|-------------------:|
| baseline              | momentum_heavy  |                     3 | out_of_sample |       32 |             7 |         1.0000 |         0.7089 |                 0.6537 |                     0.0553 |        -0.1660 |                -0.1675 |     0.6250 |             0.0357 |
| baseline              | momentum_heavy  |                    15 | out_of_sample |       32 |             7 |         1.0000 |         0.6548 |                 0.6537 |                     0.0012 |        -0.1680 |                -0.1675 |     0.6250 |            -0.0223 |
| baseline              | mixed_model     |                    15 | out_of_sample |       32 |             7 |         1.0000 |         0.6526 |                 0.6537 |                    -0.0011 |        -0.1644 |                -0.1675 |     0.5938 |            -0.0331 |
| baseline              | low_volatility  |                    15 | out_of_sample |       32 |             7 |         1.0000 |         0.6226 |                 0.6537 |                    -0.0311 |        -0.1563 |                -0.1675 |     0.5625 |            -0.0625 |
| baseline              | trend_following |                    15 | out_of_sample |       32 |             7 |         1.0000 |         0.6249 |                 0.6537 |                    -0.0287 |        -0.1747 |                -0.1675 |     0.5938 |            -0.0812 |
| defensive_mode        | momentum_heavy  |                     3 | out_of_sample |       32 |             7 |         1.0000 |         0.5943 |                 0.6537 |                    -0.0593 |        -0.1660 |                -0.1675 |     0.5938 |            -0.0945 |
| reduced_exposure_mode | momentum_heavy  |                     3 | out_of_sample |       32 |             7 |         0.8906 |         0.5679 |                 0.6537 |                    -0.0858 |        -0.1660 |                -0.1675 |     0.6250 |            -0.1054 |
| baseline              | trend_following |                     3 | out_of_sample |       32 |             7 |         1.0000 |         0.5618 |                 0.6537 |                    -0.0919 |        -0.1767 |                -0.1675 |     0.6250 |            -0.1328 |
| baseline              | volume_heavy    |                    15 | out_of_sample |       32 |             7 |         1.0000 |         0.5729 |                 0.6537 |                    -0.0807 |        -0.1746 |                -0.1675 |     0.5938 |            -0.1330 |
| defensive_mode        | momentum_heavy  |                    15 | out_of_sample |       32 |             7 |         1.0000 |         0.5466 |                 0.6537 |                    -0.1070 |        -0.1792 |                -0.1675 |     0.5625 |            -0.1842 |

## Regime Signal Coverage

- Total signal months: 96
- BIST100 below MA200 months: 19
- Below-MA200 rate: 19.79%
