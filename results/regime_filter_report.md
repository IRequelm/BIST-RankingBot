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
| baseline              |             2.0835 |                         0.3623 |            -0.1902 |                     0.4830 |                 0.2931 |                  1 |
| defensive_mode        |             2.0099 |                         0.2887 |            -0.1901 |                     0.4175 |                 0.2118 |                  1 |
| reduced_exposure_mode |             1.7958 |                         0.0745 |            -0.1929 |                     0.3770 |                -0.0001 |                  1 |
| cash_mode             |             1.5688 |                        -0.1524 |            -0.2024 |                     0.2701 |                -0.3147 |                  1 |

## Best Out-Of-Sample Combinations

| policy                | base_model      |   base_portfolio_size | period        |   months |   bear_months |   avg_exposure |   total_return |   bist100_total_return |   excess_return_vs_bist100 |   max_drawdown |   bist100_max_drawdown |   win_rate |   robustness_score |
|:----------------------|:----------------|----------------------:|:--------------|---------:|--------------:|---------------:|---------------:|-----------------------:|---------------------------:|---------------:|-----------------------:|-----------:|-------------------:|
| baseline              | mixed_model     |                    15 | out_of_sample |       30 |             7 |         1.0000 |         0.6856 |                 0.7013 |                    -0.0157 |        -0.1644 |                -0.1675 |     0.6333 |            -0.0279 |
| baseline              | momentum_heavy  |                    15 | out_of_sample |       30 |             7 |         1.0000 |         0.6780 |                 0.7013 |                    -0.0232 |        -0.1680 |                -0.1675 |     0.6333 |            -0.0426 |
| baseline              | low_volatility  |                    15 | out_of_sample |       30 |             7 |         1.0000 |         0.6614 |                 0.7013 |                    -0.0399 |        -0.1563 |                -0.1675 |     0.6000 |            -0.0526 |
| baseline              | trend_following |                    15 | out_of_sample |       30 |             7 |         1.0000 |         0.6509 |                 0.7013 |                    -0.0503 |        -0.1747 |                -0.1675 |     0.6333 |            -0.0830 |
| baseline              | momentum_heavy  |                     3 | out_of_sample |       30 |             7 |         1.0000 |         0.6176 |                 0.7013 |                    -0.0836 |        -0.1660 |                -0.1675 |     0.6333 |            -0.0991 |
| baseline              | volume_heavy    |                    15 | out_of_sample |       30 |             7 |         1.0000 |         0.6044 |                 0.7013 |                    -0.0969 |        -0.1746 |                -0.1675 |     0.6333 |            -0.1294 |
| defensive_mode        | mixed_model     |                    15 | out_of_sample |       30 |             7 |         1.0000 |         0.5793 |                 0.7013 |                    -0.1220 |        -0.1757 |                -0.1675 |     0.5667 |            -0.1900 |
| reduced_exposure_mode | mixed_model     |                    15 | out_of_sample |       30 |             7 |         0.8833 |         0.5493 |                 0.7013 |                    -0.1520 |        -0.1817 |                -0.1675 |     0.6333 |            -0.1986 |
| defensive_mode        | low_volatility  |                    15 | out_of_sample |       30 |             7 |         1.0000 |         0.5495 |                 0.7013 |                    -0.1518 |        -0.1661 |                -0.1675 |     0.5667 |            -0.2006 |
| defensive_mode        | momentum_heavy  |                    15 | out_of_sample |       30 |             7 |         1.0000 |         0.5683 |                 0.7013 |                    -0.1330 |        -0.1792 |                -0.1675 |     0.5667 |            -0.2080 |

## Regime Signal Coverage

- Total signal months: 94
- BIST100 below MA200 months: 19
- Below-MA200 rate: 20.21%
