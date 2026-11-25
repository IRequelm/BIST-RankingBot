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
| baseline              |             2.0099 |                         0.4255 |            -0.2011 |                     0.2621 |                 0.3267 |                  1 |
| defensive_mode        |             1.9183 |                         0.3340 |            -0.2094 |                     0.1427 |                 0.2080 |                  1 |
| reduced_exposure_mode |             1.7483 |                         0.1640 |            -0.1943 |                     0.2348 |                 0.0787 |                  1 |
| cash_mode             |             1.5441 |                        -0.0403 |            -0.2027 |                     0.1960 |                -0.2109 |                  1 |

## Best Out-Of-Sample Combinations

| policy                | base_model      |   base_portfolio_size | period        |   months |   bear_months |   avg_exposure |   total_return |   bist100_total_return |   excess_return_vs_bist100 |   max_drawdown |   bist100_max_drawdown |   win_rate |   robustness_score |
|:----------------------|:----------------|----------------------:|:--------------|---------:|--------------:|---------------:|---------------:|-----------------------:|---------------------------:|---------------:|-----------------------:|-----------:|-------------------:|
| baseline              | mixed_model     |                    15 | out_of_sample |       34 |             9 |         1.0000 |         0.5001 |                 0.2906 |                     0.2095 |        -0.1961 |                -0.2550 |     0.5882 |             0.1114 |
| baseline              | trend_following |                    15 | out_of_sample |       34 |             9 |         1.0000 |         0.4410 |                 0.2906 |                     0.1504 |        -0.1926 |                -0.2550 |     0.5882 |             0.0592 |
| baseline              | momentum_heavy  |                    15 | out_of_sample |       34 |             9 |         1.0000 |         0.4419 |                 0.2906 |                     0.1513 |        -0.1948 |                -0.2550 |     0.5882 |             0.0558 |
| reduced_exposure_mode | mixed_model     |                    15 | out_of_sample |       34 |             9 |         0.8676 |         0.4097 |                 0.2906 |                     0.1191 |        -0.1817 |                -0.2550 |     0.5882 |             0.0499 |
| reduced_exposure_mode | momentum_heavy  |                     3 | out_of_sample |       34 |             9 |         0.8676 |         0.3718 |                 0.2906 |                     0.0812 |        -0.1660 |                -0.2550 |     0.5294 |             0.0138 |
| reduced_exposure_mode | momentum_heavy  |                    15 | out_of_sample |       34 |             9 |         0.8676 |         0.3688 |                 0.2906 |                     0.0782 |        -0.1851 |                -0.2550 |     0.5882 |             0.0020 |
| reduced_exposure_mode | low_volatility  |                    15 | out_of_sample |       34 |             9 |         0.8676 |         0.3571 |                 0.2906 |                     0.0664 |        -0.1737 |                -0.2550 |     0.5588 |            -0.0016 |
| reduced_exposure_mode | trend_following |                    15 | out_of_sample |       34 |             9 |         0.8676 |         0.3679 |                 0.2906 |                     0.0773 |        -0.1882 |                -0.2550 |     0.5882 |            -0.0049 |
| baseline              | low_volatility  |                    15 | out_of_sample |       34 |             9 |         1.0000 |         0.4344 |                 0.2906 |                     0.1438 |        -0.2209 |                -0.2550 |     0.5588 |            -0.0186 |
| baseline              | trend_following |                     3 | out_of_sample |       34 |             9 |         1.0000 |         0.3225 |                 0.2906 |                     0.0319 |        -0.1767 |                -0.2550 |     0.5588 |            -0.0421 |

## Regime Signal Coverage

- Total signal months: 98
- BIST100 below MA200 months: 22
- Below-MA200 rate: 22.45%
