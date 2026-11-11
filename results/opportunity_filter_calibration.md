# Opportunity Filter Calibration

## Finding

- Baseline model: trend_following Top3
- Current issue: the fixed 5% opportunity threshold allocates too much to CASH and hurts returns.
- Improvement tested: calibrated opportunity filters that keep cash support but use relative thresholds.
- Selected filter: top1_positive_est
- Decision: accepted
- Reason: Accepted because the selected filter materially improved out-of-sample return versus the current 5% threshold while preserving a drawdown improvement versus the full-invested baseline.

## Expected Return Distribution

| period        |    count |   mean |    std |     min |     10% |     20% |     25% |     30% |     40% |    50% |    60% |    75% |    80% |    90% |    max |
|:--------------|---------:|-------:|-------:|--------:|--------:|--------:|--------:|--------:|--------:|-------:|-------:|-------:|-------:|-------:|-------:|
| out_of_sample | 102.0000 | 0.0376 | 0.0414 | -0.0375 | -0.0080 |  0.0107 |  0.0185 |  0.0210 |  0.0265 | 0.0300 | 0.0394 | 0.0519 | 0.0616 | 0.0870 | 0.2095 |
| train         | 129.0000 | 0.0155 | 0.0348 | -0.0375 | -0.0262 | -0.0163 | -0.0142 | -0.0122 | -0.0045 | 0.0142 | 0.0239 | 0.0472 | 0.0475 | 0.0573 | 0.1788 |
| validation    |  72.0000 | 0.0247 | 0.0417 | -0.0479 | -0.0120 | -0.0070 | -0.0014 |  0.0015 |  0.0058 | 0.0233 | 0.0297 | 0.0442 | 0.0472 | 0.0793 | 0.1970 |

## Out-Of-Sample Comparison

| threshold               | period        |   months |   avg_cash_weight |   avg_qualified_count |   selection_score |   strategy_total_return |   bist100_total_return |   excess_return_over_benchmark |   strategy_max_drawdown |   bist100_max_drawdown |   win_rate |   return_vs_current_5pct |   drawdown_vs_baseline |
|:------------------------|:--------------|---------:|------------------:|----------------------:|------------------:|------------------------:|-----------------------:|-------------------------------:|------------------------:|-----------------------:|-----------:|-------------------------:|-----------------------:|
| percentile_positive_p10 | out_of_sample |       34 |            0.3627 |                1.9118 |           -0.0021 |                  0.4759 |                 0.3725 |                         0.1034 |                 -0.1925 |                -0.2550 |     0.5588 |                   0.3058 |                -0.0158 |
| percentile_positive_p20 | out_of_sample |       34 |            0.3627 |                1.9118 |           -0.0021 |                  0.4759 |                 0.3725 |                         0.1034 |                 -0.1925 |                -0.2550 |     0.5588 |                   0.3058 |                -0.0158 |
| percentile_positive_p30 | out_of_sample |       34 |            0.3627 |                1.9118 |           -0.0021 |                  0.4759 |                 0.3725 |                         0.1034 |                 -0.1925 |                -0.2550 |     0.5588 |                   0.3058 |                -0.0158 |
| percentile_positive_p40 | out_of_sample |       34 |            0.3627 |                1.9118 |           -0.0021 |                  0.4759 |                 0.3725 |                         0.1034 |                 -0.1925 |                -0.2550 |     0.5588 |                   0.3058 |                -0.0158 |
| percentile_positive_p50 | out_of_sample |       34 |            0.3627 |                1.9118 |           -0.0021 |                  0.4759 |                 0.3725 |                         0.1034 |                 -0.1925 |                -0.2550 |     0.5588 |                   0.3058 |                -0.0158 |
| top2_positive_est       | out_of_sample |       34 |            0.3627 |                1.9118 |           -0.0021 |                  0.4759 |                 0.3725 |                         0.1034 |                 -0.1925 |                -0.2550 |     0.5588 |                   0.3058 |                -0.0158 |
| percentile_p10          | out_of_sample |       34 |            0.3333 |                2.0000 |           -0.0395 |                  0.4385 |                 0.3725 |                         0.0660 |                 -0.1925 |                -0.2550 |     0.5588 |                   0.2684 |                -0.0158 |
| percentile_p20          | out_of_sample |       34 |            0.3333 |                2.0000 |           -0.0395 |                  0.4385 |                 0.3725 |                         0.0660 |                 -0.1925 |                -0.2550 |     0.5588 |                   0.2684 |                -0.0158 |
| percentile_p30          | out_of_sample |       34 |            0.3333 |                2.0000 |           -0.0395 |                  0.4385 |                 0.3725 |                         0.0660 |                 -0.1925 |                -0.2550 |     0.5588 |                   0.2684 |                -0.0158 |
| percentile_p40          | out_of_sample |       34 |            0.3333 |                2.0000 |           -0.0395 |                  0.4385 |                 0.3725 |                         0.0660 |                 -0.1925 |                -0.2550 |     0.5588 |                   0.2684 |                -0.0158 |
| percentile_p50          | out_of_sample |       34 |            0.3333 |                2.0000 |           -0.0395 |                  0.4385 |                 0.3725 |                         0.0660 |                 -0.1925 |                -0.2550 |     0.5588 |                   0.2684 |                -0.0158 |
| baseline_full_invested  | out_of_sample |       34 |            0.0000 |                3.0000 |           -0.0332 |                  0.3986 |                 0.3725 |                         0.0261 |                 -0.1767 |                -0.2550 |     0.5882 |                   0.2285 |                 0.0000 |
| fixed_1pct              | out_of_sample |       34 |            0.2059 |                2.3824 |           -0.2028 |                  0.3081 |                 0.3725 |                        -0.0645 |                 -0.1942 |                -0.2550 |     0.5000 |                   0.1379 |                -0.0175 |
| top1_positive_est       | out_of_sample |       34 |            0.6667 |                1.0000 |           -0.1506 |                  0.2234 |                 0.3725 |                        -0.1491 |                 -0.1331 |                -0.2550 |     0.5294 |                   0.0533 |                 0.0436 |
| fixed_2pct              | out_of_sample |       34 |            0.2941 |                2.1176 |           -0.2281 |                  0.2094 |                 0.3725 |                        -0.1631 |                 -0.1502 |                -0.2550 |     0.4706 |                   0.0393 |                 0.0265 |
| fixed_0pct              | out_of_sample |       34 |            0.1569 |                2.5294 |           -0.2964 |                  0.2057 |                 0.3725 |                        -0.1669 |                 -0.1971 |                -0.2550 |     0.5294 |                   0.0355 |                -0.0204 |
| top3_positive_est       | out_of_sample |       34 |            0.1569 |                2.5294 |           -0.2964 |                  0.2057 |                 0.3725 |                        -0.1669 |                 -0.1971 |                -0.2550 |     0.5294 |                   0.0355 |                -0.0204 |
| current_fixed_5pct      | out_of_sample |       34 |            0.7255 |                0.8235 |           -0.1538 |                  0.1701 |                 0.3725 |                        -0.2024 |                 -0.0639 |                -0.2550 |     0.3529 |                   0.0000 |                 0.1128 |
| fixed_3pct              | out_of_sample |       34 |            0.5294 |                1.4118 |           -0.4885 |                 -0.0215 |                 0.3725 |                        -0.3941 |                 -0.1502 |                -0.2550 |     0.4118 |                  -0.1917 |                 0.0265 |

## Interpretation

The expected return estimator is noisy and has weak negative correlation with realized next-month returns. A fixed 5% threshold is above the median estimated return in most periods, so it over-allocates to CASH. A positive-floor percentile filter is more realistic: it rejects the weakest current opportunities while staying invested when the opportunity set is broadly positive.
