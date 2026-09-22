# Follow-Up Improvement Research

This is research-only. Production follow-up tracking remains fixed and still reads reports/tracking_state.json.

## Policy Summary

| policy_id   | policy_name                   | frequency   |   portfolio_size | total_return   | benchmark_total_return   | cagr   | bist100_cagr   | excess_cagr   | monthly_win_rate_vs_bist100   | average_monthly_excess_return   | max_drawdown   |   average_monthly_turnover |   average_trades_per_month | transaction_cost_impact   | worst_underperformance_month   | worst_underperformance   | best_outperformance_month   | best_outperformance   |   intervals |
|:------------|:------------------------------|:------------|-----------------:|:---------------|:-------------------------|:-------|:---------------|:--------------|:------------------------------|:--------------------------------|:---------------|---------------------------:|---------------------------:|:--------------------------|:-------------------------------|:-------------------------|:----------------------------|:----------------------|------------:|
| A           | Current baseline monthly Top3 | monthly     |                3 | 83.48%         | 74.94%                   | 25.01% | 22.84%         | 2.17%         | 46.88%                        | 0.23%                           | -19.32%        |                    1.21875 |                    3.65625 | 14.61%                    | 2024-04                        | -10.59%                  | 2025-04                     | 15.27%                |          33 |
| B           | Weekly rebalance Top3         | weekly      |                3 | -4.35%         | 74.94%                   | -1.62% | 22.84%         | -24.46%       | 39.39%                        | -1.70%                          | -42.13%        |                    3.08081 |                    9.24242 | 21.66%                    | 2024-03                        | -12.42%                  | 2025-03                     | 12.41%                |         142 |
| C           | Weekly rebalance Top5         | weekly      |                5 | 10.66%         | 74.94%                   | 3.79%  | 22.84%         | -19.05%       | 42.42%                        | -1.31%                          | -36.45%        |                    2.73333 |                   13.6667  | 21.91%                    | 2024-08                        | -9.16%                   | 2026-03                     | 6.68%                 |         142 |
| D           | Relative Strength Top3        | weekly      |                3 | -0.14%         | 74.94%                   | -0.05% | 22.84%         | -22.89%       | 36.36%                        | -1.62%                          | -38.81%        |                    4.25253 |                   12.7576  | 32.28%                    | 2026-02                        | -14.58%                  | 2026-08                     | 8.57%                 |         142 |
| E           | Benchmark-aware Top3          | weekly      |                3 | -5.70%         | 74.94%                   | -2.13% | 22.84%         | -24.97%       | 33.33%                        | -1.81%                          | -39.49%        |                    4.25253 |                   12.7576  | 30.51%                    | 2026-02                        | -11.73%                  | 2026-08                     | 8.57%                 |         142 |
| F           | Leadership Rotation Overlay   | weekly      |                3 | -8.69%         | 74.94%                   | -3.29% | 22.84%         | -26.13%       | 39.39%                        | -1.84%                          | -42.16%        |                    4.11111 |                   12.3333  | 28.49%                    | 2026-02                        | -11.73%                  | 2026-08                     | 8.44%                 |         142 |

## Decision

- Did weekly rebalance improve excess return? Recent yes, historical no, so rejected. Historical excess CAGR delta vs baseline: -26.63%; recent excess delta: 7.62%.
- Did relative strength improve excess return? Recent yes, historical no, so rejected. Historical excess CAGR delta vs baseline: -25.06%; recent excess delta: 7.57%.
- Did benchmark-aware selection improve excess return? Recent yes, historical no, so rejected. Historical excess CAGR delta vs baseline: -27.15%; recent excess delta: 8.34%.
- Did any policy beat BIST100 robustly? No under the current acceptance filter.
- Next paper-trading candidate: none. No policy passed both historical and recent acceptance criteria.
- Current one-month fixed hold should be kept for tracking, while weekly/relative-strength variants remain research-only.

## Acceptance Rule

A policy is only eligible if it improves both historical walk-forward excess return and the recent 2026-06 counterfactual excess return. Policies that only fix June 2026 are rejected.
