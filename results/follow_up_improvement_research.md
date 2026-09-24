# Follow-Up Improvement Research

This is research-only. Production follow-up tracking remains fixed and still reads reports/tracking_state.json.

## Policy Summary

| policy_id   | policy_name                   | frequency   |   portfolio_size | total_return   | benchmark_total_return   | cagr   | bist100_cagr   | excess_cagr   | monthly_win_rate_vs_bist100   | average_monthly_excess_return   | max_drawdown   |   average_monthly_turnover |   average_trades_per_month | transaction_cost_impact   | worst_underperformance_month   | worst_underperformance   | best_outperformance_month   | best_outperformance   |   intervals |
|:------------|:------------------------------|:------------|-----------------:|:---------------|:-------------------------|:-------|:---------------|:--------------|:------------------------------|:--------------------------------|:---------------|---------------------------:|---------------------------:|:--------------------------|:-------------------------------|:-------------------------|:----------------------------|:----------------------|------------:|
| A           | Current baseline monthly Top3 | monthly     |                3 | 84.27%         | 73.81%                   | 25.15% | 22.50%         | 2.66%         | 46.88%                        | 0.27%                           | -19.32%        |                    1.21875 |                    3.65625 | 14.67%                    | 2024-04                        | -10.59%                  | 2025-04                     | 15.27%                |          33 |
| B           | Weekly rebalance Top3         | weekly      |                3 | -5.50%         | 73.81%                   | -2.06% | 22.50%         | -24.55%       | 39.39%                        | -1.72%                          | -42.13%        |                    3.10101 |                    9.30303 | 21.56%                    | 2024-03                        | -12.42%                  | 2025-03                     | 12.41%                |         143 |
| C           | Weekly rebalance Top5         | weekly      |                5 | 10.94%         | 73.81%                   | 3.88%  | 22.50%         | -18.61%       | 42.42%                        | -1.29%                          | -36.45%        |                    2.7697  |                   13.8485  | 22.29%                    | 2024-08                        | -9.16%                   | 2026-03                     | 6.68%                 |         143 |
| D           | Relative Strength Top3        | weekly      |                3 | -2.04%         | 73.81%                   | -0.75% | 22.50%         | -23.25%       | 36.36%                        | -1.66%                          | -38.81%        |                    4.29293 |                   12.8788  | 32.02%                    | 2026-02                        | -14.58%                  | 2026-08                     | 8.57%                 |         143 |
| E           | Benchmark-aware Top3          | weekly      |                3 | -7.50%         | 73.81%                   | -2.82% | 22.50%         | -25.32%       | 33.33%                        | -1.85%                          | -39.49%        |                    4.29293 |                   12.8788  | 30.26%                    | 2026-02                        | -11.73%                  | 2026-08                     | 8.57%                 |         143 |
| F           | Leadership Rotation Overlay   | weekly      |                3 | -10.43%        | 73.81%                   | -3.96% | 22.50%         | -26.46%       | 39.39%                        | -1.88%                          | -42.16%        |                    4.15152 |                   12.4545  | 28.26%                    | 2026-02                        | -11.73%                  | 2026-08                     | 8.44%                 |         143 |

## Decision

- Did weekly rebalance improve excess return? Recent yes, historical no, so rejected. Historical excess CAGR delta vs baseline: -27.21%; recent excess delta: 3.79%.
- Did relative strength improve excess return? Recent yes, historical no, so rejected. Historical excess CAGR delta vs baseline: -25.91%; recent excess delta: 3.00%.
- Did benchmark-aware selection improve excess return? Recent yes, historical no, so rejected. Historical excess CAGR delta vs baseline: -27.97%; recent excess delta: 3.75%.
- Did any policy beat BIST100 robustly? No under the current acceptance filter.
- Next paper-trading candidate: none. No policy passed both historical and recent acceptance criteria.
- Current one-month fixed hold should be kept for tracking, while weekly/relative-strength variants remain research-only.

## Acceptance Rule

A policy is only eligible if it improves both historical walk-forward excess return and the recent 2026-06 counterfactual excess return. Policies that only fix June 2026 are rejected.
