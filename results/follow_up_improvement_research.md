# Follow-Up Improvement Research

This is research-only. Production follow-up tracking remains fixed and still reads reports/tracking_state.json.

## Policy Summary

| policy_id   | policy_name                   | frequency   |   portfolio_size | total_return   | benchmark_total_return   | cagr   | bist100_cagr   | excess_cagr   | monthly_win_rate_vs_bist100   | average_monthly_excess_return   | max_drawdown   |   average_monthly_turnover |   average_trades_per_month | transaction_cost_impact   | worst_underperformance_month   | worst_underperformance   | best_outperformance_month   | best_outperformance   |   intervals |
|:------------|:------------------------------|:------------|-----------------:|:---------------|:-------------------------|:-------|:---------------|:--------------|:------------------------------|:--------------------------------|:---------------|---------------------------:|---------------------------:|:--------------------------|:-------------------------------|:-------------------------|:----------------------------|:----------------------|------------:|
| A           | Current baseline monthly Top3 | monthly     |                3 | 83.22%         | 83.79%                   | 25.43% | 25.58%         | -0.14%        | 46.88%                        | 0.07%                           | -19.32%        |                    1.21875 |                    3.65625 | 14.59%                    | 2024-04                        | -10.59%                  | 2025-04                     | 15.27%                |          33 |
| B           | Weekly rebalance Top3         | weekly      |                3 | -3.65%         | 83.79%                   | -1.38% | 25.58%         | -26.96%       | 39.39%                        | -1.82%                          | -42.13%        |                    3.06061 |                    9.18182 | 21.66%                    | 2024-03                        | -12.42%                  | 2025-03                     | 12.41%                |         140 |
| C           | Weekly rebalance Top5         | weekly      |                5 | 12.53%         | 83.79%                   | 4.52%  | 25.58%         | -21.06%       | 42.42%                        | -1.41%                          | -36.45%        |                    2.70909 |                   13.5455  | 22.05%                    | 2024-08                        | -9.16%                   | 2026-03                     | 6.68%                 |         140 |
| D           | Relative Strength Top3        | weekly      |                3 | 0.96%          | 83.79%                   | 0.36%  | 25.58%         | -25.22%       | 36.36%                        | -1.73%                          | -38.81%        |                    4.17172 |                   12.5152  | 31.92%                    | 2026-02                        | -14.58%                  | 2026-08                     | 8.57%                 |         140 |
| E           | Benchmark-aware Top3          | weekly      |                3 | -5.41%         | 83.79%                   | -2.06% | 25.58%         | -27.64%       | 33.33%                        | -1.94%                          | -39.49%        |                    4.21212 |                   12.6364  | 30.27%                    | 2026-02                        | -11.73%                  | 2026-08                     | 8.57%                 |         140 |
| F           | Leadership Rotation Overlay   | weekly      |                3 | -6.97%         | 83.79%                   | -2.67% | 25.58%         | -28.25%       | 39.39%                        | -1.93%                          | -42.16%        |                    4.05051 |                   12.1515  | 28.52%                    | 2026-02                        | -11.73%                  | 2026-08                     | 8.44%                 |         140 |

## Decision

- Did weekly rebalance improve excess return? Recent yes, historical no, so rejected. Historical excess CAGR delta vs baseline: -26.82%; recent excess delta: 9.57%.
- Did relative strength improve excess return? Recent yes, historical no, so rejected. Historical excess CAGR delta vs baseline: -25.07%; recent excess delta: 9.91%.
- Did benchmark-aware selection improve excess return? Recent yes, historical no, so rejected. Historical excess CAGR delta vs baseline: -27.49%; recent excess delta: 9.84%.
- Did any policy beat BIST100 robustly? No under the current acceptance filter.
- Next paper-trading candidate: none. No policy passed both historical and recent acceptance criteria.
- Current one-month fixed hold should be kept for tracking, while weekly/relative-strength variants remain research-only.

## Acceptance Rule

A policy is only eligible if it improves both historical walk-forward excess return and the recent 2026-06 counterfactual excess return. Policies that only fix June 2026 are rejected.
