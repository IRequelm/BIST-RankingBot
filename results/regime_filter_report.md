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
| baseline              |             2.0383 |                         0.4267 |            -0.2002 |                     0.3475 |                 0.3314 |                  1 |
| defensive_mode        |             1.9476 |                         0.3359 |            -0.2051 |                     0.2304 |                 0.2234 |                  1 |
| reduced_exposure_mode |             1.7623 |                         0.1507 |            -0.1942 |                     0.2768 |                 0.0675 |                  1 |
| cash_mode             |             1.5441 |                        -0.0676 |            -0.2027 |                     0.1960 |                -0.2382 |                  1 |

## Best Out-Of-Sample Combinations

| policy                | base_model      |   base_portfolio_size | period        |   months |   bear_months |   avg_exposure |   total_return |   bist100_total_return |   excess_return_vs_bist100 |   max_drawdown |   bist100_max_drawdown |   win_rate |   robustness_score |
|:----------------------|:----------------|----------------------:|:--------------|---------:|--------------:|---------------:|---------------:|-----------------------:|---------------------------:|---------------:|-----------------------:|-----------:|-------------------:|
| baseline              | mixed_model     |                    15 | out_of_sample |       34 |             9 |         1.0000 |         0.5811 |                 0.3725 |                     0.2086 |        -0.1961 |                -0.2550 |     0.5882 |             0.1105 |
| baseline              | trend_following |                    15 | out_of_sample |       34 |             9 |         1.0000 |         0.5392 |                 0.3725 |                     0.1667 |        -0.1926 |                -0.2550 |     0.5882 |             0.0755 |
| baseline              | momentum_heavy  |                    15 | out_of_sample |       34 |             9 |         1.0000 |         0.5402 |                 0.3725 |                     0.1677 |        -0.1948 |                -0.2550 |     0.5882 |             0.0721 |
| reduced_exposure_mode | mixed_model     |                    15 | out_of_sample |       34 |             9 |         0.8676 |         0.4488 |                 0.3725 |                     0.0763 |        -0.1817 |                -0.2550 |     0.5882 |             0.0071 |
| baseline              | momentum_heavy  |                     3 | out_of_sample |       34 |             9 |         1.0000 |         0.4638 |                 0.3725 |                     0.0913 |        -0.1839 |                -0.2550 |     0.5588 |             0.0030 |
| reduced_exposure_mode | momentum_heavy  |                     3 | out_of_sample |       34 |             9 |         0.8676 |         0.4106 |                 0.3725 |                     0.0381 |        -0.1660 |                -0.2550 |     0.5588 |            -0.0145 |
| baseline              | low_volatility  |                    15 | out_of_sample |       34 |             9 |         1.0000 |         0.5140 |                 0.3725 |                     0.1414 |        -0.2209 |                -0.2550 |     0.5588 |            -0.0210 |
| reduced_exposure_mode | momentum_heavy  |                    15 | out_of_sample |       34 |             9 |         0.8676 |         0.4162 |                 0.3725 |                     0.0437 |        -0.1851 |                -0.2550 |     0.5882 |            -0.0325 |
| baseline              | trend_following |                     3 | out_of_sample |       34 |             9 |         1.0000 |         0.3986 |                 0.3725 |                     0.0261 |        -0.1767 |                -0.2550 |     0.5882 |            -0.0332 |
| reduced_exposure_mode | trend_following |                    15 | out_of_sample |       34 |             9 |         0.8676 |         0.4153 |                 0.3725 |                     0.0428 |        -0.1882 |                -0.2550 |     0.5882 |            -0.0394 |

## Regime Signal Coverage

- Total signal months: 98
- BIST100 below MA200 months: 22
- Below-MA200 rate: 22.45%
