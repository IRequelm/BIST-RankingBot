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
| percentile_positive_p10 | out_of_sample |       29 |            0.3563 |                1.9310 |            0.1007 |                  0.7211 |                 0.7112 |                         0.0098 |                 -0.1097 |                -0.1675 |     0.6207 |                   0.5188 |                 0.0670 |
| percentile_positive_p20 | out_of_sample |       29 |            0.3563 |                1.9310 |            0.1007 |                  0.7211 |                 0.7112 |                         0.0098 |                 -0.1097 |                -0.1675 |     0.6207 |                   0.5188 |                 0.0670 |
| percentile_positive_p30 | out_of_sample |       29 |            0.3563 |                1.9310 |            0.1007 |                  0.7211 |                 0.7112 |                         0.0098 |                 -0.1097 |                -0.1675 |     0.6207 |                   0.5188 |                 0.0670 |
| percentile_positive_p40 | out_of_sample |       29 |            0.3563 |                1.9310 |            0.1007 |                  0.7211 |                 0.7112 |                         0.0098 |                 -0.1097 |                -0.1675 |     0.6207 |                   0.5188 |                 0.0670 |
| percentile_positive_p50 | out_of_sample |       29 |            0.3563 |                1.9310 |            0.1007 |                  0.7211 |                 0.7112 |                         0.0098 |                 -0.1097 |                -0.1675 |     0.6207 |                   0.5188 |                 0.0670 |
| top2_positive_est       | out_of_sample |       29 |            0.3563 |                1.9310 |            0.1007 |                  0.7211 |                 0.7112 |                         0.0098 |                 -0.1097 |                -0.1675 |     0.6207 |                   0.5188 |                 0.0670 |
| percentile_p10          | out_of_sample |       29 |            0.3333 |                2.0000 |            0.0687 |                  0.6962 |                 0.7112 |                        -0.0150 |                 -0.1133 |                -0.1675 |     0.6207 |                   0.4940 |                 0.0634 |
| percentile_p20          | out_of_sample |       29 |            0.3333 |                2.0000 |            0.0687 |                  0.6962 |                 0.7112 |                        -0.0150 |                 -0.1133 |                -0.1675 |     0.6207 |                   0.4940 |                 0.0634 |
| percentile_p30          | out_of_sample |       29 |            0.3333 |                2.0000 |            0.0687 |                  0.6962 |                 0.7112 |                        -0.0150 |                 -0.1133 |                -0.1675 |     0.6207 |                   0.4940 |                 0.0634 |
| percentile_p40          | out_of_sample |       29 |            0.3333 |                2.0000 |            0.0687 |                  0.6962 |                 0.7112 |                        -0.0150 |                 -0.1133 |                -0.1675 |     0.6207 |                   0.4940 |                 0.0634 |
| percentile_p50          | out_of_sample |       29 |            0.3333 |                2.0000 |            0.0687 |                  0.6962 |                 0.7112 |                        -0.0150 |                 -0.1133 |                -0.1675 |     0.6207 |                   0.4940 |                 0.0634 |
| fixed_1pct              | out_of_sample |       29 |            0.1839 |                2.4483 |           -0.2231 |                  0.5833 |                 0.7112 |                        -0.1279 |                 -0.1942 |                -0.1675 |     0.5862 |                   0.3811 |                -0.0175 |
| baseline_full_invested  | out_of_sample |       29 |            0.0000 |                3.0000 |           -0.2305 |                  0.5238 |                 0.7112 |                        -0.1874 |                 -0.1767 |                -0.1675 |     0.6207 |                   0.3216 |                 0.0000 |
| fixed_2pct              | out_of_sample |       29 |            0.2874 |                2.1379 |           -0.2718 |                  0.4639 |                 0.7112 |                        -0.2473 |                 -0.1502 |                -0.1675 |     0.5517 |                   0.2617 |                 0.0265 |
| fixed_0pct              | out_of_sample |       29 |            0.1379 |                2.5862 |           -0.4175 |                  0.3948 |                 0.7112 |                        -0.3164 |                 -0.1971 |                -0.1675 |     0.5862 |                   0.1926 |                -0.0204 |
| top3_positive_est       | out_of_sample |       29 |            0.1379 |                2.5862 |           -0.4175 |                  0.3948 |                 0.7112 |                        -0.3164 |                 -0.1971 |                -0.1675 |     0.5862 |                   0.1926 |                -0.0204 |
| top1_positive_est       | out_of_sample |       29 |            0.6667 |                1.0000 |           -0.4514 |                  0.2674 |                 0.7112 |                        -0.4439 |                 -0.1331 |                -0.1675 |     0.5172 |                   0.0651 |                 0.0436 |
| current_fixed_5pct      | out_of_sample |       29 |            0.7011 |                0.8966 |           -0.4472 |                  0.2022 |                 0.7112 |                        -0.5090 |                 -0.0639 |                -0.1675 |     0.3793 |                   0.0000 |                 0.1128 |
| fixed_3pct              | out_of_sample |       29 |            0.5172 |                1.4483 |           -0.6481 |                  0.1394 |                 0.7112 |                        -0.5718 |                 -0.1502 |                -0.1675 |     0.4483 |                  -0.0628 |                 0.0265 |

## Interpretation

The expected return estimator is noisy and has weak negative correlation with realized next-month returns. A fixed 5% threshold is above the median estimated return in most periods, so it over-allocates to CASH. A positive-floor percentile filter is more realistic: it rejects the weakest current opportunities while staying invested when the opportunity set is broadly positive.
