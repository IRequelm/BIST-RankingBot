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
| baseline              |             2.0947 |                         0.3806 |            -0.1902 |                     0.5166 |                 0.3115 |                  1 |
| defensive_mode        |             2.0206 |                         0.3065 |            -0.1901 |                     0.4496 |                 0.2295 |                  1 |
| reduced_exposure_mode |             1.8062 |                         0.0920 |            -0.1929 |                     0.4082 |                 0.0176 |                  1 |
| cash_mode             |             1.5784 |                        -0.1358 |            -0.2024 |                     0.2988 |                -0.2988 |                  1 |

## Best Out-Of-Sample Combinations

| policy                | base_model      |   base_portfolio_size | period        |   months |   bear_months |   avg_exposure |   total_return |   bist100_total_return |   excess_return_vs_bist100 |   max_drawdown |   bist100_max_drawdown |   win_rate |   robustness_score |
|:----------------------|:----------------|----------------------:|:--------------|---------:|--------------:|---------------:|---------------:|-----------------------:|---------------------------:|---------------:|-----------------------:|-----------:|-------------------:|
| baseline              | mixed_model     |                    15 | out_of_sample |       29 |             7 |         1.0000 |         0.7037 |                 0.6800 |                     0.0238 |        -0.1644 |                -0.1675 |     0.6207 |             0.0052 |
| baseline              | low_volatility  |                    15 | out_of_sample |       29 |             7 |         1.0000 |         0.6916 |                 0.6800 |                     0.0117 |        -0.1563 |                -0.1675 |     0.5862 |            -0.0079 |
| baseline              | momentum_heavy  |                    15 | out_of_sample |       29 |             7 |         1.0000 |         0.6954 |                 0.6800 |                     0.0154 |        -0.1680 |                -0.1675 |     0.6207 |            -0.0102 |
| baseline              | momentum_heavy  |                     3 | out_of_sample |       29 |             7 |         1.0000 |         0.6731 |                 0.6800 |                    -0.0068 |        -0.1660 |                -0.1675 |     0.6207 |            -0.0285 |
| baseline              | trend_following |                    15 | out_of_sample |       29 |             7 |         1.0000 |         0.6691 |                 0.6800 |                    -0.0109 |        -0.1747 |                -0.1675 |     0.6207 |            -0.0499 |
| baseline              | volume_heavy    |                    15 | out_of_sample |       29 |             7 |         1.0000 |         0.6186 |                 0.6800 |                    -0.0614 |        -0.1746 |                -0.1675 |     0.6207 |            -0.1002 |
| defensive_mode        | momentum_heavy  |                     3 | out_of_sample |       29 |             7 |         1.0000 |         0.5609 |                 0.6800 |                    -0.1190 |        -0.1660 |                -0.1675 |     0.5862 |            -0.1580 |
| defensive_mode        | low_volatility  |                    15 | out_of_sample |       29 |             7 |         1.0000 |         0.5777 |                 0.6800 |                    -0.1023 |        -0.1661 |                -0.1675 |     0.5517 |            -0.1585 |
| defensive_mode        | mixed_model     |                    15 | out_of_sample |       29 |             7 |         1.0000 |         0.5963 |                 0.6800 |                    -0.0837 |        -0.1757 |                -0.1675 |     0.5517 |            -0.1592 |
| reduced_exposure_mode | momentum_heavy  |                     3 | out_of_sample |       29 |             7 |         0.8793 |         0.5350 |                 0.6800 |                    -0.1449 |        -0.1660 |                -0.1675 |     0.6207 |            -0.1667 |

## Regime Signal Coverage

- Total signal months: 93
- BIST100 below MA200 months: 19
- Below-MA200 rate: 20.43%
