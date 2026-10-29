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
| baseline              |             2.0244 |                         0.4323 |            -0.1928 |                     0.3057 |                 0.3495 |                  1 |
| defensive_mode        |             1.9465 |                         0.3544 |            -0.1954 |                     0.2273 |                 0.2588 |                  1 |
| reduced_exposure_mode |             1.7549 |                         0.1628 |            -0.1934 |                     0.2546 |                 0.0787 |                  1 |
| cash_mode             |             1.5441 |                        -0.0481 |            -0.2027 |                     0.1960 |                -0.2169 |                  1 |

## Best Out-Of-Sample Combinations

| policy                | base_model      |   base_portfolio_size | period        |   months |   bear_months |   avg_exposure |   total_return |   bist100_total_return |   excess_return_vs_bist100 |   max_drawdown |   bist100_max_drawdown |   win_rate |   robustness_score |
|:----------------------|:----------------|----------------------:|:--------------|---------:|--------------:|---------------:|---------------:|-----------------------:|---------------------------:|---------------:|-----------------------:|-----------:|-------------------:|
| baseline              | mixed_model     |                    15 | out_of_sample |       33 |             8 |         1.0000 |         0.4810 |                 0.3141 |                     0.1669 |        -0.1644 |                -0.2269 |     0.5758 |             0.1259 |
| baseline              | momentum_heavy  |                     3 | out_of_sample |       33 |             8 |         1.0000 |         0.4887 |                 0.3141 |                     0.1746 |        -0.1660 |                -0.2269 |     0.5455 |             0.1153 |
| baseline              | momentum_heavy  |                    15 | out_of_sample |       33 |             8 |         1.0000 |         0.4572 |                 0.3141 |                     0.1431 |        -0.1680 |                -0.2269 |     0.5758 |             0.0949 |
| baseline              | trend_following |                    15 | out_of_sample |       33 |             8 |         1.0000 |         0.4562 |                 0.3141 |                     0.1421 |        -0.1747 |                -0.2269 |     0.5758 |             0.0807 |
| reduced_exposure_mode | momentum_heavy  |                     3 | out_of_sample |       33 |             8 |         0.8788 |         0.4210 |                 0.3141 |                     0.1069 |        -0.1660 |                -0.2269 |     0.5455 |             0.0476 |
| baseline              | trend_following |                     3 | out_of_sample |       33 |             8 |         1.0000 |         0.4223 |                 0.3141 |                     0.1082 |        -0.1767 |                -0.2269 |     0.5758 |             0.0427 |
| baseline              | low_volatility  |                    15 | out_of_sample |       33 |             8 |         1.0000 |         0.4238 |                 0.3141 |                     0.1098 |        -0.1819 |                -0.2269 |     0.5455 |             0.0186 |
| reduced_exposure_mode | mixed_model     |                    15 | out_of_sample |       33 |             8 |         0.8788 |         0.3989 |                 0.3141 |                     0.0848 |        -0.1817 |                -0.2269 |     0.5758 |             0.0094 |
| defensive_mode        | momentum_heavy  |                     3 | out_of_sample |       33 |             8 |         1.0000 |         0.3802 |                 0.3141 |                     0.0661 |        -0.1660 |                -0.2269 |     0.5152 |            -0.0084 |
| baseline              | volume_heavy    |                    15 | out_of_sample |       33 |             8 |         1.0000 |         0.3646 |                 0.3141 |                     0.0505 |        -0.1781 |                -0.2269 |     0.5758 |            -0.0179 |

## Regime Signal Coverage

- Total signal months: 97
- BIST100 below MA200 months: 21
- Below-MA200 rate: 21.65%
