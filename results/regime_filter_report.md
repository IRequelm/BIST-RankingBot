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
| baseline              |             2.0926 |                         0.3762 |            -0.1902 |                     0.5102 |                 0.3072 |                  1 |
| defensive_mode        |             2.0186 |                         0.3023 |            -0.1901 |                     0.4436 |                 0.2253 |                  1 |
| reduced_exposure_mode |             1.8042 |                         0.0878 |            -0.1929 |                     0.4023 |                 0.0134 |                  1 |
| cash_mode             |             1.5766 |                        -0.1398 |            -0.2024 |                     0.2935 |                -0.3028 |                  1 |

## Best Out-Of-Sample Combinations

| policy                | base_model      |   base_portfolio_size | period        |   months |   bear_months |   avg_exposure |   total_return |   bist100_total_return |   excess_return_vs_bist100 |   max_drawdown |   bist100_max_drawdown |   win_rate |   robustness_score |
|:----------------------|:----------------|----------------------:|:--------------|---------:|--------------:|---------------:|---------------:|-----------------------:|---------------------------:|---------------:|-----------------------:|-----------:|-------------------:|
| baseline              | mixed_model     |                    15 | out_of_sample |       29 |             7 |         1.0000 |         0.6964 |                 0.6867 |                     0.0097 |        -0.1644 |                -0.1675 |     0.6207 |            -0.0089 |
| baseline              | momentum_heavy  |                    15 | out_of_sample |       29 |             7 |         1.0000 |         0.6946 |                 0.6867 |                     0.0079 |        -0.1680 |                -0.1675 |     0.6207 |            -0.0177 |
| baseline              | low_volatility  |                    15 | out_of_sample |       29 |             7 |         1.0000 |         0.6843 |                 0.6867 |                    -0.0024 |        -0.1563 |                -0.1675 |     0.5862 |            -0.0219 |
| baseline              | momentum_heavy  |                     3 | out_of_sample |       29 |             7 |         1.0000 |         0.6712 |                 0.6867 |                    -0.0155 |        -0.1660 |                -0.1675 |     0.6207 |            -0.0372 |
| baseline              | trend_following |                    15 | out_of_sample |       29 |             7 |         1.0000 |         0.6618 |                 0.6867 |                    -0.0249 |        -0.1747 |                -0.1675 |     0.6207 |            -0.0638 |
| baseline              | volume_heavy    |                    15 | out_of_sample |       29 |             7 |         1.0000 |         0.6195 |                 0.6867 |                    -0.0672 |        -0.1746 |                -0.1675 |     0.6207 |            -0.1059 |
| defensive_mode        | momentum_heavy  |                     3 | out_of_sample |       29 |             7 |         1.0000 |         0.5591 |                 0.6867 |                    -0.1276 |        -0.1660 |                -0.1675 |     0.5862 |            -0.1665 |
| defensive_mode        | low_volatility  |                    15 | out_of_sample |       29 |             7 |         1.0000 |         0.5709 |                 0.6867 |                    -0.1158 |        -0.1661 |                -0.1675 |     0.5517 |            -0.1721 |
| defensive_mode        | mixed_model     |                    15 | out_of_sample |       29 |             7 |         1.0000 |         0.5894 |                 0.6867 |                    -0.0973 |        -0.1757 |                -0.1675 |     0.5517 |            -0.1728 |
| reduced_exposure_mode | momentum_heavy  |                     3 | out_of_sample |       29 |             7 |         0.8793 |         0.5333 |                 0.6867 |                    -0.1534 |        -0.1660 |                -0.1675 |     0.6207 |            -0.1752 |

## Regime Signal Coverage

- Total signal months: 93
- BIST100 below MA200 months: 19
- Below-MA200 rate: 20.43%
