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
| baseline              |             2.0636 |                         0.4212 |            -0.1902 |                     0.4231 |                 0.3479 |                  1 |
| defensive_mode        |             1.9894 |                         0.3471 |            -0.1901 |                     0.3561 |                 0.2677 |                  1 |
| reduced_exposure_mode |             1.7761 |                         0.1337 |            -0.1929 |                     0.3179 |                 0.0550 |                  1 |
| cash_mode             |             1.5495 |                        -0.0928 |            -0.2024 |                     0.2122 |                -0.2606 |                  1 |

## Best Out-Of-Sample Combinations

| policy                | base_model      |   base_portfolio_size | period        |   months |   bear_months |   avg_exposure |   total_return |   bist100_total_return |   excess_return_vs_bist100 |   max_drawdown |   bist100_max_drawdown |   win_rate |   robustness_score |
|:----------------------|:----------------|----------------------:|:--------------|---------:|--------------:|---------------:|---------------:|-----------------------:|---------------------------:|---------------:|-----------------------:|-----------:|-------------------:|
| baseline              | momentum_heavy  |                     3 | out_of_sample |       33 |             8 |         1.0000 |         0.6695 |                 0.4646 |                     0.2050 |        -0.1660 |                -0.1728 |     0.5758 |             0.1608 |
| baseline              | mixed_model     |                    15 | out_of_sample |       33 |             8 |         1.0000 |         0.5870 |                 0.4646 |                     0.1224 |        -0.1644 |                -0.1728 |     0.6061 |             0.0966 |
| baseline              | momentum_heavy  |                    15 | out_of_sample |       33 |             8 |         1.0000 |         0.5827 |                 0.4646 |                     0.1181 |        -0.1680 |                -0.1728 |     0.6061 |             0.0852 |
| defensive_mode        | momentum_heavy  |                     3 | out_of_sample |       33 |             8 |         1.0000 |         0.5730 |                 0.4646 |                     0.1084 |        -0.1660 |                -0.1728 |     0.5758 |             0.0642 |
| baseline              | trend_following |                    15 | out_of_sample |       33 |             8 |         1.0000 |         0.5605 |                 0.4646 |                     0.0959 |        -0.1747 |                -0.1728 |     0.6061 |             0.0496 |
| baseline              | low_volatility  |                    15 | out_of_sample |       33 |             8 |         1.0000 |         0.5389 |                 0.4646 |                     0.0743 |        -0.1563 |                -0.1728 |     0.5758 |             0.0495 |
| reduced_exposure_mode | momentum_heavy  |                     3 | out_of_sample |       33 |             8 |         0.8788 |         0.5375 |                 0.4646 |                     0.0729 |        -0.1660 |                -0.1728 |     0.5758 |             0.0287 |
| baseline              | trend_following |                     3 | out_of_sample |       33 |             8 |         1.0000 |         0.5258 |                 0.4646 |                     0.0612 |        -0.1767 |                -0.1728 |     0.5758 |            -0.0043 |
| baseline              | volume_heavy    |                    15 | out_of_sample |       33 |             8 |         1.0000 |         0.5033 |                 0.4646 |                     0.0387 |        -0.1746 |                -0.1728 |     0.6061 |            -0.0074 |
| defensive_mode        | mixed_model     |                    15 | out_of_sample |       33 |             8 |         1.0000 |         0.4679 |                 0.4646 |                     0.0033 |        -0.1757 |                -0.1728 |     0.5455 |            -0.0753 |

## Regime Signal Coverage

- Total signal months: 97
- BIST100 below MA200 months: 21
- Below-MA200 rate: 21.65%
