# Follow-Up Improvement Research

This is research-only. Production follow-up tracking remains fixed and still reads reports/tracking_state.json.

## Policy Summary

| policy_id   | policy_name                   | frequency   |   portfolio_size | total_return   | benchmark_total_return   | cagr   | bist100_cagr   | excess_cagr   | monthly_win_rate_vs_bist100   | average_monthly_excess_return   | max_drawdown   |   average_monthly_turnover |   average_trades_per_month | transaction_cost_impact   | worst_underperformance_month   | worst_underperformance   | best_outperformance_month   | best_outperformance   |   intervals |
|:------------|:------------------------------|:------------|-----------------:|:---------------|:-------------------------|:-------|:---------------|:--------------|:------------------------------|:--------------------------------|:---------------|---------------------------:|---------------------------:|:--------------------------|:-------------------------------|:-------------------------|:----------------------------|:----------------------|------------:|
| A           | Current baseline monthly Top3 | monthly     |                3 | 84.95%         | 88.82%                   | 26.33% | 27.33%         | -1.00%        | 45.16%                        | 0.01%                           | -19.32%        |                    1.21505 |                    3.64516 | 14.19%                    | 2024-04                        | -10.59%                  | 2025-04                     | 15.27%                |          32 |
| B           | Weekly rebalance Top3         | weekly      |                3 | -2.76%         | 88.82%                   | -1.06% | 27.33%         | -28.39%       | 37.50%                        | -1.93%                          | -42.13%        |                    3.13542 |                    9.40625 | 21.70%                    | 2024-03                        | -12.42%                  | 2025-03                     | 12.41%                |         138 |
| C           | Weekly rebalance Top5         | weekly      |                5 | 15.51%         | 88.82%                   | 5.63%  | 27.33%         | -21.70%       | 40.62%                        | -1.45%                          | -36.45%        |                    2.74375 |                   13.7188  | 22.19%                    | 2024-08                        | -9.16%                   | 2026-03                     | 6.68%                 |         138 |
| D           | Relative Strength Top3        | weekly      |                3 | 1.71%          | 88.82%                   | 0.65%  | 27.33%         | -26.68%       | 34.38%                        | -1.85%                          | -38.81%        |                    4.28125 |                   12.8438  | 31.97%                    | 2026-02                        | -14.58%                  | 2026-08                     | 8.18%                 |         138 |
| E           | Benchmark-aware Top3          | weekly      |                3 | -4.65%         | 88.82%                   | -1.79% | 27.33%         | -29.12%       | 31.25%                        | -2.06%                          | -39.49%        |                    4.30208 |                   12.9062  | 30.18%                    | 2026-02                        | -11.73%                  | 2026-08                     | 8.18%                 |         138 |
| F           | Leadership Rotation Overlay   | weekly      |                3 | -6.11%         | 88.82%                   | -2.37% | 27.33%         | -29.69%       | 37.50%                        | -2.04%                          | -42.16%        |                    4.15625 |                   12.4688  | 28.62%                    | 2026-02                        | -11.73%                  | 2026-08                     | 8.34%                 |         138 |

## Decision

- Did weekly rebalance improve excess return? Recent yes, historical no, so rejected. Historical excess CAGR delta vs baseline: -27.38%; recent excess delta: 9.11%.
- Did relative strength improve excess return? Recent yes, historical no, so rejected. Historical excess CAGR delta vs baseline: -25.68%; recent excess delta: 9.25%.
- Did benchmark-aware selection improve excess return? Recent yes, historical no, so rejected. Historical excess CAGR delta vs baseline: -28.12%; recent excess delta: 9.25%.
- Did any policy beat BIST100 robustly? No under the current acceptance filter.
- Next paper-trading candidate: none. No policy passed both historical and recent acceptance criteria.
- Current one-month fixed hold should be kept for tracking, while weekly/relative-strength variants remain research-only.

## Acceptance Rule

A policy is only eligible if it improves both historical walk-forward excess return and the recent 2026-06 counterfactual excess return. Policies that only fix June 2026 are rejected.
