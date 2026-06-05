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
| out_of_sample |  87.0000 | 0.0381 | 0.0389 | -0.0375 | -0.0037 |  0.0149 |  0.0185 |  0.0210 |  0.0271 | 0.0300 | 0.0382 | 0.0542 | 0.0619 | 0.0881 | 0.2095 |
| train         | 129.0000 | 0.0155 | 0.0348 | -0.0375 | -0.0262 | -0.0163 | -0.0142 | -0.0122 | -0.0045 | 0.0142 | 0.0239 | 0.0472 | 0.0475 | 0.0573 | 0.1788 |
| validation    |  72.0000 | 0.0247 | 0.0417 | -0.0479 | -0.0120 | -0.0070 | -0.0014 |  0.0015 |  0.0058 | 0.0233 | 0.0297 | 0.0442 | 0.0472 | 0.0793 | 0.1970 |

## Out-Of-Sample Comparison

| threshold               | period        |   months |   avg_cash_weight |   avg_qualified_count |   selection_score |   strategy_total_return |   bist100_total_return |   excess_return_over_benchmark |   strategy_max_drawdown |   bist100_max_drawdown |   win_rate |   return_vs_current_5pct |   drawdown_vs_baseline |
|:------------------------|:--------------|---------:|------------------:|----------------------:|------------------:|------------------------:|-----------------------:|-------------------------------:|------------------------:|-----------------------:|-----------:|-------------------------:|-----------------------:|
| percentile_positive_p10 | out_of_sample |       29 |            0.3563 |                1.9310 |            0.1013 |                  0.6405 |                 0.6129 |                         0.0277 |                 -0.1097 |                -0.1675 |     0.5862 |                   0.4849 |                 0.0670 |
| percentile_positive_p20 | out_of_sample |       29 |            0.3563 |                1.9310 |            0.1013 |                  0.6405 |                 0.6129 |                         0.0277 |                 -0.1097 |                -0.1675 |     0.5862 |                   0.4849 |                 0.0670 |
| percentile_positive_p30 | out_of_sample |       29 |            0.3563 |                1.9310 |            0.1013 |                  0.6405 |                 0.6129 |                         0.0277 |                 -0.1097 |                -0.1675 |     0.5862 |                   0.4849 |                 0.0670 |
| percentile_positive_p40 | out_of_sample |       29 |            0.3563 |                1.9310 |            0.1013 |                  0.6405 |                 0.6129 |                         0.0277 |                 -0.1097 |                -0.1675 |     0.5862 |                   0.4849 |                 0.0670 |
| percentile_positive_p50 | out_of_sample |       29 |            0.3563 |                1.9310 |            0.1013 |                  0.6405 |                 0.6129 |                         0.0277 |                 -0.1097 |                -0.1675 |     0.5862 |                   0.4849 |                 0.0670 |
| top2_positive_est       | out_of_sample |       29 |            0.3563 |                1.9310 |            0.1013 |                  0.6405 |                 0.6129 |                         0.0277 |                 -0.1097 |                -0.1675 |     0.5862 |                   0.4849 |                 0.0670 |
| percentile_p10          | out_of_sample |       29 |            0.3333 |                2.0000 |            0.0705 |                  0.6168 |                 0.6129 |                         0.0039 |                 -0.1133 |                -0.1675 |     0.5862 |                   0.4611 |                 0.0634 |
| percentile_p20          | out_of_sample |       29 |            0.3333 |                2.0000 |            0.0705 |                  0.6168 |                 0.6129 |                         0.0039 |                 -0.1133 |                -0.1675 |     0.5862 |                   0.4611 |                 0.0634 |
| percentile_p30          | out_of_sample |       29 |            0.3333 |                2.0000 |            0.0705 |                  0.6168 |                 0.6129 |                         0.0039 |                 -0.1133 |                -0.1675 |     0.5862 |                   0.4611 |                 0.0634 |
| percentile_p40          | out_of_sample |       29 |            0.3333 |                2.0000 |            0.0705 |                  0.6168 |                 0.6129 |                         0.0039 |                 -0.1133 |                -0.1675 |     0.5862 |                   0.4611 |                 0.0634 |
| percentile_p50          | out_of_sample |       29 |            0.3333 |                2.0000 |            0.0705 |                  0.6168 |                 0.6129 |                         0.0039 |                 -0.1133 |                -0.1675 |     0.5862 |                   0.4611 |                 0.0634 |
| fixed_1pct              | out_of_sample |       29 |            0.1839 |                2.4483 |           -0.2092 |                  0.4989 |                 0.6129 |                        -0.1140 |                 -0.1942 |                -0.1675 |     0.5862 |                   0.3432 |                -0.0175 |
| baseline_full_invested  | out_of_sample |       29 |            0.0000 |                3.0000 |           -0.2134 |                  0.4425 |                 0.6129 |                        -0.1703 |                 -0.1767 |                -0.1675 |     0.6207 |                   0.2869 |                 0.0000 |
| fixed_2pct              | out_of_sample |       29 |            0.2874 |                2.1379 |           -0.2515 |                  0.3859 |                 0.6129 |                        -0.2270 |                 -0.1502 |                -0.1675 |     0.5517 |                   0.2302 |                 0.0265 |
| fixed_0pct              | out_of_sample |       29 |            0.1379 |                2.5862 |           -0.3935 |                  0.3205 |                 0.6129 |                        -0.2924 |                 -0.1971 |                -0.1675 |     0.5862 |                   0.1648 |                -0.0204 |
| top3_positive_est       | out_of_sample |       29 |            0.1379 |                2.5862 |           -0.3935 |                  0.3205 |                 0.6129 |                        -0.2924 |                 -0.1971 |                -0.1675 |     0.5862 |                   0.1648 |                -0.0204 |
| top1_positive_est       | out_of_sample |       29 |            0.6667 |                1.0000 |           -0.4194 |                  0.2183 |                 0.6129 |                        -0.3946 |                 -0.1331 |                -0.1675 |     0.4828 |                   0.0626 |                 0.0436 |
| current_fixed_5pct      | out_of_sample |       29 |            0.7011 |                0.8966 |           -0.4127 |                  0.1557 |                 0.6129 |                        -0.4572 |                 -0.0639 |                -0.1675 |     0.3448 |                   0.0000 |                 0.1128 |
| fixed_3pct              | out_of_sample |       29 |            0.5172 |                1.4483 |           -0.6105 |                  0.0786 |                 0.6129 |                        -0.5342 |                 -0.1502 |                -0.1675 |     0.4483 |                  -0.0770 |                 0.0265 |

## Interpretation

The expected return estimator is noisy and has weak negative correlation with realized next-month returns. A fixed 5% threshold is above the median estimated return in most periods, so it over-allocates to CASH. A positive-floor percentile filter is more realistic: it rejects the weakest current opportunities while staying invested when the opportunity set is broadly positive.
