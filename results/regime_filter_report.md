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
| baseline              |             2.0589 |                         0.4449 |            -0.1904 |                     0.4090 |                 0.3707 |                  1 |
| defensive_mode        |             1.9811 |                         0.3671 |            -0.1904 |                     0.3310 |                 0.2816 |                  1 |
| reduced_exposure_mode |             1.7709 |                         0.1570 |            -0.1932 |                     0.3026 |                 0.0771 |                  1 |
| cash_mode             |             1.5441 |                        -0.0699 |            -0.2027 |                     0.1960 |                -0.2387 |                  1 |

## Best Out-Of-Sample Combinations

| policy                | base_model      |   base_portfolio_size | period        |   months |   bear_months |   avg_exposure |   total_return |   bist100_total_return |   excess_return_vs_bist100 |   max_drawdown |   bist100_max_drawdown |   win_rate |   robustness_score |
|:----------------------|:----------------|----------------------:|:--------------|---------:|--------------:|---------------:|---------------:|-----------------------:|---------------------------:|---------------:|-----------------------:|-----------:|-------------------:|
| baseline              | mixed_model     |                    15 | out_of_sample |       33 |             8 |         1.0000 |         0.5851 |                 0.3796 |                     0.2056 |        -0.1644 |                -0.1884 |     0.6061 |             0.1797 |
| baseline              | momentum_heavy  |                     3 | out_of_sample |       33 |             8 |         1.0000 |         0.6022 |                 0.3796 |                     0.2227 |        -0.1660 |                -0.1884 |     0.5455 |             0.1633 |
| baseline              | momentum_heavy  |                    15 | out_of_sample |       33 |             8 |         1.0000 |         0.5596 |                 0.3796 |                     0.1800 |        -0.1680 |                -0.1884 |     0.6061 |             0.1471 |
| baseline              | trend_following |                    15 | out_of_sample |       33 |             8 |         1.0000 |         0.5586 |                 0.3796 |                     0.1790 |        -0.1747 |                -0.1884 |     0.6061 |             0.1328 |
| baseline              | low_volatility  |                    15 | out_of_sample |       33 |             8 |         1.0000 |         0.5256 |                 0.3796 |                     0.1461 |        -0.1563 |                -0.1884 |     0.5758 |             0.1213 |
| baseline              | trend_following |                     3 | out_of_sample |       33 |             8 |         1.0000 |         0.5308 |                 0.3796 |                     0.1512 |        -0.1767 |                -0.1884 |     0.5758 |             0.0857 |
| defensive_mode        | momentum_heavy  |                     3 | out_of_sample |       33 |             8 |         1.0000 |         0.4969 |                 0.3796 |                     0.1173 |        -0.1660 |                -0.1884 |     0.5152 |             0.0428 |
| baseline              | volume_heavy    |                    15 | out_of_sample |       33 |             8 |         1.0000 |         0.4660 |                 0.3796 |                     0.0864 |        -0.1746 |                -0.1884 |     0.6061 |             0.0404 |
| reduced_exposure_mode | momentum_heavy  |                     3 | out_of_sample |       33 |             8 |         0.8788 |         0.4731 |                 0.3796 |                     0.0935 |        -0.1660 |                -0.1884 |     0.5455 |             0.0342 |
| reduced_exposure_mode | mixed_model     |                    15 | out_of_sample |       33 |             8 |         0.8788 |         0.4468 |                 0.3796 |                     0.0672 |        -0.1817 |                -0.1884 |     0.6061 |             0.0069 |

## Regime Signal Coverage

- Total signal months: 97
- BIST100 below MA200 months: 21
- Below-MA200 rate: 21.65%
