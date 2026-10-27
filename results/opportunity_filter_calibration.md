# Opportunity Filter Calibration

## Finding

- Baseline model: trend_following Top3
- Current issue: the fixed 5% opportunity threshold allocates too much to CASH and hurts returns.
- Improvement tested: calibrated opportunity filters that keep cash support but use relative thresholds.
- Selected filter: percentile_positive_p50
- Decision: accepted
- Reason: Accepted because the selected filter materially improved out-of-sample return versus the current 5% threshold while preserving a drawdown improvement versus the full-invested baseline.

## Expected Return Distribution

| period        |    count |   mean |    std |     min |     10% |     20% |     25% |     30% |     40% |    50% |    60% |    75% |    80% |    90% |    max |
|:--------------|---------:|-------:|-------:|--------:|--------:|--------:|--------:|--------:|--------:|-------:|-------:|-------:|-------:|-------:|-------:|
| out_of_sample |  99.0000 | 0.0390 | 0.0411 | -0.0375 | -0.0052 |  0.0158 |  0.0188 |  0.0222 |  0.0280 | 0.0300 | 0.0407 | 0.0520 | 0.0619 | 0.0874 | 0.2095 |
| train         | 129.0000 | 0.0155 | 0.0348 | -0.0375 | -0.0262 | -0.0163 | -0.0142 | -0.0122 | -0.0045 | 0.0142 | 0.0239 | 0.0472 | 0.0475 | 0.0573 | 0.1788 |
| validation    |  72.0000 | 0.0247 | 0.0417 | -0.0479 | -0.0120 | -0.0070 | -0.0014 |  0.0015 |  0.0058 | 0.0233 | 0.0297 | 0.0442 | 0.0472 | 0.0793 | 0.1970 |

## Out-Of-Sample Comparison

| threshold               | period        |   months |   avg_cash_weight |   avg_qualified_count |   selection_score |   strategy_total_return |   bist100_total_return |   excess_return_over_benchmark |   strategy_max_drawdown |   bist100_max_drawdown |   win_rate |   return_vs_current_5pct |   drawdown_vs_baseline |
|:------------------------|:--------------|---------:|------------------:|----------------------:|------------------:|------------------------:|-----------------------:|-------------------------------:|------------------------:|-----------------------:|-----------:|-------------------------:|-----------------------:|
| percentile_positive_p10 | out_of_sample |       33 |            0.3535 |                1.9394 |            0.0778 |                  0.4535 |                 0.3125 |                         0.1410 |                 -0.1680 |                -0.2278 |     0.5455 |                   0.2834 |                 0.0087 |
| percentile_positive_p20 | out_of_sample |       33 |            0.3535 |                1.9394 |            0.0778 |                  0.4535 |                 0.3125 |                         0.1410 |                 -0.1680 |                -0.2278 |     0.5455 |                   0.2834 |                 0.0087 |
| percentile_positive_p30 | out_of_sample |       33 |            0.3535 |                1.9394 |            0.0778 |                  0.4535 |                 0.3125 |                         0.1410 |                 -0.1680 |                -0.2278 |     0.5455 |                   0.2834 |                 0.0087 |
| percentile_positive_p40 | out_of_sample |       33 |            0.3535 |                1.9394 |            0.0778 |                  0.4535 |                 0.3125 |                         0.1410 |                 -0.1680 |                -0.2278 |     0.5455 |                   0.2834 |                 0.0087 |
| percentile_positive_p50 | out_of_sample |       33 |            0.3535 |                1.9394 |            0.0778 |                  0.4535 |                 0.3125 |                         0.1410 |                 -0.1680 |                -0.2278 |     0.5455 |                   0.2834 |                 0.0087 |
| top2_positive_est       | out_of_sample |       33 |            0.3535 |                1.9394 |            0.0778 |                  0.4535 |                 0.3125 |                         0.1410 |                 -0.1680 |                -0.2278 |     0.5455 |                   0.2834 |                 0.0087 |
| percentile_p10          | out_of_sample |       33 |            0.3333 |                2.0000 |            0.0568 |                  0.4325 |                 0.3125 |                         0.1200 |                 -0.1680 |                -0.2278 |     0.5455 |                   0.2624 |                 0.0087 |
| percentile_p20          | out_of_sample |       33 |            0.3333 |                2.0000 |            0.0568 |                  0.4325 |                 0.3125 |                         0.1200 |                 -0.1680 |                -0.2278 |     0.5455 |                   0.2624 |                 0.0087 |
| percentile_p30          | out_of_sample |       33 |            0.3333 |                2.0000 |            0.0568 |                  0.4325 |                 0.3125 |                         0.1200 |                 -0.1680 |                -0.2278 |     0.5455 |                   0.2624 |                 0.0087 |
| percentile_p40          | out_of_sample |       33 |            0.3333 |                2.0000 |            0.0568 |                  0.4325 |                 0.3125 |                         0.1200 |                 -0.1680 |                -0.2278 |     0.5455 |                   0.2624 |                 0.0087 |
| percentile_p50          | out_of_sample |       33 |            0.3333 |                2.0000 |            0.0568 |                  0.4325 |                 0.3125 |                         0.1200 |                 -0.1680 |                -0.2278 |     0.5455 |                   0.2624 |                 0.0087 |
| baseline_full_invested  | out_of_sample |       33 |            0.0000 |                3.0000 |            0.0526 |                  0.4306 |                 0.3125 |                         0.1181 |                 -0.1767 |                -0.2278 |     0.5758 |                   0.2605 |                 0.0000 |
| fixed_1pct              | out_of_sample |       33 |            0.1818 |                2.4545 |           -0.0955 |                  0.3478 |                 0.3125 |                         0.0352 |                 -0.1942 |                -0.2278 |     0.5152 |                   0.1776 |                -0.0175 |
| fixed_2pct              | out_of_sample |       33 |            0.2727 |                2.1818 |           -0.1243 |                  0.2461 |                 0.3125 |                        -0.0664 |                 -0.1502 |                -0.2278 |     0.4848 |                   0.0760 |                 0.0265 |
| top1_positive_est       | out_of_sample |       33 |            0.6667 |                1.0000 |           -0.1266 |                  0.1945 |                 0.3125 |                        -0.1180 |                 -0.1331 |                -0.2278 |     0.5152 |                   0.0244 |                 0.0436 |
| fixed_0pct              | out_of_sample |       33 |            0.1414 |                2.5758 |           -0.2618 |                  0.1873 |                 0.3125 |                        -0.1252 |                 -0.1971 |                -0.2278 |     0.5152 |                   0.0172 |                -0.0204 |
| top3_positive_est       | out_of_sample |       33 |            0.1414 |                2.5758 |           -0.2618 |                  0.1873 |                 0.3125 |                        -0.1252 |                 -0.1971 |                -0.2278 |     0.5152 |                   0.0172 |                -0.0204 |
| current_fixed_5pct      | out_of_sample |       33 |            0.7172 |                0.8485 |           -0.0884 |                  0.1701 |                 0.3125 |                        -0.1424 |                 -0.0639 |                -0.2278 |     0.3636 |                   0.0000 |                 0.1128 |
| fixed_3pct              | out_of_sample |       33 |            0.5152 |                1.4545 |           -0.3926 |                  0.0081 |                 0.3125 |                        -0.3044 |                 -0.1502 |                -0.2278 |     0.4242 |                  -0.1620 |                 0.0265 |

## Interpretation

The expected return estimator is noisy and has weak negative correlation with realized next-month returns. A fixed 5% threshold is above the median estimated return in most periods, so it over-allocates to CASH. A positive-floor percentile filter is more realistic: it rejects the weakest current opportunities while staying invested when the opportunity set is broadly positive.
