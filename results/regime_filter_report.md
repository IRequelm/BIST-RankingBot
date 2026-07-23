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
| baseline              |             2.0705 |                         0.3616 |            -0.1902 |                     0.4438 |                 0.2885 |                  1 |
| defensive_mode        |             1.9973 |                         0.2885 |            -0.1901 |                     0.3795 |                 0.2076 |                  1 |
| reduced_exposure_mode |             1.7835 |                         0.0747 |            -0.1929 |                     0.3404 |                -0.0038 |                  1 |
| cash_mode             |             1.5574 |                        -0.1514 |            -0.2024 |                     0.2361 |                -0.3175 |                  1 |

## Best Out-Of-Sample Combinations

| policy                | base_model      |   base_portfolio_size | period        |   months |   bear_months |   avg_exposure |   total_return |   bist100_total_return |   excess_return_vs_bist100 |   max_drawdown |   bist100_max_drawdown |   win_rate |   robustness_score |
|:----------------------|:----------------|----------------------:|:--------------|---------:|--------------:|---------------:|---------------:|-----------------------:|---------------------------:|---------------:|-----------------------:|-----------:|-------------------:|
| baseline              | momentum_heavy  |                    15 | out_of_sample |       30 |             7 |         1.0000 |         0.6620 |                 0.6641 |                    -0.0020 |        -0.1680 |                -0.1675 |     0.6333 |            -0.0213 |
| baseline              | mixed_model     |                    15 | out_of_sample |       30 |             7 |         1.0000 |         0.6518 |                 0.6641 |                    -0.0122 |        -0.1644 |                -0.1675 |     0.6000 |            -0.0411 |
| baseline              | low_volatility  |                    15 | out_of_sample |       30 |             7 |         1.0000 |         0.6345 |                 0.6641 |                    -0.0296 |        -0.1563 |                -0.1675 |     0.5667 |            -0.0589 |
| baseline              | trend_following |                    15 | out_of_sample |       30 |             7 |         1.0000 |         0.6352 |                 0.6641 |                    -0.0288 |        -0.1747 |                -0.1675 |     0.6333 |            -0.0615 |
| baseline              | momentum_heavy  |                     3 | out_of_sample |       30 |             7 |         1.0000 |         0.6007 |                 0.6641 |                    -0.0634 |        -0.1660 |                -0.1675 |     0.6000 |            -0.0954 |
| baseline              | volume_heavy    |                    15 | out_of_sample |       30 |             7 |         1.0000 |         0.5722 |                 0.6641 |                    -0.0918 |        -0.1746 |                -0.1675 |     0.6000 |            -0.1409 |
| defensive_mode        | momentum_heavy  |                    15 | out_of_sample |       30 |             7 |         1.0000 |         0.5534 |                 0.6641 |                    -0.1107 |        -0.1792 |                -0.1675 |     0.5667 |            -0.1857 |
| reduced_exposure_mode | momentum_heavy  |                    15 | out_of_sample |       30 |             7 |         0.8833 |         0.5257 |                 0.6641 |                    -0.1384 |        -0.1851 |                -0.1675 |     0.6333 |            -0.1920 |
| defensive_mode        | mixed_model     |                    15 | out_of_sample |       30 |             7 |         1.0000 |         0.5477 |                 0.6641 |                    -0.1164 |        -0.1757 |                -0.1675 |     0.5333 |            -0.2011 |
| defensive_mode        | low_volatility  |                    15 | out_of_sample |       30 |             7 |         1.0000 |         0.5244 |                 0.6641 |                    -0.1397 |        -0.1661 |                -0.1675 |     0.5333 |            -0.2051 |

## Regime Signal Coverage

- Total signal months: 94
- BIST100 below MA200 months: 19
- Below-MA200 rate: 20.21%
