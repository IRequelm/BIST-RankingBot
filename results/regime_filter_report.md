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
| baseline              |             2.0755 |                         0.3558 |            -0.1902 |                     0.4590 |                 0.2816 |                  1 |
| defensive_mode        |             2.0023 |                         0.2825 |            -0.1901 |                     0.3945 |                 0.2006 |                  1 |
| reduced_exposure_mode |             1.7883 |                         0.0686 |            -0.1929 |                     0.3547 |                -0.0110 |                  1 |
| cash_mode             |             1.5619 |                        -0.1579 |            -0.2024 |                     0.2495 |                -0.3251 |                  1 |

## Best Out-Of-Sample Combinations

| policy                | base_model      |   base_portfolio_size | period        |   months |   bear_months |   avg_exposure |   total_return |   bist100_total_return |   excess_return_vs_bist100 |   max_drawdown |   bist100_max_drawdown |   win_rate |   robustness_score |
|:----------------------|:----------------|----------------------:|:--------------|---------:|--------------:|---------------:|---------------:|-----------------------:|---------------------------:|---------------:|-----------------------:|-----------:|-------------------:|
| baseline              | mixed_model     |                    15 | out_of_sample |       30 |             7 |         1.0000 |         0.6648 |                 0.6969 |                    -0.0321 |        -0.1644 |                -0.1675 |     0.6000 |            -0.0610 |
| baseline              | momentum_heavy  |                    15 | out_of_sample |       30 |             7 |         1.0000 |         0.6577 |                 0.6969 |                    -0.0392 |        -0.1680 |                -0.1675 |     0.6000 |            -0.0752 |
| baseline              | low_volatility  |                    15 | out_of_sample |       30 |             7 |         1.0000 |         0.6365 |                 0.6969 |                    -0.0604 |        -0.1563 |                -0.1675 |     0.5667 |            -0.0897 |
| baseline              | trend_following |                    15 | out_of_sample |       30 |             7 |         1.0000 |         0.6309 |                 0.6969 |                    -0.0659 |        -0.1747 |                -0.1675 |     0.6000 |            -0.1153 |
| baseline              | momentum_heavy  |                     3 | out_of_sample |       30 |             7 |         1.0000 |         0.6022 |                 0.6969 |                    -0.0947 |        -0.1660 |                -0.1675 |     0.6000 |            -0.1268 |
| baseline              | volume_heavy    |                    15 | out_of_sample |       30 |             7 |         1.0000 |         0.5846 |                 0.6969 |                    -0.1123 |        -0.1746 |                -0.1675 |     0.6000 |            -0.1614 |
| defensive_mode        | mixed_model     |                    15 | out_of_sample |       30 |             7 |         1.0000 |         0.5598 |                 0.6969 |                    -0.1370 |        -0.1757 |                -0.1675 |     0.5333 |            -0.2217 |
| reduced_exposure_mode | mixed_model     |                    15 | out_of_sample |       30 |             7 |         0.8833 |         0.5302 |                 0.6969 |                    -0.1667 |        -0.1817 |                -0.1675 |     0.6000 |            -0.2300 |
| defensive_mode        | low_volatility  |                    15 | out_of_sample |       30 |             7 |         1.0000 |         0.5263 |                 0.6969 |                    -0.1706 |        -0.1661 |                -0.1675 |     0.5333 |            -0.2360 |
| defensive_mode        | momentum_heavy  |                    15 | out_of_sample |       30 |             7 |         1.0000 |         0.5493 |                 0.6969 |                    -0.1476 |        -0.1792 |                -0.1675 |     0.5333 |            -0.2393 |

## Regime Signal Coverage

- Total signal months: 94
- BIST100 below MA200 months: 19
- Below-MA200 rate: 20.21%
