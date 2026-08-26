# Follow-Up Improvement Research

This is research-only. Production follow-up tracking remains fixed and still reads reports/tracking_state.json.

## Policy Summary

| policy_id   | policy_name                   | frequency   |   portfolio_size | total_return   | benchmark_total_return   | cagr   | bist100_cagr   | excess_cagr   | monthly_win_rate_vs_bist100   | average_monthly_excess_return   | max_drawdown   |   average_monthly_turnover |   average_trades_per_month | transaction_cost_impact   | worst_underperformance_month   | worst_underperformance   | best_outperformance_month   | best_outperformance   |   intervals |
|:------------|:------------------------------|:------------|-----------------:|:---------------|:-------------------------|:-------|:---------------|:--------------|:------------------------------|:--------------------------------|:---------------|---------------------------:|---------------------------:|:--------------------------|:-------------------------------|:-------------------------|:----------------------------|:----------------------|------------:|
| A           | Current baseline monthly Top3 | monthly     |                3 | 85.14%         | 89.83%                   | 26.23% | 27.42%         | -1.20%        | 45.16%                        | -0.00%                          | -19.32%        |                    1.21505 |                    3.64516 | 14.20%                    | 2024-04                        | -10.59%                  | 2025-04                     | 15.27%                |          32 |
| B           | Weekly rebalance Top3         | weekly      |                3 | -2.10%         | 89.83%                   | -0.80% | 27.42%         | -28.22%       | 37.50%                        | -1.93%                          | -42.13%        |                    3.15625 |                    9.46875 | 22.00%                    | 2024-03                        | -12.42%                  | 2025-03                     | 12.41%                |         139 |
| C           | Weekly rebalance Top5         | weekly      |                5 | 15.06%         | 89.83%                   | 5.45%  | 27.42%         | -21.98%       | 40.62%                        | -1.48%                          | -36.45%        |                    2.78125 |                   13.9062  | 22.44%                    | 2024-08                        | -9.16%                   | 2026-03                     | 6.68%                 |         139 |
| D           | Relative Strength Top3        | weekly      |                3 | 2.40%          | 89.83%                   | 0.90%  | 27.42%         | -26.52%       | 34.38%                        | -1.84%                          | -38.81%        |                    4.30208 |                   12.9062  | 32.37%                    | 2026-02                        | -14.58%                  | 2026-08                     | 8.39%                 |         139 |
| E           | Benchmark-aware Top3          | weekly      |                3 | -4.00%         | 89.83%                   | -1.53% | 27.42%         | -28.96%       | 31.25%                        | -2.06%                          | -39.49%        |                    4.32292 |                   12.9688  | 30.55%                    | 2026-02                        | -11.73%                  | 2026-08                     | 8.39%                 |         139 |
| F           | Leadership Rotation Overlay   | weekly      |                3 | -5.47%         | 89.83%                   | -2.10% | 27.42%         | -29.53%       | 37.50%                        | -2.04%                          | -42.16%        |                    4.17708 |                   12.5312  | 28.98%                    | 2026-02                        | -11.73%                  | 2026-08                     | 8.55%                 |         139 |

## Decision

- Did weekly rebalance improve excess return? Recent yes, historical no, so rejected. Historical excess CAGR delta vs baseline: -27.02%; recent excess delta: 9.20%.
- Did relative strength improve excess return? Recent yes, historical no, so rejected. Historical excess CAGR delta vs baseline: -25.32%; recent excess delta: 9.35%.
- Did benchmark-aware selection improve excess return? Recent yes, historical no, so rejected. Historical excess CAGR delta vs baseline: -27.76%; recent excess delta: 9.35%.
- Did any policy beat BIST100 robustly? No under the current acceptance filter.
- Next paper-trading candidate: none. No policy passed both historical and recent acceptance criteria.
- Current one-month fixed hold should be kept for tracking, while weekly/relative-strength variants remain research-only.

## Acceptance Rule

A policy is only eligible if it improves both historical walk-forward excess return and the recent 2026-06 counterfactual excess return. Policies that only fix June 2026 are rejected.
