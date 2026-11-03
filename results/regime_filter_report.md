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
| baseline              |             2.0051 |                         0.4209 |            -0.2002 |                     0.2478 |                 0.3233 |                  1 |
| defensive_mode        |             1.9266 |                         0.3425 |            -0.2051 |                     0.1676 |                 0.2275 |                  1 |
| reduced_exposure_mode |             1.7460 |                         0.1618 |            -0.1942 |                     0.2277 |                 0.0763 |                  1 |
| cash_mode             |             1.5441 |                        -0.0401 |            -0.2027 |                     0.1960 |                -0.2107 |                  1 |

## Best Out-Of-Sample Combinations

| policy                | base_model      |   base_portfolio_size | period        |   months |   bear_months |   avg_exposure |   total_return |   bist100_total_return |   excess_return_vs_bist100 |   max_drawdown |   bist100_max_drawdown |   win_rate |   robustness_score |
|:----------------------|:----------------|----------------------:|:--------------|---------:|--------------:|---------------:|---------------:|-----------------------:|---------------------------:|---------------:|-----------------------:|-----------:|-------------------:|
| reduced_exposure_mode | momentum_heavy  |                     3 | out_of_sample |       34 |             9 |         0.8676 |         0.3932 |                 0.2901 |                     0.1030 |        -0.1660 |                -0.2550 |     0.5455 |             0.0437 |
| baseline              | momentum_heavy  |                     3 | out_of_sample |       34 |             9 |         1.0000 |         0.4280 |                 0.2901 |                     0.1379 |        -0.1839 |                -0.2550 |     0.5455 |             0.0429 |
| baseline              | mixed_model     |                    15 | out_of_sample |       34 |             9 |         1.0000 |         0.4168 |                 0.2901 |                     0.1267 |        -0.1961 |                -0.2550 |     0.5758 |             0.0224 |
| baseline              | trend_following |                     3 | out_of_sample |       34 |             9 |         1.0000 |         0.3643 |                 0.2901 |                     0.0742 |        -0.1767 |                -0.2550 |     0.5758 |             0.0087 |
| baseline              | trend_following |                    15 | out_of_sample |       34 |             9 |         1.0000 |         0.3931 |                 0.2901 |                     0.1030 |        -0.1926 |                -0.2550 |     0.5758 |             0.0056 |
| reduced_exposure_mode | mixed_model     |                    15 | out_of_sample |       34 |             9 |         0.8676 |         0.3694 |                 0.2901 |                     0.0793 |        -0.1817 |                -0.2550 |     0.5758 |             0.0039 |
| baseline              | momentum_heavy  |                    15 | out_of_sample |       34 |             9 |         1.0000 |         0.3940 |                 0.2901 |                     0.1039 |        -0.1948 |                -0.2550 |     0.5758 |             0.0021 |
| reduced_exposure_mode | trend_following |                     3 | out_of_sample |       34 |             9 |         0.8676 |         0.3310 |                 0.2901 |                     0.0409 |        -0.1767 |                -0.2550 |     0.5758 |            -0.0246 |
| reduced_exposure_mode | momentum_heavy  |                    15 | out_of_sample |       34 |             9 |         0.8676 |         0.3456 |                 0.2901 |                     0.0555 |        -0.1851 |                -0.2550 |     0.5758 |            -0.0269 |
| reduced_exposure_mode | trend_following |                    15 | out_of_sample |       34 |             9 |         0.8676 |         0.3448 |                 0.2901 |                     0.0547 |        -0.1882 |                -0.2550 |     0.5758 |            -0.0338 |

## Regime Signal Coverage

- Total signal months: 98
- BIST100 below MA200 months: 22
- Below-MA200 rate: 22.45%
