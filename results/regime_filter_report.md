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
| baseline              |             2.0904 |                         0.4164 |            -0.1902 |                     0.5037 |                 0.3469 |                  1 |
| defensive_mode        |             2.0162 |                         0.3421 |            -0.1901 |                     0.4362 |                 0.2653 |                  1 |
| reduced_exposure_mode |             1.8020 |                         0.1280 |            -0.1929 |                     0.3958 |                 0.0532 |                  1 |
| cash_mode             |             1.5744 |                        -0.0997 |            -0.2024 |                     0.2869 |                -0.2605 |                  1 |

## Best Out-Of-Sample Combinations

| policy                | base_model      |   base_portfolio_size | period        |   months |   bear_months |   avg_exposure |   total_return |   bist100_total_return |   excess_return_vs_bist100 |   max_drawdown |   bist100_max_drawdown |   win_rate |   robustness_score |
|:----------------------|:----------------|----------------------:|:--------------|---------:|--------------:|---------------:|---------------:|-----------------------:|---------------------------:|---------------:|-----------------------:|-----------:|-------------------:|
| baseline              | momentum_heavy  |                     3 | out_of_sample |       32 |             7 |         1.0000 |         0.7522 |                 0.5597 |                     0.1925 |        -0.1660 |                -0.1675 |     0.6250 |             0.1730 |
| baseline              | mixed_model     |                    15 | out_of_sample |       32 |             7 |         1.0000 |         0.6752 |                 0.5597 |                     0.1155 |        -0.1644 |                -0.1675 |     0.6250 |             0.0991 |
| baseline              | momentum_heavy  |                    15 | out_of_sample |       32 |             7 |         1.0000 |         0.6742 |                 0.5597 |                     0.1145 |        -0.1680 |                -0.1675 |     0.6250 |             0.0910 |
| baseline              | low_volatility  |                    15 | out_of_sample |       32 |             7 |         1.0000 |         0.6347 |                 0.5597 |                     0.0750 |        -0.1563 |                -0.1675 |     0.5938 |             0.0593 |
| baseline              | trend_following |                    15 | out_of_sample |       32 |             7 |         1.0000 |         0.6472 |                 0.5597 |                     0.0875 |        -0.1747 |                -0.1675 |     0.6250 |             0.0507 |
| defensive_mode        | momentum_heavy  |                     3 | out_of_sample |       32 |             7 |         1.0000 |         0.6347 |                 0.5597 |                     0.0750 |        -0.1660 |                -0.1675 |     0.5938 |             0.0398 |
| reduced_exposure_mode | momentum_heavy  |                     3 | out_of_sample |       32 |             7 |         0.8906 |         0.6075 |                 0.5597 |                     0.0479 |        -0.1660 |                -0.1675 |     0.6250 |             0.0283 |
| baseline              | trend_following |                     3 | out_of_sample |       32 |             7 |         1.0000 |         0.6013 |                 0.5597 |                     0.0417 |        -0.1767 |                -0.1675 |     0.6250 |             0.0008 |
| baseline              | volume_heavy    |                    15 | out_of_sample |       32 |             7 |         1.0000 |         0.5945 |                 0.5597 |                     0.0348 |        -0.1746 |                -0.1675 |     0.6250 |            -0.0018 |
| defensive_mode        | mixed_model     |                    15 | out_of_sample |       32 |             7 |         1.0000 |         0.5695 |                 0.5597 |                     0.0099 |        -0.1757 |                -0.1675 |     0.5625 |            -0.0602 |

## Regime Signal Coverage

- Total signal months: 96
- BIST100 below MA200 months: 20
- Below-MA200 rate: 20.83%
