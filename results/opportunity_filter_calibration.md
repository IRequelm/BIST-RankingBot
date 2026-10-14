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
| out_of_sample |  99.0000 | 0.0389 | 0.0411 | -0.0375 | -0.0052 |  0.0158 |  0.0188 |  0.0222 |  0.0280 | 0.0300 | 0.0402 | 0.0520 | 0.0619 | 0.0874 | 0.2095 |
| train         | 129.0000 | 0.0155 | 0.0348 | -0.0375 | -0.0262 | -0.0163 | -0.0142 | -0.0122 | -0.0045 | 0.0142 | 0.0239 | 0.0472 | 0.0475 | 0.0573 | 0.1788 |
| validation    |  72.0000 | 0.0247 | 0.0417 | -0.0479 | -0.0120 | -0.0070 | -0.0014 |  0.0015 |  0.0058 | 0.0233 | 0.0297 | 0.0442 | 0.0472 | 0.0793 | 0.1970 |

## Out-Of-Sample Comparison

| threshold               | period        |   months |   avg_cash_weight |   avg_qualified_count |   selection_score |   strategy_total_return |   bist100_total_return |   excess_return_over_benchmark |   strategy_max_drawdown |   bist100_max_drawdown |   win_rate |   return_vs_current_5pct |   drawdown_vs_baseline |
|:------------------------|:--------------|---------:|------------------:|----------------------:|------------------:|------------------------:|-----------------------:|-------------------------------:|------------------------:|-----------------------:|-----------:|-------------------------:|-----------------------:|
| baseline_full_invested  | out_of_sample |       33 |            0.0000 |                3.0000 |            0.0078 |                  0.5152 |                 0.4418 |                         0.0733 |                 -0.1767 |                -0.1728 |     0.5758 |                   0.3451 |                 0.0000 |
| percentile_positive_p10 | out_of_sample |       33 |            0.3535 |                1.9394 |            0.0598 |                  0.5054 |                 0.4418 |                         0.0636 |                 -0.1382 |                -0.1728 |     0.5455 |                   0.3353 |                 0.0385 |
| percentile_positive_p20 | out_of_sample |       33 |            0.3535 |                1.9394 |            0.0598 |                  0.5054 |                 0.4418 |                         0.0636 |                 -0.1382 |                -0.1728 |     0.5455 |                   0.3353 |                 0.0385 |
| percentile_positive_p30 | out_of_sample |       33 |            0.3535 |                1.9394 |            0.0598 |                  0.5054 |                 0.4418 |                         0.0636 |                 -0.1382 |                -0.1728 |     0.5455 |                   0.3353 |                 0.0385 |
| percentile_positive_p40 | out_of_sample |       33 |            0.3535 |                1.9394 |            0.0598 |                  0.5054 |                 0.4418 |                         0.0636 |                 -0.1382 |                -0.1728 |     0.5455 |                   0.3353 |                 0.0385 |
| percentile_positive_p50 | out_of_sample |       33 |            0.3535 |                1.9394 |            0.0598 |                  0.5054 |                 0.4418 |                         0.0636 |                 -0.1382 |                -0.1728 |     0.5455 |                   0.3353 |                 0.0385 |
| top2_positive_est       | out_of_sample |       33 |            0.3535 |                1.9394 |            0.0598 |                  0.5054 |                 0.4418 |                         0.0636 |                 -0.1382 |                -0.1728 |     0.5455 |                   0.3353 |                 0.0385 |
| percentile_p10          | out_of_sample |       33 |            0.3333 |                2.0000 |            0.0381 |                  0.4836 |                 0.4418 |                         0.0418 |                 -0.1382 |                -0.1728 |     0.5455 |                   0.3135 |                 0.0385 |
| percentile_p20          | out_of_sample |       33 |            0.3333 |                2.0000 |            0.0381 |                  0.4836 |                 0.4418 |                         0.0418 |                 -0.1382 |                -0.1728 |     0.5455 |                   0.3135 |                 0.0385 |
| percentile_p30          | out_of_sample |       33 |            0.3333 |                2.0000 |            0.0381 |                  0.4836 |                 0.4418 |                         0.0418 |                 -0.1382 |                -0.1728 |     0.5455 |                   0.3135 |                 0.0385 |
| percentile_p40          | out_of_sample |       33 |            0.3333 |                2.0000 |            0.0381 |                  0.4836 |                 0.4418 |                         0.0418 |                 -0.1382 |                -0.1728 |     0.5455 |                   0.3135 |                 0.0385 |
| percentile_p50          | out_of_sample |       33 |            0.3333 |                2.0000 |            0.0381 |                  0.4836 |                 0.4418 |                         0.0418 |                 -0.1382 |                -0.1728 |     0.5455 |                   0.3135 |                 0.0385 |
| fixed_1pct              | out_of_sample |       33 |            0.1818 |                2.4545 |           -0.1767 |                  0.3959 |                 0.4418 |                        -0.0459 |                 -0.1942 |                -0.1728 |     0.5152 |                   0.2258 |                -0.0175 |
| fixed_2pct              | out_of_sample |       33 |            0.2727 |                2.1818 |           -0.2091 |                  0.2907 |                 0.4418 |                        -0.1512 |                 -0.1502 |                -0.1728 |     0.4848 |                   0.1205 |                 0.0265 |
| fixed_0pct              | out_of_sample |       33 |            0.1414 |                2.5758 |           -0.3487 |                  0.2297 |                 0.4418 |                        -0.2121 |                 -0.1971 |                -0.1728 |     0.5152 |                   0.0596 |                -0.0204 |
| top3_positive_est       | out_of_sample |       33 |            0.1414 |                2.5758 |           -0.3487 |                  0.2297 |                 0.4418 |                        -0.2121 |                 -0.1971 |                -0.1728 |     0.5152 |                   0.0596 |                -0.0204 |
| top1_positive_est       | out_of_sample |       33 |            0.6667 |                1.0000 |           -0.2327 |                  0.2177 |                 0.4418 |                        -0.2241 |                 -0.1331 |                -0.1728 |     0.5152 |                   0.0476 |                 0.0436 |
| current_fixed_5pct      | out_of_sample |       33 |            0.7172 |                0.8485 |           -0.2177 |                  0.1701 |                 0.4418 |                        -0.2717 |                 -0.0639 |                -0.1728 |     0.3636 |                   0.0000 |                 0.1128 |
| fixed_3pct              | out_of_sample |       33 |            0.5152 |                1.4545 |           -0.4859 |                  0.0442 |                 0.4418 |                        -0.3977 |                 -0.1502 |                -0.1728 |     0.4242 |                  -0.1260 |                 0.0265 |

## Interpretation

The expected return estimator is noisy and has weak negative correlation with realized next-month returns. A fixed 5% threshold is above the median estimated return in most periods, so it over-allocates to CASH. A positive-floor percentile filter is more realistic: it rejects the weakest current opportunities while staying invested when the opportunity set is broadly positive.
