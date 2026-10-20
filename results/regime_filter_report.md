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
| baseline              |             2.0459 |                         0.4434 |            -0.1904 |                     0.3702 |                 0.3656 |                  1 |
| defensive_mode        |             1.9671 |                         0.3646 |            -0.1908 |                     0.2890 |                 0.2783 |                  1 |
| reduced_exposure_mode |             1.7649 |                         0.1624 |            -0.1932 |                     0.2845 |                 0.0790 |                  1 |
| cash_mode             |             1.5441 |                        -0.0585 |            -0.2027 |                     0.1960 |                -0.2272 |                  1 |

## Best Out-Of-Sample Combinations

| policy                | base_model      |   base_portfolio_size | period        |   months |   bear_months |   avg_exposure |   total_return |   bist100_total_return |   excess_return_vs_bist100 |   max_drawdown |   bist100_max_drawdown |   win_rate |   robustness_score |
|:----------------------|:----------------|----------------------:|:--------------|---------:|--------------:|---------------:|---------------:|-----------------------:|---------------------------:|---------------:|-----------------------:|-----------:|-------------------:|
| baseline              | mixed_model     |                    15 | out_of_sample |       33 |             8 |         1.0000 |         0.5500 |                 0.3452 |                     0.2047 |        -0.1644 |                -0.2086 |     0.5758 |             0.1637 |
| baseline              | momentum_heavy  |                     3 | out_of_sample |       33 |             8 |         1.0000 |         0.5454 |                 0.3452 |                     0.2001 |        -0.1660 |                -0.2086 |     0.5455 |             0.1408 |
| baseline              | momentum_heavy  |                    15 | out_of_sample |       33 |             8 |         1.0000 |         0.5250 |                 0.3452 |                     0.1798 |        -0.1680 |                -0.2086 |     0.5758 |             0.1317 |
| baseline              | trend_following |                    15 | out_of_sample |       33 |             8 |         1.0000 |         0.5241 |                 0.3452 |                     0.1788 |        -0.1747 |                -0.2086 |     0.5758 |             0.1174 |
| baseline              | low_volatility  |                    15 | out_of_sample |       33 |             8 |         1.0000 |         0.4946 |                 0.3452 |                     0.1493 |        -0.1563 |                -0.2086 |     0.5455 |             0.1094 |
| baseline              | trend_following |                     3 | out_of_sample |       33 |             8 |         1.0000 |         0.4765 |                 0.3452 |                     0.1312 |        -0.1767 |                -0.2086 |     0.5758 |             0.0657 |
| reduced_exposure_mode | momentum_heavy  |                     3 | out_of_sample |       33 |             8 |         0.8788 |         0.4470 |                 0.3452 |                     0.1017 |        -0.1660 |                -0.2086 |     0.5455 |             0.0424 |
| defensive_mode        | momentum_heavy  |                     3 | out_of_sample |       33 |             8 |         1.0000 |         0.4496 |                 0.3452 |                     0.1044 |        -0.1660 |                -0.2086 |     0.5152 |             0.0299 |
| baseline              | volume_heavy    |                    15 | out_of_sample |       33 |             8 |         1.0000 |         0.4346 |                 0.3452 |                     0.0894 |        -0.1746 |                -0.2086 |     0.5758 |             0.0281 |
| reduced_exposure_mode | mixed_model     |                    15 | out_of_sample |       33 |             8 |         0.8788 |         0.4306 |                 0.3452 |                     0.0854 |        -0.1817 |                -0.2086 |     0.5758 |             0.0099 |

## Regime Signal Coverage

- Total signal months: 97
- BIST100 below MA200 months: 21
- Below-MA200 rate: 21.65%
