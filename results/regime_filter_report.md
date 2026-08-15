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
| baseline              |             2.0624 |                         0.3523 |            -0.1903 |                     0.4197 |                 0.2807 |                  1 |
| defensive_mode        |             1.9895 |                         0.2794 |            -0.1903 |                     0.3563 |                 0.1999 |                  1 |
| reduced_exposure_mode |             1.7761 |                         0.0659 |            -0.1931 |                     0.3180 |                -0.0113 |                  1 |
| cash_mode             |             1.5505 |                        -0.1596 |            -0.2026 |                     0.2152 |                -0.3236 |                  1 |

## Best Out-Of-Sample Combinations

| policy                | base_model      |   base_portfolio_size | period        |   months |   bear_months |   avg_exposure |   total_return |   bist100_total_return |   excess_return_vs_bist100 |   max_drawdown |   bist100_max_drawdown |   win_rate |   robustness_score |
|:----------------------|:----------------|----------------------:|:--------------|---------:|--------------:|---------------:|---------------:|-----------------------:|---------------------------:|---------------:|-----------------------:|-----------:|-------------------:|
| baseline              | mixed_model     |                    15 | out_of_sample |       31 |             7 |         1.0000 |         0.6215 |                 0.6680 |                    -0.0465 |        -0.1644 |                -0.1675 |     0.6129 |            -0.0689 |
| baseline              | momentum_heavy  |                    15 | out_of_sample |       31 |             7 |         1.0000 |         0.6246 |                 0.6680 |                    -0.0434 |        -0.1680 |                -0.1675 |     0.6129 |            -0.0730 |
| baseline              | low_volatility  |                    15 | out_of_sample |       31 |             7 |         1.0000 |         0.5970 |                 0.6680 |                    -0.0710 |        -0.1563 |                -0.1675 |     0.5806 |            -0.0934 |
| baseline              | trend_following |                    15 | out_of_sample |       31 |             7 |         1.0000 |         0.5984 |                 0.6680 |                    -0.0696 |        -0.1747 |                -0.1675 |     0.6129 |            -0.1125 |
| baseline              | momentum_heavy  |                     3 | out_of_sample |       31 |             7 |         1.0000 |         0.5684 |                 0.6680 |                    -0.0996 |        -0.1660 |                -0.1675 |     0.6129 |            -0.1252 |
| baseline              | volume_heavy    |                    15 | out_of_sample |       31 |             7 |         1.0000 |         0.5434 |                 0.6680 |                    -0.1246 |        -0.1746 |                -0.1675 |     0.6129 |            -0.1673 |
| defensive_mode        | mixed_model     |                    15 | out_of_sample |       31 |             7 |         1.0000 |         0.5192 |                 0.6680 |                    -0.1487 |        -0.1757 |                -0.1675 |     0.5484 |            -0.2259 |
| defensive_mode        | momentum_heavy  |                    15 | out_of_sample |       31 |             7 |         1.0000 |         0.5183 |                 0.6680 |                    -0.1497 |        -0.1792 |                -0.1675 |     0.5484 |            -0.2338 |
| reduced_exposure_mode | mixed_model     |                    15 | out_of_sample |       31 |             7 |         0.8871 |         0.4904 |                 0.6680 |                    -0.1776 |        -0.1817 |                -0.1675 |     0.6129 |            -0.2345 |
| defensive_mode        | low_volatility  |                    15 | out_of_sample |       31 |             7 |         1.0000 |         0.4894 |                 0.6680 |                    -0.1786 |        -0.1661 |                -0.1675 |     0.5484 |            -0.2365 |

## Regime Signal Coverage

- Total signal months: 95
- BIST100 below MA200 months: 19
- Below-MA200 rate: 20.00%
