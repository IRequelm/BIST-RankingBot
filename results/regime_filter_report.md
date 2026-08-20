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
| baseline              |             2.0718 |                         0.3505 |            -0.1903 |                     0.4479 |                 0.2786 |                  1 |
| defensive_mode        |             1.9985 |                         0.2771 |            -0.1903 |                     0.3832 |                 0.1974 |                  1 |
| reduced_exposure_mode |             1.7848 |                         0.0634 |            -0.1931 |                     0.3441 |                -0.0141 |                  1 |
| cash_mode             |             1.5585 |                        -0.1628 |            -0.2026 |                     0.2394 |                -0.3271 |                  1 |

## Best Out-Of-Sample Combinations

| policy                | base_model      |   base_portfolio_size | period        |   months |   bear_months |   avg_exposure |   total_return |   bist100_total_return |   excess_return_vs_bist100 |   max_drawdown |   bist100_max_drawdown |   win_rate |   robustness_score |
|:----------------------|:----------------|----------------------:|:--------------|---------:|--------------:|---------------:|---------------:|-----------------------:|---------------------------:|---------------:|-----------------------:|-----------:|-------------------:|
| baseline              | momentum_heavy  |                     3 | out_of_sample |       31 |             7 |         1.0000 |         0.6391 |                 0.7017 |                    -0.0626 |        -0.1660 |                -0.1675 |     0.6129 |            -0.0882 |
| baseline              | mixed_model     |                    15 | out_of_sample |       31 |             7 |         1.0000 |         0.6229 |                 0.7017 |                    -0.0788 |        -0.1644 |                -0.1675 |     0.6129 |            -0.1012 |
| baseline              | momentum_heavy  |                    15 | out_of_sample |       31 |             7 |         1.0000 |         0.6260 |                 0.7017 |                    -0.0757 |        -0.1680 |                -0.1675 |     0.6129 |            -0.1052 |
| baseline              | low_volatility  |                    15 | out_of_sample |       31 |             7 |         1.0000 |         0.6012 |                 0.7017 |                    -0.1006 |        -0.1563 |                -0.1675 |     0.5806 |            -0.1229 |
| baseline              | trend_following |                    15 | out_of_sample |       31 |             7 |         1.0000 |         0.5998 |                 0.7017 |                    -0.1019 |        -0.1747 |                -0.1675 |     0.6129 |            -0.1448 |
| baseline              | volume_heavy    |                    15 | out_of_sample |       31 |             7 |         1.0000 |         0.5447 |                 0.7017 |                    -0.1570 |        -0.1746 |                -0.1675 |     0.6129 |            -0.1997 |
| defensive_mode        | momentum_heavy  |                     3 | out_of_sample |       31 |             7 |         1.0000 |         0.5292 |                 0.7017 |                    -0.1725 |        -0.1660 |                -0.1675 |     0.5806 |            -0.2143 |
| reduced_exposure_mode | momentum_heavy  |                     3 | out_of_sample |       31 |             7 |         0.8871 |         0.5038 |                 0.7017 |                    -0.1979 |        -0.1660 |                -0.1675 |     0.6129 |            -0.2235 |
| baseline              | trend_following |                     3 | out_of_sample |       31 |             7 |         1.0000 |         0.4980 |                 0.7017 |                    -0.2037 |        -0.1767 |                -0.1675 |     0.6129 |            -0.2507 |
| defensive_mode        | mixed_model     |                    15 | out_of_sample |       31 |             7 |         1.0000 |         0.5206 |                 0.7017 |                    -0.1811 |        -0.1757 |                -0.1675 |     0.5484 |            -0.2583 |

## Regime Signal Coverage

- Total signal months: 95
- BIST100 below MA200 months: 19
- Below-MA200 rate: 20.00%
