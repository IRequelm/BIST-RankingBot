# Follow-Up Improvement Research

This is research-only. Production follow-up tracking remains fixed and still reads reports/tracking_state.json.

## Policy Summary

| policy_id   | policy_name                   | frequency   |   portfolio_size | total_return   | benchmark_total_return   | cagr   | bist100_cagr   | excess_cagr   | monthly_win_rate_vs_bist100   | average_monthly_excess_return   | max_drawdown   |   average_monthly_turnover |   average_trades_per_month | transaction_cost_impact   | worst_underperformance_month   | worst_underperformance   | best_outperformance_month   | best_outperformance   |   intervals |
|:------------|:------------------------------|:------------|-----------------:|:---------------|:-------------------------|:-------|:---------------|:--------------|:------------------------------|:--------------------------------|:---------------|---------------------------:|---------------------------:|:--------------------------|:-------------------------------|:-------------------------|:----------------------------|:----------------------|------------:|
| A           | Current baseline monthly Top3 | monthly     |                3 | 68.27%         | 58.31%                   | 20.55% | 17.94%         | 2.61%         | 45.45%                        | 0.24%                           | -19.32%        |                    1.24242 |                    3.72727 | 14.17%                    | 2024-04                        | -10.59%                  | 2025-04                     | 15.27%                |          34 |
| B           | Weekly rebalance Top3         | weekly      |                3 | -14.24%        | 58.31%                   | -5.37% | 17.94%         | -23.30%       | 41.18%                        | -1.68%                          | -42.13%        |                    3.06863 |                    9.20588 | 20.01%                    | 2024-03                        | -12.42%                  | 2025-03                     | 12.41%                |         146 |
| C           | Weekly rebalance Top5         | weekly      |                5 | 8.37%          | 58.31%                   | 2.93%  | 17.94%         | -15.01%       | 44.12%                        | -1.06%                          | -36.45%        |                    2.67647 |                   13.3824  | 21.67%                    | 2024-08                        | -9.16%                   | 2026-09                     | 6.85%                 |         146 |
| D           | Relative Strength Top3        | weekly      |                3 | -10.23%        | 58.31%                   | -3.80% | 17.94%         | -21.74%       | 35.29%                        | -1.60%                          | -38.81%        |                    4.28431 |                   12.8529  | 30.31%                    | 2026-02                        | -14.58%                  | 2026-08                     | 8.57%                 |         146 |
| E           | Benchmark-aware Top3          | weekly      |                3 | -16.21%        | 58.31%                   | -6.16% | 17.94%         | -24.09%       | 32.35%                        | -1.82%                          | -40.42%        |                    4.26471 |                   12.7941  | 28.18%                    | 2026-02                        | -11.73%                  | 2026-08                     | 8.57%                 |         146 |
| F           | Leadership Rotation Overlay   | weekly      |                3 | -17.49%        | 58.31%                   | -6.67% | 17.94%         | -24.61%       | 35.29%                        | -1.80%                          | -42.16%        |                    4.20588 |                   12.6176  | 27.36%                    | 2026-02                        | -11.73%                  | 2026-08                     | 8.44%                 |         146 |

## Decision

- Did weekly rebalance improve excess return? No. Historical excess CAGR delta vs baseline: -25.92%; recent excess delta: -1.08%.
- Did relative strength improve excess return? No. Historical excess CAGR delta vs baseline: -24.35%; recent excess delta: -0.88%.
- Did benchmark-aware selection improve excess return? No. Historical excess CAGR delta vs baseline: -26.71%; recent excess delta: -1.29%.
- Did any policy beat BIST100 robustly? No under the current acceptance filter.
- Next paper-trading candidate: none. No policy passed both historical and recent acceptance criteria.
- Current one-month fixed hold should be kept for tracking, while weekly/relative-strength variants remain research-only.

## Acceptance Rule

A policy is only eligible if it improves both historical walk-forward excess return and the recent 2026-06 counterfactual excess return. Policies that only fix June 2026 are rejected.
