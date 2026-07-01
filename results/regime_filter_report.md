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
| baseline              |             2.0801 |                         0.3719 |            -0.1902 |                     0.4727 |                 0.3008 |                  1 |
| defensive_mode        |             2.0066 |                         0.2985 |            -0.1901 |                     0.4076 |                 0.2195 |                  1 |
| reduced_exposure_mode |             1.7926 |                         0.0844 |            -0.1929 |                     0.3674 |                 0.0079 |                  1 |
| cash_mode             |             1.5658 |                        -0.1423 |            -0.2024 |                     0.2612 |                -0.3074 |                  1 |

## Best Out-Of-Sample Combinations

| policy                | base_model      |   base_portfolio_size | period        |   months |   bear_months |   avg_exposure |   total_return |   bist100_total_return |   excess_return_vs_bist100 |   max_drawdown |   bist100_max_drawdown |   win_rate |   robustness_score |
|:----------------------|:----------------|----------------------:|:--------------|---------:|--------------:|---------------:|---------------:|-----------------------:|---------------------------:|---------------:|-----------------------:|-----------:|-------------------:|
| baseline              | mixed_model     |                    15 | out_of_sample |       29 |             7 |         1.0000 |         0.6651 |                 0.6620 |                     0.0031 |        -0.1644 |                -0.1675 |     0.6207 |            -0.0155 |
| baseline              | low_volatility  |                    15 | out_of_sample |       29 |             7 |         1.0000 |         0.6533 |                 0.6620 |                    -0.0088 |        -0.1563 |                -0.1675 |     0.5862 |            -0.0283 |
| baseline              | momentum_heavy  |                    15 | out_of_sample |       29 |             7 |         1.0000 |         0.6580 |                 0.6620 |                    -0.0041 |        -0.1680 |                -0.1675 |     0.6207 |            -0.0297 |
| baseline              | trend_following |                    15 | out_of_sample |       29 |             7 |         1.0000 |         0.6312 |                 0.6620 |                    -0.0308 |        -0.1747 |                -0.1675 |     0.6207 |            -0.0698 |
| baseline              | momentum_heavy  |                     3 | out_of_sample |       29 |             7 |         1.0000 |         0.6077 |                 0.6620 |                    -0.0543 |        -0.1660 |                -0.1675 |     0.6207 |            -0.0761 |
| baseline              | volume_heavy    |                    15 | out_of_sample |       29 |             7 |         1.0000 |         0.5849 |                 0.6620 |                    -0.0772 |        -0.1746 |                -0.1675 |     0.6207 |            -0.1159 |
| defensive_mode        | low_volatility  |                    15 | out_of_sample |       29 |             7 |         1.0000 |         0.5419 |                 0.6620 |                    -0.1201 |        -0.1661 |                -0.1675 |     0.5517 |            -0.1764 |
| defensive_mode        | mixed_model     |                    15 | out_of_sample |       29 |             7 |         1.0000 |         0.5601 |                 0.6620 |                    -0.1019 |        -0.1757 |                -0.1675 |     0.5517 |            -0.1774 |
| reduced_exposure_mode | mixed_model     |                    15 | out_of_sample |       29 |             7 |         0.8793 |         0.5305 |                 0.6620 |                    -0.1316 |        -0.1817 |                -0.1675 |     0.6207 |            -0.1845 |
| reduced_exposure_mode | low_volatility  |                    15 | out_of_sample |       29 |             7 |         0.8793 |         0.5162 |                 0.6620 |                    -0.1458 |        -0.1688 |                -0.1675 |     0.5862 |            -0.1903 |

## Regime Signal Coverage

- Total signal months: 93
- BIST100 below MA200 months: 19
- Below-MA200 rate: 20.43%
