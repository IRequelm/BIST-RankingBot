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
| baseline              |             2.0919 |                         0.3783 |            -0.1902 |                     0.5081 |                 0.3092 |                  1 |
| defensive_mode        |             2.0179 |                         0.3044 |            -0.1901 |                     0.4416 |                 0.2274 |                  1 |
| reduced_exposure_mode |             1.8035 |                         0.0900 |            -0.1929 |                     0.4003 |                 0.0155 |                  1 |
| cash_mode             |             1.5760 |                        -0.1376 |            -0.2024 |                     0.2917 |                -0.3006 |                  1 |

## Best Out-Of-Sample Combinations

| policy                | base_model      |   base_portfolio_size | period        |   months |   bear_months |   avg_exposure |   total_return |   bist100_total_return |   excess_return_vs_bist100 |   max_drawdown |   bist100_max_drawdown |   win_rate |   robustness_score |
|:----------------------|:----------------|----------------------:|:--------------|---------:|--------------:|---------------:|---------------:|-----------------------:|---------------------------:|---------------:|-----------------------:|-----------:|-------------------:|
| baseline              | mixed_model     |                    15 | out_of_sample |       29 |             7 |         1.0000 |         0.6942 |                 0.6783 |                     0.0159 |        -0.1644 |                -0.1675 |     0.6207 |            -0.0027 |
| baseline              | low_volatility  |                    15 | out_of_sample |       29 |             7 |         1.0000 |         0.6821 |                 0.6783 |                     0.0039 |        -0.1563 |                -0.1675 |     0.5862 |            -0.0157 |
| baseline              | momentum_heavy  |                    15 | out_of_sample |       29 |             7 |         1.0000 |         0.6854 |                 0.6783 |                     0.0071 |        -0.1680 |                -0.1675 |     0.6207 |            -0.0186 |
| baseline              | momentum_heavy  |                     3 | out_of_sample |       29 |             7 |         1.0000 |         0.6687 |                 0.6783 |                    -0.0095 |        -0.1660 |                -0.1675 |     0.6207 |            -0.0313 |
| baseline              | trend_following |                    15 | out_of_sample |       29 |             7 |         1.0000 |         0.6597 |                 0.6783 |                    -0.0186 |        -0.1747 |                -0.1675 |     0.6207 |            -0.0576 |
| baseline              | volume_heavy    |                    15 | out_of_sample |       29 |             7 |         1.0000 |         0.6091 |                 0.6783 |                    -0.0692 |        -0.1746 |                -0.1675 |     0.6207 |            -0.1079 |
| defensive_mode        | momentum_heavy  |                     3 | out_of_sample |       29 |             7 |         1.0000 |         0.5568 |                 0.6783 |                    -0.1215 |        -0.1660 |                -0.1675 |     0.5862 |            -0.1604 |
| defensive_mode        | low_volatility  |                    15 | out_of_sample |       29 |             7 |         1.0000 |         0.5688 |                 0.6783 |                    -0.1095 |        -0.1661 |                -0.1675 |     0.5517 |            -0.1657 |
| defensive_mode        | mixed_model     |                    15 | out_of_sample |       29 |             7 |         1.0000 |         0.5873 |                 0.6783 |                    -0.0909 |        -0.1757 |                -0.1675 |     0.5517 |            -0.1665 |
| reduced_exposure_mode | momentum_heavy  |                     3 | out_of_sample |       29 |             7 |         0.8793 |         0.5310 |                 0.6783 |                    -0.1473 |        -0.1660 |                -0.1675 |     0.6207 |            -0.1690 |

## Regime Signal Coverage

- Total signal months: 93
- BIST100 below MA200 months: 19
- Below-MA200 rate: 20.43%
