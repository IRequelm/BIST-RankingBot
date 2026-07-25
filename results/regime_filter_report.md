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
| baseline              |             2.0691 |                         0.3680 |            -0.1902 |                     0.4398 |                 0.2949 |                  1 |
| defensive_mode        |             1.9961 |                         0.2949 |            -0.1901 |                     0.3759 |                 0.2141 |                  1 |
| reduced_exposure_mode |             1.7823 |                         0.0812 |            -0.1929 |                     0.3368 |                 0.0027 |                  1 |
| cash_mode             |             1.5564 |                        -0.1448 |            -0.2024 |                     0.2328 |                -0.3109 |                  1 |

## Best Out-Of-Sample Combinations

| policy                | base_model      |   base_portfolio_size | period        |   months |   bear_months |   avg_exposure |   total_return |   bist100_total_return |   excess_return_vs_bist100 |   max_drawdown |   bist100_max_drawdown |   win_rate |   robustness_score |
|:----------------------|:----------------|----------------------:|:--------------|---------:|--------------:|---------------:|---------------:|-----------------------:|---------------------------:|---------------:|-----------------------:|-----------:|-------------------:|
| baseline              | momentum_heavy  |                    15 | out_of_sample |       30 |             7 |         1.0000 |         0.6673 |                 0.6411 |                     0.0262 |        -0.1680 |                -0.1675 |     0.6333 |             0.0069 |
| baseline              | mixed_model     |                    15 | out_of_sample |       30 |             7 |         1.0000 |         0.6477 |                 0.6411 |                     0.0066 |        -0.1644 |                -0.1675 |     0.6000 |            -0.0223 |
| baseline              | trend_following |                    15 | out_of_sample |       30 |             7 |         1.0000 |         0.6404 |                 0.6411 |                    -0.0007 |        -0.1747 |                -0.1675 |     0.6333 |            -0.0333 |
| baseline              | low_volatility  |                    15 | out_of_sample |       30 |             7 |         1.0000 |         0.6256 |                 0.6411 |                    -0.0155 |        -0.1563 |                -0.1675 |     0.5667 |            -0.0448 |
| baseline              | momentum_heavy  |                     3 | out_of_sample |       30 |             7 |         1.0000 |         0.5941 |                 0.6411 |                    -0.0470 |        -0.1660 |                -0.1675 |     0.6000 |            -0.0791 |
| baseline              | volume_heavy    |                    15 | out_of_sample |       30 |             7 |         1.0000 |         0.5683 |                 0.6411 |                    -0.0728 |        -0.1746 |                -0.1675 |     0.6000 |            -0.1219 |
| defensive_mode        | momentum_heavy  |                    15 | out_of_sample |       30 |             7 |         1.0000 |         0.5583 |                 0.6411 |                    -0.0828 |        -0.1792 |                -0.1675 |     0.5667 |            -0.1579 |
| reduced_exposure_mode | momentum_heavy  |                    15 | out_of_sample |       30 |             7 |         0.8833 |         0.5305 |                 0.6411 |                    -0.1106 |        -0.1851 |                -0.1675 |     0.6333 |            -0.1642 |
| defensive_mode        | mixed_model     |                    15 | out_of_sample |       30 |             7 |         1.0000 |         0.5438 |                 0.6411 |                    -0.0973 |        -0.1757 |                -0.1675 |     0.5333 |            -0.1820 |
| defensive_mode        | trend_following |                    15 | out_of_sample |       30 |             7 |         1.0000 |         0.5332 |                 0.6411 |                    -0.1079 |        -0.1822 |                -0.1675 |     0.5667 |            -0.1891 |

## Regime Signal Coverage

- Total signal months: 94
- BIST100 below MA200 months: 19
- Below-MA200 rate: 20.21%
