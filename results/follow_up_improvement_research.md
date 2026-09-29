# Follow-Up Improvement Research

This is research-only. Production follow-up tracking remains fixed and still reads reports/tracking_state.json.

## Policy Summary

| policy_id   | policy_name                   | frequency   |   portfolio_size | total_return   | benchmark_total_return   | cagr   | bist100_cagr   | excess_cagr   | monthly_win_rate_vs_bist100   | average_monthly_excess_return   | max_drawdown   |   average_monthly_turnover |   average_trades_per_month | transaction_cost_impact   | worst_underperformance_month   | worst_underperformance   | best_outperformance_month   | best_outperformance   |   intervals |
|:------------|:------------------------------|:------------|-----------------:|:---------------|:-------------------------|:-------|:---------------|:--------------|:------------------------------|:--------------------------------|:---------------|---------------------------:|---------------------------:|:--------------------------|:-------------------------------|:-------------------------|:----------------------------|:----------------------|------------:|
| A           | Current baseline monthly Top3 | monthly     |                3 | 82.41%         | 65.17%                   | 24.55% | 20.11%         | 4.44%         | 46.88%                        | 0.39%                           | -19.32%        |                    1.21875 |                    3.65625 | 14.53%                    | 2024-04                        | -10.59%                  | 2026-09                     | 18.09%                |          33 |
| B           | Weekly rebalance Top3         | weekly      |                3 | -5.88%         | 65.17%                   | -2.19% | 20.11%         | -22.30%       | 39.39%                        | -1.59%                          | -42.13%        |                    3.10101 |                    9.30303 | 21.47%                    | 2024-03                        | -12.42%                  | 2025-03                     | 12.41%                |         143 |
| C           | Weekly rebalance Top5         | weekly      |                5 | 9.27%          | 65.17%                   | 3.29%  | 20.11%         | -16.82%       | 42.42%                        | -1.19%                          | -36.45%        |                    2.7697  |                   13.8485  | 21.96%                    | 2024-08                        | -9.16%                   | 2026-09                     | 8.06%                 |         143 |
| D           | Relative Strength Top3        | weekly      |                3 | -2.43%         | 65.17%                   | -0.90% | 20.11%         | -21.01%       | 36.36%                        | -1.54%                          | -38.81%        |                    4.29293 |                   12.8788  | 31.89%                    | 2026-02                        | -14.58%                  | 2026-08                     | 8.57%                 |         143 |
| E           | Benchmark-aware Top3          | weekly      |                3 | -7.86%         | 65.17%                   | -2.95% | 20.11%         | -23.06%       | 33.33%                        | -1.72%                          | -39.49%        |                    4.29293 |                   12.8788  | 30.14%                    | 2026-02                        | -11.73%                  | 2026-09                     | 8.83%                 |         143 |
| F           | Leadership Rotation Overlay   | weekly      |                3 | -10.79%        | 65.17%                   | -4.08% | 20.11%         | -24.20%       | 39.39%                        | -1.75%                          | -42.16%        |                    4.15152 |                   12.4545  | 28.15%                    | 2026-02                        | -11.73%                  | 2026-08                     | 8.44%                 |         143 |

## Decision

- Did weekly rebalance improve excess return? Recent yes, historical no, so rejected. Historical excess CAGR delta vs baseline: -26.74%; recent excess delta: 4.68%.
- Did relative strength improve excess return? Recent yes, historical no, so rejected. Historical excess CAGR delta vs baseline: -25.45%; recent excess delta: 3.90%.
- Did benchmark-aware selection improve excess return? Recent yes, historical no, so rejected. Historical excess CAGR delta vs baseline: -27.50%; recent excess delta: 4.65%.
- Did any policy beat BIST100 robustly? No under the current acceptance filter.
- Next paper-trading candidate: none. No policy passed both historical and recent acceptance criteria.
- Current one-month fixed hold should be kept for tracking, while weekly/relative-strength variants remain research-only.

## Acceptance Rule

A policy is only eligible if it improves both historical walk-forward excess return and the recent 2026-06 counterfactual excess return. Policies that only fix June 2026 are rejected.
