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
| baseline              |             2.0224 |                         0.4461 |            -0.1935 |                     0.2995 |                 0.3620 |                  1 |
| defensive_mode        |             1.9444 |                         0.3682 |            -0.1963 |                     0.2209 |                 0.2708 |                  1 |
| reduced_exposure_mode |             1.7540 |                         0.1777 |            -0.1935 |                     0.2517 |                 0.0936 |                  1 |
| cash_mode             |             1.5441 |                        -0.0322 |            -0.2027 |                     0.1960 |                -0.2028 |                  1 |

## Best Out-Of-Sample Combinations

| policy                | base_model      |   base_portfolio_size | period        |   months |   bear_months |   avg_exposure |   total_return |   bist100_total_return |   excess_return_vs_bist100 |   max_drawdown |   bist100_max_drawdown |   win_rate |   robustness_score |
|:----------------------|:----------------|----------------------:|:--------------|---------:|--------------:|---------------:|---------------:|-----------------------:|---------------------------:|---------------:|-----------------------:|-----------:|-------------------:|
| baseline              | mixed_model     |                    15 | out_of_sample |       33 |             8 |         1.0000 |         0.4746 |                 0.2663 |                     0.2082 |        -0.1644 |                -0.2550 |     0.5758 |             0.1672 |
| baseline              | momentum_heavy  |                     3 | out_of_sample |       33 |             8 |         1.0000 |         0.4845 |                 0.2663 |                     0.2182 |        -0.1660 |                -0.2550 |     0.5455 |             0.1588 |
| baseline              | momentum_heavy  |                    15 | out_of_sample |       33 |             8 |         1.0000 |         0.4508 |                 0.2663 |                     0.1845 |        -0.1680 |                -0.2550 |     0.5758 |             0.1364 |
| baseline              | trend_following |                    15 | out_of_sample |       33 |             8 |         1.0000 |         0.4499 |                 0.2663 |                     0.1836 |        -0.1747 |                -0.2550 |     0.5758 |             0.1221 |
| reduced_exposure_mode | momentum_heavy  |                     3 | out_of_sample |       33 |             8 |         0.8788 |         0.4191 |                 0.2663 |                     0.1527 |        -0.1660 |                -0.2550 |     0.5455 |             0.0934 |
| baseline              | trend_following |                     3 | out_of_sample |       33 |             8 |         1.0000 |         0.4183 |                 0.2663 |                     0.1520 |        -0.1767 |                -0.2550 |     0.5758 |             0.0865 |
| reduced_exposure_mode | mixed_model     |                    15 | out_of_sample |       33 |             8 |         0.8788 |         0.3960 |                 0.2663 |                     0.1296 |        -0.1817 |                -0.2550 |     0.5758 |             0.0542 |
| baseline              | low_volatility  |                    15 | out_of_sample |       33 |             8 |         1.0000 |         0.4123 |                 0.2663 |                     0.1460 |        -0.1886 |                -0.2550 |     0.5455 |             0.0415 |
| defensive_mode        | momentum_heavy  |                     3 | out_of_sample |       33 |             8 |         1.0000 |         0.3730 |                 0.2663 |                     0.1067 |        -0.1660 |                -0.2550 |     0.5152 |             0.0322 |
| reduced_exposure_mode | trend_following |                     3 | out_of_sample |       33 |             8 |         0.8788 |         0.3558 |                 0.2663 |                     0.0895 |        -0.1767 |                -0.2550 |     0.5758 |             0.0240 |

## Regime Signal Coverage

- Total signal months: 97
- BIST100 below MA200 months: 21
- Below-MA200 rate: 21.65%
