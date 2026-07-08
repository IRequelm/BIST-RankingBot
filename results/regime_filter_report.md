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
| baseline              |             2.0815 |                         0.3586 |            -0.1902 |                     0.4770 |                 0.2883 |                  1 |
| defensive_mode        |             2.0080 |                         0.2851 |            -0.1901 |                     0.4117 |                 0.2071 |                  1 |
| reduced_exposure_mode |             1.7939 |                         0.0710 |            -0.1929 |                     0.3714 |                -0.0047 |                  1 |
| cash_mode             |             1.5670 |                        -0.1558 |            -0.2024 |                     0.2649 |                -0.3192 |                  1 |

## Best Out-Of-Sample Combinations

| policy                | base_model      |   base_portfolio_size | period        |   months |   bear_months |   avg_exposure |   total_return |   bist100_total_return |   excess_return_vs_bist100 |   max_drawdown |   bist100_max_drawdown |   win_rate |   robustness_score |
|:----------------------|:----------------|----------------------:|:--------------|---------:|--------------:|---------------:|---------------:|-----------------------:|---------------------------:|---------------:|-----------------------:|-----------:|-------------------:|
| baseline              | mixed_model     |                    15 | out_of_sample |       30 |             7 |         1.0000 |         0.6713 |                 0.7062 |                    -0.0349 |        -0.1644 |                -0.1675 |     0.6333 |            -0.0472 |
| baseline              | momentum_heavy  |                    15 | out_of_sample |       30 |             7 |         1.0000 |         0.6659 |                 0.7062 |                    -0.0403 |        -0.1680 |                -0.1675 |     0.6333 |            -0.0597 |
| baseline              | momentum_heavy  |                     3 | out_of_sample |       30 |             7 |         1.0000 |         0.6415 |                 0.7062 |                    -0.0648 |        -0.1660 |                -0.1675 |     0.6333 |            -0.0802 |
| baseline              | low_volatility  |                    15 | out_of_sample |       30 |             7 |         1.0000 |         0.6416 |                 0.7062 |                    -0.0647 |        -0.1563 |                -0.1675 |     0.5667 |            -0.0940 |
| baseline              | trend_following |                    15 | out_of_sample |       30 |             7 |         1.0000 |         0.6390 |                 0.7062 |                    -0.0672 |        -0.1747 |                -0.1675 |     0.6333 |            -0.0999 |
| baseline              | volume_heavy    |                    15 | out_of_sample |       30 |             7 |         1.0000 |         0.5908 |                 0.7062 |                    -0.1155 |        -0.1746 |                -0.1675 |     0.6333 |            -0.1479 |
| defensive_mode        | momentum_heavy  |                     3 | out_of_sample |       30 |             7 |         1.0000 |         0.5314 |                 0.7062 |                    -0.1749 |        -0.1660 |                -0.1675 |     0.6000 |            -0.2069 |
| defensive_mode        | mixed_model     |                    15 | out_of_sample |       30 |             7 |         1.0000 |         0.5659 |                 0.7062 |                    -0.1403 |        -0.1757 |                -0.1675 |     0.5667 |            -0.2084 |
| reduced_exposure_mode | momentum_heavy  |                     3 | out_of_sample |       30 |             7 |         0.8833 |         0.5060 |                 0.7062 |                    -0.2003 |        -0.1660 |                -0.1675 |     0.6333 |            -0.2157 |
| reduced_exposure_mode | mixed_model     |                    15 | out_of_sample |       30 |             7 |         0.8833 |         0.5362 |                 0.7062 |                    -0.1701 |        -0.1817 |                -0.1675 |     0.6333 |            -0.2167 |

## Regime Signal Coverage

- Total signal months: 94
- BIST100 below MA200 months: 19
- Below-MA200 rate: 20.21%
