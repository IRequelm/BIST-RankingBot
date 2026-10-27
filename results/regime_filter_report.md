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
| baseline              |             2.0233 |                         0.4316 |            -0.1930 |                     0.3023 |                 0.3484 |                  1 |
| defensive_mode        |             1.9425 |                         0.3508 |            -0.1972 |                     0.2151 |                 0.2517 |                  1 |
| reduced_exposure_mode |             1.7544 |                         0.1628 |            -0.1934 |                     0.2530 |                 0.0788 |                  1 |
| cash_mode             |             1.5441 |                        -0.0476 |            -0.2027 |                     0.1960 |                -0.2163 |                  1 |

## Best Out-Of-Sample Combinations

| policy                | base_model      |   base_portfolio_size | period        |   months |   bear_months |   avg_exposure |   total_return |   bist100_total_return |   excess_return_vs_bist100 |   max_drawdown |   bist100_max_drawdown |   win_rate |   robustness_score |
|:----------------------|:----------------|----------------------:|:--------------|---------:|--------------:|---------------:|---------------:|-----------------------:|---------------------------:|---------------:|-----------------------:|-----------:|-------------------:|
| baseline              | momentum_heavy  |                     3 | out_of_sample |       33 |             8 |         1.0000 |         0.4974 |                 0.3125 |                     0.1848 |        -0.1660 |                -0.2278 |     0.5455 |             0.1255 |
| baseline              | mixed_model     |                    15 | out_of_sample |       33 |             8 |         1.0000 |         0.4725 |                 0.3125 |                     0.1600 |        -0.1645 |                -0.2278 |     0.5758 |             0.1189 |
| baseline              | momentum_heavy  |                    15 | out_of_sample |       33 |             8 |         1.0000 |         0.4488 |                 0.3125 |                     0.1363 |        -0.1680 |                -0.2278 |     0.5758 |             0.0882 |
| baseline              | trend_following |                    15 | out_of_sample |       33 |             8 |         1.0000 |         0.4479 |                 0.3125 |                     0.1354 |        -0.1747 |                -0.2278 |     0.5758 |             0.0739 |
| reduced_exposure_mode | momentum_heavy  |                     3 | out_of_sample |       33 |             8 |         0.8788 |         0.4250 |                 0.3125 |                     0.1125 |        -0.1660 |                -0.2278 |     0.5455 |             0.0531 |
| baseline              | trend_following |                     3 | out_of_sample |       33 |             8 |         1.0000 |         0.4306 |                 0.3125 |                     0.1181 |        -0.1767 |                -0.2278 |     0.5758 |             0.0526 |
| baseline              | low_volatility  |                    15 | out_of_sample |       33 |             8 |         1.0000 |         0.4193 |                 0.3125 |                     0.1068 |        -0.1845 |                -0.2278 |     0.5455 |             0.0105 |
| reduced_exposure_mode | mixed_model     |                    15 | out_of_sample |       33 |             8 |         0.8788 |         0.3950 |                 0.3125 |                     0.0825 |        -0.1817 |                -0.2278 |     0.5758 |             0.0071 |
| reduced_exposure_mode | trend_following |                     3 | out_of_sample |       33 |             8 |         0.8788 |         0.3614 |                 0.3125 |                     0.0489 |        -0.1767 |                -0.2278 |     0.5758 |            -0.0166 |
| defensive_mode        | momentum_heavy  |                     3 | out_of_sample |       33 |             8 |         1.0000 |         0.3664 |                 0.3125 |                     0.0539 |        -0.1660 |                -0.2278 |     0.5152 |            -0.0206 |

## Regime Signal Coverage

- Total signal months: 97
- BIST100 below MA200 months: 21
- Below-MA200 rate: 21.65%
