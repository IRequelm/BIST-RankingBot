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
| baseline              |             2.0716 |                         0.4488 |            -0.1902 |                     0.4472 |                 0.3743 |                  1 |
| defensive_mode        |             1.9981 |                         0.3753 |            -0.1901 |                     0.3821 |                 0.2935 |                  1 |
| reduced_exposure_mode |             1.7845 |                         0.1617 |            -0.1929 |                     0.3433 |                 0.0819 |                  1 |
| cash_mode             |             1.5582 |                        -0.0646 |            -0.2024 |                     0.2384 |                -0.2323 |                  1 |

## Best Out-Of-Sample Combinations

| policy                | base_model      |   base_portfolio_size | period        |   months |   bear_months |   avg_exposure |   total_return |   bist100_total_return |   excess_return_vs_bist100 |   max_drawdown |   bist100_max_drawdown |   win_rate |   robustness_score |
|:----------------------|:----------------|----------------------:|:--------------|---------:|--------------:|---------------:|---------------:|-----------------------:|---------------------------:|---------------:|-----------------------:|-----------:|-------------------:|
| baseline              | momentum_heavy  |                     3 | out_of_sample |       32 |             7 |         1.0000 |         0.7022 |                 0.4061 |                     0.2961 |        -0.1660 |                -0.1728 |     0.5938 |             0.2609 |
| baseline              | mixed_model     |                    15 | out_of_sample |       32 |             7 |         1.0000 |         0.6077 |                 0.4061 |                     0.2015 |        -0.1644 |                -0.1728 |     0.5938 |             0.1695 |
| baseline              | momentum_heavy  |                    15 | out_of_sample |       32 |             7 |         1.0000 |         0.6069 |                 0.4061 |                     0.2008 |        -0.1680 |                -0.1728 |     0.5938 |             0.1617 |
| defensive_mode        | momentum_heavy  |                     3 | out_of_sample |       32 |             7 |         1.0000 |         0.5880 |                 0.4061 |                     0.1819 |        -0.1660 |                -0.1728 |     0.5625 |             0.1311 |
| baseline              | low_volatility  |                    15 | out_of_sample |       32 |             7 |         1.0000 |         0.5675 |                 0.4061 |                     0.1614 |        -0.1563 |                -0.1728 |     0.5625 |             0.1300 |
| baseline              | trend_following |                    15 | out_of_sample |       32 |             7 |         1.0000 |         0.5808 |                 0.4061 |                     0.1747 |        -0.1747 |                -0.1728 |     0.5938 |             0.1222 |
| reduced_exposure_mode | momentum_heavy  |                     3 | out_of_sample |       32 |             7 |         0.8906 |         0.5616 |                 0.4061 |                     0.1555 |        -0.1660 |                -0.1728 |     0.5938 |             0.1203 |
| baseline              | trend_following |                     3 | out_of_sample |       32 |             7 |         1.0000 |         0.5556 |                 0.4061 |                     0.1495 |        -0.1767 |                -0.1728 |     0.5938 |             0.0930 |
| baseline              | volume_heavy    |                    15 | out_of_sample |       32 |             7 |         1.0000 |         0.5302 |                 0.4061 |                     0.1241 |        -0.1746 |                -0.1728 |     0.5938 |             0.0718 |
| defensive_mode        | mixed_model     |                    15 | out_of_sample |       32 |             7 |         1.0000 |         0.5063 |                 0.4061 |                     0.1002 |        -0.1757 |                -0.1728 |     0.5312 |             0.0144 |

## Regime Signal Coverage

- Total signal months: 96
- BIST100 below MA200 months: 20
- Below-MA200 rate: 20.83%
