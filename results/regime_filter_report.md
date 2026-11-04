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
| baseline              |             2.0117 |                         0.4251 |            -0.2002 |                     0.2674 |                 0.3298 |                  1 |
| defensive_mode        |             1.9309 |                         0.3443 |            -0.2051 |                     0.1803 |                 0.2317 |                  1 |
| reduced_exposure_mode |             1.7492 |                         0.1626 |            -0.1942 |                     0.2374 |                 0.0794 |                  1 |
| cash_mode             |             1.5441 |                        -0.0425 |            -0.2027 |                     0.1960 |                -0.2131 |                  1 |

## Best Out-Of-Sample Combinations

| policy                | base_model      |   base_portfolio_size | period        |   months |   bear_months |   avg_exposure |   total_return |   bist100_total_return |   excess_return_vs_bist100 |   max_drawdown |   bist100_max_drawdown |   win_rate |   robustness_score |
|:----------------------|:----------------|----------------------:|:--------------|---------:|--------------:|---------------:|---------------:|-----------------------:|---------------------------:|---------------:|-----------------------:|-----------:|-------------------:|
| baseline              | mixed_model     |                    15 | out_of_sample |       34 |             9 |         1.0000 |         0.4527 |                 0.2974 |                     0.1553 |        -0.1961 |                -0.2550 |     0.5882 |             0.0572 |
| baseline              | momentum_heavy  |                     3 | out_of_sample |       34 |             9 |         1.0000 |         0.4332 |                 0.2974 |                     0.1357 |        -0.1839 |                -0.2550 |     0.5588 |             0.0475 |
| reduced_exposure_mode | momentum_heavy  |                     3 | out_of_sample |       34 |             9 |         0.8676 |         0.3957 |                 0.2974 |                     0.0983 |        -0.1660 |                -0.2550 |     0.5588 |             0.0456 |
| baseline              | trend_following |                    15 | out_of_sample |       34 |             9 |         1.0000 |         0.4266 |                 0.2974 |                     0.1292 |        -0.1926 |                -0.2550 |     0.5882 |             0.0380 |
| baseline              | momentum_heavy  |                    15 | out_of_sample |       34 |             9 |         1.0000 |         0.4275 |                 0.2974 |                     0.1301 |        -0.1948 |                -0.2550 |     0.5882 |             0.0345 |
| reduced_exposure_mode | mixed_model     |                    15 | out_of_sample |       34 |             9 |         0.8676 |         0.3867 |                 0.2974 |                     0.0893 |        -0.1817 |                -0.2550 |     0.5882 |             0.0202 |
| baseline              | trend_following |                     3 | out_of_sample |       34 |             9 |         1.0000 |         0.3693 |                 0.2974 |                     0.0719 |        -0.1767 |                -0.2550 |     0.5882 |             0.0126 |
| reduced_exposure_mode | momentum_heavy  |                    15 | out_of_sample |       34 |             9 |         0.8676 |         0.3618 |                 0.2974 |                     0.0644 |        -0.1851 |                -0.2550 |     0.5882 |            -0.0117 |
| reduced_exposure_mode | trend_following |                    15 | out_of_sample |       34 |             9 |         0.8676 |         0.3609 |                 0.2974 |                     0.0635 |        -0.1882 |                -0.2550 |     0.5882 |            -0.0187 |
| reduced_exposure_mode | trend_following |                     3 | out_of_sample |       34 |             9 |         0.8676 |         0.3335 |                 0.2974 |                     0.0361 |        -0.1767 |                -0.2550 |     0.5882 |            -0.0232 |

## Regime Signal Coverage

- Total signal months: 98
- BIST100 below MA200 months: 22
- Below-MA200 rate: 22.45%
