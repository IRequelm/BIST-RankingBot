# Follow-Up Improvement Research

This is research-only. Production follow-up tracking remains fixed and still reads reports/tracking_state.json.

## Policy Summary

| policy_id   | policy_name                   | frequency   |   portfolio_size | total_return   | benchmark_total_return   | cagr   | bist100_cagr   | excess_cagr   | monthly_win_rate_vs_bist100   | average_monthly_excess_return   | max_drawdown   |   average_monthly_turnover |   average_trades_per_month | transaction_cost_impact   | worst_underperformance_month   | worst_underperformance   | best_outperformance_month   | best_outperformance   |   intervals |
|:------------|:------------------------------|:------------|-----------------:|:---------------|:-------------------------|:-------|:---------------|:--------------|:------------------------------|:--------------------------------|:---------------|---------------------------:|---------------------------:|:--------------------------|:-------------------------------|:-------------------------|:----------------------------|:----------------------|------------:|
| A           | Current baseline monthly Top3 | monthly     |                3 | 71.23%         | 85.22%                   | 24.10% | 28.07%         | -3.97%        | 44.83%                        | -0.19%                          | -19.32%        |                    1.22989 |                    3.68966 | 12.41%                    | 2024-04                        | -10.59%                  | 2025-04                     | 15.27%                |          30 |
| B           | Weekly rebalance Top3         | weekly      |                3 | -8.74%         | 85.22%                   | -3.60% | 28.07%         | -31.67%       | 36.67%                        | -2.23%                          | -42.13%        |                    3.23333 |                    9.7     | 19.62%                    | 2024-03                        | -12.42%                  | 2025-03                     | 12.41%                |         131 |
| C           | Weekly rebalance Top5         | weekly      |                5 | 16.75%         | 85.22%                   | 6.41%  | 28.07%         | -21.66%       | 40.00%                        | -1.46%                          | -36.45%        |                    2.78    |                   13.9     | 21.22%                    | 2024-08                        | -9.16%                   | 2026-03                     | 6.68%                 |         131 |
| D           | Relative Strength Top3        | weekly      |                3 | -4.38%         | 85.22%                   | -1.78% | 28.07%         | -29.85%       | 33.33%                        | -2.14%                          | -35.17%        |                    4.41111 |                   13.2333  | 28.91%                    | 2026-02                        | -14.58%                  | 2025-03                     | 6.67%                 |         131 |
| E           | Benchmark-aware Top3          | weekly      |                3 | -10.36%        | 85.22%                   | -4.30% | 28.07%         | -32.37%       | 30.00%                        | -2.37%                          | -38.70%        |                    4.43333 |                   13.3     | 27.29%                    | 2026-02                        | -11.73%                  | 2025-03                     | 6.25%                 |         131 |
| F           | Leadership Rotation Overlay   | weekly      |                3 | -13.09%        | 85.22%                   | -5.48% | 28.07%         | -33.55%       | 36.67%                        | -2.40%                          | -42.16%        |                    4.3     |                   12.9     | 25.59%                    | 2026-02                        | -11.73%                  | 2024-04                     | 7.40%                 |         131 |

## Decision

- Did weekly rebalance improve excess return? Recent yes, historical no, so rejected. Historical excess CAGR delta vs baseline: -27.70%; recent excess delta: 0.91%.
- Did relative strength improve excess return? Recent yes, historical no, so rejected. Historical excess CAGR delta vs baseline: -25.88%; recent excess delta: 1.21%.
- Did benchmark-aware selection improve excess return? Recent yes, historical no, so rejected. Historical excess CAGR delta vs baseline: -28.39%; recent excess delta: 1.21%.
- Did any policy beat BIST100 robustly? No under the current acceptance filter.
- Next paper-trading candidate: none. No policy passed both historical and recent acceptance criteria.
- Current one-month fixed hold should be kept for tracking, while weekly/relative-strength variants remain research-only.

## Acceptance Rule

A policy is only eligible if it improves both historical walk-forward excess return and the recent 2026-06 counterfactual excess return. Policies that only fix June 2026 are rejected.
