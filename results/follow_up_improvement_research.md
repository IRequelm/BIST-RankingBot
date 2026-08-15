# Follow-Up Improvement Research

This is research-only. Production follow-up tracking remains fixed and still reads reports/tracking_state.json.

## Policy Summary

| policy_id   | policy_name                   | frequency   |   portfolio_size | total_return   | benchmark_total_return   | cagr   | bist100_cagr   | excess_cagr   | monthly_win_rate_vs_bist100   | average_monthly_excess_return   | max_drawdown   |   average_monthly_turnover |   average_trades_per_month | transaction_cost_impact   | worst_underperformance_month   | worst_underperformance   | best_outperformance_month   | best_outperformance   |   intervals |
|:------------|:------------------------------|:------------|-----------------:|:---------------|:-------------------------|:-------|:---------------|:--------------|:------------------------------|:--------------------------------|:---------------|---------------------------:|---------------------------:|:--------------------------|:-------------------------------|:-------------------------|:----------------------------|:----------------------|------------:|
| A           | Current baseline monthly Top3 | monthly     |                3 | 71.12%         | 85.88%                   | 22.81% | 26.76%         | -3.95%        | 45.16%                        | -0.20%                          | -19.32%        |                    1.21505 |                    3.64516 | 13.15%                    | 2024-04                        | -10.59%                  | 2025-04                     | 15.27%                |          32 |
| B           | Weekly rebalance Top3         | weekly      |                3 | -10.36%        | 85.88%                   | -4.10% | 26.76%         | -30.85%       | 37.50%                        | -2.15%                          | -42.13%        |                    3.11458 |                    9.34375 | 19.87%                    | 2024-03                        | -12.42%                  | 2025-03                     | 12.41%                |         137 |
| C           | Weekly rebalance Top5         | weekly      |                5 | 10.81%         | 85.88%                   | 4.00%  | 26.76%         | -22.76%       | 40.62%                        | -1.54%                          | -36.45%        |                    2.69375 |                   13.4688  | 20.88%                    | 2024-08                        | -9.16%                   | 2026-03                     | 6.68%                 |         137 |
| D           | Relative Strength Top3        | weekly      |                3 | -3.01%         | 85.88%                   | -1.16% | 26.76%         | -27.92%       | 34.38%                        | -1.97%                          | -36.78%        |                    4.26042 |                   12.7812  | 30.33%                    | 2026-02                        | -14.58%                  | 2025-03                     | 6.67%                 |         137 |
| E           | Benchmark-aware Top3          | weekly      |                3 | -9.08%         | 85.88%                   | -3.58% | 26.76%         | -30.33%       | 31.25%                        | -2.19%                          | -38.70%        |                    4.28125 |                   12.8438  | 28.62%                    | 2026-02                        | -11.73%                  | 2025-03                     | 6.25%                 |         137 |
| F           | Leadership Rotation Overlay   | weekly      |                3 | -12.60%        | 85.88%                   | -5.02% | 26.76%         | -31.78%       | 37.50%                        | -2.24%                          | -42.16%        |                    4.13542 |                   12.4062  | 26.50%                    | 2026-02                        | -11.73%                  | 2024-04                     | 7.40%                 |         137 |

## Decision

- Did weekly rebalance improve excess return? Recent yes, historical no, so rejected. Historical excess CAGR delta vs baseline: -26.90%; recent excess delta: 1.95%.
- Did relative strength improve excess return? Recent yes, historical no, so rejected. Historical excess CAGR delta vs baseline: -23.97%; recent excess delta: 5.45%.
- Did benchmark-aware selection improve excess return? Recent yes, historical no, so rejected. Historical excess CAGR delta vs baseline: -26.38%; recent excess delta: 5.45%.
- Did any policy beat BIST100 robustly? No under the current acceptance filter.
- Next paper-trading candidate: none. No policy passed both historical and recent acceptance criteria.
- Current one-month fixed hold should be kept for tracking, while weekly/relative-strength variants remain research-only.

## Acceptance Rule

A policy is only eligible if it improves both historical walk-forward excess return and the recent 2026-06 counterfactual excess return. Policies that only fix June 2026 are rejected.
