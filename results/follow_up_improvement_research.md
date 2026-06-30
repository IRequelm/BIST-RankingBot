# Follow-Up Improvement Research

This is research-only. Production follow-up tracking remains fixed and still reads reports/tracking_state.json.

## Policy Summary

| policy_id   | policy_name                   | frequency   |   portfolio_size | total_return   | benchmark_total_return   | cagr   | bist100_cagr   | excess_cagr   | monthly_win_rate_vs_bist100   | average_monthly_excess_return   | max_drawdown   |   average_monthly_turnover |   average_trades_per_month | transaction_cost_impact   | worst_underperformance_month   | worst_underperformance   | best_outperformance_month   | best_outperformance   |   intervals |
|:------------|:------------------------------|:------------|-----------------:|:---------------|:-------------------------|:-------|:---------------|:--------------|:------------------------------|:--------------------------------|:---------------|---------------------------:|---------------------------:|:--------------------------|:-------------------------------|:-------------------------|:----------------------------|:----------------------|------------:|
| A           | Current baseline monthly Top3 | monthly     |                3 | 73.99%         | 86.03%                   | 24.92% | 28.33%         | -3.40%        | 44.83%                        | -0.15%                          | -19.32%        |                    1.22989 |                    3.68966 | 12.60%                    | 2024-04                        | -10.59%                  | 2025-04                     | 15.27%                |          30 |
| B           | Weekly rebalance Top3         | weekly      |                3 | -7.52%         | 86.03%                   | -3.09% | 28.33%         | -31.42%       | 36.67%                        | -2.20%                          | -42.13%        |                    3.21111 |                    9.63333 | 19.73%                    | 2024-03                        | -12.42%                  | 2025-03                     | 12.41%                |         130 |
| C           | Weekly rebalance Top5         | weekly      |                5 | 17.53%         | 86.03%                   | 6.70%  | 28.33%         | -21.62%       | 40.00%                        | -1.46%                          | -36.45%        |                    2.76667 |                   13.8333  | 21.25%                    | 2024-08                        | -9.16%                   | 2026-03                     | 6.68%                 |         130 |
| D           | Relative Strength Top3        | weekly      |                3 | -3.18%         | 86.03%                   | -1.29% | 28.33%         | -29.62%       | 33.33%                        | -2.12%                          | -35.17%        |                    4.36667 |                   13.1     | 28.93%                    | 2026-02                        | -14.58%                  | 2025-03                     | 6.67%                 |         130 |
| E           | Benchmark-aware Top3          | weekly      |                3 | -9.24%         | 86.03%                   | -3.82% | 28.33%         | -32.15%       | 30.00%                        | -2.34%                          | -38.70%        |                    4.38889 |                   13.1667  | 27.31%                    | 2026-02                        | -11.73%                  | 2025-03                     | 6.25%                 |         130 |
| F           | Leadership Rotation Overlay   | weekly      |                3 | -12.68%        | 86.03%                   | -5.30% | 28.33%         | -33.63%       | 36.67%                        | -2.39%                          | -42.16%        |                    4.27778 |                   12.8333  | 25.56%                    | 2026-02                        | -11.73%                  | 2024-04                     | 7.40%                 |         130 |

## Decision

- Did weekly rebalance improve excess return? Recent yes, historical no, so rejected. Historical excess CAGR delta vs baseline: -28.01%; recent excess delta: 0.66%.
- Did relative strength improve excess return? Recent yes, historical no, so rejected. Historical excess CAGR delta vs baseline: -26.21%; recent excess delta: 0.88%.
- Did benchmark-aware selection improve excess return? Recent yes, historical no, so rejected. Historical excess CAGR delta vs baseline: -28.74%; recent excess delta: 0.88%.
- Did any policy beat BIST100 robustly? No under the current acceptance filter.
- Next paper-trading candidate: none. No policy passed both historical and recent acceptance criteria.
- Current one-month fixed hold should be kept for tracking, while weekly/relative-strength variants remain research-only.

## Acceptance Rule

A policy is only eligible if it improves both historical walk-forward excess return and the recent 2026-06 counterfactual excess return. Policies that only fix June 2026 are rejected.
