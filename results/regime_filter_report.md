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
| baseline              |             1.9969 |                         0.4247 |            -0.2049 |                     0.2231 |                 0.3162 |                  1 |
| defensive_mode        |             1.9093 |                         0.3371 |            -0.2149 |                     0.1155 |                 0.2001 |                  1 |
| reduced_exposure_mode |             1.7420 |                         0.1698 |            -0.1951 |                     0.2156 |                 0.0809 |                  1 |
| cash_mode             |             1.5441 |                        -0.0281 |            -0.2027 |                     0.1960 |                -0.1987 |                  1 |

## Best Out-Of-Sample Combinations

| policy                | base_model      |   base_portfolio_size | period        |   months |   bear_months |   avg_exposure |   total_return |   bist100_total_return |   excess_return_vs_bist100 |   max_drawdown |   bist100_max_drawdown |   win_rate |   robustness_score |
|:----------------------|:----------------|----------------------:|:--------------|---------:|--------------:|---------------:|---------------:|-----------------------:|---------------------------:|---------------:|-----------------------:|-----------:|-------------------:|
| baseline              | mixed_model     |                    15 | out_of_sample |       34 |             9 |         1.0000 |         0.4510 |                 0.2541 |                     0.1969 |        -0.1961 |                -0.2622 |     0.5882 |             0.0988 |
| reduced_exposure_mode | mixed_model     |                    15 | out_of_sample |       34 |             9 |         0.8676 |         0.3859 |                 0.2541 |                     0.1318 |        -0.1817 |                -0.2622 |     0.5882 |             0.0626 |
| reduced_exposure_mode | momentum_heavy  |                     3 | out_of_sample |       34 |             9 |         0.8676 |         0.3531 |                 0.2541 |                     0.0990 |        -0.1660 |                -0.2622 |     0.5294 |             0.0316 |
| baseline              | trend_following |                    15 | out_of_sample |       34 |             9 |         1.0000 |         0.3924 |                 0.2541 |                     0.1383 |        -0.1931 |                -0.2622 |     0.5588 |             0.0315 |
| baseline              | momentum_heavy  |                    15 | out_of_sample |       34 |             9 |         1.0000 |         0.3932 |                 0.2541 |                     0.1391 |        -0.1952 |                -0.2622 |     0.5588 |             0.0281 |
| reduced_exposure_mode | low_volatility  |                    15 | out_of_sample |       34 |             9 |         0.8676 |         0.3337 |                 0.2541 |                     0.0796 |        -0.1737 |                -0.2622 |     0.5588 |             0.0115 |
| reduced_exposure_mode | momentum_heavy  |                    15 | out_of_sample |       34 |             9 |         0.8676 |         0.3453 |                 0.2541 |                     0.0912 |        -0.1851 |                -0.2622 |     0.5588 |             0.0003 |
| reduced_exposure_mode | trend_following |                    15 | out_of_sample |       34 |             9 |         0.8676 |         0.3444 |                 0.2541 |                     0.0903 |        -0.1882 |                -0.2622 |     0.5588 |            -0.0066 |
| baseline              | low_volatility  |                    15 | out_of_sample |       34 |             9 |         1.0000 |         0.3863 |                 0.2541 |                     0.1322 |        -0.2209 |                -0.2622 |     0.5588 |            -0.0302 |
| reduced_exposure_mode | trend_following |                     3 | out_of_sample |       34 |             9 |         0.8676 |         0.2928 |                 0.2541 |                     0.0387 |        -0.1767 |                -0.2622 |     0.5588 |            -0.0353 |

## Regime Signal Coverage

- Total signal months: 98
- BIST100 below MA200 months: 22
- Below-MA200 rate: 22.45%
