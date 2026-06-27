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
| baseline              |             2.0947 |                         0.3812 |            -0.1902 |                     0.5166 |                 0.3121 |                  1 |
| defensive_mode        |             2.0206 |                         0.3071 |            -0.1901 |                     0.4496 |                 0.2301 |                  1 |
| reduced_exposure_mode |             1.8062 |                         0.0926 |            -0.1929 |                     0.4082 |                 0.0181 |                  1 |
| cash_mode             |             1.5784 |                        -0.1352 |            -0.2024 |                     0.2988 |                -0.2982 |                  1 |

## Best Out-Of-Sample Combinations

| policy                | base_model      |   base_portfolio_size | period        |   months |   bear_months |   avg_exposure |   total_return |   bist100_total_return |   excess_return_vs_bist100 |   max_drawdown |   bist100_max_drawdown |   win_rate |   robustness_score |
|:----------------------|:----------------|----------------------:|:--------------|---------:|--------------:|---------------:|---------------:|-----------------------:|---------------------------:|---------------:|-----------------------:|-----------:|-------------------:|
| baseline              | mixed_model     |                    15 | out_of_sample |       29 |             7 |         1.0000 |         0.7037 |                 0.6783 |                     0.0254 |        -0.1644 |                -0.1675 |     0.6207 |             0.0069 |
| baseline              | low_volatility  |                    15 | out_of_sample |       29 |             7 |         1.0000 |         0.6916 |                 0.6783 |                     0.0133 |        -0.1563 |                -0.1675 |     0.5862 |            -0.0062 |
| baseline              | momentum_heavy  |                    15 | out_of_sample |       29 |             7 |         1.0000 |         0.6954 |                 0.6783 |                     0.0171 |        -0.1680 |                -0.1675 |     0.6207 |            -0.0085 |
| baseline              | momentum_heavy  |                     3 | out_of_sample |       29 |             7 |         1.0000 |         0.6731 |                 0.6783 |                    -0.0051 |        -0.1660 |                -0.1675 |     0.6207 |            -0.0269 |
| baseline              | trend_following |                    15 | out_of_sample |       29 |             7 |         1.0000 |         0.6691 |                 0.6783 |                    -0.0092 |        -0.1747 |                -0.1675 |     0.6207 |            -0.0482 |
| baseline              | volume_heavy    |                    15 | out_of_sample |       29 |             7 |         1.0000 |         0.6186 |                 0.6783 |                    -0.0597 |        -0.1746 |                -0.1675 |     0.6207 |            -0.0985 |
| defensive_mode        | momentum_heavy  |                     3 | out_of_sample |       29 |             7 |         1.0000 |         0.5609 |                 0.6783 |                    -0.1174 |        -0.1660 |                -0.1675 |     0.5862 |            -0.1563 |
| defensive_mode        | low_volatility  |                    15 | out_of_sample |       29 |             7 |         1.0000 |         0.5777 |                 0.6783 |                    -0.1006 |        -0.1661 |                -0.1675 |     0.5517 |            -0.1569 |
| defensive_mode        | mixed_model     |                    15 | out_of_sample |       29 |             7 |         1.0000 |         0.5963 |                 0.6783 |                    -0.0820 |        -0.1757 |                -0.1675 |     0.5517 |            -0.1575 |
| reduced_exposure_mode | momentum_heavy  |                     3 | out_of_sample |       29 |             7 |         0.8793 |         0.5350 |                 0.6783 |                    -0.1433 |        -0.1660 |                -0.1675 |     0.6207 |            -0.1650 |

## Regime Signal Coverage

- Total signal months: 93
- BIST100 below MA200 months: 19
- Below-MA200 rate: 20.43%
