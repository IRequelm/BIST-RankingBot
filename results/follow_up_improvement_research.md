# Follow-Up Improvement Research

This is research-only. Production follow-up tracking remains fixed and still reads reports/tracking_state.json.

## Policy Summary

| policy_id   | policy_name                   | frequency   |   portfolio_size | total_return   | benchmark_total_return   | cagr   | bist100_cagr   | excess_cagr   | monthly_win_rate_vs_bist100   | average_monthly_excess_return   | max_drawdown   |   average_monthly_turnover |   average_trades_per_month | transaction_cost_impact   | worst_underperformance_month   | worst_underperformance   | best_outperformance_month   | best_outperformance   |   intervals |
|:------------|:------------------------------|:------------|-----------------:|:---------------|:-------------------------|:-------|:---------------|:--------------|:------------------------------|:--------------------------------|:---------------|---------------------------:|---------------------------:|:--------------------------|:-------------------------------|:-------------------------|:----------------------------|:----------------------|------------:|
| A           | Current baseline monthly Top3 | monthly     |                3 | 48.83%         | 44.59%                   | 15.05% | 13.88%         | 1.17%         | 44.12%                        | 0.15%                           | -19.32%        |                    1.2451  |                    3.73529 | 12.99%                    | 2024-04                        | -10.59%                  | 2025-04                     | 15.27%                |          35 |
| B           | Weekly rebalance Top3         | weekly      |                3 | -23.78%        | 44.59%                   | -9.13% | 13.88%         | -23.01%       | 40.00%                        | -1.72%                          | -42.13%        |                    3.0381  |                    9.11429 | 18.18%                    | 2024-03                        | -12.42%                  | 2025-03                     | 12.41%                |         149 |
| C           | Weekly rebalance Top5         | weekly      |                5 | -2.92%         | 44.59%                   | -1.04% | 13.88%         | -14.92%       | 42.86%                        | -1.09%                          | -36.45%        |                    2.65714 |                   13.2857  | 19.89%                    | 2024-08                        | -9.16%                   | 2026-09                     | 6.85%                 |         149 |
| D           | Relative Strength Top3        | weekly      |                3 | -13.94%        | 44.59%                   | -5.16% | 13.88%         | -19.04%       | 37.14%                        | -1.43%                          | -40.05%        |                    4.21905 |                   12.6571  | 29.53%                    | 2026-02                        | -14.58%                  | 2026-08                     | 8.57%                 |         149 |
| E           | Benchmark-aware Top3          | weekly      |                3 | -19.78%        | 44.59%                   | -7.48% | 13.88%         | -21.36%       | 34.29%                        | -1.64%                          | -41.05%        |                    4.21905 |                   12.6571  | 27.56%                    | 2026-02                        | -11.73%                  | 2026-08                     | 8.57%                 |         149 |
| F           | Leadership Rotation Overlay   | weekly      |                3 | -21.91%        | 44.59%                   | -8.35% | 13.88%         | -22.23%       | 37.14%                        | -1.66%                          | -42.16%        |                    4.1619  |                   12.4857  | 26.46%                    | 2026-02                        | -11.73%                  | 2026-08                     | 8.44%                 |         149 |

## Decision

- Did weekly rebalance improve excess return? Recent yes, historical no, so rejected. Historical excess CAGR delta vs baseline: -24.18%; recent excess delta: 1.99%.
- Did relative strength improve excess return? Recent yes, historical no, so rejected. Historical excess CAGR delta vs baseline: -20.21%; recent excess delta: 8.73%.
- Did benchmark-aware selection improve excess return? Recent yes, historical no, so rejected. Historical excess CAGR delta vs baseline: -22.53%; recent excess delta: 8.22%.
- Did any policy beat BIST100 robustly? No under the current acceptance filter.
- Next paper-trading candidate: none. No policy passed both historical and recent acceptance criteria.
- Current one-month fixed hold should be kept for tracking, while weekly/relative-strength variants remain research-only.

## Acceptance Rule

A policy is only eligible if it improves both historical walk-forward excess return and the recent 2026-06 counterfactual excess return. Policies that only fix June 2026 are rejected.
