# Follow-Up Improvement Research

This is research-only. Production follow-up tracking remains fixed and still reads reports/tracking_state.json.

## Policy Summary

| policy_id   | policy_name                   | frequency   |   portfolio_size | total_return   | benchmark_total_return   | cagr   | bist100_cagr   | excess_cagr   | monthly_win_rate_vs_bist100   | average_monthly_excess_return   | max_drawdown   |   average_monthly_turnover |   average_trades_per_month | transaction_cost_impact   | worst_underperformance_month   | worst_underperformance   | best_outperformance_month   | best_outperformance   |   intervals |
|:------------|:------------------------------|:------------|-----------------:|:---------------|:-------------------------|:-------|:---------------|:--------------|:------------------------------|:--------------------------------|:---------------|---------------------------:|---------------------------:|:--------------------------|:-------------------------------|:-------------------------|:----------------------------|:----------------------|------------:|
| A           | Current baseline monthly Top3 | monthly     |                3 | 71.77%         | 88.22%                   | 24.22% | 28.86%         | -4.64%        | 43.33%                        | -0.24%                          | -19.32%        |                    1.18889 |                    3.56667 | 12.44%                    | 2024-04                        | -10.59%                  | 2025-04                     | 15.27%                |          30 |
| B           | Weekly rebalance Top3         | weekly      |                3 | -8.76%         | 88.22%                   | -3.61% | 28.86%         | -32.47%       | 35.48%                        | -2.21%                          | -42.13%        |                    3.12903 |                    9.3871  | 19.62%                    | 2024-03                        | -12.42%                  | 2025-03                     | 12.41%                |         131 |
| C           | Weekly rebalance Top5         | weekly      |                5 | 17.09%         | 88.22%                   | 6.53%  | 28.86%         | -22.33%       | 38.71%                        | -1.46%                          | -36.45%        |                    2.69032 |                   13.4516  | 21.28%                    | 2024-08                        | -9.16%                   | 2026-03                     | 6.68%                 |         131 |
| D           | Relative Strength Top3        | weekly      |                3 | -3.82%         | 88.22%                   | -1.55% | 28.86%         | -30.41%       | 32.26%                        | -2.11%                          | -35.17%        |                    4.26882 |                   12.8065  | 29.08%                    | 2026-02                        | -14.58%                  | 2025-03                     | 6.67%                 |         131 |
| E           | Benchmark-aware Top3          | weekly      |                3 | -9.83%         | 88.22%                   | -4.06% | 28.86%         | -32.93%       | 29.03%                        | -2.33%                          | -38.70%        |                    4.29032 |                   12.871   | 27.45%                    | 2026-02                        | -11.73%                  | 2025-03                     | 6.25%                 |         131 |
| F           | Leadership Rotation Overlay   | weekly      |                3 | -12.22%        | 88.22%                   | -5.09% | 28.86%         | -33.95%       | 35.48%                        | -2.34%                          | -42.16%        |                    4.16129 |                   12.4839  | 25.85%                    | 2026-02                        | -11.73%                  | 2024-04                     | 7.40%                 |         131 |

## Decision

- Did weekly rebalance improve excess return? Recent yes, historical no, so rejected. Historical excess CAGR delta vs baseline: -27.83%; recent excess delta: 0.58%.
- Did relative strength improve excess return? Recent yes, historical no, so rejected. Historical excess CAGR delta vs baseline: -25.77%; recent excess delta: 1.50%.
- Did benchmark-aware selection improve excess return? Recent yes, historical no, so rejected. Historical excess CAGR delta vs baseline: -28.28%; recent excess delta: 1.50%.
- Did any policy beat BIST100 robustly? No under the current acceptance filter.
- Next paper-trading candidate: none. No policy passed both historical and recent acceptance criteria.
- Current one-month fixed hold should be kept for tracking, while weekly/relative-strength variants remain research-only.

## Acceptance Rule

A policy is only eligible if it improves both historical walk-forward excess return and the recent 2026-06 counterfactual excess return. Policies that only fix June 2026 are rejected.
