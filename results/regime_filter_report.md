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
| baseline              |             2.0841 |                         0.4240 |            -0.1902 |                     0.4849 |                 0.3506 |                  1 |
| defensive_mode        |             2.0101 |                         0.3499 |            -0.1901 |                     0.4181 |                 0.2691 |                  1 |
| reduced_exposure_mode |             1.7962 |                         0.1360 |            -0.1929 |                     0.3782 |                 0.0572 |                  1 |
| cash_mode             |             1.5690 |                        -0.0912 |            -0.2024 |                     0.2706 |                -0.2559 |                  1 |

## Best Out-Of-Sample Combinations

| policy                | base_model      |   base_portfolio_size | period        |   months |   bear_months |   avg_exposure |   total_return |   bist100_total_return |   excess_return_vs_bist100 |   max_drawdown |   bist100_max_drawdown |   win_rate |   robustness_score |
|:----------------------|:----------------|----------------------:|:--------------|---------:|--------------:|---------------:|---------------:|-----------------------:|---------------------------:|---------------:|-----------------------:|-----------:|-------------------:|
| baseline              | momentum_heavy  |                     3 | out_of_sample |       32 |             7 |         1.0000 |         0.7477 |                 0.5182 |                     0.2295 |        -0.1660 |                -0.1675 |     0.6250 |             0.2099 |
| baseline              | mixed_model     |                    15 | out_of_sample |       32 |             7 |         1.0000 |         0.6526 |                 0.5182 |                     0.1344 |        -0.1644 |                -0.1675 |     0.5938 |             0.1024 |
| baseline              | momentum_heavy  |                    15 | out_of_sample |       32 |             7 |         1.0000 |         0.6499 |                 0.5182 |                     0.1318 |        -0.1680 |                -0.1675 |     0.5938 |             0.0926 |
| defensive_mode        | momentum_heavy  |                     3 | out_of_sample |       32 |             7 |         1.0000 |         0.6304 |                 0.5182 |                     0.1123 |        -0.1660 |                -0.1675 |     0.5938 |             0.0771 |
| reduced_exposure_mode | momentum_heavy  |                     3 | out_of_sample |       32 |             7 |         0.8906 |         0.6034 |                 0.5182 |                     0.0852 |        -0.1660 |                -0.1675 |     0.6250 |             0.0656 |
| baseline              | trend_following |                    15 | out_of_sample |       32 |             7 |         1.0000 |         0.6249 |                 0.5182 |                     0.1067 |        -0.1747 |                -0.1675 |     0.5938 |             0.0543 |
| baseline              | low_volatility  |                    15 | out_of_sample |       32 |             7 |         1.0000 |         0.6016 |                 0.5182 |                     0.0835 |        -0.1563 |                -0.1675 |     0.5625 |             0.0521 |
| baseline              | trend_following |                     3 | out_of_sample |       32 |             7 |         1.0000 |         0.5972 |                 0.5182 |                     0.0790 |        -0.1767 |                -0.1675 |     0.6250 |             0.0381 |
| baseline              | volume_heavy    |                    15 | out_of_sample |       32 |             7 |         1.0000 |         0.5729 |                 0.5182 |                     0.0547 |        -0.1746 |                -0.1675 |     0.5938 |             0.0025 |
| defensive_mode        | mixed_model     |                    15 | out_of_sample |       32 |             7 |         1.0000 |         0.5483 |                 0.5182 |                     0.0302 |        -0.1757 |                -0.1675 |     0.5312 |            -0.0556 |

## Regime Signal Coverage

- Total signal months: 96
- BIST100 below MA200 months: 20
- Below-MA200 rate: 20.83%
