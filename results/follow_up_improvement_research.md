# Follow-Up Improvement Research

This is research-only. Production follow-up tracking remains fixed and still reads reports/tracking_state.json.

## Policy Summary

| policy_id   | policy_name                   | frequency   |   portfolio_size | total_return   | benchmark_total_return   | cagr   | bist100_cagr   | excess_cagr   | monthly_win_rate_vs_bist100   | average_monthly_excess_return   | max_drawdown   |   average_monthly_turnover |   average_trades_per_month | transaction_cost_impact   | worst_underperformance_month   | worst_underperformance   | best_outperformance_month   | best_outperformance   |   intervals |
|:------------|:------------------------------|:------------|-----------------:|:---------------|:-------------------------|:-------|:---------------|:--------------|:------------------------------|:--------------------------------|:---------------|---------------------------:|---------------------------:|:--------------------------|:-------------------------------|:-------------------------|:----------------------------|:----------------------|------------:|
| A           | Current baseline monthly Top3 | monthly     |                3 | 75.47%         | 63.21%                   | 22.62% | 19.45%         | 3.18%         | 48.48%                        | 0.28%                           | -19.32%        |                    1.20202 |                    3.60606 | 14.24%                    | 2024-04                        | -10.59%                  | 2025-04                     | 15.27%                |          34 |
| B           | Weekly rebalance Top3         | weekly      |                3 | -9.80%         | 63.21%                   | -3.67% | 19.45%         | -23.12%       | 38.24%                        | -1.63%                          | -42.13%        |                    3.0098  |                    9.02941 | 20.58%                    | 2024-03                        | -12.42%                  | 2025-03                     | 12.41%                |         144 |
| C           | Weekly rebalance Top5         | weekly      |                5 | 3.95%          | 63.21%                   | 1.41%  | 19.45%         | -18.03%       | 41.18%                        | -1.27%                          | -36.45%        |                    2.7     |                   13.5     | 20.99%                    | 2024-08                        | -9.16%                   | 2026-09                     | 7.20%                 |         144 |
| D           | Relative Strength Top3        | weekly      |                3 | -7.71%         | 63.21%                   | -2.87% | 19.45%         | -22.31%       | 35.29%                        | -1.62%                          | -38.81%        |                    4.18627 |                   12.5588  | 30.34%                    | 2026-02                        | -14.58%                  | 2026-08                     | 8.57%                 |         144 |
| E           | Benchmark-aware Top3          | weekly      |                3 | -12.85%        | 63.21%                   | -4.87% | 19.45%         | -24.31%       | 32.35%                        | -1.80%                          | -39.49%        |                    4.18627 |                   12.5588  | 28.68%                    | 2026-02                        | -11.73%                  | 2026-08                     | 8.57%                 |         144 |
| F           | Leadership Rotation Overlay   | weekly      |                3 | -13.64%        | 63.21%                   | -5.18% | 19.45%         | -24.63%       | 38.24%                        | -1.76%                          | -42.16%        |                    4.06863 |                   12.2059  | 27.57%                    | 2026-02                        | -11.73%                  | 2026-08                     | 8.44%                 |         144 |

## Decision

- Did weekly rebalance improve excess return? Recent yes, historical no, so rejected. Historical excess CAGR delta vs baseline: -26.29%; recent excess delta: 3.45%.
- Did relative strength improve excess return? Recent yes, historical no, so rejected. Historical excess CAGR delta vs baseline: -25.49%; recent excess delta: 1.43%.
- Did benchmark-aware selection improve excess return? Recent yes, historical no, so rejected. Historical excess CAGR delta vs baseline: -27.49%; recent excess delta: 2.13%.
- Did any policy beat BIST100 robustly? No under the current acceptance filter.
- Next paper-trading candidate: none. No policy passed both historical and recent acceptance criteria.
- Current one-month fixed hold should be kept for tracking, while weekly/relative-strength variants remain research-only.

## Acceptance Rule

A policy is only eligible if it improves both historical walk-forward excess return and the recent 2026-06 counterfactual excess return. Policies that only fix June 2026 are rejected.
