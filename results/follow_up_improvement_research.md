# Follow-Up Improvement Research

This is research-only. Production follow-up tracking remains fixed and still reads reports/tracking_state.json.

## Policy Summary

| policy_id   | policy_name                   | frequency   |   portfolio_size | total_return   | benchmark_total_return   | cagr   | bist100_cagr   | excess_cagr   | monthly_win_rate_vs_bist100   | average_monthly_excess_return   | max_drawdown   |   average_monthly_turnover |   average_trades_per_month | transaction_cost_impact   | worst_underperformance_month   | worst_underperformance   | best_outperformance_month   | best_outperformance   |   intervals |
|:------------|:------------------------------|:------------|-----------------:|:---------------|:-------------------------|:-------|:---------------|:--------------|:------------------------------|:--------------------------------|:---------------|---------------------------:|---------------------------:|:--------------------------|:-------------------------------|:-------------------------|:----------------------------|:----------------------|------------:|
| A           | Current baseline monthly Top3 | monthly     |                3 | 79.85%         | 62.30%                   | 23.70% | 19.18%         | 4.52%         | 48.48%                        | 0.37%                           | -19.32%        |                    1.20202 |                    3.60606 | 14.59%                    | 2024-04                        | -10.59%                  | 2025-04                     | 15.27%                |          34 |
| B           | Weekly rebalance Top3         | weekly      |                3 | -7.65%         | 62.30%                   | -2.84% | 19.18%         | -22.02%       | 41.18%                        | -1.55%                          | -42.13%        |                    3.02941 |                    9.08824 | 21.22%                    | 2024-03                        | -12.42%                  | 2025-03                     | 12.41%                |         145 |
| C           | Weekly rebalance Top5         | weekly      |                5 | 6.63%          | 62.30%                   | 2.35%  | 19.18%         | -16.83%       | 44.12%                        | -1.18%                          | -36.45%        |                    2.71176 |                   13.5588  | 21.63%                    | 2024-08                        | -9.16%                   | 2026-09                     | 7.20%                 |         145 |
| D           | Relative Strength Top3        | weekly      |                3 | -6.02%         | 62.30%                   | -2.22% | 19.18%         | -21.41%       | 35.29%                        | -1.55%                          | -38.81%        |                    4.20588 |                   12.6176  | 31.06%                    | 2026-02                        | -14.58%                  | 2026-08                     | 8.57%                 |         145 |
| E           | Benchmark-aware Top3          | weekly      |                3 | -11.25%        | 62.30%                   | -4.23% | 19.18%         | -23.41%       | 32.35%                        | -1.73%                          | -39.49%        |                    4.20588 |                   12.6176  | 29.36%                    | 2026-02                        | -11.73%                  | 2026-08                     | 8.57%                 |         145 |
| F           | Leadership Rotation Overlay   | weekly      |                3 | -11.96%        | 62.30%                   | -4.51% | 19.18%         | -23.69%       | 41.18%                        | -1.69%                          | -42.16%        |                    4.08824 |                   12.2647  | 28.25%                    | 2026-02                        | -11.73%                  | 2026-08                     | 8.44%                 |         145 |

## Decision

- Did weekly rebalance improve excess return? Recent yes, historical no, so rejected. Historical excess CAGR delta vs baseline: -26.54%; recent excess delta: 4.68%.
- Did relative strength improve excess return? Recent yes, historical no, so rejected. Historical excess CAGR delta vs baseline: -25.92%; recent excess delta: 2.08%.
- Did benchmark-aware selection improve excess return? Recent yes, historical no, so rejected. Historical excess CAGR delta vs baseline: -27.93%; recent excess delta: 2.80%.
- Did any policy beat BIST100 robustly? No under the current acceptance filter.
- Next paper-trading candidate: none. No policy passed both historical and recent acceptance criteria.
- Current one-month fixed hold should be kept for tracking, while weekly/relative-strength variants remain research-only.

## Acceptance Rule

A policy is only eligible if it improves both historical walk-forward excess return and the recent 2026-06 counterfactual excess return. Policies that only fix June 2026 are rejected.
