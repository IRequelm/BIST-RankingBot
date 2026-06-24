# Follow-Up Improvement Research

This is research-only. Production follow-up tracking remains fixed and still reads reports/tracking_state.json.

## Policy Summary

| policy_id   | policy_name                   | frequency   |   portfolio_size | total_return   | benchmark_total_return   | cagr   | bist100_cagr   | excess_cagr   | monthly_win_rate_vs_bist100   | average_monthly_excess_return   | max_drawdown   |   average_monthly_turnover |   average_trades_per_month | transaction_cost_impact   | worst_underperformance_month   | worst_underperformance   | best_outperformance_month   | best_outperformance   |   intervals |
|:------------|:------------------------------|:------------|-----------------:|:---------------|:-------------------------|:-------|:---------------|:--------------|:------------------------------|:--------------------------------|:---------------|---------------------------:|---------------------------:|:--------------------------|:-------------------------------|:-------------------------|:----------------------------|:----------------------|------------:|
| A           | Current baseline monthly Top3 | monthly     |                3 | 75.72%         | 90.70%                   | 25.61% | 29.84%         | -4.23%        | 41.38%                        | -0.20%                          | -19.32%        |                    1.22989 |                    3.68966 | 12.72%                    | 2024-04                        | -10.59%                  | 2025-04                     | 15.27%                |          30 |
| B           | Weekly rebalance Top3         | weekly      |                3 | -2.12%         | 90.70%                   | -0.86% | 29.84%         | -30.70%       | 40.00%                        | -2.09%                          | -42.13%        |                    3.21111 |                    9.63333 | 20.89%                    | 2024-03                        | -12.42%                  | 2025-03                     | 12.41%                |         130 |
| C           | Weekly rebalance Top5         | weekly      |                5 | 25.44%         | 90.70%                   | 9.60%  | 29.84%         | -20.24%       | 43.33%                        | -1.32%                          | -36.45%        |                    2.76667 |                   13.8333  | 22.66%                    | 2024-08                        | -9.16%                   | 2026-03                     | 6.68%                 |         130 |
| D           | Relative Strength Top3        | weekly      |                3 | 3.72%          | 90.70%                   | 1.49%  | 29.84%         | -28.35%       | 36.67%                        | -1.96%                          | -35.17%        |                    4.36667 |                   13.1     | 30.98%                    | 2026-02                        | -14.58%                  | 2025-03                     | 6.67%                 |         130 |
| E           | Benchmark-aware Top3          | weekly      |                3 | -2.77%         | 90.70%                   | -1.13% | 29.84%         | -30.97%       | 33.33%                        | -2.19%                          | -38.70%        |                    4.38889 |                   13.1667  | 29.25%                    | 2026-02                        | -11.73%                  | 2025-03                     | 6.25%                 |         130 |
| F           | Leadership Rotation Overlay   | weekly      |                3 | -6.81%         | 90.70%                   | -2.81% | 29.84%         | -32.65%       | 36.67%                        | -2.25%                          | -42.16%        |                    4.27778 |                   12.8333  | 27.27%                    | 2026-02                        | -11.73%                  | 2024-04                     | 7.40%                 |         130 |

## Decision

- Did weekly rebalance improve excess return? Recent yes, historical no, so rejected. Historical excess CAGR delta vs baseline: -26.47%; recent excess delta: 5.54%.
- Did relative strength improve excess return? Recent yes, historical no, so rejected. Historical excess CAGR delta vs baseline: -24.12%; recent excess delta: 7.08%.
- Did benchmark-aware selection improve excess return? Recent yes, historical no, so rejected. Historical excess CAGR delta vs baseline: -26.74%; recent excess delta: 7.08%.
- Did any policy beat BIST100 robustly? No under the current acceptance filter.
- Next paper-trading candidate: none. No policy passed both historical and recent acceptance criteria.
- Current one-month fixed hold should be kept for tracking, while weekly/relative-strength variants remain research-only.

## Acceptance Rule

A policy is only eligible if it improves both historical walk-forward excess return and the recent 2026-06 counterfactual excess return. Policies that only fix June 2026 are rejected.
