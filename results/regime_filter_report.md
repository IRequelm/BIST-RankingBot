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
| baseline              |             2.0822 |                         0.3651 |            -0.1902 |                     0.4791 |                 0.2951 |                  1 |
| defensive_mode        |             2.0087 |                         0.2916 |            -0.1901 |                     0.4138 |                 0.2138 |                  1 |
| reduced_exposure_mode |             1.7946 |                         0.0774 |            -0.1929 |                     0.3734 |                 0.0020 |                  1 |
| cash_mode             |             1.5677 |                        -0.1494 |            -0.2024 |                     0.2668 |                -0.3125 |                  1 |

## Best Out-Of-Sample Combinations

| policy                | base_model      |   base_portfolio_size | period        |   months |   bear_months |   avg_exposure |   total_return |   bist100_total_return |   excess_return_vs_bist100 |   max_drawdown |   bist100_max_drawdown |   win_rate |   robustness_score |
|:----------------------|:----------------|----------------------:|:--------------|---------:|--------------:|---------------:|---------------:|-----------------------:|---------------------------:|---------------:|-----------------------:|-----------:|-------------------:|
| baseline              | mixed_model     |                    15 | out_of_sample |       30 |             7 |         1.0000 |         0.6830 |                 0.6890 |                    -0.0060 |        -0.1644 |                -0.1675 |     0.6333 |            -0.0182 |
| baseline              | momentum_heavy  |                    15 | out_of_sample |       30 |             7 |         1.0000 |         0.6742 |                 0.6890 |                    -0.0147 |        -0.1680 |                -0.1675 |     0.6333 |            -0.0341 |
| baseline              | low_volatility  |                    15 | out_of_sample |       30 |             7 |         1.0000 |         0.6631 |                 0.6890 |                    -0.0259 |        -0.1563 |                -0.1675 |     0.6000 |            -0.0385 |
| baseline              | trend_following |                    15 | out_of_sample |       30 |             7 |         1.0000 |         0.6472 |                 0.6890 |                    -0.0417 |        -0.1747 |                -0.1675 |     0.6333 |            -0.0744 |
| baseline              | momentum_heavy  |                     3 | out_of_sample |       30 |             7 |         1.0000 |         0.6029 |                 0.6890 |                    -0.0861 |        -0.1660 |                -0.1675 |     0.6000 |            -0.1182 |
| baseline              | volume_heavy    |                    15 | out_of_sample |       30 |             7 |         1.0000 |         0.6018 |                 0.6890 |                    -0.0871 |        -0.1746 |                -0.1675 |     0.6333 |            -0.1196 |
| defensive_mode        | mixed_model     |                    15 | out_of_sample |       30 |             7 |         1.0000 |         0.5768 |                 0.6890 |                    -0.1121 |        -0.1757 |                -0.1675 |     0.5667 |            -0.1802 |
| defensive_mode        | low_volatility  |                    15 | out_of_sample |       30 |             7 |         1.0000 |         0.5511 |                 0.6890 |                    -0.1379 |        -0.1661 |                -0.1675 |     0.5667 |            -0.1867 |
| reduced_exposure_mode | mixed_model     |                    15 | out_of_sample |       30 |             7 |         0.8833 |         0.5469 |                 0.6890 |                    -0.1421 |        -0.1817 |                -0.1675 |     0.6333 |            -0.1887 |
| defensive_mode        | momentum_heavy  |                    15 | out_of_sample |       30 |             7 |         1.0000 |         0.5648 |                 0.6890 |                    -0.1242 |        -0.1792 |                -0.1675 |     0.5667 |            -0.1992 |

## Regime Signal Coverage

- Total signal months: 94
- BIST100 below MA200 months: 19
- Below-MA200 rate: 20.21%
