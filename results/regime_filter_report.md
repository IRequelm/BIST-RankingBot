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
| baseline              |             2.0367 |                         0.4197 |            -0.1906 |                     0.3424 |                 0.3413 |                  1 |
| defensive_mode        |             1.9555 |                         0.3385 |            -0.1926 |                     0.2541 |                 0.2486 |                  1 |
| reduced_exposure_mode |             1.7606 |                         0.1437 |            -0.1932 |                     0.2717 |                 0.0600 |                  1 |
| cash_mode             |             1.5441 |                        -0.0729 |            -0.2027 |                     0.1960 |                -0.2417 |                  1 |

## Best Out-Of-Sample Combinations

| policy                | base_model      |   base_portfolio_size | period        |   months |   bear_months |   avg_exposure |   total_return |   bist100_total_return |   excess_return_vs_bist100 |   max_drawdown |   bist100_max_drawdown |   win_rate |   robustness_score |
|:----------------------|:----------------|----------------------:|:--------------|---------:|--------------:|---------------:|---------------:|-----------------------:|---------------------------:|---------------:|-----------------------:|-----------:|-------------------:|
| baseline              | mixed_model     |                    15 | out_of_sample |       33 |             8 |         1.0000 |         0.5226 |                 0.3885 |                     0.1341 |        -0.1644 |                -0.1831 |     0.5758 |             0.0931 |
| baseline              | momentum_heavy  |                    15 | out_of_sample |       33 |             8 |         1.0000 |         0.4981 |                 0.3885 |                     0.1096 |        -0.1680 |                -0.1831 |     0.5758 |             0.0615 |
| baseline              | momentum_heavy  |                     3 | out_of_sample |       33 |             8 |         1.0000 |         0.5030 |                 0.3885 |                     0.1145 |        -0.1660 |                -0.1831 |     0.5455 |             0.0551 |
| baseline              | trend_following |                    15 | out_of_sample |       33 |             8 |         1.0000 |         0.4972 |                 0.3885 |                     0.1086 |        -0.1747 |                -0.1831 |     0.5758 |             0.0472 |
| baseline              | low_volatility  |                    15 | out_of_sample |       33 |             8 |         1.0000 |         0.4720 |                 0.3885 |                     0.0835 |        -0.1563 |                -0.1831 |     0.5455 |             0.0436 |
| baseline              | trend_following |                     3 | out_of_sample |       33 |             8 |         1.0000 |         0.4360 |                 0.3885 |                     0.0475 |        -0.1767 |                -0.1831 |     0.5758 |            -0.0181 |
| reduced_exposure_mode | momentum_heavy  |                     3 | out_of_sample |       33 |             8 |         0.8788 |         0.4276 |                 0.3885 |                     0.0390 |        -0.1660 |                -0.1831 |     0.5455 |            -0.0203 |
| baseline              | volume_heavy    |                    15 | out_of_sample |       33 |             8 |         1.0000 |         0.4113 |                 0.3885 |                     0.0227 |        -0.1746 |                -0.1831 |     0.5758 |            -0.0385 |
| reduced_exposure_mode | mixed_model     |                    15 | out_of_sample |       33 |             8 |         0.8788 |         0.4180 |                 0.3885 |                     0.0295 |        -0.1817 |                -0.1831 |     0.5758 |            -0.0459 |
| defensive_mode        | momentum_heavy  |                     3 | out_of_sample |       33 |             8 |         1.0000 |         0.4103 |                 0.3885 |                     0.0218 |        -0.1660 |                -0.1831 |     0.5152 |            -0.0527 |

## Regime Signal Coverage

- Total signal months: 97
- BIST100 below MA200 months: 21
- Below-MA200 rate: 21.65%
