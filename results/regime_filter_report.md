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
| baseline              |             2.0810 |                         0.3701 |            -0.1902 |                     0.4753 |                 0.2987 |                  1 |
| defensive_mode        |             2.0074 |                         0.2966 |            -0.1901 |                     0.4100 |                 0.2174 |                  1 |
| reduced_exposure_mode |             1.7934 |                         0.0825 |            -0.1929 |                     0.3698 |                 0.0057 |                  1 |
| cash_mode             |             1.5665 |                        -0.1443 |            -0.2024 |                     0.2634 |                -0.3088 |                  1 |

## Best Out-Of-Sample Combinations

| policy                | base_model      |   base_portfolio_size | period        |   months |   bear_months |   avg_exposure |   total_return |   bist100_total_return |   excess_return_vs_bist100 |   max_drawdown |   bist100_max_drawdown |   win_rate |   robustness_score |
|:----------------------|:----------------|----------------------:|:--------------|---------:|--------------:|---------------:|---------------:|-----------------------:|---------------------------:|---------------:|-----------------------:|-----------:|-------------------:|
| baseline              | mixed_model     |                    15 | out_of_sample |       30 |             7 |         1.0000 |         0.6708 |                 0.6701 |                     0.0007 |        -0.1644 |                -0.1675 |     0.6333 |            -0.0115 |
| baseline              | momentum_heavy  |                    15 | out_of_sample |       30 |             7 |         1.0000 |         0.6659 |                 0.6701 |                    -0.0042 |        -0.1680 |                -0.1675 |     0.6333 |            -0.0235 |
| baseline              | momentum_heavy  |                     3 | out_of_sample |       30 |             7 |         1.0000 |         0.6357 |                 0.6701 |                    -0.0343 |        -0.1660 |                -0.1675 |     0.6333 |            -0.0497 |
| baseline              | low_volatility  |                    15 | out_of_sample |       30 |             7 |         1.0000 |         0.6461 |                 0.6701 |                    -0.0239 |        -0.1563 |                -0.1675 |     0.5667 |            -0.0532 |
| baseline              | trend_following |                    15 | out_of_sample |       30 |             7 |         1.0000 |         0.6390 |                 0.6701 |                    -0.0310 |        -0.1747 |                -0.1675 |     0.6333 |            -0.0637 |
| baseline              | volume_heavy    |                    15 | out_of_sample |       30 |             7 |         1.0000 |         0.5902 |                 0.6701 |                    -0.0798 |        -0.1746 |                -0.1675 |     0.6333 |            -0.1123 |
| defensive_mode        | mixed_model     |                    15 | out_of_sample |       30 |             7 |         1.0000 |         0.5654 |                 0.6701 |                    -0.1047 |        -0.1757 |                -0.1675 |     0.5667 |            -0.1727 |
| defensive_mode        | momentum_heavy  |                     3 | out_of_sample |       30 |             7 |         1.0000 |         0.5260 |                 0.6701 |                    -0.1440 |        -0.1660 |                -0.1675 |     0.6000 |            -0.1761 |
| reduced_exposure_mode | mixed_model     |                    15 | out_of_sample |       30 |             7 |         0.8833 |         0.5357 |                 0.6701 |                    -0.1344 |        -0.1817 |                -0.1675 |     0.6333 |            -0.1810 |
| reduced_exposure_mode | momentum_heavy  |                     3 | out_of_sample |       30 |             7 |         0.8833 |         0.5007 |                 0.6701 |                    -0.1694 |        -0.1660 |                -0.1675 |     0.6333 |            -0.1848 |

## Regime Signal Coverage

- Total signal months: 94
- BIST100 below MA200 months: 19
- Below-MA200 rate: 20.21%
