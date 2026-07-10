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
| out_of_sample |  90.0000 | 0.0374 | 0.0388 | -0.0375 | -0.0052 |  0.0144 |  0.0185 |  0.0210 |  0.0272 | 0.0300 | 0.0380 | 0.0520 | 0.0618 | 0.0872 | 0.2095 |
| train         | 129.0000 | 0.0155 | 0.0348 | -0.0375 | -0.0262 | -0.0163 | -0.0142 | -0.0122 | -0.0045 | 0.0142 | 0.0239 | 0.0472 | 0.0475 | 0.0573 | 0.1788 |
| validation    |  72.0000 | 0.0247 | 0.0417 | -0.0479 | -0.0120 | -0.0070 | -0.0014 |  0.0015 |  0.0058 | 0.0233 | 0.0297 | 0.0442 | 0.0472 | 0.0793 | 0.1970 |

## Out-Of-Sample Comparison

| threshold               | period        |   months |   avg_cash_weight |   avg_qualified_count |   selection_score |   strategy_total_return |   bist100_total_return |   excess_return_over_benchmark |   strategy_max_drawdown |   bist100_max_drawdown |   win_rate |   return_vs_current_5pct |   drawdown_vs_baseline |
|:------------------------|:--------------|---------:|------------------:|----------------------:|------------------:|------------------------:|-----------------------:|-------------------------------:|------------------------:|-----------------------:|-----------:|-------------------------:|-----------------------:|
| percentile_positive_p10 | out_of_sample |       30 |            0.3556 |                1.9333 |            0.0492 |                  0.6288 |                 0.6601 |                        -0.0313 |                 -0.1097 |                -0.1675 |     0.6000 |                   0.4575 |                 0.0670 |
| percentile_positive_p20 | out_of_sample |       30 |            0.3556 |                1.9333 |            0.0492 |                  0.6288 |                 0.6601 |                        -0.0313 |                 -0.1097 |                -0.1675 |     0.6000 |                   0.4575 |                 0.0670 |
| percentile_positive_p30 | out_of_sample |       30 |            0.3556 |                1.9333 |            0.0492 |                  0.6288 |                 0.6601 |                        -0.0313 |                 -0.1097 |                -0.1675 |     0.6000 |                   0.4575 |                 0.0670 |
| percentile_positive_p40 | out_of_sample |       30 |            0.3556 |                1.9333 |            0.0492 |                  0.6288 |                 0.6601 |                        -0.0313 |                 -0.1097 |                -0.1675 |     0.6000 |                   0.4575 |                 0.0670 |
| percentile_positive_p50 | out_of_sample |       30 |            0.3556 |                1.9333 |            0.0492 |                  0.6288 |                 0.6601 |                        -0.0313 |                 -0.1097 |                -0.1675 |     0.6000 |                   0.4575 |                 0.0670 |
| top2_positive_est       | out_of_sample |       30 |            0.3556 |                1.9333 |            0.0492 |                  0.6288 |                 0.6601 |                        -0.0313 |                 -0.1097 |                -0.1675 |     0.6000 |                   0.4575 |                 0.0670 |
| percentile_p10          | out_of_sample |       30 |            0.3333 |                2.0000 |            0.0185 |                  0.6052 |                 0.6601 |                        -0.0549 |                 -0.1133 |                -0.1675 |     0.6000 |                   0.4339 |                 0.0634 |
| percentile_p20          | out_of_sample |       30 |            0.3333 |                2.0000 |            0.0185 |                  0.6052 |                 0.6601 |                        -0.0549 |                 -0.1133 |                -0.1675 |     0.6000 |                   0.4339 |                 0.0634 |
| percentile_p30          | out_of_sample |       30 |            0.3333 |                2.0000 |            0.0185 |                  0.6052 |                 0.6601 |                        -0.0549 |                 -0.1133 |                -0.1675 |     0.6000 |                   0.4339 |                 0.0634 |
| percentile_p40          | out_of_sample |       30 |            0.3333 |                2.0000 |            0.0185 |                  0.6052 |                 0.6601 |                        -0.0549 |                 -0.1133 |                -0.1675 |     0.6000 |                   0.4339 |                 0.0634 |
| percentile_p50          | out_of_sample |       30 |            0.3333 |                2.0000 |            0.0185 |                  0.6052 |                 0.6601 |                        -0.0549 |                 -0.1133 |                -0.1675 |     0.6000 |                   0.4339 |                 0.0634 |
| fixed_1pct              | out_of_sample |       30 |            0.1889 |                2.4333 |           -0.2642 |                  0.5009 |                 0.6601 |                        -0.1592 |                 -0.1942 |                -0.1675 |     0.5667 |                   0.3297 |                -0.0175 |
| baseline_full_invested  | out_of_sample |       30 |            0.0000 |                3.0000 |           -0.2610 |                  0.4525 |                 0.6601 |                        -0.2076 |                 -0.1767 |                -0.1675 |     0.6000 |                   0.2813 |                 0.0000 |
| fixed_2pct              | out_of_sample |       30 |            0.2889 |                2.1333 |           -0.3060 |                  0.3878 |                 0.6601 |                        -0.2723 |                 -0.1502 |                -0.1675 |     0.5333 |                   0.2165 |                 0.0265 |
| fixed_0pct              | out_of_sample |       30 |            0.1444 |                2.5667 |           -0.4487 |                  0.3223 |                 0.6601 |                        -0.3378 |                 -0.1971 |                -0.1675 |     0.5667 |                   0.1510 |                -0.0204 |
| top3_positive_est       | out_of_sample |       30 |            0.1444 |                2.5667 |           -0.4487 |                  0.3223 |                 0.6601 |                        -0.3378 |                 -0.1971 |                -0.1675 |     0.5667 |                   0.1510 |                -0.0204 |
| top1_positive_est       | out_of_sample |       30 |            0.6667 |                1.0000 |           -0.4478 |                  0.2284 |                 0.6601 |                        -0.4317 |                 -0.1331 |                -0.1675 |     0.5000 |                   0.0572 |                 0.0436 |
| current_fixed_5pct      | out_of_sample |       30 |            0.7111 |                0.8667 |           -0.4334 |                  0.1713 |                 0.6601 |                        -0.4888 |                 -0.0639 |                -0.1675 |     0.3667 |                   0.0000 |                 0.1128 |
| fixed_3pct              | out_of_sample |       30 |            0.5222 |                1.4333 |           -0.6508 |                  0.0930 |                 0.6601 |                        -0.5671 |                 -0.1502 |                -0.1675 |     0.4333 |                  -0.0783 |                 0.0265 |

## Interpretation

The expected return estimator is noisy and has weak negative correlation with realized next-month returns. A fixed 5% threshold is above the median estimated return in most periods, so it over-allocates to CASH. A positive-floor percentile filter is more realistic: it rejects the weakest current opportunities while staying invested when the opportunity set is broadly positive.
