# Follow-Up Improvement Research

This is research-only. Production follow-up tracking remains fixed and still reads reports/tracking_state.json.

## Policy Summary

| policy_id   | policy_name                   | frequency   |   portfolio_size | total_return   | benchmark_total_return   | cagr   | bist100_cagr   | excess_cagr   | monthly_win_rate_vs_bist100   | average_monthly_excess_return   | max_drawdown   |   average_monthly_turnover |   average_trades_per_month | transaction_cost_impact   | worst_underperformance_month   | worst_underperformance   | best_outperformance_month   | best_outperformance   |   intervals |
|:------------|:------------------------------|:------------|-----------------:|:---------------|:-------------------------|:-------|:---------------|:--------------|:------------------------------|:--------------------------------|:---------------|---------------------------:|---------------------------:|:--------------------------|:-------------------------------|:-------------------------|:----------------------------|:----------------------|------------:|
| A           | Current baseline monthly Top3 | monthly     |                3 | 79.61%         | 61.20%                   | 23.82% | 19.03%         | 4.79%         | 46.88%                        | 0.40%                           | -19.32%        |                    1.21875 |                    3.65625 | 14.31%                    | 2024-04                        | -10.59%                  | 2026-09                     | 18.63%                |          33 |
| B           | Weekly rebalance Top3         | weekly      |                3 | -6.71%         | 61.20%                   | -2.50% | 19.03%         | -21.53%       | 39.39%                        | -1.55%                          | -42.13%        |                    3.10101 |                    9.30303 | 21.29%                    | 2024-03                        | -12.42%                  | 2025-03                     | 12.41%                |         144 |
| C           | Weekly rebalance Top5         | weekly      |                5 | 8.20%          | 61.20%                   | 2.92%  | 19.03%         | -16.12%       | 42.42%                        | -1.16%                          | -36.45%        |                    2.78182 |                   13.9091  | 21.85%                    | 2024-08                        | -9.16%                   | 2026-09                     | 9.23%                 |         144 |
| D           | Relative Strength Top3        | weekly      |                3 | -3.42%         | 61.20%                   | -1.26% | 19.03%         | -20.30%       | 36.36%                        | -1.50%                          | -38.81%        |                    4.31313 |                   12.9394  | 31.74%                    | 2026-02                        | -14.58%                  | 2026-09                     | 9.26%                 |         144 |
| E           | Benchmark-aware Top3          | weekly      |                3 | -8.80%         | 61.20%                   | -3.31% | 19.03%         | -22.34%       | 33.33%                        | -1.69%                          | -39.49%        |                    4.31313 |                   12.9394  | 30.00%                    | 2026-02                        | -11.73%                  | 2026-09                     | 9.96%                 |         144 |
| F           | Leadership Rotation Overlay   | weekly      |                3 | -11.82%        | 61.20%                   | -4.48% | 19.03%         | -23.52%       | 39.39%                        | -1.72%                          | -42.16%        |                    4.19192 |                   12.5758  | 28.14%                    | 2026-02                        | -11.73%                  | 2026-09                     | 8.47%                 |         144 |

## Decision

- Did weekly rebalance improve excess return? Recent yes, historical no, so rejected. Historical excess CAGR delta vs baseline: -26.32%; recent excess delta: 4.47%.
- Did relative strength improve excess return? Recent yes, historical no, so rejected. Historical excess CAGR delta vs baseline: -25.09%; recent excess delta: 3.55%.
- Did benchmark-aware selection improve excess return? Recent yes, historical no, so rejected. Historical excess CAGR delta vs baseline: -27.13%; recent excess delta: 4.29%.
- Did any policy beat BIST100 robustly? No under the current acceptance filter.
- Next paper-trading candidate: none. No policy passed both historical and recent acceptance criteria.
- Current one-month fixed hold should be kept for tracking, while weekly/relative-strength variants remain research-only.

## Acceptance Rule

A policy is only eligible if it improves both historical walk-forward excess return and the recent 2026-06 counterfactual excess return. Policies that only fix June 2026 are rejected.
