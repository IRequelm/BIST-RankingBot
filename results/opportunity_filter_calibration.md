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
| out_of_sample |  99.0000 | 0.0370 | 0.0374 | -0.0375 | -0.0052 |  0.0158 |  0.0185 |  0.0214 |  0.0280 | 0.0300 | 0.0402 | 0.0511 | 0.0599 | 0.0870 | 0.2095 |
| train         | 129.0000 | 0.0155 | 0.0348 | -0.0375 | -0.0262 | -0.0163 | -0.0142 | -0.0122 | -0.0045 | 0.0142 | 0.0239 | 0.0472 | 0.0475 | 0.0573 | 0.1788 |
| validation    |  72.0000 | 0.0247 | 0.0417 | -0.0479 | -0.0120 | -0.0070 | -0.0014 |  0.0015 |  0.0058 | 0.0233 | 0.0297 | 0.0442 | 0.0472 | 0.0793 | 0.1970 |

## Out-Of-Sample Comparison

| threshold               | period        |   months |   avg_cash_weight |   avg_qualified_count |   selection_score |   strategy_total_return |   bist100_total_return |   excess_return_over_benchmark |   strategy_max_drawdown |   bist100_max_drawdown |   win_rate |   return_vs_current_5pct |   drawdown_vs_baseline |
|:------------------------|:--------------|---------:|------------------:|----------------------:|------------------:|------------------------:|-----------------------:|-------------------------------:|------------------------:|-----------------------:|-----------:|-------------------------:|-----------------------:|
| fixed_1pct              | out_of_sample |       33 |            0.1818 |                2.4545 |            0.0702 |                  0.6270 |                 0.4564 |                         0.1706 |                 -0.1942 |                -0.1728 |     0.5758 |                   0.4557 |                -0.0175 |
| baseline_full_invested  | out_of_sample |       33 |            0.0000 |                3.0000 |            0.0578 |                  0.5645 |                 0.4564 |                         0.1081 |                 -0.1767 |                -0.1728 |     0.6061 |                   0.3932 |                 0.0000 |
| percentile_positive_p10 | out_of_sample |       33 |            0.3535 |                1.9394 |            0.1622 |                  0.5571 |                 0.4564 |                         0.1007 |                 -0.1132 |                -0.1728 |     0.5758 |                   0.3858 |                 0.0635 |
| percentile_positive_p20 | out_of_sample |       33 |            0.3535 |                1.9394 |            0.1622 |                  0.5571 |                 0.4564 |                         0.1007 |                 -0.1132 |                -0.1728 |     0.5758 |                   0.3858 |                 0.0635 |
| percentile_positive_p30 | out_of_sample |       33 |            0.3535 |                1.9394 |            0.1622 |                  0.5571 |                 0.4564 |                         0.1007 |                 -0.1132 |                -0.1728 |     0.5758 |                   0.3858 |                 0.0635 |
| percentile_positive_p40 | out_of_sample |       33 |            0.3535 |                1.9394 |            0.1622 |                  0.5571 |                 0.4564 |                         0.1007 |                 -0.1132 |                -0.1728 |     0.5758 |                   0.3858 |                 0.0635 |
| percentile_positive_p50 | out_of_sample |       33 |            0.3535 |                1.9394 |            0.1622 |                  0.5571 |                 0.4564 |                         0.1007 |                 -0.1132 |                -0.1728 |     0.5758 |                   0.3858 |                 0.0635 |
| top2_positive_est       | out_of_sample |       33 |            0.3535 |                1.9394 |            0.1622 |                  0.5571 |                 0.4564 |                         0.1007 |                 -0.1132 |                -0.1728 |     0.5758 |                   0.3858 |                 0.0635 |
| percentile_p10          | out_of_sample |       33 |            0.3333 |                2.0000 |            0.1395 |                  0.5346 |                 0.4564 |                         0.0782 |                 -0.1133 |                -0.1728 |     0.5758 |                   0.3633 |                 0.0634 |
| percentile_p20          | out_of_sample |       33 |            0.3333 |                2.0000 |            0.1395 |                  0.5346 |                 0.4564 |                         0.0782 |                 -0.1133 |                -0.1728 |     0.5758 |                   0.3633 |                 0.0634 |
| percentile_p30          | out_of_sample |       33 |            0.3333 |                2.0000 |            0.1395 |                  0.5346 |                 0.4564 |                         0.0782 |                 -0.1133 |                -0.1728 |     0.5758 |                   0.3633 |                 0.0634 |
| percentile_p40          | out_of_sample |       33 |            0.3333 |                2.0000 |            0.1395 |                  0.5346 |                 0.4564 |                         0.0782 |                 -0.1133 |                -0.1728 |     0.5758 |                   0.3633 |                 0.0634 |
| percentile_p50          | out_of_sample |       33 |            0.3333 |                2.0000 |            0.1395 |                  0.5346 |                 0.4564 |                         0.0782 |                 -0.1133 |                -0.1728 |     0.5758 |                   0.3633 |                 0.0634 |
| fixed_0pct              | out_of_sample |       33 |            0.1414 |                2.5758 |           -0.1294 |                  0.4333 |                 0.4564 |                        -0.0230 |                 -0.1971 |                -0.1728 |     0.5758 |                   0.2621 |                -0.0204 |
| top3_positive_est       | out_of_sample |       33 |            0.1414 |                2.5758 |           -0.1294 |                  0.4333 |                 0.4564 |                        -0.0230 |                 -0.1971 |                -0.1728 |     0.5758 |                   0.2621 |                -0.0204 |
| fixed_2pct              | out_of_sample |       33 |            0.2828 |                2.1515 |           -0.1560 |                  0.3432 |                 0.4564 |                        -0.1132 |                 -0.1502 |                -0.1728 |     0.5152 |                   0.1719 |                 0.0265 |
| top1_positive_est       | out_of_sample |       33 |            0.6667 |                1.0000 |           -0.2195 |                  0.2455 |                 0.4564 |                        -0.2109 |                 -0.1331 |                -0.1728 |     0.5152 |                   0.0742 |                 0.0436 |
| current_fixed_5pct      | out_of_sample |       33 |            0.7374 |                0.7879 |           -0.2463 |                  0.1713 |                 0.4564 |                        -0.2851 |                 -0.0639 |                -0.1728 |     0.3333 |                   0.0000 |                 0.1128 |
| fixed_3pct              | out_of_sample |       33 |            0.5152 |                1.4545 |           -0.4075 |                  0.1068 |                 0.4564 |                        -0.3496 |                 -0.1502 |                -0.1728 |     0.4848 |                  -0.0645 |                 0.0265 |

## Interpretation

The expected return estimator is noisy and has weak negative correlation with realized next-month returns. A fixed 5% threshold is above the median estimated return in most periods, so it over-allocates to CASH. A positive-floor percentile filter is more realistic: it rejects the weakest current opportunities while staying invested when the opportunity set is broadly positive.
