# Follow-Up Improvement Research

This is research-only. Production follow-up tracking remains fixed and still reads reports/tracking_state.json.

## Policy Summary

| policy_id   | policy_name                   | frequency   |   portfolio_size | total_return   | benchmark_total_return   | cagr   | bist100_cagr   | excess_cagr   | monthly_win_rate_vs_bist100   | average_monthly_excess_return   | max_drawdown   |   average_monthly_turnover |   average_trades_per_month | transaction_cost_impact   | worst_underperformance_month   | worst_underperformance   | best_outperformance_month   | best_outperformance   |   intervals |
|:------------|:------------------------------|:------------|-----------------:|:---------------|:-------------------------|:-------|:---------------|:--------------|:------------------------------|:--------------------------------|:---------------|---------------------------:|---------------------------:|:--------------------------|:-------------------------------|:-------------------------|:----------------------------|:----------------------|------------:|
| A           | Current baseline monthly Top3 | monthly     |                3 | 90.91%         | 88.79%                   | 27.19% | 26.66%         | 0.53%         | 46.88%                        | 0.13%                           | -19.32%        |                    1.21875 |                    3.65625 | 15.18%                    | 2024-04                        | -10.59%                  | 2025-04                     | 15.27%                |          33 |
| B           | Weekly rebalance Top3         | weekly      |                3 | -0.02%         | 88.79%                   | -0.01% | 26.66%         | -26.67%       | 39.39%                        | -1.79%                          | -42.13%        |                    3.08081 |                    9.24242 | 22.63%                    | 2024-03                        | -12.42%                  | 2025-03                     | 12.41%                |         141 |
| C           | Weekly rebalance Top5         | weekly      |                5 | 17.70%         | 88.79%                   | 6.25%  | 26.66%         | -20.42%       | 42.42%                        | -1.35%                          | -36.45%        |                    2.70909 |                   13.5455  | 23.07%                    | 2024-08                        | -9.16%                   | 2026-03                     | 6.68%                 |         141 |
| D           | Relative Strength Top3        | weekly      |                3 | 5.07%          | 88.79%                   | 1.86%  | 26.66%         | -24.81%       | 36.36%                        | -1.69%                          | -38.81%        |                    4.19192 |                   12.5758  | 33.39%                    | 2026-02                        | -14.58%                  | 2026-08                     | 8.57%                 |         141 |
| E           | Benchmark-aware Top3          | weekly      |                3 | -1.85%         | 88.79%                   | -0.69% | 26.66%         | -27.35%       | 33.33%                        | -1.91%                          | -39.49%        |                    4.23232 |                   12.697   | 31.58%                    | 2026-02                        | -11.73%                  | 2026-08                     | 8.57%                 |         141 |
| F           | Leadership Rotation Overlay   | weekly      |                3 | -3.47%         | 88.79%                   | -1.30% | 26.66%         | -27.97%       | 39.39%                        | -1.89%                          | -42.16%        |                    4.07071 |                   12.2121  | 29.76%                    | 2026-02                        | -11.73%                  | 2026-08                     | 8.44%                 |         141 |

## Decision

- Did weekly rebalance improve excess return? Recent yes, historical no, so rejected. Historical excess CAGR delta vs baseline: -27.20%; recent excess delta: 5.60%.
- Did relative strength improve excess return? Recent yes, historical no, so rejected. Historical excess CAGR delta vs baseline: -25.33%; recent excess delta: 6.27%.
- Did benchmark-aware selection improve excess return? Recent yes, historical no, so rejected. Historical excess CAGR delta vs baseline: -27.88%; recent excess delta: 5.88%.
- Did any policy beat BIST100 robustly? No under the current acceptance filter.
- Next paper-trading candidate: none. No policy passed both historical and recent acceptance criteria.
- Current one-month fixed hold should be kept for tracking, while weekly/relative-strength variants remain research-only.

## Acceptance Rule

A policy is only eligible if it improves both historical walk-forward excess return and the recent 2026-06 counterfactual excess return. Policies that only fix June 2026 are rejected.
