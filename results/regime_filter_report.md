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
| baseline              |             2.0599 |                         0.3682 |            -0.1902 |                     0.4122 |                 0.2967 |                  1 |
| defensive_mode        |             1.9872 |                         0.2954 |            -0.1901 |                     0.3492 |                 0.2163 |                  1 |
| reduced_exposure_mode |             1.7738 |                         0.0820 |            -0.1929 |                     0.3110 |                 0.0051 |                  1 |
| cash_mode             |             1.5484 |                        -0.1434 |            -0.2024 |                     0.2089 |                -0.3070 |                  1 |

## Best Out-Of-Sample Combinations

| policy                | base_model      |   base_portfolio_size | period        |   months |   bear_months |   avg_exposure |   total_return |   bist100_total_return |   excess_return_vs_bist100 |   max_drawdown |   bist100_max_drawdown |   win_rate |   robustness_score |
|:----------------------|:----------------|----------------------:|:--------------|---------:|--------------:|---------------:|---------------:|-----------------------:|---------------------------:|---------------:|-----------------------:|-----------:|-------------------:|
| baseline              | mixed_model     |                    15 | out_of_sample |       31 |             7 |         1.0000 |         0.6015 |                 0.6129 |                    -0.0115 |        -0.1644 |                -0.1675 |     0.6129 |            -0.0339 |
| baseline              | momentum_heavy  |                    15 | out_of_sample |       31 |             7 |         1.0000 |         0.6005 |                 0.6129 |                    -0.0124 |        -0.1680 |                -0.1675 |     0.6129 |            -0.0419 |
| baseline              | low_volatility  |                    15 | out_of_sample |       31 |             7 |         1.0000 |         0.5850 |                 0.6129 |                    -0.0279 |        -0.1563 |                -0.1675 |     0.5806 |            -0.0502 |
| baseline              | trend_following |                    15 | out_of_sample |       31 |             7 |         1.0000 |         0.5747 |                 0.6129 |                    -0.0382 |        -0.1747 |                -0.1675 |     0.6129 |            -0.0811 |
| baseline              | momentum_heavy  |                     3 | out_of_sample |       31 |             7 |         1.0000 |         0.5542 |                 0.6129 |                    -0.0587 |        -0.1660 |                -0.1675 |     0.6129 |            -0.0843 |
| baseline              | volume_heavy    |                    15 | out_of_sample |       31 |             7 |         1.0000 |         0.5265 |                 0.6129 |                    -0.0864 |        -0.1746 |                -0.1675 |     0.6129 |            -0.1290 |
| defensive_mode        | mixed_model     |                    15 | out_of_sample |       31 |             7 |         1.0000 |         0.5005 |                 0.6129 |                    -0.1125 |        -0.1757 |                -0.1675 |     0.5484 |            -0.1896 |
| defensive_mode        | low_volatility  |                    15 | out_of_sample |       31 |             7 |         1.0000 |         0.4783 |                 0.6129 |                    -0.1347 |        -0.1661 |                -0.1675 |     0.5484 |            -0.1926 |
| reduced_exposure_mode | mixed_model     |                    15 | out_of_sample |       31 |             7 |         0.8871 |         0.4720 |                 0.6129 |                    -0.1410 |        -0.1817 |                -0.1675 |     0.6129 |            -0.1978 |
| defensive_mode        | momentum_heavy  |                    15 | out_of_sample |       31 |             7 |         1.0000 |         0.4959 |                 0.6129 |                    -0.1170 |        -0.1792 |                -0.1675 |     0.5484 |            -0.2012 |

## Regime Signal Coverage

- Total signal months: 95
- BIST100 below MA200 months: 19
- Below-MA200 rate: 20.00%
