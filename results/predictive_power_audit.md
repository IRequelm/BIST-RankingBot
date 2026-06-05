# Predictive Power Audit

## Questions Answered

- Does the ranking system have predictive power? **No clear predictive power was found.**
- Is expected_return_mid usable? **No; recommendation: remove it from gating and replace it.**
- Should production strategy change here? **No. This is diagnostic research only.**

## Core Findings

- Score Spearman correlation with next-month return: -0.0058
- expected_return_mid Spearman correlation with next-month return: -0.0526
- Top score decile average next-month return: 3.92%
- Bottom score decile average next-month return: 4.20%
- Top3 aggregate CAGR: 46.10%
- Bottom10 aggregate CAGR: 49.57%
- Best forward factor by Spearman: volatility (0.1512)

## Rank Bucket Test

|   bucket |    count |   average_next_month_return |   median_next_month_return |   win_rate |   average_excess_return |
|---------:|---------:|----------------------------:|---------------------------:|-----------:|------------------------:|
|   1.0000 | 960.0000 |                      0.0420 |                     0.0251 |     0.5750 |                  0.0104 |
|   2.0000 | 960.0000 |                      0.0359 |                     0.0198 |     0.5948 |                  0.0044 |
|   3.0000 | 480.0000 |                      0.0411 |                     0.0331 |     0.6021 |                  0.0095 |
|   4.0000 | 960.0000 |                      0.0376 |                     0.0259 |     0.5875 |                  0.0061 |
|   5.0000 | 960.0000 |                      0.0362 |                     0.0224 |     0.5750 |                  0.0046 |
|   6.0000 | 480.0000 |                      0.0405 |                     0.0316 |     0.6042 |                  0.0089 |
|   7.0000 | 960.0000 |                      0.0348 |                     0.0260 |     0.5823 |                  0.0032 |
|   8.0000 | 480.0000 |                      0.0377 |                     0.0233 |     0.5875 |                  0.0061 |
|   9.0000 | 960.0000 |                      0.0367 |                     0.0257 |     0.5979 |                  0.0052 |
|  10.0000 | 960.0000 |                      0.0392 |                     0.0248 |     0.5750 |                  0.0076 |

## Forward Correlation Test

| factor              |   count |   pearson_corr |   spearman_corr |
|:--------------------|--------:|---------------:|----------------:|
| volatility          |    8160 |         0.1474 |          0.1512 |
| momentum_6m         |    8160 |        -0.0053 |         -0.0049 |
| score               |    8160 |        -0.0077 |         -0.0058 |
| momentum_1m         |    8160 |         0.0150 |         -0.0125 |
| momentum_3m         |    8160 |        -0.0169 |         -0.0352 |
| volume_increase     |    8160 |        -0.0266 |         -0.0447 |
| expected_return_mid |    7989 |        -0.0274 |         -0.0526 |

## Top-N Forward Test

| portfolio   |   count |   average_next_month_return |   average_excess_return |   win_rate_vs_bist100 |   cagr |   max_drawdown |
|:------------|--------:|----------------------------:|------------------------:|----------------------:|-------:|---------------:|
| Top1        |     480 |                      0.0459 |                  0.0144 |                0.4396 | 0.5616 |        -0.3440 |
| Bottom10    |     480 |                      0.0385 |                  0.0069 |                0.5792 | 0.4957 |        -0.3087 |
| Top5        |     480 |                      0.0380 |                  0.0064 |                0.5896 | 0.4926 |        -0.2637 |
| Top10       |     480 |                      0.0373 |                  0.0058 |                0.5687 | 0.4862 |        -0.2422 |
| Top3        |     480 |                      0.0367 |                  0.0051 |                0.5000 | 0.4610 |        -0.3727 |

## Pre-Move Detection Test

|     count |   top_decile_capture |   top_two_decile_capture |   top3_capture |   top5_capture |   average_pre_move_rank |
|----------:|---------------------:|-------------------------:|---------------:|---------------:|------------------------:|
| 2400.0000 |               0.1221 |                   0.2296 |         0.1754 |         0.2825 |                  9.0504 |

## Factor Importance

| factor              |   count |   spearman_corr |   top_bottom_spread |   top_quintile_return |   bottom_quintile_return |
|:--------------------|--------:|----------------:|--------------------:|----------------------:|-------------------------:|
| volatility          |    8160 |          0.1512 |              0.0559 |                0.0753 |                   0.0194 |
| momentum_6m         |    8160 |         -0.0049 |              0.0010 |                0.0430 |                   0.0420 |
| score               |    8160 |         -0.0058 |             -0.0017 |                0.0372 |                   0.0389 |
| momentum_1m         |    8160 |         -0.0125 |             -0.0008 |                0.0470 |                   0.0477 |
| momentum_3m         |    8160 |         -0.0352 |             -0.0085 |                0.0396 |                   0.0481 |
| volume_increase     |    8160 |         -0.0447 |             -0.0113 |                0.0265 |                   0.0379 |
| expected_return_mid |    7989 |         -0.0526 |             -0.0089 |                0.0248 |                   0.0337 |

## Is The Bot Early Or Late?

The bot is only partially early. Future top-quartile winners are captured in the top score decile/top two deciles at a limited rate, so the system often recognizes strength after it has already appeared in momentum inputs rather than reliably before the next move.

## Conclusion

The ranking system does not show reliable forward predictive power in its current form. Score deciles are not monotonic, the top score decile does not beat the bottom score decile, and Bottom10 has a higher aggregate CAGR than Top3 in this broad all-model audit. expected_return_mid is worse than raw score because it has a negative forward correlation and is only a backward-looking score-neighborhood median. It should be removed from buy/sell gating and replaced with a directly validated forward model. The only factor with meaningful standalone forward correlation in this audit is volatility, but the current score treats volatility mostly as a penalty, so the ranking logic itself needs recalibration before it should be trusted for prediction.
