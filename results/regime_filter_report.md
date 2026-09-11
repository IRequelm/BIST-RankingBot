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
| baseline              |             2.1051 |                         0.3862 |            -0.1902 |                     0.5476 |                 0.3170 |                  1 |
| defensive_mode        |             2.0301 |                         0.3113 |            -0.1901 |                     0.4781 |                 0.2347 |                  1 |
| reduced_exposure_mode |             1.8156 |                         0.0968 |            -0.1929 |                     0.4365 |                 0.0222 |                  1 |
| cash_mode             |             1.5869 |                        -0.1319 |            -0.2024 |                     0.3244 |                -0.2925 |                  1 |

## Best Out-Of-Sample Combinations

| policy                | base_model      |   base_portfolio_size | period        |   months |   bear_months |   avg_exposure |   total_return |   bist100_total_return |   excess_return_vs_bist100 |   max_drawdown |   bist100_max_drawdown |   win_rate |   robustness_score |
|:----------------------|:----------------|----------------------:|:--------------|---------:|--------------:|---------------:|---------------:|-----------------------:|---------------------------:|---------------:|-----------------------:|-----------:|-------------------:|
| baseline              | momentum_heavy  |                     3 | out_of_sample |       32 |             7 |         1.0000 |         0.7761 |                 0.6941 |                     0.0820 |        -0.1660 |                -0.1675 |     0.6250 |             0.0624 |
| baseline              | mixed_model     |                    15 | out_of_sample |       32 |             7 |         1.0000 |         0.7502 |                 0.6941 |                     0.0561 |        -0.1644 |                -0.1675 |     0.6250 |             0.0397 |
| baseline              | momentum_heavy  |                    15 | out_of_sample |       32 |             7 |         1.0000 |         0.7448 |                 0.6941 |                     0.0508 |        -0.1680 |                -0.1675 |     0.6250 |             0.0273 |
| baseline              | trend_following |                    15 | out_of_sample |       32 |             7 |         1.0000 |         0.7209 |                 0.6941 |                     0.0268 |        -0.1747 |                -0.1675 |     0.6250 |            -0.0100 |
| baseline              | low_volatility  |                    15 | out_of_sample |       32 |             7 |         1.0000 |         0.6911 |                 0.6941 |                    -0.0030 |        -0.1563 |                -0.1675 |     0.5938 |            -0.0187 |
| baseline              | volume_heavy    |                    15 | out_of_sample |       32 |             7 |         1.0000 |         0.6658 |                 0.6941 |                    -0.0282 |        -0.1746 |                -0.1675 |     0.6250 |            -0.0649 |
| defensive_mode        | momentum_heavy  |                     3 | out_of_sample |       32 |             7 |         1.0000 |         0.6569 |                 0.6941 |                    -0.0371 |        -0.1660 |                -0.1675 |     0.5938 |            -0.0723 |
| reduced_exposure_mode | momentum_heavy  |                     3 | out_of_sample |       32 |             7 |         0.8906 |         0.6294 |                 0.6941 |                    -0.0646 |        -0.1660 |                -0.1675 |     0.6250 |            -0.0842 |
| baseline              | trend_following |                     3 | out_of_sample |       32 |             7 |         1.0000 |         0.6232 |                 0.6941 |                    -0.0709 |        -0.1767 |                -0.1675 |     0.6250 |            -0.1118 |
| defensive_mode        | mixed_model     |                    15 | out_of_sample |       32 |             7 |         1.0000 |         0.6398 |                 0.6941 |                    -0.0543 |        -0.1757 |                -0.1675 |     0.5625 |            -0.1244 |

## Regime Signal Coverage

- Total signal months: 96
- BIST100 below MA200 months: 19
- Below-MA200 rate: 19.79%
