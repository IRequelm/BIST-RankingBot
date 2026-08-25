# Follow-Up Improvement Research

This is research-only. Production follow-up tracking remains fixed and still reads reports/tracking_state.json.

## Policy Summary

| policy_id   | policy_name                   | frequency   |   portfolio_size | total_return   | benchmark_total_return   | cagr   | bist100_cagr   | excess_cagr   | monthly_win_rate_vs_bist100   | average_monthly_excess_return   | max_drawdown   |   average_monthly_turnover |   average_trades_per_month | transaction_cost_impact   | worst_underperformance_month   | worst_underperformance   | best_outperformance_month   | best_outperformance   |   intervals |
|:------------|:------------------------------|:------------|-----------------:|:---------------|:-------------------------|:-------|:---------------|:--------------|:------------------------------|:--------------------------------|:---------------|---------------------------:|---------------------------:|:--------------------------|:-------------------------------|:-------------------------|:----------------------------|:----------------------|------------:|
| A           | Current baseline monthly Top3 | monthly     |                3 | 87.01%         | 90.20%                   | 26.73% | 27.55%         | -0.82%        | 45.16%                        | 0.02%                           | -19.32%        |                    1.21505 |                    3.64516 | 14.34%                    | 2024-04                        | -10.59%                  | 2025-04                     | 15.27%                |          32 |
| B           | Weekly rebalance Top3         | weekly      |                3 | -0.62%         | 90.20%                   | -0.24% | 27.55%         | -27.79%       | 37.50%                        | -1.88%                          | -42.13%        |                    3.13542 |                    9.40625 | 22.17%                    | 2024-03                        | -12.42%                  | 2025-03                     | 12.41%                |         138 |
| C           | Weekly rebalance Top5         | weekly      |                5 | 15.99%         | 90.20%                   | 5.77%  | 27.55%         | -21.78%       | 40.62%                        | -1.46%                          | -36.45%        |                    2.74375 |                   13.7188  | 22.28%                    | 2024-08                        | -9.16%                   | 2026-03                     | 6.68%                 |         138 |
| D           | Relative Strength Top3        | weekly      |                3 | 3.94%          | 90.20%                   | 1.47%  | 27.55%         | -26.08%       | 34.38%                        | -1.80%                          | -38.81%        |                    4.28125 |                   12.8438  | 32.67%                    | 2026-02                        | -14.58%                  | 2026-08                     | 9.89%                 |         138 |
| E           | Benchmark-aware Top3          | weekly      |                3 | -2.56%         | 90.20%                   | -0.98% | 27.55%         | -28.53%       | 31.25%                        | -2.01%                          | -39.49%        |                    4.30208 |                   12.9062  | 30.84%                    | 2026-02                        | -11.73%                  | 2026-08                     | 9.89%                 |         138 |
| F           | Leadership Rotation Overlay   | weekly      |                3 | -4.05%         | 90.20%                   | -1.55% | 27.55%         | -29.10%       | 37.50%                        | -1.99%                          | -42.16%        |                    4.15625 |                   12.4688  | 29.25%                    | 2026-02                        | -11.73%                  | 2026-08                     | 10.05%                |         138 |

## Decision

- Did weekly rebalance improve excess return? Recent yes, historical no, so rejected. Historical excess CAGR delta vs baseline: -26.97%; recent excess delta: 10.35%.
- Did relative strength improve excess return? Recent yes, historical no, so rejected. Historical excess CAGR delta vs baseline: -25.26%; recent excess delta: 10.49%.
- Did benchmark-aware selection improve excess return? Recent yes, historical no, so rejected. Historical excess CAGR delta vs baseline: -27.71%; recent excess delta: 10.49%.
- Did any policy beat BIST100 robustly? No under the current acceptance filter.
- Next paper-trading candidate: none. No policy passed both historical and recent acceptance criteria.
- Current one-month fixed hold should be kept for tracking, while weekly/relative-strength variants remain research-only.

## Acceptance Rule

A policy is only eligible if it improves both historical walk-forward excess return and the recent 2026-06 counterfactual excess return. Policies that only fix June 2026 are rejected.
