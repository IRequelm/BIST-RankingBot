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
| baseline              |             2.0614 |                         0.4267 |            -0.1902 |                     0.4166 |                 0.3523 |                  1 |
| defensive_mode        |             1.9884 |                         0.3537 |            -0.1901 |                     0.3529 |                 0.2719 |                  1 |
| reduced_exposure_mode |             1.7750 |                         0.1404 |            -0.1929 |                     0.3149 |                 0.0606 |                  1 |
| cash_mode             |             1.5495 |                        -0.0852 |            -0.2024 |                     0.2122 |                -0.2529 |                  1 |

## Best Out-Of-Sample Combinations

| policy                | base_model      |   base_portfolio_size | period        |   months |   bear_months |   avg_exposure |   total_return |   bist100_total_return |   excess_return_vs_bist100 |   max_drawdown |   bist100_max_drawdown |   win_rate |   robustness_score |
|:----------------------|:----------------|----------------------:|:--------------|---------:|--------------:|---------------:|---------------:|-----------------------:|---------------------------:|---------------:|-----------------------:|-----------:|-------------------:|
| baseline              | momentum_heavy  |                     3 | out_of_sample |       33 |             8 |         1.0000 |         0.6821 |                 0.4416 |                     0.2405 |        -0.1660 |                -0.1728 |     0.5938 |             0.2053 |
| baseline              | mixed_model     |                    15 | out_of_sample |       33 |             8 |         1.0000 |         0.5630 |                 0.4416 |                     0.1214 |        -0.1644 |                -0.1728 |     0.5938 |             0.0893 |
| baseline              | momentum_heavy  |                    15 | out_of_sample |       33 |             8 |         1.0000 |         0.5587 |                 0.4416 |                     0.1171 |        -0.1680 |                -0.1728 |     0.5938 |             0.0780 |
| defensive_mode        | momentum_heavy  |                     3 | out_of_sample |       33 |             8 |         1.0000 |         0.5693 |                 0.4416 |                     0.1277 |        -0.1660 |                -0.1728 |     0.5625 |             0.0769 |
| reduced_exposure_mode | momentum_heavy  |                     3 | out_of_sample |       33 |             8 |         0.8788 |         0.5433 |                 0.4416 |                     0.1016 |        -0.1660 |                -0.1728 |     0.5938 |             0.0664 |
| baseline              | low_volatility  |                    15 | out_of_sample |       33 |             8 |         1.0000 |         0.5202 |                 0.4416 |                     0.0786 |        -0.1563 |                -0.1728 |     0.5625 |             0.0472 |
| baseline              | trend_following |                    15 | out_of_sample |       33 |             8 |         1.0000 |         0.5368 |                 0.4416 |                     0.0952 |        -0.1747 |                -0.1728 |     0.5938 |             0.0428 |
| baseline              | trend_following |                     3 | out_of_sample |       33 |             8 |         1.0000 |         0.5373 |                 0.4416 |                     0.0957 |        -0.1767 |                -0.1728 |     0.5938 |             0.0391 |
| baseline              | volume_heavy    |                    15 | out_of_sample |       33 |             8 |         1.0000 |         0.4877 |                 0.4416 |                     0.0460 |        -0.1746 |                -0.1728 |     0.5938 |            -0.0062 |
| defensive_mode        | mixed_model     |                    15 | out_of_sample |       33 |             8 |         1.0000 |         0.4644 |                 0.4416 |                     0.0228 |        -0.1757 |                -0.1728 |     0.5312 |            -0.0630 |

## Regime Signal Coverage

- Total signal months: 97
- BIST100 below MA200 months: 21
- Below-MA200 rate: 21.65%
