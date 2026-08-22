# Follow-Up Improvement Research

This is research-only. Production follow-up tracking remains fixed and still reads reports/tracking_state.json.

## Policy Summary

| policy_id   | policy_name                   | frequency   |   portfolio_size | total_return   | benchmark_total_return   | cagr   | bist100_cagr   | excess_cagr   | monthly_win_rate_vs_bist100   | average_monthly_excess_return   | max_drawdown   |   average_monthly_turnover |   average_trades_per_month | transaction_cost_impact   | worst_underperformance_month   | worst_underperformance   | best_outperformance_month   | best_outperformance   |   intervals |
|:------------|:------------------------------|:------------|-----------------:|:---------------|:-------------------------|:-------|:---------------|:--------------|:------------------------------|:--------------------------------|:---------------|---------------------------:|---------------------------:|:--------------------------|:-------------------------------|:-------------------------|:----------------------------|:----------------------|------------:|
| A           | Current baseline monthly Top3 | monthly     |                3 | 84.11%         | 90.38%                   | 26.08% | 27.69%         | -1.61%        | 45.16%                        | -0.03%                          | -19.32%        |                    1.21505 |                    3.64516 | 14.13%                    | 2024-04                        | -10.59%                  | 2025-04                     | 15.27%                |          32 |
| B           | Weekly rebalance Top3         | weekly      |                3 | -2.33%         | 90.38%                   | -0.89% | 27.69%         | -28.58%       | 37.50%                        | -1.94%                          | -42.13%        |                    3.13542 |                    9.40625 | 21.79%                    | 2024-03                        | -12.42%                  | 2025-03                     | 12.41%                |         138 |
| C           | Weekly rebalance Top5         | weekly      |                5 | 14.64%         | 90.38%                   | 5.32%  | 27.69%         | -22.37%       | 40.62%                        | -1.50%                          | -36.45%        |                    2.74375 |                   13.7188  | 22.03%                    | 2024-08                        | -9.16%                   | 2026-03                     | 6.68%                 |         138 |
| D           | Relative Strength Top3        | weekly      |                3 | 2.16%          | 90.38%                   | 0.81%  | 27.69%         | -26.88%       | 34.38%                        | -1.86%                          | -38.81%        |                    4.28125 |                   12.8438  | 32.12%                    | 2026-02                        | -14.58%                  | 2026-08                     | 7.82%                 |         138 |
| E           | Benchmark-aware Top3          | weekly      |                3 | -4.23%         | 90.38%                   | -1.63% | 27.69%         | -29.32%       | 31.25%                        | -2.08%                          | -39.49%        |                    4.30208 |                   12.9062  | 30.31%                    | 2026-02                        | -11.73%                  | 2026-08                     | 7.82%                 |         138 |
| F           | Leadership Rotation Overlay   | weekly      |                3 | -5.69%         | 90.38%                   | -2.20% | 27.69%         | -29.89%       | 37.50%                        | -2.05%                          | -42.16%        |                    4.15625 |                   12.4688  | 28.75%                    | 2026-02                        | -11.73%                  | 2026-08                     | 7.98%                 |         138 |

## Decision

- Did weekly rebalance improve excess return? Recent yes, historical no, so rejected. Historical excess CAGR delta vs baseline: -26.97%; recent excess delta: 8.94%.
- Did relative strength improve excess return? Recent yes, historical no, so rejected. Historical excess CAGR delta vs baseline: -25.26%; recent excess delta: 9.08%.
- Did benchmark-aware selection improve excess return? Recent yes, historical no, so rejected. Historical excess CAGR delta vs baseline: -27.71%; recent excess delta: 9.08%.
- Did any policy beat BIST100 robustly? No under the current acceptance filter.
- Next paper-trading candidate: none. No policy passed both historical and recent acceptance criteria.
- Current one-month fixed hold should be kept for tracking, while weekly/relative-strength variants remain research-only.

## Acceptance Rule

A policy is only eligible if it improves both historical walk-forward excess return and the recent 2026-06 counterfactual excess return. Policies that only fix June 2026 are rejected.
