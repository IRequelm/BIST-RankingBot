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
| out_of_sample |  96.0000 | 0.0373 | 0.0376 | -0.0375 | -0.0039 |  0.0167 |  0.0185 |  0.0215 |  0.0279 | 0.0300 | 0.0385 | 0.0518 | 0.0605 | 0.0870 | 0.2095 |
| train         | 129.0000 | 0.0155 | 0.0348 | -0.0375 | -0.0262 | -0.0163 | -0.0142 | -0.0122 | -0.0045 | 0.0142 | 0.0239 | 0.0472 | 0.0475 | 0.0573 | 0.1788 |
| validation    |  72.0000 | 0.0247 | 0.0417 | -0.0479 | -0.0120 | -0.0070 | -0.0014 |  0.0015 |  0.0058 | 0.0233 | 0.0297 | 0.0442 | 0.0472 | 0.0793 | 0.1970 |

## Out-Of-Sample Comparison

| threshold               | period        |   months |   avg_cash_weight |   avg_qualified_count |   selection_score |   strategy_total_return |   bist100_total_return |   excess_return_over_benchmark |   strategy_max_drawdown |   bist100_max_drawdown |   win_rate |   return_vs_current_5pct |   drawdown_vs_baseline |
|:------------------------|:--------------|---------:|------------------:|----------------------:|------------------:|------------------------:|-----------------------:|-------------------------------:|------------------------:|-----------------------:|-----------:|-------------------------:|-----------------------:|
| fixed_1pct              | out_of_sample |       32 |            0.1771 |                2.4688 |            0.1249 |                  0.6381 |                 0.4061 |                         0.2320 |                 -0.1942 |                -0.1728 |     0.5625 |                   0.4668 |                -0.0175 |
| percentile_positive_p10 | out_of_sample |       32 |            0.3542 |                1.9375 |            0.2193 |                  0.5636 |                 0.4061 |                         0.1575 |                 -0.1097 |                -0.1728 |     0.5625 |                   0.3923 |                 0.0670 |
| percentile_positive_p20 | out_of_sample |       32 |            0.3542 |                1.9375 |            0.2193 |                  0.5636 |                 0.4061 |                         0.1575 |                 -0.1097 |                -0.1728 |     0.5625 |                   0.3923 |                 0.0670 |
| percentile_positive_p30 | out_of_sample |       32 |            0.3542 |                1.9375 |            0.2193 |                  0.5636 |                 0.4061 |                         0.1575 |                 -0.1097 |                -0.1728 |     0.5625 |                   0.3923 |                 0.0670 |
| percentile_positive_p40 | out_of_sample |       32 |            0.3542 |                1.9375 |            0.2193 |                  0.5636 |                 0.4061 |                         0.1575 |                 -0.1097 |                -0.1728 |     0.5625 |                   0.3923 |                 0.0670 |
| percentile_positive_p50 | out_of_sample |       32 |            0.3542 |                1.9375 |            0.2193 |                  0.5636 |                 0.4061 |                         0.1575 |                 -0.1097 |                -0.1728 |     0.5625 |                   0.3923 |                 0.0670 |
| top2_positive_est       | out_of_sample |       32 |            0.3542 |                1.9375 |            0.2193 |                  0.5636 |                 0.4061 |                         0.1575 |                 -0.1097 |                -0.1728 |     0.5625 |                   0.3923 |                 0.0670 |
| baseline_full_invested  | out_of_sample |       32 |            0.0000 |                3.0000 |            0.0930 |                  0.5556 |                 0.4061 |                         0.1495 |                 -0.1767 |                -0.1728 |     0.5938 |                   0.3843 |                 0.0000 |
| percentile_p10          | out_of_sample |       32 |            0.3333 |                2.0000 |            0.1896 |                  0.5410 |                 0.4061 |                         0.1349 |                 -0.1133 |                -0.1728 |     0.5625 |                   0.3697 |                 0.0634 |
| percentile_p20          | out_of_sample |       32 |            0.3333 |                2.0000 |            0.1896 |                  0.5410 |                 0.4061 |                         0.1349 |                 -0.1133 |                -0.1728 |     0.5625 |                   0.3697 |                 0.0634 |
| percentile_p30          | out_of_sample |       32 |            0.3333 |                2.0000 |            0.1896 |                  0.5410 |                 0.4061 |                         0.1349 |                 -0.1133 |                -0.1728 |     0.5625 |                   0.3697 |                 0.0634 |
| percentile_p40          | out_of_sample |       32 |            0.3333 |                2.0000 |            0.1896 |                  0.5410 |                 0.4061 |                         0.1349 |                 -0.1133 |                -0.1728 |     0.5625 |                   0.3697 |                 0.0634 |
| percentile_p50          | out_of_sample |       32 |            0.3333 |                2.0000 |            0.1896 |                  0.5410 |                 0.4061 |                         0.1349 |                 -0.1133 |                -0.1728 |     0.5625 |                   0.3697 |                 0.0634 |
| fixed_0pct              | out_of_sample |       32 |            0.1354 |                2.5938 |           -0.0760 |                  0.4431 |                 0.4061 |                         0.0370 |                 -0.1971 |                -0.1728 |     0.5625 |                   0.2718 |                -0.0204 |
| top3_positive_est       | out_of_sample |       32 |            0.1354 |                2.5938 |           -0.0760 |                  0.4431 |                 0.4061 |                         0.0370 |                 -0.1971 |                -0.1728 |     0.5625 |                   0.2718 |                -0.0204 |
| fixed_2pct              | out_of_sample |       32 |            0.2812 |                2.1562 |           -0.1042 |                  0.3523 |                 0.4061 |                        -0.0538 |                 -0.1502 |                -0.1728 |     0.5000 |                   0.1810 |                 0.0265 |
| top1_positive_est       | out_of_sample |       32 |            0.6667 |                1.0000 |           -0.1551 |                  0.2515 |                 0.4061 |                        -0.1546 |                 -0.1331 |                -0.1728 |     0.5312 |                   0.0803 |                 0.0436 |
| current_fixed_5pct      | out_of_sample |       32 |            0.7292 |                0.8125 |           -0.1908 |                  0.1713 |                 0.4061 |                        -0.2348 |                 -0.0639 |                -0.1728 |     0.3438 |                   0.0000 |                 0.1128 |
| fixed_3pct              | out_of_sample |       32 |            0.5208 |                1.4375 |           -0.3607 |                  0.1114 |                 0.4061 |                        -0.2947 |                 -0.1502 |                -0.1728 |     0.4688 |                  -0.0599 |                 0.0265 |

## Interpretation

The expected return estimator is noisy and has weak negative correlation with realized next-month returns. A fixed 5% threshold is above the median estimated return in most periods, so it over-allocates to CASH. A positive-floor percentile filter is more realistic: it rejects the weakest current opportunities while staying invested when the opportunity set is broadly positive.
