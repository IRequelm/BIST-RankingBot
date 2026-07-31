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
| baseline              |             2.0554 |                         0.3798 |            -0.1902 |                     0.3986 |                 0.3058 |                  1 |
| defensive_mode        |             1.9830 |                         0.3073 |            -0.1901 |                     0.3366 |                 0.2257 |                  1 |
| reduced_exposure_mode |             1.7696 |                         0.0940 |            -0.1929 |                     0.2986 |                 0.0147 |                  1 |
| cash_mode             |             1.5446 |                        -0.1310 |            -0.2024 |                     0.1976 |                -0.2980 |                  1 |

## Best Out-Of-Sample Combinations

| policy         | base_model      |   base_portfolio_size | period        |   months |   bear_months |   avg_exposure |   total_return |   bist100_total_return |   excess_return_vs_bist100 |   max_drawdown |   bist100_max_drawdown |   win_rate |   robustness_score |
|:---------------|:----------------|----------------------:|:--------------|---------:|--------------:|---------------:|---------------:|-----------------------:|---------------------------:|---------------:|-----------------------:|-----------:|-------------------:|
| baseline       | momentum_heavy  |                    15 | out_of_sample |       30 |             7 |         1.0000 |         0.6010 |                 0.5645 |                     0.0365 |        -0.1680 |                -0.1675 |     0.6000 |             0.0005 |
| baseline       | mixed_model     |                    15 | out_of_sample |       30 |             7 |         1.0000 |         0.5919 |                 0.5645 |                     0.0274 |        -0.1644 |                -0.1675 |     0.6000 |            -0.0015 |
| baseline       | low_volatility  |                    15 | out_of_sample |       30 |             7 |         1.0000 |         0.5765 |                 0.5645 |                     0.0120 |        -0.1563 |                -0.1675 |     0.5667 |            -0.0174 |
| baseline       | trend_following |                    15 | out_of_sample |       30 |             7 |         1.0000 |         0.5752 |                 0.5645 |                     0.0107 |        -0.1747 |                -0.1675 |     0.6000 |            -0.0386 |
| baseline       | momentum_heavy  |                     3 | out_of_sample |       30 |             7 |         1.0000 |         0.5559 |                 0.5645 |                    -0.0085 |        -0.1660 |                -0.1675 |     0.6000 |            -0.0406 |
| baseline       | volume_heavy    |                    15 | out_of_sample |       30 |             7 |         1.0000 |         0.5152 |                 0.5645 |                    -0.0493 |        -0.1746 |                -0.1675 |     0.6000 |            -0.0984 |
| defensive_mode | mixed_model     |                    15 | out_of_sample |       30 |             7 |         1.0000 |         0.4915 |                 0.5645 |                    -0.0729 |        -0.1757 |                -0.1675 |     0.5333 |            -0.1577 |
| defensive_mode | low_volatility  |                    15 | out_of_sample |       30 |             7 |         1.0000 |         0.4703 |                 0.5645 |                    -0.0942 |        -0.1661 |                -0.1675 |     0.5333 |            -0.1597 |
| defensive_mode | momentum_heavy  |                    15 | out_of_sample |       30 |             7 |         1.0000 |         0.4963 |                 0.5645 |                    -0.0682 |        -0.1792 |                -0.1675 |     0.5333 |            -0.1599 |
| defensive_mode | momentum_heavy  |                     3 | out_of_sample |       30 |             7 |         1.0000 |         0.4516 |                 0.5645 |                    -0.1129 |        -0.1660 |                -0.1675 |     0.5667 |            -0.1616 |

## Regime Signal Coverage

- Total signal months: 94
- BIST100 below MA200 months: 19
- Below-MA200 rate: 20.21%
