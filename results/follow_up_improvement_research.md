# Follow-Up Improvement Research

This is research-only. Production follow-up tracking remains fixed and still reads reports/tracking_state.json.

## Policy Summary

| policy_id   | policy_name                   | frequency   |   portfolio_size | total_return   | benchmark_total_return   | cagr   | bist100_cagr   | excess_cagr   | monthly_win_rate_vs_bist100   | average_monthly_excess_return   | max_drawdown   |   average_monthly_turnover |   average_trades_per_month | transaction_cost_impact   | worst_underperformance_month   | worst_underperformance   | best_outperformance_month   | best_outperformance   |   intervals |
|:------------|:------------------------------|:------------|-----------------:|:---------------|:-------------------------|:-------|:---------------|:--------------|:------------------------------|:--------------------------------|:---------------|---------------------------:|---------------------------:|:--------------------------|:-------------------------------|:-------------------------|:----------------------------|:----------------------|------------:|
| A           | Current baseline monthly Top3 | monthly     |                3 | 74.96%         | 85.30%                   | 23.75% | 26.48%         | -2.74%        | 45.16%                        | -0.12%                          | -19.32%        |                    1.21505 |                    3.64516 | 13.44%                    | 2024-04                        | -10.59%                  | 2025-04                     | 15.27%                |          32 |
| B           | Weekly rebalance Top3         | weekly      |                3 | -7.57%         | 85.30%                   | -2.96% | 26.48%         | -29.44%       | 37.50%                        | -2.04%                          | -42.13%        |                    3.13542 |                    9.40625 | 20.64%                    | 2024-03                        | -12.42%                  | 2025-03                     | 12.41%                |         138 |
| C           | Weekly rebalance Top5         | weekly      |                5 | 13.11%         | 85.30%                   | 4.80%  | 26.48%         | -21.68%       | 40.62%                        | -1.46%                          | -36.45%        |                    2.73125 |                   13.6562  | 21.63%                    | 2024-08                        | -9.16%                   | 2026-03                     | 6.68%                 |         138 |
| D           | Relative Strength Top3        | weekly      |                3 | -3.21%         | 85.30%                   | -1.23% | 26.48%         | -27.72%       | 34.38%                        | -1.97%                          | -37.15%        |                    4.30208 |                   12.9062  | 30.61%                    | 2026-02                        | -14.58%                  | 2025-03                     | 6.67%                 |         138 |
| E           | Benchmark-aware Top3          | weekly      |                3 | -9.26%         | 85.30%                   | -3.63% | 26.48%         | -30.12%       | 31.25%                        | -2.18%                          | -38.70%        |                    4.32292 |                   12.9688  | 28.88%                    | 2026-02                        | -11.73%                  | 2025-03                     | 6.25%                 |         138 |
| F           | Leadership Rotation Overlay   | weekly      |                3 | -9.76%         | 85.30%                   | -3.84% | 26.48%         | -30.32%       | 37.50%                        | -2.12%                          | -42.16%        |                    4.15625 |                   12.4688  | 27.52%                    | 2026-02                        | -11.73%                  | 2024-04                     | 7.40%                 |         138 |

## Decision

- Did weekly rebalance improve excess return? Recent yes, historical no, so rejected. Historical excess CAGR delta vs baseline: -26.70%; recent excess delta: 6.94%.
- Did relative strength improve excess return? Recent yes, historical no, so rejected. Historical excess CAGR delta vs baseline: -24.98%; recent excess delta: 7.20%.
- Did benchmark-aware selection improve excess return? Recent yes, historical no, so rejected. Historical excess CAGR delta vs baseline: -27.38%; recent excess delta: 7.20%.
- Did any policy beat BIST100 robustly? No under the current acceptance filter.
- Next paper-trading candidate: none. No policy passed both historical and recent acceptance criteria.
- Current one-month fixed hold should be kept for tracking, while weekly/relative-strength variants remain research-only.

## Acceptance Rule

A policy is only eligible if it improves both historical walk-forward excess return and the recent 2026-06 counterfactual excess return. Policies that only fix June 2026 are rejected.
