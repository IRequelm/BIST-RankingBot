# Follow-Up Improvement Research

This is research-only. Production follow-up tracking remains fixed and still reads reports/tracking_state.json.

## Policy Summary

| policy_id   | policy_name                   | frequency   |   portfolio_size | total_return   | benchmark_total_return   | cagr   | bist100_cagr   | excess_cagr   | monthly_win_rate_vs_bist100   | average_monthly_excess_return   | max_drawdown   |   average_monthly_turnover |   average_trades_per_month | transaction_cost_impact   | worst_underperformance_month   | worst_underperformance   | best_outperformance_month   | best_outperformance   |   intervals |
|:------------|:------------------------------|:------------|-----------------:|:---------------|:-------------------------|:-------|:---------------|:--------------|:------------------------------|:--------------------------------|:---------------|---------------------------:|---------------------------:|:--------------------------|:-------------------------------|:-------------------------|:----------------------------|:----------------------|------------:|
| A           | Current baseline monthly Top3 | monthly     |                3 | 86.38%         | 69.04%                   | 25.65% | 21.23%         | 4.42%         | 46.88%                        | 0.40%                           | -19.32%        |                    1.21875 |                    3.65625 | 14.83%                    | 2024-04                        | -10.59%                  | 2026-09                     | 18.33%                |          33 |
| B           | Weekly rebalance Top3         | weekly      |                3 | -4.16%         | 69.04%                   | -1.54% | 21.23%         | -22.77%       | 39.39%                        | -1.60%                          | -42.13%        |                    3.10101 |                    9.30303 | 21.86%                    | 2024-03                        | -12.42%                  | 2025-03                     | 12.41%                |         143 |
| C           | Weekly rebalance Top5         | weekly      |                5 | 11.85%         | 69.04%                   | 4.19%  | 21.23%         | -17.04%       | 42.42%                        | -1.19%                          | -36.45%        |                    2.7697  |                   13.8485  | 22.47%                    | 2024-08                        | -9.16%                   | 2026-09                     | 8.27%                 |         143 |
| D           | Relative Strength Top3        | weekly      |                3 | -0.65%         | 69.04%                   | -0.24% | 21.23%         | -21.47%       | 36.36%                        | -1.55%                          | -38.81%        |                    4.29293 |                   12.8788  | 32.47%                    | 2026-02                        | -14.58%                  | 2026-08                     | 8.57%                 |         143 |
| E           | Benchmark-aware Top3          | weekly      |                3 | -6.18%         | 69.04%                   | -2.31% | 21.23%         | -23.54%       | 33.33%                        | -1.73%                          | -39.49%        |                    4.29293 |                   12.8788  | 30.69%                    | 2026-02                        | -11.73%                  | 2026-08                     | 8.57%                 |         143 |
| F           | Leadership Rotation Overlay   | weekly      |                3 | -9.16%         | 69.04%                   | -3.46% | 21.23%         | -24.69%       | 39.39%                        | -1.76%                          | -42.16%        |                    4.15152 |                   12.4545  | 28.66%                    | 2026-02                        | -11.73%                  | 2026-08                     | 8.44%                 |         143 |

## Decision

- Did weekly rebalance improve excess return? Recent yes, historical no, so rejected. Historical excess CAGR delta vs baseline: -27.19%; recent excess delta: 4.24%.
- Did relative strength improve excess return? Recent yes, historical no, so rejected. Historical excess CAGR delta vs baseline: -25.89%; recent excess delta: 3.44%.
- Did benchmark-aware selection improve excess return? Recent yes, historical no, so rejected. Historical excess CAGR delta vs baseline: -27.96%; recent excess delta: 4.20%.
- Did any policy beat BIST100 robustly? No under the current acceptance filter.
- Next paper-trading candidate: none. No policy passed both historical and recent acceptance criteria.
- Current one-month fixed hold should be kept for tracking, while weekly/relative-strength variants remain research-only.

## Acceptance Rule

A policy is only eligible if it improves both historical walk-forward excess return and the recent 2026-06 counterfactual excess return. Policies that only fix June 2026 are rejected.
