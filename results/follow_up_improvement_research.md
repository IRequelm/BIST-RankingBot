# Follow-Up Improvement Research

This is research-only. Production follow-up tracking remains fixed and still reads reports/tracking_state.json.

## Policy Summary

| policy_id   | policy_name                   | frequency   |   portfolio_size | total_return   | benchmark_total_return   | cagr   | bist100_cagr   | excess_cagr   | monthly_win_rate_vs_bist100   | average_monthly_excess_return   | max_drawdown   |   average_monthly_turnover |   average_trades_per_month | transaction_cost_impact   | worst_underperformance_month   | worst_underperformance   | best_outperformance_month   | best_outperformance   |   intervals |
|:------------|:------------------------------|:------------|-----------------:|:---------------|:-------------------------|:-------|:---------------|:--------------|:------------------------------|:--------------------------------|:---------------|---------------------------:|---------------------------:|:--------------------------|:-------------------------------|:-------------------------|:----------------------------|:----------------------|------------:|
| A           | Current baseline monthly Top3 | monthly     |                3 | 71.11%         | 89.59%                   | 24.00% | 29.20%         | -5.20%        | 43.33%                        | -0.27%                          | -19.32%        |                    1.23333 |                     3.7    | 12.89%                    | 2024-04                        | -10.59%                  | 2025-04                     | 15.27%                |          31 |
| B           | Weekly rebalance Top3         | weekly      |                3 | -9.18%         | 89.59%                   | -3.78% | 29.20%         | -32.98%       | 35.48%                        | -2.25%                          | -42.13%        |                    3.12903 |                     9.3871 | 19.53%                    | 2024-03                        | -12.42%                  | 2025-03                     | 12.41%                |         131 |
| C           | Weekly rebalance Top5         | weekly      |                5 | 16.73%         | 89.59%                   | 6.39%  | 29.20%         | -22.81%       | 38.71%                        | -1.49%                          | -36.45%        |                    2.69032 |                    13.4516 | 21.22%                    | 2024-08                        | -9.16%                   | 2026-03                     | 6.68%                 |         131 |
| D           | Relative Strength Top3        | weekly      |                3 | -3.03%         | 89.59%                   | -1.22% | 29.20%         | -30.42%       | 32.26%                        | -2.10%                          | -35.17%        |                    4.26882 |                    12.8065 | 29.31%                    | 2026-02                        | -14.58%                  | 2025-03                     | 6.67%                 |         131 |
| E           | Benchmark-aware Top3          | weekly      |                3 | -9.09%         | 89.59%                   | -3.74% | 29.20%         | -32.95%       | 29.03%                        | -2.33%                          | -38.70%        |                    4.29032 |                    12.871  | 27.67%                    | 2026-02                        | -11.73%                  | 2025-03                     | 6.25%                 |         131 |
| F           | Leadership Rotation Overlay   | weekly      |                3 | -11.83%        | 89.59%                   | -4.92% | 29.20%         | -34.12%       | 35.48%                        | -2.35%                          | -42.16%        |                    4.16129 |                    12.4839 | 25.96%                    | 2026-02                        | -11.73%                  | 2024-04                     | 7.40%                 |         131 |

## Decision

- Did weekly rebalance improve excess return? Recent yes, historical no, so rejected. Historical excess CAGR delta vs baseline: -27.78%; recent excess delta: 0.71%.
- Did relative strength improve excess return? Recent yes, historical no, so rejected. Historical excess CAGR delta vs baseline: -25.22%; recent excess delta: 2.91%.
- Did benchmark-aware selection improve excess return? Recent yes, historical no, so rejected. Historical excess CAGR delta vs baseline: -27.75%; recent excess delta: 2.91%.
- Did any policy beat BIST100 robustly? No under the current acceptance filter.
- Next paper-trading candidate: none. No policy passed both historical and recent acceptance criteria.
- Current one-month fixed hold should be kept for tracking, while weekly/relative-strength variants remain research-only.

## Acceptance Rule

A policy is only eligible if it improves both historical walk-forward excess return and the recent 2026-06 counterfactual excess return. Policies that only fix June 2026 are rejected.
