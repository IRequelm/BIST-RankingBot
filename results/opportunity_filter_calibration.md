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
| fixed_1pct              | out_of_sample |       33 |            0.1818 |                2.4545 |            0.0758 |                  0.6182 |                 0.4268 |                         0.1914 |                 -0.1942 |                -0.1728 |     0.5455 |                   0.4469 |                -0.0175 |
| percentile_positive_p10 | out_of_sample |       33 |            0.3535 |                1.9394 |            0.1675 |                  0.5486 |                 0.4268 |                         0.1218 |                 -0.1135 |                -0.1728 |     0.5455 |                   0.3773 |                 0.0632 |
| percentile_positive_p20 | out_of_sample |       33 |            0.3535 |                1.9394 |            0.1675 |                  0.5486 |                 0.4268 |                         0.1218 |                 -0.1135 |                -0.1728 |     0.5455 |                   0.3773 |                 0.0632 |
| percentile_positive_p30 | out_of_sample |       33 |            0.3535 |                1.9394 |            0.1675 |                  0.5486 |                 0.4268 |                         0.1218 |                 -0.1135 |                -0.1728 |     0.5455 |                   0.3773 |                 0.0632 |
| percentile_positive_p40 | out_of_sample |       33 |            0.3535 |                1.9394 |            0.1675 |                  0.5486 |                 0.4268 |                         0.1218 |                 -0.1135 |                -0.1728 |     0.5455 |                   0.3773 |                 0.0632 |
| percentile_positive_p50 | out_of_sample |       33 |            0.3535 |                1.9394 |            0.1675 |                  0.5486 |                 0.4268 |                         0.1218 |                 -0.1135 |                -0.1728 |     0.5455 |                   0.3773 |                 0.0632 |
| top2_positive_est       | out_of_sample |       33 |            0.3535 |                1.9394 |            0.1675 |                  0.5486 |                 0.4268 |                         0.1218 |                 -0.1135 |                -0.1728 |     0.5455 |                   0.3773 |                 0.0632 |
| baseline_full_invested  | out_of_sample |       33 |            0.0000 |                3.0000 |            0.0626 |                  0.5398 |                 0.4268 |                         0.1130 |                 -0.1767 |                -0.1728 |     0.6061 |                   0.3685 |                 0.0000 |
| percentile_p10          | out_of_sample |       33 |            0.3333 |                2.0000 |            0.1451 |                  0.5262 |                 0.4268 |                         0.0994 |                 -0.1135 |                -0.1728 |     0.5455 |                   0.3549 |                 0.0632 |
| percentile_p20          | out_of_sample |       33 |            0.3333 |                2.0000 |            0.1451 |                  0.5262 |                 0.4268 |                         0.0994 |                 -0.1135 |                -0.1728 |     0.5455 |                   0.3549 |                 0.0632 |
| percentile_p30          | out_of_sample |       33 |            0.3333 |                2.0000 |            0.1451 |                  0.5262 |                 0.4268 |                         0.0994 |                 -0.1135 |                -0.1728 |     0.5455 |                   0.3549 |                 0.0632 |
| percentile_p40          | out_of_sample |       33 |            0.3333 |                2.0000 |            0.1451 |                  0.5262 |                 0.4268 |                         0.0994 |                 -0.1135 |                -0.1728 |     0.5455 |                   0.3549 |                 0.0632 |
| percentile_p50          | out_of_sample |       33 |            0.3333 |                2.0000 |            0.1451 |                  0.5262 |                 0.4268 |                         0.0994 |                 -0.1135 |                -0.1728 |     0.5455 |                   0.3549 |                 0.0632 |
| fixed_0pct              | out_of_sample |       33 |            0.1414 |                2.5758 |           -0.1227 |                  0.4256 |                 0.4268 |                        -0.0012 |                 -0.1971 |                -0.1728 |     0.5455 |                   0.2543 |                -0.0204 |
| top3_positive_est       | out_of_sample |       33 |            0.1414 |                2.5758 |           -0.1227 |                  0.4256 |                 0.4268 |                        -0.0012 |                 -0.1971 |                -0.1728 |     0.5455 |                   0.2543 |                -0.0204 |
| fixed_2pct              | out_of_sample |       33 |            0.2828 |                2.1515 |           -0.1489 |                  0.3359 |                 0.4268 |                        -0.0909 |                 -0.1502 |                -0.1728 |     0.4848 |                   0.1646 |                 0.0265 |
| top1_positive_est       | out_of_sample |       33 |            0.6667 |                1.0000 |           -0.1941 |                  0.2412 |                 0.4268 |                        -0.1856 |                 -0.1331 |                -0.1728 |     0.5152 |                   0.0699 |                 0.0436 |
| current_fixed_5pct      | out_of_sample |       33 |            0.7374 |                0.7879 |           -0.2167 |                  0.1713 |                 0.4268 |                        -0.2555 |                 -0.0639 |                -0.1728 |     0.3333 |                   0.0000 |                 0.1128 |
| fixed_3pct              | out_of_sample |       33 |            0.5152 |                1.4545 |           -0.3991 |                  0.1008 |                 0.4268 |                        -0.3260 |                 -0.1502 |                -0.1728 |     0.4545 |                  -0.0705 |                 0.0265 |

## Interpretation

The expected return estimator is noisy and has weak negative correlation with realized next-month returns. A fixed 5% threshold is above the median estimated return in most periods, so it over-allocates to CASH. A positive-floor percentile filter is more realistic: it rejects the weakest current opportunities while staying invested when the opportunity set is broadly positive.
