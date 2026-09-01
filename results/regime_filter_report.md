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
| baseline              |             2.0907 |                         0.3742 |            -0.1902 |                     0.5045 |                 0.3027 |                  1 |
| defensive_mode        |             2.0165 |                         0.3000 |            -0.1901 |                     0.4372 |                 0.2209 |                  1 |
| reduced_exposure_mode |             1.8023 |                         0.0858 |            -0.1929 |                     0.3966 |                 0.0089 |                  1 |
| cash_mode             |             1.5746 |                        -0.1418 |            -0.2024 |                     0.2877 |                -0.3055 |                  1 |

## Best Out-Of-Sample Combinations

| policy                | base_model      |   base_portfolio_size | period        |   months |   bear_months |   avg_exposure |   total_return |   bist100_total_return |   excess_return_vs_bist100 |   max_drawdown |   bist100_max_drawdown |   win_rate |   robustness_score |
|:----------------------|:----------------|----------------------:|:--------------|---------:|--------------:|---------------:|---------------:|-----------------------:|---------------------------:|---------------:|-----------------------:|-----------:|-------------------:|
| baseline              | momentum_heavy  |                     3 | out_of_sample |       31 |             7 |         1.0000 |         0.7159 |                 0.6870 |                     0.0289 |        -0.1660 |                -0.1675 |     0.6129 |             0.0032 |
| baseline              | mixed_model     |                    15 | out_of_sample |       31 |             7 |         1.0000 |         0.6820 |                 0.6870 |                    -0.0050 |        -0.1644 |                -0.1675 |     0.6129 |            -0.0274 |
| baseline              | momentum_heavy  |                    15 | out_of_sample |       31 |             7 |         1.0000 |         0.6810 |                 0.6870 |                    -0.0060 |        -0.1680 |                -0.1675 |     0.6129 |            -0.0355 |
| baseline              | low_volatility  |                    15 | out_of_sample |       31 |             7 |         1.0000 |         0.6527 |                 0.6870 |                    -0.0343 |        -0.1563 |                -0.1675 |     0.5806 |            -0.0567 |
| baseline              | trend_following |                    15 | out_of_sample |       31 |             7 |         1.0000 |         0.6539 |                 0.6870 |                    -0.0331 |        -0.1747 |                -0.1675 |     0.6129 |            -0.0760 |
| defensive_mode        | momentum_heavy  |                     3 | out_of_sample |       31 |             7 |         1.0000 |         0.6008 |                 0.6870 |                    -0.0862 |        -0.1660 |                -0.1675 |     0.5806 |            -0.1280 |
| baseline              | volume_heavy    |                    15 | out_of_sample |       31 |             7 |         1.0000 |         0.6017 |                 0.6870 |                    -0.0854 |        -0.1746 |                -0.1675 |     0.6129 |            -0.1280 |
| reduced_exposure_mode | momentum_heavy  |                     3 | out_of_sample |       31 |             7 |         0.8871 |         0.5742 |                 0.6870 |                    -0.1128 |        -0.1660 |                -0.1675 |     0.6129 |            -0.1384 |
| baseline              | trend_following |                     3 | out_of_sample |       31 |             7 |         1.0000 |         0.5682 |                 0.6870 |                    -0.1189 |        -0.1767 |                -0.1675 |     0.6129 |            -0.1658 |
| defensive_mode        | mixed_model     |                    15 | out_of_sample |       31 |             7 |         1.0000 |         0.5760 |                 0.6870 |                    -0.1111 |        -0.1757 |                -0.1675 |     0.5484 |            -0.1882 |

## Regime Signal Coverage

- Total signal months: 95
- BIST100 below MA200 months: 19
- Below-MA200 rate: 20.00%
