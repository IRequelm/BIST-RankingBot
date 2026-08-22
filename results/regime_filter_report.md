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
| baseline              |             2.0867 |                         0.3631 |            -0.1902 |                     0.4925 |                 0.2916 |                  1 |
| defensive_mode        |             2.0127 |                         0.2891 |            -0.1901 |                     0.4257 |                 0.2100 |                  1 |
| reduced_exposure_mode |             1.7986 |                         0.0750 |            -0.1929 |                     0.3855 |                -0.0019 |                  1 |
| cash_mode             |             1.5712 |                        -0.1523 |            -0.2024 |                     0.2775 |                -0.3160 |                  1 |

## Best Out-Of-Sample Combinations

| policy                | base_model      |   base_portfolio_size | period        |   months |   bear_months |   avg_exposure |   total_return |   bist100_total_return |   excess_return_vs_bist100 |   max_drawdown |   bist100_max_drawdown |   win_rate |   robustness_score |
|:----------------------|:----------------|----------------------:|:--------------|---------:|--------------:|---------------:|---------------:|-----------------------:|---------------------------:|---------------:|-----------------------:|-----------:|-------------------:|
| baseline              | momentum_heavy  |                     3 | out_of_sample |       31 |             7 |         1.0000 |         0.6957 |                 0.7083 |                    -0.0126 |        -0.1660 |                -0.1675 |     0.6129 |            -0.0382 |
| baseline              | mixed_model     |                    15 | out_of_sample |       31 |             7 |         1.0000 |         0.6640 |                 0.7083 |                    -0.0443 |        -0.1644 |                -0.1675 |     0.6129 |            -0.0668 |
| baseline              | momentum_heavy  |                    15 | out_of_sample |       31 |             7 |         1.0000 |         0.6630 |                 0.7083 |                    -0.0453 |        -0.1680 |                -0.1675 |     0.6129 |            -0.0749 |
| baseline              | low_volatility  |                    15 | out_of_sample |       31 |             7 |         1.0000 |         0.6417 |                 0.7083 |                    -0.0666 |        -0.1563 |                -0.1675 |     0.5806 |            -0.0889 |
| baseline              | trend_following |                    15 | out_of_sample |       31 |             7 |         1.0000 |         0.6361 |                 0.7083 |                    -0.0722 |        -0.1747 |                -0.1675 |     0.6129 |            -0.1150 |
| defensive_mode        | momentum_heavy  |                     3 | out_of_sample |       31 |             7 |         1.0000 |         0.5820 |                 0.7083 |                    -0.1263 |        -0.1660 |                -0.1675 |     0.5806 |            -0.1680 |
| baseline              | volume_heavy    |                    15 | out_of_sample |       31 |             7 |         1.0000 |         0.5822 |                 0.7083 |                    -0.1261 |        -0.1746 |                -0.1675 |     0.6129 |            -0.1688 |
| reduced_exposure_mode | momentum_heavy  |                     3 | out_of_sample |       31 |             7 |         0.8871 |         0.5558 |                 0.7083 |                    -0.1525 |        -0.1660 |                -0.1675 |     0.6129 |            -0.1782 |
| baseline              | trend_following |                     3 | out_of_sample |       31 |             7 |         1.0000 |         0.5497 |                 0.7083 |                    -0.1586 |        -0.1767 |                -0.1675 |     0.6129 |            -0.2055 |
| defensive_mode        | mixed_model     |                    15 | out_of_sample |       31 |             7 |         1.0000 |         0.5590 |                 0.7083 |                    -0.1493 |        -0.1757 |                -0.1675 |     0.5484 |            -0.2264 |

## Regime Signal Coverage

- Total signal months: 95
- BIST100 below MA200 months: 19
- Below-MA200 rate: 20.00%
