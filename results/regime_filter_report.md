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
| baseline              |             2.0537 |                         0.3578 |            -0.1903 |                     0.3936 |                 0.2859 |                  1 |
| defensive_mode        |             1.9813 |                         0.2853 |            -0.1903 |                     0.3316 |                 0.2056 |                  1 |
| reduced_exposure_mode |             1.7680 |                         0.0721 |            -0.1931 |                     0.2938 |                -0.0055 |                  1 |
| cash_mode             |             1.5431 |                        -0.1529 |            -0.2026 |                     0.1931 |                -0.3171 |                  1 |

## Best Out-Of-Sample Combinations

| policy                | base_model      |   base_portfolio_size | period        |   months |   bear_months |   avg_exposure |   total_return |   bist100_total_return |   excess_return_vs_bist100 |   max_drawdown |   bist100_max_drawdown |   win_rate |   robustness_score |
|:----------------------|:----------------|----------------------:|:--------------|---------:|--------------:|---------------:|---------------:|-----------------------:|---------------------------:|---------------:|-----------------------:|-----------:|-------------------:|
| baseline              | mixed_model     |                    15 | out_of_sample |       31 |             7 |         1.0000 |         0.5945 |                 0.6255 |                    -0.0311 |        -0.1644 |                -0.1675 |     0.6129 |            -0.0535 |
| baseline              | momentum_heavy  |                    15 | out_of_sample |       31 |             7 |         1.0000 |         0.5975 |                 0.6255 |                    -0.0280 |        -0.1680 |                -0.1675 |     0.6129 |            -0.0576 |
| baseline              | low_volatility  |                    15 | out_of_sample |       31 |             7 |         1.0000 |         0.5746 |                 0.6255 |                    -0.0509 |        -0.1563 |                -0.1675 |     0.5806 |            -0.0732 |
| baseline              | trend_following |                    15 | out_of_sample |       31 |             7 |         1.0000 |         0.5718 |                 0.6255 |                    -0.0538 |        -0.1747 |                -0.1675 |     0.6129 |            -0.0966 |
| baseline              | momentum_heavy  |                     3 | out_of_sample |       31 |             7 |         1.0000 |         0.5367 |                 0.6255 |                    -0.0889 |        -0.1660 |                -0.1675 |     0.6129 |            -0.1145 |
| baseline              | volume_heavy    |                    15 | out_of_sample |       31 |             7 |         1.0000 |         0.5176 |                 0.6255 |                    -0.1079 |        -0.1746 |                -0.1675 |     0.6129 |            -0.1506 |
| defensive_mode        | mixed_model     |                    15 | out_of_sample |       31 |             7 |         1.0000 |         0.4939 |                 0.6255 |                    -0.1316 |        -0.1757 |                -0.1675 |     0.5484 |            -0.2088 |
| defensive_mode        | low_volatility  |                    15 | out_of_sample |       31 |             7 |         1.0000 |         0.4686 |                 0.6255 |                    -0.1570 |        -0.1661 |                -0.1675 |     0.5484 |            -0.2149 |
| defensive_mode        | momentum_heavy  |                    15 | out_of_sample |       31 |             7 |         1.0000 |         0.4931 |                 0.6255 |                    -0.1325 |        -0.1792 |                -0.1675 |     0.5484 |            -0.2167 |
| reduced_exposure_mode | mixed_model     |                    15 | out_of_sample |       31 |             7 |         0.8871 |         0.4655 |                 0.6255 |                    -0.1600 |        -0.1817 |                -0.1675 |     0.6129 |            -0.2169 |

## Regime Signal Coverage

- Total signal months: 95
- BIST100 below MA200 months: 19
- Below-MA200 rate: 20.00%
