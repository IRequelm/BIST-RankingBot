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
| baseline              |             2.0868 |                         0.3763 |            -0.1902 |                     0.4929 |                 0.3072 |                  1 |
| defensive_mode        |             2.0131 |                         0.3025 |            -0.1901 |                     0.4269 |                 0.2255 |                  1 |
| reduced_exposure_mode |             1.7988 |                         0.0883 |            -0.1929 |                     0.3862 |                 0.0138 |                  1 |
| cash_mode             |             1.5716 |                        -0.1390 |            -0.2024 |                     0.2785 |                -0.3020 |                  1 |

## Best Out-Of-Sample Combinations

| policy                | base_model      |   base_portfolio_size | period        |   months |   bear_months |   avg_exposure |   total_return |   bist100_total_return |   excess_return_vs_bist100 |   max_drawdown |   bist100_max_drawdown |   win_rate |   robustness_score |
|:----------------------|:----------------|----------------------:|:--------------|---------:|--------------:|---------------:|---------------:|-----------------------:|---------------------------:|---------------:|-----------------------:|-----------:|-------------------:|
| baseline              | mixed_model     |                    15 | out_of_sample |       29 |             7 |         1.0000 |         0.6818 |                 0.6693 |                     0.0125 |        -0.1644 |                -0.1675 |     0.6207 |            -0.0061 |
| baseline              | low_volatility  |                    15 | out_of_sample |       29 |             7 |         1.0000 |         0.6698 |                 0.6693 |                     0.0005 |        -0.1563 |                -0.1675 |     0.5862 |            -0.0190 |
| baseline              | momentum_heavy  |                    15 | out_of_sample |       29 |             7 |         1.0000 |         0.6730 |                 0.6693 |                     0.0037 |        -0.1680 |                -0.1675 |     0.6207 |            -0.0220 |
| baseline              | momentum_heavy  |                     3 | out_of_sample |       29 |             7 |         1.0000 |         0.6354 |                 0.6693 |                    -0.0339 |        -0.1660 |                -0.1675 |     0.6207 |            -0.0556 |
| baseline              | trend_following |                    15 | out_of_sample |       29 |             7 |         1.0000 |         0.6475 |                 0.6693 |                    -0.0217 |        -0.1747 |                -0.1675 |     0.6207 |            -0.0607 |
| baseline              | volume_heavy    |                    15 | out_of_sample |       29 |             7 |         1.0000 |         0.5996 |                 0.6693 |                    -0.0696 |        -0.1746 |                -0.1675 |     0.6207 |            -0.1084 |
| defensive_mode        | low_volatility  |                    15 | out_of_sample |       29 |             7 |         1.0000 |         0.5573 |                 0.6693 |                    -0.1119 |        -0.1661 |                -0.1675 |     0.5517 |            -0.1682 |
| defensive_mode        | mixed_model     |                    15 | out_of_sample |       29 |             7 |         1.0000 |         0.5757 |                 0.6693 |                    -0.0936 |        -0.1757 |                -0.1675 |     0.5517 |            -0.1691 |
| reduced_exposure_mode | mixed_model     |                    15 | out_of_sample |       29 |             7 |         0.8793 |         0.5458 |                 0.6693 |                    -0.1235 |        -0.1817 |                -0.1675 |     0.6207 |            -0.1765 |
| reduced_exposure_mode | low_volatility  |                    15 | out_of_sample |       29 |             7 |         0.8793 |         0.5314 |                 0.6693 |                    -0.1379 |        -0.1688 |                -0.1675 |     0.5862 |            -0.1824 |

## Regime Signal Coverage

- Total signal months: 93
- BIST100 below MA200 months: 19
- Below-MA200 rate: 20.43%
