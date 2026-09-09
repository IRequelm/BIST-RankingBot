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
| baseline              |             2.0820 |                         0.3627 |            -0.1902 |                     0.4784 |                 0.2886 |                  1 |
| defensive_mode        |             2.0081 |                         0.2889 |            -0.1901 |                     0.4122 |                 0.2073 |                  1 |
| reduced_exposure_mode |             1.7942 |                         0.0749 |            -0.1929 |                     0.3723 |                -0.0046 |                  1 |
| cash_mode             |             1.5672 |                        -0.1521 |            -0.2024 |                     0.2653 |                -0.3176 |                  1 |

## Best Out-Of-Sample Combinations

| policy                | base_model      |   base_portfolio_size | period        |   months |   bear_months |   avg_exposure |   total_return |   bist100_total_return |   excess_return_vs_bist100 |   max_drawdown |   bist100_max_drawdown |   win_rate |   robustness_score |
|:----------------------|:----------------|----------------------:|:--------------|---------:|--------------:|---------------:|---------------:|-----------------------:|---------------------------:|---------------:|-----------------------:|-----------:|-------------------:|
| baseline              | momentum_heavy  |                     3 | out_of_sample |       32 |             7 |         1.0000 |         0.7003 |                 0.6954 |                     0.0049 |        -0.1660 |                -0.1675 |     0.5938 |            -0.0303 |
| baseline              | mixed_model     |                    15 | out_of_sample |       32 |             7 |         1.0000 |         0.6444 |                 0.6954 |                    -0.0510 |        -0.1644 |                -0.1675 |     0.5938 |            -0.0830 |
| baseline              | momentum_heavy  |                    15 | out_of_sample |       32 |             7 |         1.0000 |         0.6443 |                 0.6954 |                    -0.0511 |        -0.1680 |                -0.1675 |     0.5938 |            -0.0902 |
| baseline              | low_volatility  |                    15 | out_of_sample |       32 |             7 |         1.0000 |         0.6133 |                 0.6954 |                    -0.0821 |        -0.1563 |                -0.1675 |     0.5625 |            -0.1135 |
| baseline              | trend_following |                    15 | out_of_sample |       32 |             7 |         1.0000 |         0.6169 |                 0.6954 |                    -0.0785 |        -0.1747 |                -0.1675 |     0.5938 |            -0.1309 |
| defensive_mode        | momentum_heavy  |                     3 | out_of_sample |       32 |             7 |         1.0000 |         0.5862 |                 0.6954 |                    -0.1092 |        -0.1660 |                -0.1675 |     0.5625 |            -0.1600 |
| reduced_exposure_mode | momentum_heavy  |                     3 | out_of_sample |       32 |             7 |         0.8906 |         0.5599 |                 0.6954 |                    -0.1355 |        -0.1660 |                -0.1675 |     0.5938 |            -0.1707 |
| baseline              | volume_heavy    |                    15 | out_of_sample |       32 |             7 |         1.0000 |         0.5652 |                 0.6954 |                    -0.1302 |        -0.1746 |                -0.1675 |     0.5938 |            -0.1825 |
| baseline              | trend_following |                     3 | out_of_sample |       32 |             7 |         1.0000 |         0.5539 |                 0.6954 |                    -0.1415 |        -0.1767 |                -0.1675 |     0.5938 |            -0.1981 |
| defensive_mode        | mixed_model     |                    15 | out_of_sample |       32 |             7 |         1.0000 |         0.5407 |                 0.6954 |                    -0.1547 |        -0.1757 |                -0.1675 |     0.5312 |            -0.2404 |

## Regime Signal Coverage

- Total signal months: 96
- BIST100 below MA200 months: 19
- Below-MA200 rate: 19.79%
