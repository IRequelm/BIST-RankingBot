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
| baseline              |             2.1001 |                         0.3681 |            -0.1902 |                     0.5328 |                 0.2990 |                  1 |
| defensive_mode        |             2.0258 |                         0.2938 |            -0.1901 |                     0.4652 |                 0.2169 |                  1 |
| reduced_exposure_mode |             1.8112 |                         0.0792 |            -0.1929 |                     0.4233 |                 0.0047 |                  1 |
| cash_mode             |             1.5830 |                        -0.1490 |            -0.2024 |                     0.3128 |                -0.3120 |                  1 |

## Best Out-Of-Sample Combinations

| policy                | base_model      |   base_portfolio_size | period        |   months |   bear_months |   avg_exposure |   total_return |   bist100_total_return |   excess_return_vs_bist100 |   max_drawdown |   bist100_max_drawdown |   win_rate |   robustness_score |
|:----------------------|:----------------|----------------------:|:--------------|---------:|--------------:|---------------:|---------------:|-----------------------:|---------------------------:|---------------:|-----------------------:|-----------:|-------------------:|
| baseline              | mixed_model     |                    15 | out_of_sample |       29 |             7 |         1.0000 |         0.7332 |                 0.7336 |                    -0.0004 |        -0.1644 |                -0.1675 |     0.6207 |            -0.0190 |
| baseline              | momentum_heavy  |                    15 | out_of_sample |       29 |             7 |         1.0000 |         0.7301 |                 0.7336 |                    -0.0035 |        -0.1680 |                -0.1675 |     0.6207 |            -0.0292 |
| baseline              | low_volatility  |                    15 | out_of_sample |       29 |             7 |         1.0000 |         0.7208 |                 0.7336 |                    -0.0127 |        -0.1563 |                -0.1675 |     0.5862 |            -0.0323 |
| baseline              | trend_following |                    15 | out_of_sample |       29 |             7 |         1.0000 |         0.6979 |                 0.7336 |                    -0.0357 |        -0.1747 |                -0.1675 |     0.6207 |            -0.0747 |
| baseline              | momentum_heavy  |                     3 | out_of_sample |       29 |             7 |         1.0000 |         0.6673 |                 0.7336 |                    -0.0663 |        -0.1660 |                -0.1675 |     0.6207 |            -0.0880 |
| baseline              | volume_heavy    |                    15 | out_of_sample |       29 |             7 |         1.0000 |         0.6525 |                 0.7336 |                    -0.0811 |        -0.1746 |                -0.1675 |     0.6207 |            -0.1199 |
| defensive_mode        | low_volatility  |                    15 | out_of_sample |       29 |             7 |         1.0000 |         0.6049 |                 0.7336 |                    -0.1287 |        -0.1661 |                -0.1675 |     0.5517 |            -0.1849 |
| defensive_mode        | mixed_model     |                    15 | out_of_sample |       29 |             7 |         1.0000 |         0.6239 |                 0.7336 |                    -0.1097 |        -0.1757 |                -0.1675 |     0.5517 |            -0.1852 |
| reduced_exposure_mode | mixed_model     |                    15 | out_of_sample |       29 |             7 |         0.8793 |         0.5930 |                 0.7336 |                    -0.1406 |        -0.1817 |                -0.1675 |     0.6207 |            -0.1935 |
| defensive_mode        | momentum_heavy  |                    15 | out_of_sample |       29 |             7 |         1.0000 |         0.6169 |                 0.7336 |                    -0.1166 |        -0.1792 |                -0.1675 |     0.5517 |            -0.1992 |

## Regime Signal Coverage

- Total signal months: 93
- BIST100 below MA200 months: 19
- Below-MA200 rate: 20.43%
