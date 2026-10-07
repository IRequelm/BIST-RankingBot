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
| baseline              |             2.0745 |                         0.4349 |            -0.1902 |                     0.4560 |                 0.3628 |                  1 |
| defensive_mode        |             1.9983 |                         0.3587 |            -0.1901 |                     0.3826 |                 0.2793 |                  1 |
| reduced_exposure_mode |             1.7811 |                         0.1416 |            -0.1929 |                     0.3332 |                 0.0641 |                  1 |
| cash_mode             |             1.5495 |                        -0.0901 |            -0.2024 |                     0.2122 |                -0.2578 |                  1 |

## Best Out-Of-Sample Combinations

| policy                | base_model      |   base_portfolio_size | period        |   months |   bear_months |   avg_exposure |   total_return |   bist100_total_return |   excess_return_vs_bist100 |   max_drawdown |   bist100_max_drawdown |   win_rate |   robustness_score |
|:----------------------|:----------------|----------------------:|:--------------|---------:|--------------:|---------------:|---------------:|-----------------------:|---------------------------:|---------------:|-----------------------:|-----------:|-------------------:|
| baseline              | momentum_heavy  |                     3 | out_of_sample |       33 |             8 |         1.0000 |         0.7119 |                 0.4564 |                     0.2555 |        -0.1660 |                -0.1728 |     0.6061 |             0.2265 |
| baseline              | mixed_model     |                    15 | out_of_sample |       33 |             8 |         1.0000 |         0.6229 |                 0.4564 |                     0.1665 |        -0.1644 |                -0.1728 |     0.6061 |             0.1407 |
| baseline              | momentum_heavy  |                    15 | out_of_sample |       33 |             8 |         1.0000 |         0.6185 |                 0.4564 |                     0.1621 |        -0.1680 |                -0.1728 |     0.6061 |             0.1292 |
| defensive_mode        | momentum_heavy  |                     3 | out_of_sample |       33 |             8 |         1.0000 |         0.6038 |                 0.4564 |                     0.1475 |        -0.1660 |                -0.1728 |     0.5758 |             0.1033 |
| baseline              | trend_following |                    15 | out_of_sample |       33 |             8 |         1.0000 |         0.5958 |                 0.4564 |                     0.1394 |        -0.1747 |                -0.1728 |     0.6061 |             0.0931 |
| baseline              | low_volatility  |                    15 | out_of_sample |       33 |             8 |         1.0000 |         0.5710 |                 0.4564 |                     0.1146 |        -0.1563 |                -0.1728 |     0.5758 |             0.0898 |
| reduced_exposure_mode | momentum_heavy  |                     3 | out_of_sample |       33 |             8 |         0.8788 |         0.5569 |                 0.4564 |                     0.1006 |        -0.1660 |                -0.1728 |     0.6061 |             0.0715 |
| baseline              | trend_following |                     3 | out_of_sample |       33 |             8 |         1.0000 |         0.5645 |                 0.4564 |                     0.1081 |        -0.1767 |                -0.1728 |     0.6061 |             0.0578 |
| baseline              | volume_heavy    |                    15 | out_of_sample |       33 |             8 |         1.0000 |         0.5362 |                 0.4564 |                     0.0798 |        -0.1746 |                -0.1728 |     0.6061 |             0.0337 |
| defensive_mode        | mixed_model     |                    15 | out_of_sample |       33 |             8 |         1.0000 |         0.4966 |                 0.4564 |                     0.0403 |        -0.1757 |                -0.1728 |     0.5455 |            -0.0384 |

## Regime Signal Coverage

- Total signal months: 97
- BIST100 below MA200 months: 21
- Below-MA200 rate: 21.65%
