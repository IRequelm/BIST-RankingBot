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
| baseline              |             2.0496 |                         0.3585 |            -0.1902 |                     0.3814 |                 0.2827 |                  1 |
| defensive_mode        |             1.9775 |                         0.2864 |            -0.1901 |                     0.3201 |                 0.2030 |                  1 |
| reduced_exposure_mode |             1.7643 |                         0.0731 |            -0.1929 |                     0.2826 |                -0.0080 |                  1 |
| cash_mode             |             1.5397 |                        -0.1514 |            -0.2024 |                     0.1829 |                -0.3194 |                  1 |

## Best Out-Of-Sample Combinations

| policy                | base_model      |   base_portfolio_size | period        |   months |   bear_months |   avg_exposure |   total_return |   bist100_total_return |   excess_return_vs_bist100 |   max_drawdown |   bist100_max_drawdown |   win_rate |   robustness_score |
|:----------------------|:----------------|----------------------:|:--------------|---------:|--------------:|---------------:|---------------:|-----------------------:|---------------------------:|---------------:|-----------------------:|-----------:|-------------------:|
| baseline              | mixed_model     |                    15 | out_of_sample |       31 |             7 |         1.0000 |         0.5918 |                 0.6110 |                    -0.0191 |        -0.1644 |                -0.1675 |     0.6129 |            -0.0416 |
| baseline              | momentum_heavy  |                    15 | out_of_sample |       31 |             7 |         1.0000 |         0.5909 |                 0.6110 |                    -0.0201 |        -0.1680 |                -0.1675 |     0.6129 |            -0.0496 |
| baseline              | low_volatility  |                    15 | out_of_sample |       31 |             7 |         1.0000 |         0.5776 |                 0.6110 |                    -0.0334 |        -0.1563 |                -0.1675 |     0.5484 |            -0.0719 |
| baseline              | trend_following |                    15 | out_of_sample |       31 |             7 |         1.0000 |         0.5652 |                 0.6110 |                    -0.0458 |        -0.1747 |                -0.1675 |     0.6129 |            -0.0886 |
| baseline              | volume_heavy    |                    15 | out_of_sample |       31 |             7 |         1.0000 |         0.5188 |                 0.6110 |                    -0.0922 |        -0.1746 |                -0.1675 |     0.6129 |            -0.1348 |
| baseline              | momentum_heavy  |                     3 | out_of_sample |       31 |             7 |         1.0000 |         0.5016 |                 0.6110 |                    -0.1094 |        -0.1660 |                -0.1675 |     0.5806 |            -0.1511 |
| defensive_mode        | mixed_model     |                    15 | out_of_sample |       31 |             7 |         1.0000 |         0.4915 |                 0.6110 |                    -0.1195 |        -0.1757 |                -0.1675 |     0.5484 |            -0.1967 |
| reduced_exposure_mode | mixed_model     |                    15 | out_of_sample |       31 |             7 |         0.8871 |         0.4631 |                 0.6110 |                    -0.1479 |        -0.1817 |                -0.1675 |     0.6129 |            -0.2047 |
| defensive_mode        | momentum_heavy  |                    15 | out_of_sample |       31 |             7 |         1.0000 |         0.4869 |                 0.6110 |                    -0.1241 |        -0.1792 |                -0.1675 |     0.5484 |            -0.2083 |
| defensive_mode        | low_volatility  |                    15 | out_of_sample |       31 |             7 |         1.0000 |         0.4713 |                 0.6110 |                    -0.1397 |        -0.1661 |                -0.1675 |     0.5161 |            -0.2137 |

## Regime Signal Coverage

- Total signal months: 95
- BIST100 below MA200 months: 19
- Below-MA200 rate: 20.00%
