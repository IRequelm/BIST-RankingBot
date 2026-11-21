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
| baseline              |             2.0146 |                         0.4238 |            -0.2006 |                     0.2762 |                 0.3262 |                  1 |
| defensive_mode        |             1.9230 |                         0.3322 |            -0.2070 |                     0.1568 |                 0.2111 |                  1 |
| reduced_exposure_mode |             1.7507 |                         0.1598 |            -0.1942 |                     0.2417 |                 0.0750 |                  1 |
| cash_mode             |             1.5441 |                        -0.0467 |            -0.2027 |                     0.1960 |                -0.2174 |                  1 |

## Best Out-Of-Sample Combinations

| policy                | base_model      |   base_portfolio_size | period        |   months |   bear_months |   avg_exposure |   total_return |   bist100_total_return |   excess_return_vs_bist100 |   max_drawdown |   bist100_max_drawdown |   win_rate |   robustness_score |
|:----------------------|:----------------|----------------------:|:--------------|---------:|--------------:|---------------:|---------------:|-----------------------:|---------------------------:|---------------:|-----------------------:|-----------:|-------------------:|
| baseline              | mixed_model     |                    15 | out_of_sample |       34 |             9 |         1.0000 |         0.5176 |                 0.3101 |                     0.2075 |        -0.1961 |                -0.2550 |     0.5882 |             0.1094 |
| baseline              | trend_following |                    15 | out_of_sample |       34 |             9 |         1.0000 |         0.4590 |                 0.3101 |                     0.1489 |        -0.1926 |                -0.2550 |     0.5882 |             0.0577 |
| baseline              | momentum_heavy  |                    15 | out_of_sample |       34 |             9 |         1.0000 |         0.4599 |                 0.3101 |                     0.1498 |        -0.1948 |                -0.2550 |     0.5882 |             0.0543 |
| reduced_exposure_mode | mixed_model     |                    15 | out_of_sample |       34 |             9 |         0.8676 |         0.4181 |                 0.3101 |                     0.1080 |        -0.1817 |                -0.2550 |     0.5882 |             0.0388 |
| reduced_exposure_mode | momentum_heavy  |                     3 | out_of_sample |       34 |             9 |         0.8676 |         0.3794 |                 0.3101 |                     0.0693 |        -0.1660 |                -0.2550 |     0.5294 |             0.0019 |
| reduced_exposure_mode | momentum_heavy  |                    15 | out_of_sample |       34 |             9 |         0.8676 |         0.3775 |                 0.3101 |                     0.0674 |        -0.1851 |                -0.2550 |     0.5882 |            -0.0088 |
| reduced_exposure_mode | low_volatility  |                    15 | out_of_sample |       34 |             9 |         0.8676 |         0.3664 |                 0.3101 |                     0.0563 |        -0.1737 |                -0.2550 |     0.5588 |            -0.0117 |
| reduced_exposure_mode | trend_following |                    15 | out_of_sample |       34 |             9 |         0.8676 |         0.3766 |                 0.3101 |                     0.0665 |        -0.1882 |                -0.2550 |     0.5882 |            -0.0157 |
| baseline              | low_volatility  |                    15 | out_of_sample |       34 |             9 |         1.0000 |         0.4537 |                 0.3101 |                     0.1436 |        -0.2209 |                -0.2550 |     0.5588 |            -0.0188 |
| baseline              | momentum_heavy  |                     3 | out_of_sample |       34 |             9 |         1.0000 |         0.3998 |                 0.3101 |                     0.0897 |        -0.2000 |                -0.2550 |     0.5294 |            -0.0455 |

## Regime Signal Coverage

- Total signal months: 98
- BIST100 below MA200 months: 22
- Below-MA200 rate: 22.45%
