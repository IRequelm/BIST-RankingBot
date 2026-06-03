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
| baseline              |             2.0778 |                         0.3860 |            -0.1902 |                     0.4658 |                 0.3158 |                  1 |
| defensive_mode        |             2.0045 |                         0.3128 |            -0.1901 |                     0.4012 |                 0.2346 |                  1 |
| reduced_exposure_mode |             1.7905 |                         0.0987 |            -0.1929 |                     0.3611 |                 0.0231 |                  1 |
| cash_mode             |             1.5639 |                        -0.1278 |            -0.2024 |                     0.2555 |                -0.2920 |                  1 |

## Best Out-Of-Sample Combinations

| policy                | base_model      |   base_portfolio_size | period        |   months |   bear_months |   avg_exposure |   total_return |   bist100_total_return |   excess_return_vs_bist100 |   max_drawdown |   bist100_max_drawdown |   win_rate |   robustness_score |
|:----------------------|:----------------|----------------------:|:--------------|---------:|--------------:|---------------:|---------------:|-----------------------:|---------------------------:|---------------:|-----------------------:|-----------:|-------------------:|
| baseline              | mixed_model     |                    15 | out_of_sample |       29 |             7 |         1.0000 |         0.6565 |                 0.6129 |                     0.0436 |        -0.1644 |                -0.1675 |     0.6207 |             0.0251 |
| baseline              | low_volatility  |                    15 | out_of_sample |       29 |             7 |         1.0000 |         0.6447 |                 0.6129 |                     0.0319 |        -0.1563 |                -0.1675 |     0.5862 |             0.0123 |
| baseline              | momentum_heavy  |                    15 | out_of_sample |       29 |             7 |         1.0000 |         0.6267 |                 0.6129 |                     0.0139 |        -0.1680 |                -0.1675 |     0.6207 |            -0.0118 |
| baseline              | trend_following |                    15 | out_of_sample |       29 |             7 |         1.0000 |         0.6228 |                 0.6129 |                     0.0099 |        -0.1747 |                -0.1675 |     0.6207 |            -0.0291 |
| baseline              | momentum_heavy  |                     3 | out_of_sample |       29 |             7 |         1.0000 |         0.5784 |                 0.6129 |                    -0.0344 |        -0.1660 |                -0.1675 |     0.6207 |            -0.0562 |
| baseline              | volume_heavy    |                    15 | out_of_sample |       29 |             7 |         1.0000 |         0.5593 |                 0.6129 |                    -0.0536 |        -0.1746 |                -0.1675 |     0.6207 |            -0.0923 |
| defensive_mode        | low_volatility  |                    15 | out_of_sample |       29 |             7 |         1.0000 |         0.5339 |                 0.6129 |                    -0.0789 |        -0.1661 |                -0.1675 |     0.5517 |            -0.1352 |
| defensive_mode        | mixed_model     |                    15 | out_of_sample |       29 |             7 |         1.0000 |         0.5520 |                 0.6129 |                    -0.0608 |        -0.1757 |                -0.1675 |     0.5517 |            -0.1363 |
| reduced_exposure_mode | mixed_model     |                    15 | out_of_sample |       29 |             7 |         0.8793 |         0.5225 |                 0.6129 |                    -0.0903 |        -0.1817 |                -0.1675 |     0.6207 |            -0.1433 |
| reduced_exposure_mode | low_volatility  |                    15 | out_of_sample |       29 |             7 |         0.8793 |         0.5084 |                 0.6129 |                    -0.1045 |        -0.1688 |                -0.1675 |     0.5862 |            -0.1490 |

## Regime Signal Coverage

- Total signal months: 93
- BIST100 below MA200 months: 19
- Below-MA200 rate: 20.43%
