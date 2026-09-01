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
| out_of_sample |  93.0000 | 0.0372 | 0.0382 | -0.0375 | -0.0046 |  0.0154 |  0.0185 |  0.0210 |  0.0274 | 0.0300 | 0.0378 | 0.0520 | 0.0613 | 0.0870 | 0.2095 |
| train         | 129.0000 | 0.0155 | 0.0348 | -0.0375 | -0.0262 | -0.0163 | -0.0142 | -0.0122 | -0.0045 | 0.0142 | 0.0239 | 0.0472 | 0.0475 | 0.0573 | 0.1788 |
| validation    |  72.0000 | 0.0247 | 0.0417 | -0.0479 | -0.0120 | -0.0070 | -0.0014 |  0.0015 |  0.0058 | 0.0233 | 0.0297 | 0.0442 | 0.0472 | 0.0793 | 0.1970 |

## Out-Of-Sample Comparison

| threshold               | period        |   months |   avg_cash_weight |   avg_qualified_count |   selection_score |   strategy_total_return |   bist100_total_return |   excess_return_over_benchmark |   strategy_max_drawdown |   bist100_max_drawdown |   win_rate |   return_vs_current_5pct |   drawdown_vs_baseline |
|:------------------------|:--------------|---------:|------------------:|----------------------:|------------------:|------------------------:|-----------------------:|-------------------------------:|------------------------:|-----------------------:|-----------:|-------------------------:|-----------------------:|
| fixed_1pct              | out_of_sample |       31 |            0.1828 |                2.4516 |           -0.1337 |                  0.6513 |                 0.6870 |                        -0.0357 |                 -0.1942 |                -0.1675 |     0.5806 |                   0.4800 |                -0.0175 |
| percentile_positive_p10 | out_of_sample |       31 |            0.3548 |                1.9355 |           -0.0073 |                  0.6089 |                 0.6870 |                        -0.0782 |                 -0.1097 |                -0.1675 |     0.5806 |                   0.4376 |                 0.0670 |
| percentile_positive_p20 | out_of_sample |       31 |            0.3548 |                1.9355 |           -0.0073 |                  0.6089 |                 0.6870 |                        -0.0782 |                 -0.1097 |                -0.1675 |     0.5806 |                   0.4376 |                 0.0670 |
| percentile_positive_p30 | out_of_sample |       31 |            0.3548 |                1.9355 |           -0.0073 |                  0.6089 |                 0.6870 |                        -0.0782 |                 -0.1097 |                -0.1675 |     0.5806 |                   0.4376 |                 0.0670 |
| percentile_positive_p40 | out_of_sample |       31 |            0.3548 |                1.9355 |           -0.0073 |                  0.6089 |                 0.6870 |                        -0.0782 |                 -0.1097 |                -0.1675 |     0.5806 |                   0.4376 |                 0.0670 |
| percentile_positive_p50 | out_of_sample |       31 |            0.3548 |                1.9355 |           -0.0073 |                  0.6089 |                 0.6870 |                        -0.0782 |                 -0.1097 |                -0.1675 |     0.5806 |                   0.4376 |                 0.0670 |
| top2_positive_est       | out_of_sample |       31 |            0.3548 |                1.9355 |           -0.0073 |                  0.6089 |                 0.6870 |                        -0.0782 |                 -0.1097 |                -0.1675 |     0.5806 |                   0.4376 |                 0.0670 |
| percentile_p10          | out_of_sample |       31 |            0.3333 |                2.0000 |           -0.0377 |                  0.5856 |                 0.6870 |                        -0.1014 |                 -0.1133 |                -0.1675 |     0.5806 |                   0.4143 |                 0.0634 |
| percentile_p20          | out_of_sample |       31 |            0.3333 |                2.0000 |           -0.0377 |                  0.5856 |                 0.6870 |                        -0.1014 |                 -0.1133 |                -0.1675 |     0.5806 |                   0.4143 |                 0.0634 |
| percentile_p30          | out_of_sample |       31 |            0.3333 |                2.0000 |           -0.0377 |                  0.5856 |                 0.6870 |                        -0.1014 |                 -0.1133 |                -0.1675 |     0.5806 |                   0.4143 |                 0.0634 |
| percentile_p40          | out_of_sample |       31 |            0.3333 |                2.0000 |           -0.0377 |                  0.5856 |                 0.6870 |                        -0.1014 |                 -0.1133 |                -0.1675 |     0.5806 |                   0.4143 |                 0.0634 |
| percentile_p50          | out_of_sample |       31 |            0.3333 |                2.0000 |           -0.0377 |                  0.5856 |                 0.6870 |                        -0.1014 |                 -0.1133 |                -0.1675 |     0.5806 |                   0.4143 |                 0.0634 |
| baseline_full_invested  | out_of_sample |       31 |            0.0000 |                3.0000 |           -0.1658 |                  0.5682 |                 0.6870 |                        -0.1189 |                 -0.1767 |                -0.1675 |     0.6129 |                   0.3969 |                 0.0000 |
| fixed_0pct              | out_of_sample |       31 |            0.1398 |                2.5806 |           -0.3362 |                  0.4547 |                 0.6870 |                        -0.2323 |                 -0.1971 |                -0.1675 |     0.5806 |                   0.2834 |                -0.0204 |
| top3_positive_est       | out_of_sample |       31 |            0.1398 |                2.5806 |           -0.3362 |                  0.4547 |                 0.6870 |                        -0.2323 |                 -0.1971 |                -0.1675 |     0.5806 |                   0.2834 |                -0.0204 |
| fixed_2pct              | out_of_sample |       31 |            0.2903 |                2.1290 |           -0.3585 |                  0.3708 |                 0.6870 |                        -0.3162 |                 -0.1502 |                -0.1675 |     0.5161 |                   0.1995 |                 0.0265 |
| top1_positive_est       | out_of_sample |       31 |            0.6667 |                1.0000 |           -0.3979 |                  0.2811 |                 0.6870 |                        -0.4059 |                 -0.1331 |                -0.1675 |     0.5484 |                   0.1098 |                 0.0436 |
| current_fixed_5pct      | out_of_sample |       31 |            0.7204 |                0.8387 |           -0.4662 |                  0.1713 |                 0.6870 |                        -0.5157 |                 -0.0639 |                -0.1675 |     0.3548 |                   0.0000 |                 0.1128 |
| fixed_3pct              | out_of_sample |       31 |            0.5269 |                1.4194 |           -0.6056 |                  0.1399 |                 0.6870 |                        -0.5472 |                 -0.1502 |                -0.1675 |     0.4839 |                  -0.0314 |                 0.0265 |

## Interpretation

The expected return estimator is noisy and has weak negative correlation with realized next-month returns. A fixed 5% threshold is above the median estimated return in most periods, so it over-allocates to CASH. A positive-floor percentile filter is more realistic: it rejects the weakest current opportunities while staying invested when the opportunity set is broadly positive.
