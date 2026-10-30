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
| baseline              |             2.0224 |                         0.4302 |            -0.1935 |                     0.2995 |                 0.3461 |                  1 |
| defensive_mode        |             1.9444 |                         0.3522 |            -0.1963 |                     0.2209 |                 0.2549 |                  1 |
| reduced_exposure_mode |             1.7540 |                         0.1618 |            -0.1935 |                     0.2517 |                 0.0777 |                  1 |
| cash_mode             |             1.5441 |                        -0.0481 |            -0.2027 |                     0.1960 |                -0.2169 |                  1 |

## Best Out-Of-Sample Combinations

| policy                | base_model      |   base_portfolio_size | period        |   months |   bear_months |   avg_exposure |   total_return |   bist100_total_return |   excess_return_vs_bist100 |   max_drawdown |   bist100_max_drawdown |   win_rate |   robustness_score |
|:----------------------|:----------------|----------------------:|:--------------|---------:|--------------:|---------------:|---------------:|-----------------------:|---------------------------:|---------------:|-----------------------:|-----------:|-------------------:|
| baseline              | mixed_model     |                    15 | out_of_sample |       33 |             8 |         1.0000 |         0.4746 |                 0.3141 |                     0.1605 |        -0.1644 |                -0.2269 |     0.5758 |             0.1195 |
| baseline              | momentum_heavy  |                     3 | out_of_sample |       33 |             8 |         1.0000 |         0.4845 |                 0.3141 |                     0.1704 |        -0.1660 |                -0.2269 |     0.5455 |             0.1111 |
| baseline              | momentum_heavy  |                    15 | out_of_sample |       33 |             8 |         1.0000 |         0.4508 |                 0.3141 |                     0.1367 |        -0.1680 |                -0.2269 |     0.5758 |             0.0886 |
| baseline              | trend_following |                    15 | out_of_sample |       33 |             8 |         1.0000 |         0.4499 |                 0.3141 |                     0.1358 |        -0.1747 |                -0.2269 |     0.5758 |             0.0744 |
| reduced_exposure_mode | momentum_heavy  |                     3 | out_of_sample |       33 |             8 |         0.8788 |         0.4191 |                 0.3141 |                     0.1050 |        -0.1660 |                -0.2269 |     0.5455 |             0.0456 |
| baseline              | trend_following |                     3 | out_of_sample |       33 |             8 |         1.0000 |         0.4183 |                 0.3141 |                     0.1042 |        -0.1767 |                -0.2269 |     0.5758 |             0.0387 |
| reduced_exposure_mode | mixed_model     |                    15 | out_of_sample |       33 |             8 |         0.8788 |         0.3960 |                 0.3141 |                     0.0819 |        -0.1817 |                -0.2269 |     0.5758 |             0.0064 |
| baseline              | low_volatility  |                    15 | out_of_sample |       33 |             8 |         1.0000 |         0.4123 |                 0.3141 |                     0.0982 |        -0.1886 |                -0.2269 |     0.5455 |            -0.0062 |
| defensive_mode        | momentum_heavy  |                     3 | out_of_sample |       33 |             8 |         1.0000 |         0.3730 |                 0.3141 |                     0.0589 |        -0.1660 |                -0.2269 |     0.5152 |            -0.0156 |
| reduced_exposure_mode | trend_following |                     3 | out_of_sample |       33 |             8 |         0.8788 |         0.3558 |                 0.3141 |                     0.0417 |        -0.1767 |                -0.2269 |     0.5758 |            -0.0238 |

## Regime Signal Coverage

- Total signal months: 97
- BIST100 below MA200 months: 21
- Below-MA200 rate: 21.65%
