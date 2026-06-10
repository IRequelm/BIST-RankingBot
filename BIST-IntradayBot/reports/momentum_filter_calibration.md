# Momentum Filter Calibration

- Research only: production strategy thresholds were not changed.
- Universe source: same ticker list as BIST-RankingBot monthly bot.
- Universe size: 18
- Data interval used: 30m
- Trading days tested: 20
- Opening strength thresholds tested: 0.20%, 0.30%, 0.40%, 0.50%
- Volume ratio thresholds tested: 1.00, 1.05, 1.10, 1.20
- Max trades per day remains capped at 3; candidate counts can exceed actual trades taken.

## Clear Answers

- Is the current filter too strict? **Yes**. Current thresholds average 0.65 trades/day and 0.65 candidates/day, with 13 no-trade days.
- Which threshold combination gives 3-10 trades per day? Because paper trading is capped at 3 trades/day, no setting can average more than 3 actual trades/day without changing the trading rule. By candidate count: No tested combination produced 3-10 final candidates per day on average.
- Which threshold combination has the best excess return? **0.50% opening strength / 1.20 volume ratio**, average excess return **0.36%** per tested day.
- Should production thresholds be changed? **Not yet.** Research suggests the current filter is too strict for trade frequency, but production should not be changed yet without a longer out-of-sample test.

## Current Production Threshold Daily Funnel

| date       |   starting_universe |   data_available |   after_momentum_filter |   after_vwap_filter |   after_mean_reversion_filter |   after_volatility_filter |   final_candidates |   trades_taken | daily_return   | bist100_return   | excess_return   | selected_symbols             |
|:-----------|--------------------:|-----------------:|------------------------:|--------------------:|------------------------------:|--------------------------:|-------------------:|---------------:|:---------------|:-----------------|:----------------|:-----------------------------|
| 2026-05-08 |                  18 |               17 |                       3 |                   3 |                             3 |                         3 |                  3 |              3 | 0.36%          | 0.12%            | 0.24%           | SISE.IS, TCELL.IS, ASELS.IS  |
| 2026-05-11 |                  18 |               17 |                       2 |                   2 |                             2 |                         2 |                  2 |              2 | -0.17%         | 0.35%            | -0.52%          | SISE.IS, ARCLK.IS            |
| 2026-05-12 |                  18 |               17 |                       2 |                   2 |                             2 |                         2 |                  2 |              2 | -1.54%         | -2.27%           | 0.72%           | PETKM.IS, SISE.IS            |
| 2026-05-13 |                  18 |               17 |                       0 |                   0 |                             0 |                         0 |                  0 |              0 | 0.00%          | -1.11%           | 1.11%           |                              |
| 2026-05-14 |                  18 |               17 |                       0 |                   0 |                             0 |                         0 |                  0 |              0 | 0.00%          | 0.35%            | -0.35%          |                              |
| 2026-05-15 |                  18 |               17 |                       1 |                   1 |                             1 |                         1 |                  1 |              1 | -1.41%         | -1.92%           | 0.51%           | PETKM.IS                     |
| 2026-05-18 |                  18 |               17 |                       0 |                   0 |                             0 |                         0 |                  0 |              0 | 0.00%          | -2.15%           | 2.15%           |                              |
| 2026-05-20 |                  18 |               17 |                       1 |                   1 |                             1 |                         1 |                  1 |              1 | -0.07%         | -0.13%           | 0.06%           | KCHOL.IS                     |
| 2026-05-21 |                  18 |               17 |                       0 |                   0 |                             0 |                         0 |                  0 |              0 | 0.00%          | -6.03%           | 6.03%           |                              |
| 2026-05-22 |                  18 |               17 |                       0 |                   0 |                             0 |                         0 |                  0 |              0 | 0.00%          | 5.04%            | -5.04%          |                              |
| 2026-05-25 |                  18 |               17 |                       0 |                   0 |                             0 |                         0 |                  0 |              0 | 0.00%          | 0.44%            | -0.44%          |                              |
| 2026-05-26 |                  18 |               17 |                       0 |                   0 |                             0 |                         0 |                  0 |              0 | 0.00%          | -1.64%           | 1.64%           |                              |
| 2026-06-01 |                  18 |               17 |                       1 |                   1 |                             1 |                         1 |                  1 |              1 | -0.89%         | 0.37%            | -1.27%          | TOASO.IS                     |
| 2026-06-02 |                  18 |               17 |                       0 |                   0 |                             0 |                         0 |                  0 |              0 | 0.00%          | 3.49%            | -3.49%          |                              |
| 2026-06-03 |                  18 |               17 |                       0 |                   0 |                             0 |                         0 |                  0 |              0 | 0.00%          | -1.79%           | 1.79%           |                              |
| 2026-06-04 |                  18 |               17 |                       1 |                   0 |                             0 |                         0 |                  0 |              0 | 0.00%          | -0.76%           | 0.76%           |                              |
| 2026-06-05 |                  18 |               17 |                       0 |                   0 |                             0 |                         0 |                  0 |              0 | 0.00%          | -1.39%           | 1.39%           |                              |
| 2026-06-08 |                  18 |               17 |                       0 |                   0 |                             0 |                         0 |                  0 |              0 | 0.00%          | 1.27%            | -1.27%          |                              |
| 2026-06-09 |                  18 |               17 |                       3 |                   3 |                             3 |                         3 |                  3 |              3 | -1.91%         | -0.84%           | -1.07%          | TOASO.IS, TCELL.IS, FROTO.IS |
| 2026-06-10 |                  18 |               17 |                       0 |                   0 |                             0 |                         0 |                  0 |              0 | 0.00%          | -0.68%           | 0.68%           |                              |

## Threshold Combination Summary

| opening_strength_threshold   |   volume_ratio_threshold |   avg_trades_per_day |   avg_candidates_per_day | win_rate   | avg_daily_return   | avg_bist100_return   | avg_excess_return   | worst_day   | max_daily_drawdown   |   no_trade_days |
|:-----------------------------|-------------------------:|---------------------:|-------------------------:|:-----------|:-------------------|:---------------------|:--------------------|:------------|:---------------------|----------------:|
| 0.50%                        |                     1.2  |                 0.35 |                     0.35 | 10.00%     | -0.10%             | -0.46%               | 0.36%               | -1.67%      | -3.19%               |              16 |
| 0.20%                        |                     1.2  |                 0.45 |                     0.5  | 15.00%     | -0.11%             | -0.46%               | 0.35%               | -1.67%      | -3.00%               |              15 |
| 0.30%                        |                     1.2  |                 0.45 |                     0.45 | 15.00%     | -0.11%             | -0.46%               | 0.35%               | -1.67%      | -3.00%               |              15 |
| 0.40%                        |                     1.2  |                 0.4  |                     0.4  | 10.00%     | -0.12%             | -0.46%               | 0.34%               | -1.67%      | -3.19%               |              16 |
| 0.50%                        |                     1.1  |                 0.5  |                     0.5  | 5.00%      | -0.17%             | -0.46%               | 0.29%               | -1.67%      | -4.29%               |              14 |
| 0.30%                        |                     1.1  |                 0.6  |                     0.6  | 10.00%     | -0.19%             | -0.46%               | 0.27%               | -1.67%      | -4.10%               |              14 |
| 0.40%                        |                     1.1  |                 0.55 |                     0.55 | 5.00%      | -0.20%             | -0.46%               | 0.26%               | -1.67%      | -4.29%               |              14 |
| 0.20%                        |                     1.1  |                 0.7  |                     0.75 | 10.00%     | -0.20%             | -0.46%               | 0.26%               | -1.90%      | -4.35%               |              14 |
| 0.50%                        |                     1.05 |                 0.6  |                     0.6  | 5.00%      | -0.26%             | -0.46%               | 0.21%               | -1.91%      | -5.87%               |              13 |
| 0.40%                        |                     1.05 |                 0.65 |                     0.65 | 5.00%      | -0.28%             | -0.46%               | 0.18%               | -1.91%      | -5.87%               |              13 |
| 0.30%                        |                     1.05 |                 0.75 |                     0.75 | 5.00%      | -0.28%             | -0.46%               | 0.18%               | -1.91%      | -5.87%               |              13 |
| 0.20%                        |                     1.05 |                 0.8  |                     0.9  | 5.00%      | -0.28%             | -0.46%               | 0.18%               | -1.91%      | -5.89%               |              13 |
| 0.50%                        |                     1    |                 0.95 |                     1.05 | 10.00%     | -0.35%             | -0.46%               | 0.12%               | -1.91%      | -7.54%               |              10 |
| 0.20%                        |                     1    |                 1.05 |                     1.4  | 15.00%     | -0.36%             | -0.46%               | 0.10%               | -1.91%      | -7.36%               |              10 |
| 0.30%                        |                     1    |                 1.05 |                     1.2  | 15.00%     | -0.36%             | -0.46%               | 0.10%               | -1.91%      | -7.36%               |              10 |
| 0.40%                        |                     1    |                 1    |                     1.1  | 10.00%     | -0.37%             | -0.46%               | 0.09%               | -1.91%      | -7.54%               |              10 |

## 3-10 Candidate Band

No tested combination produced 3-10 final candidates per day on average.

## Warnings

- KOZAL.IS: 15m intraday data unavailable.
- 15m data had only 5 usable sessions; need 20, trying fallback.
- KOZAL.IS: 30m intraday data unavailable.
