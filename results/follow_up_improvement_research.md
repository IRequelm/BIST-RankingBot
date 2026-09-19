# Follow-Up Improvement Research

This is research-only. Production follow-up tracking remains fixed and still reads reports/tracking_state.json.

## Policy Summary

| policy_id   | policy_name                   | frequency   |   portfolio_size | total_return   | benchmark_total_return   | cagr   | bist100_cagr   | excess_cagr   | monthly_win_rate_vs_bist100   | average_monthly_excess_return   | max_drawdown   |   average_monthly_turnover |   average_trades_per_month | transaction_cost_impact   | worst_underperformance_month   | worst_underperformance   | best_outperformance_month   | best_outperformance   |   intervals |
|:------------|:------------------------------|:------------|-----------------:|:---------------|:-------------------------|:-------|:---------------|:--------------|:------------------------------|:--------------------------------|:---------------|---------------------------:|---------------------------:|:--------------------------|:-------------------------------|:-------------------------|:----------------------------|:----------------------|------------:|
| A           | Current baseline monthly Top3 | monthly     |                3 | 76.26%         | 74.24%                   | 23.26% | 22.73%         | 0.52%         | 46.88%                        | 0.11%                           | -19.32%        |                    1.21875 |                    3.65625 | 14.05%                    | 2024-04                        | -10.59%                  | 2025-04                     | 15.27%                |          33 |
| B           | Weekly rebalance Top3         | weekly      |                3 | -7.46%         | 74.24%                   | -2.82% | 22.73%         | -25.56%       | 39.39%                        | -1.79%                          | -42.13%        |                    3.08081 |                    9.24242 | 20.96%                    | 2024-03                        | -12.42%                  | 2025-03                     | 12.41%                |         142 |
| C           | Weekly rebalance Top5         | weekly      |                5 | 6.71%          | 74.24%                   | 2.43%  | 22.73%         | -20.31%       | 42.42%                        | -1.41%                          | -36.45%        |                    2.73333 |                   13.6667  | 21.14%                    | 2024-08                        | -9.16%                   | 2026-03                     | 6.68%                 |         142 |
| D           | Relative Strength Top3        | weekly      |                3 | -3.29%         | 74.24%                   | -1.23% | 22.73%         | -23.96%       | 36.36%                        | -1.71%                          | -38.81%        |                    4.25253 |                   12.7576  | 31.27%                    | 2026-02                        | -14.58%                  | 2026-08                     | 8.57%                 |         142 |
| E           | Benchmark-aware Top3          | weekly      |                3 | -8.67%         | 74.24%                   | -3.29% | 22.73%         | -26.03%       | 33.33%                        | -1.89%                          | -39.49%        |                    4.25253 |                   12.7576  | 29.55%                    | 2026-02                        | -11.73%                  | 2026-08                     | 8.57%                 |         142 |
| F           | Leadership Rotation Overlay   | weekly      |                3 | -11.58%        | 74.24%                   | -4.44% | 22.73%         | -27.17%       | 39.39%                        | -1.92%                          | -42.16%        |                    4.11111 |                   12.3333  | 27.60%                    | 2026-02                        | -11.73%                  | 2026-08                     | 8.44%                 |         142 |

## Decision

- Did weekly rebalance improve excess return? Recent yes, historical no, so rejected. Historical excess CAGR delta vs baseline: -26.08%; recent excess delta: 7.89%.
- Did relative strength improve excess return? Recent yes, historical no, so rejected. Historical excess CAGR delta vs baseline: -24.49%; recent excess delta: 7.94%.
- Did benchmark-aware selection improve excess return? Recent yes, historical no, so rejected. Historical excess CAGR delta vs baseline: -26.55%; recent excess delta: 8.69%.
- Did any policy beat BIST100 robustly? No under the current acceptance filter.
- Next paper-trading candidate: none. No policy passed both historical and recent acceptance criteria.
- Current one-month fixed hold should be kept for tracking, while weekly/relative-strength variants remain research-only.

## Acceptance Rule

A policy is only eligible if it improves both historical walk-forward excess return and the recent 2026-06 counterfactual excess return. Policies that only fix June 2026 are rejected.
