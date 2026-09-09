# Follow-Up Improvement Research

This is research-only. Production follow-up tracking remains fixed and still reads reports/tracking_state.json.

## Policy Summary

| policy_id   | policy_name                   | frequency   |   portfolio_size | total_return   | benchmark_total_return   | cagr   | bist100_cagr   | excess_cagr   | monthly_win_rate_vs_bist100   | average_monthly_excess_return   | max_drawdown   |   average_monthly_turnover |   average_trades_per_month | transaction_cost_impact   | worst_underperformance_month   | worst_underperformance   | best_outperformance_month   | best_outperformance   |   intervals |
|:------------|:------------------------------|:------------|-----------------:|:---------------|:-------------------------|:-------|:---------------|:--------------|:------------------------------|:--------------------------------|:---------------|---------------------------:|---------------------------:|:--------------------------|:-------------------------------|:-------------------------|:----------------------------|:----------------------|------------:|
| A           | Current baseline monthly Top3 | monthly     |                3 | 82.20%         | 88.94%                   | 25.06% | 26.76%         | -1.70%        | 46.88%                        | -0.04%                          | -19.32%        |                    1.21875 |                    3.65625 | 14.51%                    | 2024-04                        | -10.59%                  | 2025-04                     | 15.27%                |          33 |
| B           | Weekly rebalance Top3         | weekly      |                3 | -4.32%         | 88.94%                   | -1.63% | 26.76%         | -28.39%       | 36.36%                        | -1.92%                          | -42.13%        |                    3.08081 |                    9.24242 | 21.66%                    | 2024-03                        | -12.42%                  | 2025-03                     | 12.41%                |         141 |
| C           | Weekly rebalance Top5         | weekly      |                5 | 12.68%         | 88.94%                   | 4.55%  | 26.76%         | -22.21%       | 39.39%                        | -1.48%                          | -36.45%        |                    2.70909 |                   13.5455  | 22.08%                    | 2024-08                        | -9.16%                   | 2026-03                     | 6.68%                 |         141 |
| D           | Relative Strength Top3        | weekly      |                3 | 0.56%          | 88.94%                   | 0.21%  | 26.76%         | -26.55%       | 33.33%                        | -1.83%                          | -38.81%        |                    4.19192 |                   12.5758  | 31.96%                    | 2026-02                        | -14.58%                  | 2026-08                     | 8.57%                 |         141 |
| E           | Benchmark-aware Top3          | weekly      |                3 | -6.06%         | 88.94%                   | -2.30% | 26.76%         | -29.07%       | 30.30%                        | -2.05%                          | -39.49%        |                    4.23232 |                   12.697   | 30.23%                    | 2026-02                        | -11.73%                  | 2026-08                     | 8.57%                 |         141 |
| F           | Leadership Rotation Overlay   | weekly      |                3 | -7.61%         | 88.94%                   | -2.91% | 26.76%         | -29.67%       | 36.36%                        | -2.03%                          | -42.16%        |                    4.07071 |                   12.2121  | 28.49%                    | 2026-02                        | -11.73%                  | 2026-08                     | 8.44%                 |         141 |

## Decision

- Did weekly rebalance improve excess return? Recent yes, historical no, so rejected. Historical excess CAGR delta vs baseline: -26.69%; recent excess delta: 7.76%.
- Did relative strength improve excess return? Recent yes, historical no, so rejected. Historical excess CAGR delta vs baseline: -24.85%; recent excess delta: 8.40%.
- Did benchmark-aware selection improve excess return? Recent yes, historical no, so rejected. Historical excess CAGR delta vs baseline: -27.36%; recent excess delta: 8.03%.
- Did any policy beat BIST100 robustly? No under the current acceptance filter.
- Next paper-trading candidate: none. No policy passed both historical and recent acceptance criteria.
- Current one-month fixed hold should be kept for tracking, while weekly/relative-strength variants remain research-only.

## Acceptance Rule

A policy is only eligible if it improves both historical walk-forward excess return and the recent 2026-06 counterfactual excess return. Policies that only fix June 2026 are rejected.
