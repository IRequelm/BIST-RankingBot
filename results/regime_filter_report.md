# Regime Filter Report

Policies tested:
- baseline: current ranking/backtest system
- cash_mode: hold cash when BIST100 is below MA200
- defensive_mode: switch to low_volatility Top 5 when BIST100 is below MA200
- reduced_exposure_mode: invest 50% when BIST100 is below MA200

Recommended policy: **defensive_mode**

Recommendation is based on average robustness score across model and portfolio combinations.

## Policy Summary

| policy                |   avg_total_return |   avg_excess_return_vs_bist100 |   avg_max_drawdown |   avg_out_of_sample_return |   avg_robustness_score |   best_combo_count |
|:----------------------|-------------------:|-------------------------------:|-------------------:|---------------------------:|-----------------------:|-------------------:|
| defensive_mode        |             2.0310 |                         0.3393 |            -0.2057 |                     0.8151 |                 0.2439 |                  1 |
| baseline              |             1.9612 |                         0.2694 |            -0.2074 |                     0.6641 |                 0.1761 |                  1 |
| reduced_exposure_mode |             1.6323 |                        -0.0594 |            -0.2162 |                     0.4829 |                -0.1704 |                  1 |
| cash_mode             |             1.3798 |                        -0.3120 |            -0.2474 |                     0.3103 |                -0.5566 |                  1 |

## Best Out-Of-Sample Combinations

| policy         | base_model      |   base_portfolio_size | period        |   months |   bear_months |   avg_exposure |   total_return |   bist100_total_return |   excess_return_vs_bist100 |   max_drawdown |   bist100_max_drawdown |   win_rate |   robustness_score |
|:---------------|:----------------|----------------------:|:--------------|---------:|--------------:|---------------:|---------------:|-----------------------:|---------------------------:|---------------:|-----------------------:|-----------:|-------------------:|
| defensive_mode | volume_heavy    |                    10 | out_of_sample |       29 |             7 |         1.0000 |         1.1034 |                 0.6129 |                     0.4905 |        -0.1378 |                -0.1675 |     0.5862 |             0.5081 |
| baseline       | momentum_heavy  |                     5 | out_of_sample |       29 |             7 |         1.0000 |         1.0177 |                 0.6129 |                     0.4048 |        -0.1350 |                -0.1675 |     0.6207 |             0.4453 |
| defensive_mode | low_volatility  |                    10 | out_of_sample |       29 |             7 |         1.0000 |         1.0114 |                 0.6129 |                     0.3985 |        -0.1578 |                -0.1675 |     0.6207 |             0.3933 |
| defensive_mode | momentum_heavy  |                     5 | out_of_sample |       29 |             7 |         1.0000 |         0.9680 |                 0.6129 |                     0.3552 |        -0.1350 |                -0.1675 |     0.5862 |             0.3784 |
| defensive_mode | low_volatility  |                     5 | out_of_sample |       29 |             7 |         1.0000 |         0.9254 |                 0.6129 |                     0.3126 |        -0.1446 |                -0.1675 |     0.5862 |             0.3164 |
| baseline       | low_volatility  |                     5 | out_of_sample |       29 |             7 |         1.0000 |         0.9254 |                 0.6129 |                     0.3126 |        -0.1446 |                -0.1675 |     0.5862 |             0.3164 |
| baseline       | low_volatility  |                    10 | out_of_sample |       29 |             7 |         1.0000 |         0.8833 |                 0.6129 |                     0.2704 |        -0.1578 |                -0.1675 |     0.6552 |             0.2825 |
| defensive_mode | mixed_model     |                    10 | out_of_sample |       29 |             7 |         1.0000 |         0.8603 |                 0.6129 |                     0.2475 |        -0.1418 |                -0.1675 |     0.5172 |             0.2225 |
| defensive_mode | trend_following |                    15 | out_of_sample |       29 |             7 |         1.0000 |         0.8603 |                 0.6129 |                     0.2474 |        -0.1662 |                -0.1675 |     0.5517 |             0.1908 |
| defensive_mode | volume_heavy    |                    15 | out_of_sample |       29 |             7 |         1.0000 |         0.8977 |                 0.6129 |                     0.2849 |        -0.1780 |                -0.1675 |     0.5172 |             0.1875 |

## Regime Signal Coverage

- Total signal months: 93
- BIST100 below MA200 months: 19
- Below-MA200 rate: 20.43%
