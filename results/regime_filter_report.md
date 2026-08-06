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
| baseline              |             2.0573 |                         0.3655 |            -0.1902 |                     0.4042 |                 0.2913 |                  1 |
| defensive_mode        |             1.9848 |                         0.2930 |            -0.1901 |                     0.3420 |                 0.2113 |                  1 |
| reduced_exposure_mode |             1.7713 |                         0.0796 |            -0.1929 |                     0.3038 |                 0.0001 |                  1 |
| cash_mode             |             1.5462 |                        -0.1455 |            -0.2024 |                     0.2024 |                -0.3118 |                  1 |

## Best Out-Of-Sample Combinations

| policy                | base_model      |   base_portfolio_size | period        |   months |   bear_months |   avg_exposure |   total_return |   bist100_total_return |   excess_return_vs_bist100 |   max_drawdown |   bist100_max_drawdown |   win_rate |   robustness_score |
|:----------------------|:----------------|----------------------:|:--------------|---------:|--------------:|---------------:|---------------:|-----------------------:|---------------------------:|---------------:|-----------------------:|-----------:|-------------------:|
| baseline              | mixed_model     |                    15 | out_of_sample |       31 |             7 |         1.0000 |         0.6230 |                 0.6128 |                     0.0103 |        -0.1644 |                -0.1675 |     0.6129 |            -0.0122 |
| baseline              | momentum_heavy  |                    15 | out_of_sample |       31 |             7 |         1.0000 |         0.6220 |                 0.6128 |                     0.0093 |        -0.1680 |                -0.1675 |     0.6129 |            -0.0203 |
| baseline              | low_volatility  |                    15 | out_of_sample |       31 |             7 |         1.0000 |         0.6073 |                 0.6128 |                    -0.0054 |        -0.1563 |                -0.1675 |     0.5806 |            -0.0278 |
| baseline              | trend_following |                    15 | out_of_sample |       31 |             7 |         1.0000 |         0.5959 |                 0.6128 |                    -0.0169 |        -0.1747 |                -0.1675 |     0.6129 |            -0.0597 |
| baseline              | volume_heavy    |                    15 | out_of_sample |       31 |             7 |         1.0000 |         0.5481 |                 0.6128 |                    -0.0646 |        -0.1746 |                -0.1675 |     0.6129 |            -0.1073 |
| baseline              | momentum_heavy  |                     3 | out_of_sample |       31 |             7 |         1.0000 |         0.5227 |                 0.6128 |                    -0.0900 |        -0.1660 |                -0.1675 |     0.5806 |            -0.1318 |
| defensive_mode        | mixed_model     |                    15 | out_of_sample |       31 |             7 |         1.0000 |         0.5207 |                 0.6128 |                    -0.0921 |        -0.1757 |                -0.1675 |     0.5484 |            -0.1693 |
| defensive_mode        | low_volatility  |                    15 | out_of_sample |       31 |             7 |         1.0000 |         0.4991 |                 0.6128 |                    -0.1137 |        -0.1661 |                -0.1675 |     0.5484 |            -0.1716 |
| reduced_exposure_mode | mixed_model     |                    15 | out_of_sample |       31 |             7 |         0.8871 |         0.4918 |                 0.6128 |                    -0.1210 |        -0.1817 |                -0.1675 |     0.6129 |            -0.1778 |
| defensive_mode        | momentum_heavy  |                    15 | out_of_sample |       31 |             7 |         1.0000 |         0.5160 |                 0.6128 |                    -0.0968 |        -0.1792 |                -0.1675 |     0.5484 |            -0.1810 |

## Regime Signal Coverage

- Total signal months: 95
- BIST100 below MA200 months: 19
- Below-MA200 rate: 20.00%
