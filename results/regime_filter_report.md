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
| baseline              |             2.0651 |                         0.3550 |            -0.1903 |                     0.4278 |                 0.2831 |                  1 |
| defensive_mode        |             1.9921 |                         0.2820 |            -0.1903 |                     0.3641 |                 0.2023 |                  1 |
| reduced_exposure_mode |             1.7786 |                         0.0685 |            -0.1931 |                     0.3255 |                -0.0091 |                  1 |
| cash_mode             |             1.5528 |                        -0.1573 |            -0.2026 |                     0.2222 |                -0.3216 |                  1 |

## Best Out-Of-Sample Combinations

| policy                | base_model      |   base_portfolio_size | period        |   months |   bear_months |   avg_exposure |   total_return |   bist100_total_return |   excess_return_vs_bist100 |   max_drawdown |   bist100_max_drawdown |   win_rate |   robustness_score |
|:----------------------|:----------------|----------------------:|:--------------|---------:|--------------:|---------------:|---------------:|-----------------------:|---------------------------:|---------------:|-----------------------:|-----------:|-------------------:|
| baseline              | mixed_model     |                    15 | out_of_sample |       31 |             7 |         1.0000 |         0.6274 |                 0.6680 |                    -0.0405 |        -0.1644 |                -0.1675 |     0.6129 |            -0.0630 |
| baseline              | momentum_heavy  |                    15 | out_of_sample |       31 |             7 |         1.0000 |         0.6306 |                 0.6680 |                    -0.0374 |        -0.1680 |                -0.1675 |     0.6129 |            -0.0670 |
| baseline              | low_volatility  |                    15 | out_of_sample |       31 |             7 |         1.0000 |         0.6041 |                 0.6680 |                    -0.0639 |        -0.1563 |                -0.1675 |     0.5806 |            -0.0863 |
| baseline              | trend_following |                    15 | out_of_sample |       31 |             7 |         1.0000 |         0.6043 |                 0.6680 |                    -0.0637 |        -0.1747 |                -0.1675 |     0.6129 |            -0.1066 |
| baseline              | momentum_heavy  |                     3 | out_of_sample |       31 |             7 |         1.0000 |         0.5738 |                 0.6680 |                    -0.0942 |        -0.1660 |                -0.1675 |     0.6129 |            -0.1198 |
| baseline              | volume_heavy    |                    15 | out_of_sample |       31 |             7 |         1.0000 |         0.5490 |                 0.6680 |                    -0.1190 |        -0.1746 |                -0.1675 |     0.6129 |            -0.1616 |
| defensive_mode        | mixed_model     |                    15 | out_of_sample |       31 |             7 |         1.0000 |         0.5248 |                 0.6680 |                    -0.1432 |        -0.1757 |                -0.1675 |     0.5484 |            -0.2203 |
| defensive_mode        | momentum_heavy  |                    15 | out_of_sample |       31 |             7 |         1.0000 |         0.5240 |                 0.6680 |                    -0.1440 |        -0.1792 |                -0.1675 |     0.5484 |            -0.2282 |
| reduced_exposure_mode | mixed_model     |                    15 | out_of_sample |       31 |             7 |         0.8871 |         0.4958 |                 0.6680 |                    -0.1721 |        -0.1817 |                -0.1675 |     0.6129 |            -0.2290 |
| defensive_mode        | low_volatility  |                    15 | out_of_sample |       31 |             7 |         1.0000 |         0.4960 |                 0.6680 |                    -0.1720 |        -0.1661 |                -0.1675 |     0.5484 |            -0.2299 |

## Regime Signal Coverage

- Total signal months: 95
- BIST100 below MA200 months: 19
- Below-MA200 rate: 20.00%
