# Follow-Up Improvement Research

This is research-only. Production follow-up tracking remains fixed and still reads reports/tracking_state.json.

## Policy Summary

| policy_id   | policy_name                   | frequency   |   portfolio_size | total_return   | benchmark_total_return   | cagr   | bist100_cagr   | excess_cagr   | monthly_win_rate_vs_bist100   | average_monthly_excess_return   | max_drawdown   |   average_monthly_turnover |   average_trades_per_month | transaction_cost_impact   | worst_underperformance_month   | worst_underperformance   | best_outperformance_month   | best_outperformance   |   intervals |
|:------------|:------------------------------|:------------|-----------------:|:---------------|:-------------------------|:-------|:---------------|:--------------|:------------------------------|:--------------------------------|:---------------|---------------------------:|---------------------------:|:--------------------------|:-------------------------------|:-------------------------|:----------------------------|:----------------------|------------:|
| A           | Current baseline monthly Top3 | monthly     |                3 | 82.82%         | 91.17%                   | 25.57% | 27.70%         | -2.13%        | 45.16%                        | -0.07%                          | -19.32%        |                    1.21505 |                    3.64516 | 14.03%                    | 2024-04                        | -10.59%                  | 2025-04                     | 15.27%                |          32 |
| B           | Weekly rebalance Top3         | weekly      |                3 | -4.57%         | 91.17%                   | -1.75% | 27.70%         | -29.45%       | 37.50%                        | -2.04%                          | -42.13%        |                    3.15625 |                    9.46875 | 21.45%                    | 2024-03                        | -12.42%                  | 2025-03                     | 12.41%                |         139 |
| C           | Weekly rebalance Top5         | weekly      |                5 | 13.64%         | 91.17%                   | 4.94%  | 27.70%         | -22.76%       | 40.62%                        | -1.54%                          | -36.45%        |                    2.78125 |                   13.9062  | 22.16%                    | 2024-08                        | -9.16%                   | 2026-03                     | 6.68%                 |         139 |
| D           | Relative Strength Top3        | weekly      |                3 | 0.35%          | 91.17%                   | 0.13%  | 27.70%         | -27.57%       | 34.38%                        | -1.94%                          | -38.81%        |                    4.30208 |                   12.9062  | 31.73%                    | 2026-02                        | -14.58%                  | 2025-03                     | 6.67%                 |         139 |
| E           | Benchmark-aware Top3          | weekly      |                3 | -5.92%         | 91.17%                   | -2.28% | 27.70%         | -29.98%       | 31.25%                        | -2.15%                          | -39.49%        |                    4.32292 |                   12.9688  | 29.94%                    | 2026-02                        | -11.73%                  | 2025-03                     | 6.25%                 |         139 |
| F           | Leadership Rotation Overlay   | weekly      |                3 | -7.86%         | 91.17%                   | -3.04% | 27.70%         | -30.74%       | 37.50%                        | -2.15%                          | -42.16%        |                    4.17708 |                   12.5312  | 28.25%                    | 2026-02                        | -11.73%                  | 2024-04                     | 7.40%                 |         139 |

## Decision

- Did weekly rebalance improve excess return? Recent yes, historical no, so rejected. Historical excess CAGR delta vs baseline: -27.31%; recent excess delta: 5.80%.
- Did relative strength improve excess return? Recent yes, historical no, so rejected. Historical excess CAGR delta vs baseline: -25.43%; recent excess delta: 6.50%.
- Did benchmark-aware selection improve excess return? Recent yes, historical no, so rejected. Historical excess CAGR delta vs baseline: -27.84%; recent excess delta: 6.50%.
- Did any policy beat BIST100 robustly? No under the current acceptance filter.
- Next paper-trading candidate: none. No policy passed both historical and recent acceptance criteria.
- Current one-month fixed hold should be kept for tracking, while weekly/relative-strength variants remain research-only.

## Acceptance Rule

A policy is only eligible if it improves both historical walk-forward excess return and the recent 2026-06 counterfactual excess return. Policies that only fix June 2026 are rejected.
