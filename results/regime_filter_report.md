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
| baseline              |             2.0206 |                         0.4160 |            -0.2003 |                     0.2943 |                 0.3198 |                  1 |
| defensive_mode        |             1.9372 |                         0.3326 |            -0.2051 |                     0.1993 |                 0.2201 |                  1 |
| reduced_exposure_mode |             1.7536 |                         0.1490 |            -0.1942 |                     0.2506 |                 0.0651 |                  1 |
| cash_mode             |             1.5441 |                        -0.0605 |            -0.2027 |                     0.1960 |                -0.2311 |                  1 |

## Best Out-Of-Sample Combinations

| policy                | base_model      |   base_portfolio_size | period        |   months |   bear_months |   avg_exposure |   total_return |   bist100_total_return |   excess_return_vs_bist100 |   max_drawdown |   bist100_max_drawdown |   win_rate |   robustness_score |
|:----------------------|:----------------|----------------------:|:--------------|---------:|--------------:|---------------:|---------------:|-----------------------:|---------------------------:|---------------:|-----------------------:|-----------:|-------------------:|
| baseline              | mixed_model     |                    15 | out_of_sample |       34 |             9 |         1.0000 |         0.5102 |                 0.3514 |                     0.1588 |        -0.1961 |                -0.2550 |     0.5882 |             0.0607 |
| baseline              | trend_following |                    15 | out_of_sample |       34 |             9 |         1.0000 |         0.4746 |                 0.3514 |                     0.1232 |        -0.1926 |                -0.2550 |     0.5882 |             0.0320 |
| baseline              | momentum_heavy  |                    15 | out_of_sample |       34 |             9 |         1.0000 |         0.4755 |                 0.3514 |                     0.1241 |        -0.1948 |                -0.2550 |     0.5882 |             0.0286 |
| reduced_exposure_mode | mixed_model     |                    15 | out_of_sample |       34 |             9 |         0.8676 |         0.4145 |                 0.3514 |                     0.0631 |        -0.1817 |                -0.2550 |     0.5882 |            -0.0061 |
| reduced_exposure_mode | momentum_heavy  |                     3 | out_of_sample |       34 |             9 |         0.8676 |         0.3893 |                 0.3514 |                     0.0378 |        -0.1660 |                -0.2550 |     0.5294 |            -0.0295 |
| reduced_exposure_mode | momentum_heavy  |                    15 | out_of_sample |       34 |             9 |         0.8676 |         0.3850 |                 0.3514 |                     0.0336 |        -0.1851 |                -0.2550 |     0.5882 |            -0.0426 |
| baseline              | momentum_heavy  |                     3 | out_of_sample |       34 |             9 |         1.0000 |         0.4200 |                 0.3514 |                     0.0686 |        -0.1884 |                -0.2550 |     0.5294 |            -0.0435 |
| reduced_exposure_mode | trend_following |                    15 | out_of_sample |       34 |             9 |         0.8676 |         0.3841 |                 0.3514 |                     0.0327 |        -0.1882 |                -0.2550 |     0.5882 |            -0.0495 |
| reduced_exposure_mode | low_volatility  |                    15 | out_of_sample |       34 |             9 |         0.8676 |         0.3622 |                 0.3514 |                     0.0108 |        -0.1737 |                -0.2550 |     0.5588 |            -0.0572 |
| baseline              | trend_following |                     3 | out_of_sample |       34 |             9 |         1.0000 |         0.3567 |                 0.3514 |                     0.0053 |        -0.1767 |                -0.2550 |     0.5588 |            -0.0687 |

## Regime Signal Coverage

- Total signal months: 98
- BIST100 below MA200 months: 22
- Below-MA200 rate: 22.45%
