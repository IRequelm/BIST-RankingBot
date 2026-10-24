# Follow-Up Improvement Research

This is research-only. Production follow-up tracking remains fixed and still reads reports/tracking_state.json.

## Policy Summary

| policy_id   | policy_name                   | frequency   |   portfolio_size | total_return   | benchmark_total_return   | cagr   | bist100_cagr   | excess_cagr   | monthly_win_rate_vs_bist100   | average_monthly_excess_return   | max_drawdown   |   average_monthly_turnover |   average_trades_per_month | transaction_cost_impact   | worst_underperformance_month   | worst_underperformance   | best_outperformance_month   | best_outperformance   |   intervals |
|:------------|:------------------------------|:------------|-----------------:|:---------------|:-------------------------|:-------|:---------------|:--------------|:------------------------------|:--------------------------------|:---------------|---------------------------:|---------------------------:|:--------------------------|:-------------------------------|:-------------------------|:----------------------------|:----------------------|------------:|
| A           | Current baseline monthly Top3 | monthly     |                3 | 53.32%         | 45.81%                   | 16.45% | 14.38%         | 2.07%         | 45.45%                        | 0.19%                           | -19.32%        |                    1.24242 |                    3.72727 | 12.93%                    | 2024-04                        | -10.59%                  | 2025-04                     | 15.27%                |          34 |
| B           | Weekly rebalance Top3         | weekly      |                3 | -21.30%        | 45.81%                   | -8.18% | 14.38%         | -22.57%       | 41.18%                        | -1.70%                          | -42.13%        |                    3.08824 |                    9.26471 | 18.51%                    | 2024-03                        | -12.42%                  | 2025-03                     | 12.41%                |         147 |
| C           | Weekly rebalance Top5         | weekly      |                5 | 0.20%          | 45.81%                   | 0.07%  | 14.38%         | -14.31%       | 44.12%                        | -1.05%                          | -36.45%        |                    2.68824 |                   13.4412  | 20.14%                    | 2024-08                        | -9.16%                   | 2026-09                     | 6.85%                 |         147 |
| D           | Relative Strength Top3        | weekly      |                3 | -11.78%        | 45.81%                   | -4.37% | 14.38%         | -18.75%       | 38.24%                        | -1.43%                          | -38.81%        |                    4.30392 |                   12.9118  | 29.95%                    | 2026-02                        | -14.58%                  | 2026-08                     | 8.57%                 |         147 |
| E           | Benchmark-aware Top3          | weekly      |                3 | -17.66%        | 45.81%                   | -6.69% | 14.38%         | -21.07%       | 35.29%                        | -1.64%                          | -40.42%        |                    4.28431 |                   12.8529  | 27.85%                    | 2026-02                        | -11.73%                  | 2026-08                     | 8.57%                 |         147 |
| F           | Leadership Rotation Overlay   | weekly      |                3 | -20.47%        | 45.81%                   | -7.84% | 14.38%         | -22.22%       | 38.24%                        | -1.68%                          | -42.16%        |                    4.22549 |                   12.6765  | 26.52%                    | 2026-02                        | -11.73%                  | 2026-08                     | 8.44%                 |         147 |

## Decision

- Did weekly rebalance improve excess return? No. Historical excess CAGR delta vs baseline: -24.63%; recent excess delta: -1.18%.
- Did relative strength improve excess return? Recent yes, historical no, so rejected. Historical excess CAGR delta vs baseline: -20.82%; recent excess delta: 5.11%.
- Did benchmark-aware selection improve excess return? Recent yes, historical no, so rejected. Historical excess CAGR delta vs baseline: -23.14%; recent excess delta: 4.71%.
- Did any policy beat BIST100 robustly? No under the current acceptance filter.
- Next paper-trading candidate: none. No policy passed both historical and recent acceptance criteria.
- Current one-month fixed hold should be kept for tracking, while weekly/relative-strength variants remain research-only.

## Acceptance Rule

A policy is only eligible if it improves both historical walk-forward excess return and the recent 2026-06 counterfactual excess return. Policies that only fix June 2026 are rejected.
