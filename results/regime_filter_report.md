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
| baseline              |             2.0701 |                         0.3617 |            -0.1902 |                     0.4427 |                 0.2899 |                  1 |
| defensive_mode        |             1.9969 |                         0.2885 |            -0.1901 |                     0.3783 |                 0.2091 |                  1 |
| reduced_exposure_mode |             1.7832 |                         0.0748 |            -0.1929 |                     0.3393 |                -0.0023 |                  1 |
| cash_mode             |             1.5571 |                        -0.1513 |            -0.2024 |                     0.2350 |                -0.3152 |                  1 |

## Best Out-Of-Sample Combinations

| policy                | base_model      |   base_portfolio_size | period        |   months |   bear_months |   avg_exposure |   total_return |   bist100_total_return |   excess_return_vs_bist100 |   max_drawdown |   bist100_max_drawdown |   win_rate |   robustness_score |
|:----------------------|:----------------|----------------------:|:--------------|---------:|--------------:|---------------:|---------------:|-----------------------:|---------------------------:|---------------:|-----------------------:|-----------:|-------------------:|
| baseline              | momentum_heavy  |                     3 | out_of_sample |       31 |             7 |         1.0000 |         0.6244 |                 0.6628 |                    -0.0383 |        -0.1660 |                -0.1675 |     0.6129 |            -0.0640 |
| baseline              | mixed_model     |                    15 | out_of_sample |       31 |             7 |         1.0000 |         0.6193 |                 0.6628 |                    -0.0434 |        -0.1644 |                -0.1675 |     0.6129 |            -0.0659 |
| baseline              | momentum_heavy  |                    15 | out_of_sample |       31 |             7 |         1.0000 |         0.6178 |                 0.6628 |                    -0.0450 |        -0.1680 |                -0.1675 |     0.6129 |            -0.0745 |
| baseline              | low_volatility  |                    15 | out_of_sample |       31 |             7 |         1.0000 |         0.6008 |                 0.6628 |                    -0.0619 |        -0.1563 |                -0.1675 |     0.5806 |            -0.0843 |
| baseline              | trend_following |                    15 | out_of_sample |       31 |             7 |         1.0000 |         0.5917 |                 0.6628 |                    -0.0711 |        -0.1747 |                -0.1675 |     0.6129 |            -0.1140 |
| baseline              | volume_heavy    |                    15 | out_of_sample |       31 |             7 |         1.0000 |         0.5444 |                 0.6628 |                    -0.1184 |        -0.1746 |                -0.1675 |     0.6129 |            -0.1611 |
| defensive_mode        | momentum_heavy  |                     3 | out_of_sample |       31 |             7 |         1.0000 |         0.5155 |                 0.6628 |                    -0.1473 |        -0.1660 |                -0.1675 |     0.5806 |            -0.1890 |
| reduced_exposure_mode | momentum_heavy  |                     3 | out_of_sample |       31 |             7 |         0.8871 |         0.4903 |                 0.6628 |                    -0.1724 |        -0.1660 |                -0.1675 |     0.6129 |            -0.1981 |
| defensive_mode        | mixed_model     |                    15 | out_of_sample |       31 |             7 |         1.0000 |         0.5172 |                 0.6628 |                    -0.1455 |        -0.1757 |                -0.1675 |     0.5484 |            -0.2227 |
| baseline              | trend_following |                     3 | out_of_sample |       31 |             7 |         1.0000 |         0.4846 |                 0.6628 |                    -0.1782 |        -0.1767 |                -0.1675 |     0.6129 |            -0.2252 |

## Regime Signal Coverage

- Total signal months: 95
- BIST100 below MA200 months: 19
- Below-MA200 rate: 20.00%
