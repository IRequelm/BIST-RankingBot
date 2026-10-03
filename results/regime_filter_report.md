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
| baseline              |             2.0658 |                         0.4303 |            -0.1902 |                     0.4298 |                 0.3582 |                  1 |
| defensive_mode        |             1.9925 |                         0.3570 |            -0.1901 |                     0.3652 |                 0.2776 |                  1 |
| reduced_exposure_mode |             1.7771 |                         0.1416 |            -0.1929 |                     0.3210 |                 0.0641 |                  1 |
| cash_mode             |             1.5495 |                        -0.0860 |            -0.2024 |                     0.2122 |                -0.2537 |                  1 |

## Best Out-Of-Sample Combinations

| policy                | base_model      |   base_portfolio_size | period        |   months |   bear_months |   avg_exposure |   total_return |   bist100_total_return |   excess_return_vs_bist100 |   max_drawdown |   bist100_max_drawdown |   win_rate |   robustness_score |
|:----------------------|:----------------|----------------------:|:--------------|---------:|--------------:|---------------:|---------------:|-----------------------:|---------------------------:|---------------:|-----------------------:|-----------:|-------------------:|
| baseline              | momentum_heavy  |                     3 | out_of_sample |       33 |             8 |         1.0000 |         0.6848 |                 0.4441 |                     0.2406 |        -0.1660 |                -0.1728 |     0.6061 |             0.2116 |
| baseline              | mixed_model     |                    15 | out_of_sample |       33 |             8 |         1.0000 |         0.5916 |                 0.4441 |                     0.1474 |        -0.1644 |                -0.1728 |     0.6061 |             0.1216 |
| baseline              | momentum_heavy  |                    15 | out_of_sample |       33 |             8 |         1.0000 |         0.5872 |                 0.4441 |                     0.1431 |        -0.1680 |                -0.1728 |     0.6061 |             0.1101 |
| defensive_mode        | momentum_heavy  |                     3 | out_of_sample |       33 |             8 |         1.0000 |         0.5836 |                 0.4441 |                     0.1394 |        -0.1660 |                -0.1728 |     0.5758 |             0.0953 |
| baseline              | trend_following |                    15 | out_of_sample |       33 |             8 |         1.0000 |         0.5649 |                 0.4441 |                     0.1208 |        -0.1747 |                -0.1728 |     0.6061 |             0.0745 |
| reduced_exposure_mode | momentum_heavy  |                     3 | out_of_sample |       33 |             8 |         0.8788 |         0.5445 |                 0.4441 |                     0.1003 |        -0.1660 |                -0.1728 |     0.6061 |             0.0713 |
| baseline              | low_volatility  |                    15 | out_of_sample |       33 |             8 |         1.0000 |         0.5398 |                 0.4441 |                     0.0957 |        -0.1563 |                -0.1728 |     0.5758 |             0.0709 |
| baseline              | trend_following |                     3 | out_of_sample |       33 |             8 |         1.0000 |         0.5397 |                 0.4441 |                     0.0956 |        -0.1767 |                -0.1728 |     0.6061 |             0.0452 |
| baseline              | volume_heavy    |                    15 | out_of_sample |       33 |             8 |         1.0000 |         0.5054 |                 0.4441 |                     0.0612 |        -0.1746 |                -0.1728 |     0.6061 |             0.0152 |
| defensive_mode        | mixed_model     |                    15 | out_of_sample |       33 |             8 |         1.0000 |         0.4777 |                 0.4441 |                     0.0336 |        -0.1757 |                -0.1728 |     0.5455 |            -0.0450 |

## Regime Signal Coverage

- Total signal months: 97
- BIST100 below MA200 months: 21
- Below-MA200 rate: 21.65%
