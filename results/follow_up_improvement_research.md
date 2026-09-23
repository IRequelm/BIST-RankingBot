# Follow-Up Improvement Research

This is research-only. Production follow-up tracking remains fixed and still reads reports/tracking_state.json.

## Policy Summary

| policy_id   | policy_name                   | frequency   |   portfolio_size | total_return   | benchmark_total_return   | cagr   | bist100_cagr   | excess_cagr   | monthly_win_rate_vs_bist100   | average_monthly_excess_return   | max_drawdown   |   average_monthly_turnover |   average_trades_per_month | transaction_cost_impact   | worst_underperformance_month   | worst_underperformance   | best_outperformance_month   | best_outperformance   |   intervals |
|:------------|:------------------------------|:------------|-----------------:|:---------------|:-------------------------|:-------|:---------------|:--------------|:------------------------------|:--------------------------------|:---------------|---------------------------:|---------------------------:|:--------------------------|:-------------------------------|:-------------------------|:----------------------------|:----------------------|------------:|
| A           | Current baseline monthly Top3 | monthly     |                3 | 86.94%         | 74.94%                   | 25.87% | 22.84%         | 3.03%         | 46.88%                        | 0.30%                           | -19.32%        |                    1.21875 |                    3.65625 | 14.87%                    | 2024-04                        | -10.59%                  | 2026-09                     | 15.32%                |          33 |
| B           | Weekly rebalance Top3         | weekly      |                3 | -3.62%         | 74.94%                   | -1.35% | 22.84%         | -24.19%       | 39.39%                        | -1.68%                          | -42.13%        |                    3.08081 |                    9.24242 | 21.83%                    | 2024-03                        | -12.42%                  | 2025-03                     | 12.41%                |         142 |
| C           | Weekly rebalance Top5         | weekly      |                5 | 12.15%         | 74.94%                   | 4.31%  | 22.84%         | -18.53%       | 42.42%                        | -1.27%                          | -36.45%        |                    2.73333 |                   13.6667  | 22.20%                    | 2024-08                        | -9.16%                   | 2026-03                     | 6.68%                 |         142 |
| D           | Relative Strength Top3        | weekly      |                3 | 0.04%          | 74.94%                   | 0.02%  | 22.84%         | -22.82%       | 36.36%                        | -1.62%                          | -38.81%        |                    4.25253 |                   12.7576  | 32.34%                    | 2026-02                        | -14.58%                  | 2026-08                     | 8.57%                 |         142 |
| E           | Benchmark-aware Top3          | weekly      |                3 | -5.53%         | 74.94%                   | -2.07% | 22.84%         | -24.91%       | 33.33%                        | -1.81%                          | -39.49%        |                    4.25253 |                   12.7576  | 30.57%                    | 2026-02                        | -11.73%                  | 2026-08                     | 8.57%                 |         142 |
| F           | Leadership Rotation Overlay   | weekly      |                3 | -8.53%         | 74.94%                   | -3.23% | 22.84%         | -26.06%       | 39.39%                        | -1.84%                          | -42.16%        |                    4.11111 |                   12.3333  | 28.54%                    | 2026-02                        | -11.73%                  | 2026-08                     | 8.44%                 |         142 |

## Decision

- Did weekly rebalance improve excess return? Recent yes, historical no, so rejected. Historical excess CAGR delta vs baseline: -27.22%; recent excess delta: 5.89%.
- Did relative strength improve excess return? Recent yes, historical no, so rejected. Historical excess CAGR delta vs baseline: -25.86%; recent excess delta: 5.23%.
- Did benchmark-aware selection improve excess return? Recent yes, historical no, so rejected. Historical excess CAGR delta vs baseline: -27.94%; recent excess delta: 5.99%.
- Did any policy beat BIST100 robustly? No under the current acceptance filter.
- Next paper-trading candidate: none. No policy passed both historical and recent acceptance criteria.
- Current one-month fixed hold should be kept for tracking, while weekly/relative-strength variants remain research-only.

## Acceptance Rule

A policy is only eligible if it improves both historical walk-forward excess return and the recent 2026-06 counterfactual excess return. Policies that only fix June 2026 are rejected.
