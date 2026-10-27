# Follow-Up Improvement Research

This is research-only. Production follow-up tracking remains fixed and still reads reports/tracking_state.json.

## Policy Summary

| policy_id   | policy_name                   | frequency   |   portfolio_size | total_return   | benchmark_total_return   | cagr   | bist100_cagr   | excess_cagr   | monthly_win_rate_vs_bist100   | average_monthly_excess_return   | max_drawdown   |   average_monthly_turnover |   average_trades_per_month | transaction_cost_impact   | worst_underperformance_month   | worst_underperformance   | best_outperformance_month   | best_outperformance   |   intervals |
|:------------|:------------------------------|:------------|-----------------:|:---------------|:-------------------------|:-------|:---------------|:--------------|:------------------------------|:--------------------------------|:---------------|---------------------------:|---------------------------:|:--------------------------|:-------------------------------|:-------------------------|:----------------------------|:----------------------|------------:|
| A           | Current baseline monthly Top3 | monthly     |                3 | 55.47%         | 46.27%                   | 16.97% | 14.47%         | 2.51%         | 45.45%                        | 0.22%                           | -19.32%        |                    1.24242 |                    3.72727 | 13.11%                    | 2024-04                        | -10.59%                  | 2025-04                     | 15.27%                |          34 |
| B           | Weekly rebalance Top3         | weekly      |                3 | -21.23%        | 46.27%                   | -8.13% | 14.47%         | -22.60%       | 41.18%                        | -1.70%                          | -42.13%        |                    3.08824 |                    9.26471 | 18.52%                    | 2024-03                        | -12.42%                  | 2025-03                     | 12.41%                |         147 |
| C           | Weekly rebalance Top5         | weekly      |                5 | -0.19%         | 46.27%                   | -0.07% | 14.47%         | -14.53%       | 44.12%                        | -1.07%                          | -36.45%        |                    2.68824 |                   13.4412  | 20.06%                    | 2024-08                        | -9.16%                   | 2026-09                     | 6.85%                 |         147 |
| D           | Relative Strength Top3        | weekly      |                3 | -12.95%        | 46.27%                   | -4.81% | 14.47%         | -19.27%       | 38.24%                        | -1.47%                          | -39.36%        |                    4.30392 |                   12.9118  | 29.56%                    | 2026-02                        | -14.58%                  | 2026-08                     | 8.57%                 |         147 |
| E           | Benchmark-aware Top3          | weekly      |                3 | -18.75%        | 46.27%                   | -7.11% | 14.47%         | -21.58%       | 35.29%                        | -1.69%                          | -40.42%        |                    4.28431 |                   12.8529  | 27.48%                    | 2026-02                        | -11.73%                  | 2026-08                     | 8.57%                 |         147 |
| F           | Leadership Rotation Overlay   | weekly      |                3 | -21.18%        | 46.27%                   | -8.11% | 14.47%         | -22.57%       | 38.24%                        | -1.71%                          | -42.16%        |                    4.22549 |                   12.6765  | 26.28%                    | 2026-02                        | -11.73%                  | 2026-08                     | 8.44%                 |         147 |

## Decision

- Did weekly rebalance improve excess return? Recent yes, historical no, so rejected. Historical excess CAGR delta vs baseline: -25.10%; recent excess delta: 1.60%.
- Did relative strength improve excess return? Recent yes, historical no, so rejected. Historical excess CAGR delta vs baseline: -21.78%; recent excess delta: 6.59%.
- Did benchmark-aware selection improve excess return? Recent yes, historical no, so rejected. Historical excess CAGR delta vs baseline: -24.08%; recent excess delta: 6.20%.
- Did any policy beat BIST100 robustly? No under the current acceptance filter.
- Next paper-trading candidate: none. No policy passed both historical and recent acceptance criteria.
- Current one-month fixed hold should be kept for tracking, while weekly/relative-strength variants remain research-only.

## Acceptance Rule

A policy is only eligible if it improves both historical walk-forward excess return and the recent 2026-06 counterfactual excess return. Policies that only fix June 2026 are rejected.
