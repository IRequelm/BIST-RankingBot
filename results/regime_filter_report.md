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
| baseline              |             2.0405 |                         0.4462 |            -0.1904 |                     0.3540 |                 0.3682 |                  1 |
| defensive_mode        |             1.9616 |                         0.3673 |            -0.1914 |                     0.2725 |                 0.2798 |                  1 |
| reduced_exposure_mode |             1.7624 |                         0.1681 |            -0.1932 |                     0.2770 |                 0.0845 |                  1 |
| cash_mode             |             1.5441 |                        -0.0502 |            -0.2027 |                     0.1960 |                -0.2190 |                  1 |

## Best Out-Of-Sample Combinations

| policy                | base_model      |   base_portfolio_size | period        |   months |   bear_months |   avg_exposure |   total_return |   bist100_total_return |   excess_return_vs_bist100 |   max_drawdown |   bist100_max_drawdown |   win_rate |   robustness_score |
|:----------------------|:----------------|----------------------:|:--------------|---------:|--------------:|---------------:|---------------:|-----------------------:|---------------------------:|---------------:|-----------------------:|-----------:|-------------------:|
| baseline              | mixed_model     |                    15 | out_of_sample |       33 |             8 |         1.0000 |         0.5346 |                 0.3206 |                     0.2140 |        -0.1644 |                -0.2231 |     0.5758 |             0.1730 |
| baseline              | momentum_heavy  |                     3 | out_of_sample |       33 |             8 |         1.0000 |         0.5262 |                 0.3206 |                     0.2056 |        -0.1660 |                -0.2231 |     0.5455 |             0.1462 |
| baseline              | momentum_heavy  |                    15 | out_of_sample |       33 |             8 |         1.0000 |         0.5099 |                 0.3206 |                     0.1893 |        -0.1680 |                -0.2231 |     0.5758 |             0.1412 |
| baseline              | trend_following |                    15 | out_of_sample |       33 |             8 |         1.0000 |         0.5089 |                 0.3206 |                     0.1884 |        -0.1747 |                -0.2231 |     0.5758 |             0.1269 |
| baseline              | low_volatility  |                    15 | out_of_sample |       33 |             8 |         1.0000 |         0.4809 |                 0.3206 |                     0.1604 |        -0.1563 |                -0.2231 |     0.5455 |             0.1204 |
| baseline              | trend_following |                     3 | out_of_sample |       33 |             8 |         1.0000 |         0.4581 |                 0.3206 |                     0.1376 |        -0.1767 |                -0.2231 |     0.5758 |             0.0720 |
| reduced_exposure_mode | momentum_heavy  |                     3 | out_of_sample |       33 |             8 |         0.8788 |         0.4382 |                 0.3206 |                     0.1176 |        -0.1660 |                -0.2231 |     0.5455 |             0.0583 |
| baseline              | volume_heavy    |                    15 | out_of_sample |       33 |             8 |         1.0000 |         0.4180 |                 0.3206 |                     0.0975 |        -0.1746 |                -0.2231 |     0.5758 |             0.0362 |
| defensive_mode        | momentum_heavy  |                     3 | out_of_sample |       33 |             8 |         1.0000 |         0.4310 |                 0.3206 |                     0.1105 |        -0.1660 |                -0.2231 |     0.5152 |             0.0360 |
| reduced_exposure_mode | mixed_model     |                    15 | out_of_sample |       33 |             8 |         0.8788 |         0.4235 |                 0.3206 |                     0.1030 |        -0.1817 |                -0.2231 |     0.5758 |             0.0275 |

## Regime Signal Coverage

- Total signal months: 97
- BIST100 below MA200 months: 21
- Below-MA200 rate: 21.65%
