# Follow-Up Improvement Research

This is research-only. Production follow-up tracking remains fixed and still reads reports/tracking_state.json.

## Policy Summary

| policy_id   | policy_name                   | frequency   |   portfolio_size | total_return   | benchmark_total_return   | cagr   | bist100_cagr   | excess_cagr   | monthly_win_rate_vs_bist100   | average_monthly_excess_return   | max_drawdown   |   average_monthly_turnover |   average_trades_per_month | transaction_cost_impact   | worst_underperformance_month   | worst_underperformance   | best_outperformance_month   | best_outperformance   |   intervals |
|:------------|:------------------------------|:------------|-----------------:|:---------------|:-------------------------|:-------|:---------------|:--------------|:------------------------------|:--------------------------------|:---------------|---------------------------:|---------------------------:|:--------------------------|:-------------------------------|:-------------------------|:----------------------------|:----------------------|------------:|
| A           | Current baseline monthly Top3 | monthly     |                3 | 82.82%         | 92.04%                   | 25.54% | 27.89%         | -2.35%        | 45.16%                        | -0.09%                          | -19.32%        |                    1.21505 |                    3.64516 | 14.03%                    | 2024-04                        | -10.59%                  | 2025-04                     | 15.27%                |          32 |
| B           | Weekly rebalance Top3         | weekly      |                3 | -4.57%         | 92.04%                   | -1.75% | 27.89%         | -29.63%       | 37.50%                        | -2.05%                          | -42.13%        |                    3.15625 |                    9.46875 | 21.45%                    | 2024-03                        | -12.42%                  | 2025-03                     | 12.41%                |         139 |
| C           | Weekly rebalance Top5         | weekly      |                5 | 13.64%         | 92.04%                   | 4.94%  | 27.89%         | -22.95%       | 37.50%                        | -1.56%                          | -36.45%        |                    2.78125 |                   13.9062  | 22.16%                    | 2024-08                        | -9.16%                   | 2026-03                     | 6.68%                 |         139 |
| D           | Relative Strength Top3        | weekly      |                3 | 0.35%          | 92.04%                   | 0.13%  | 27.89%         | -27.75%       | 34.38%                        | -1.95%                          | -38.81%        |                    4.30208 |                   12.9062  | 31.73%                    | 2026-02                        | -14.58%                  | 2025-03                     | 6.67%                 |         139 |
| E           | Benchmark-aware Top3          | weekly      |                3 | -5.92%         | 92.04%                   | -2.27% | 27.89%         | -30.16%       | 31.25%                        | -2.17%                          | -39.49%        |                    4.32292 |                   12.9688  | 29.94%                    | 2026-02                        | -11.73%                  | 2025-03                     | 6.25%                 |         139 |
| F           | Leadership Rotation Overlay   | weekly      |                3 | -7.86%         | 92.04%                   | -3.04% | 27.89%         | -30.92%       | 37.50%                        | -2.16%                          | -42.16%        |                    4.17708 |                   12.5312  | 28.25%                    | 2026-02                        | -11.73%                  | 2024-04                     | 7.40%                 |         139 |

## Decision

- Did weekly rebalance improve excess return? Recent yes, historical no, so rejected. Historical excess CAGR delta vs baseline: -27.28%; recent excess delta: 5.80%.
- Did relative strength improve excess return? Recent yes, historical no, so rejected. Historical excess CAGR delta vs baseline: -25.40%; recent excess delta: 6.50%.
- Did benchmark-aware selection improve excess return? Recent yes, historical no, so rejected. Historical excess CAGR delta vs baseline: -27.81%; recent excess delta: 6.50%.
- Did any policy beat BIST100 robustly? No under the current acceptance filter.
- Next paper-trading candidate: none. No policy passed both historical and recent acceptance criteria.
- Current one-month fixed hold should be kept for tracking, while weekly/relative-strength variants remain research-only.

## Acceptance Rule

A policy is only eligible if it improves both historical walk-forward excess return and the recent 2026-06 counterfactual excess return. Policies that only fix June 2026 are rejected.
