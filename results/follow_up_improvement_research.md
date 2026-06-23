# Follow-Up Improvement Research

This is research-only. Production follow-up tracking remains fixed and still reads reports/tracking_state.json.

## Policy Summary

| policy_id   | policy_name                   | frequency   |   portfolio_size | total_return   | benchmark_total_return   | cagr   | bist100_cagr   | excess_cagr   | monthly_win_rate_vs_bist100   | average_monthly_excess_return   | max_drawdown   |   average_monthly_turnover |   average_trades_per_month | transaction_cost_impact   | worst_underperformance_month   | worst_underperformance   | best_outperformance_month   | best_outperformance   |   intervals |
|:------------|:------------------------------|:------------|-----------------:|:---------------|:-------------------------|:-------|:---------------|:--------------|:------------------------------|:--------------------------------|:---------------|---------------------------:|---------------------------:|:--------------------------|:-------------------------------|:-------------------------|:----------------------------|:----------------------|------------:|
| A           | Current baseline monthly Top3 | monthly     |                3 | 75.72%         | 93.20%                   | 25.64% | 30.56%         | -4.92%        | 41.38%                        | -0.25%                          | -19.32%        |                    1.22989 |                    3.68966 | 12.72%                    | 2024-04                        | -10.59%                  | 2025-04                     | 15.27%                |          30 |
| B           | Weekly rebalance Top3         | weekly      |                3 | -2.12%         | 93.20%                   | -0.86% | 30.56%         | -31.42%       | 40.00%                        | -2.14%                          | -42.13%        |                    3.21111 |                    9.63333 | 20.89%                    | 2024-03                        | -12.42%                  | 2025-03                     | 12.41%                |         129 |
| C           | Weekly rebalance Top5         | weekly      |                5 | 25.64%         | 93.20%                   | 9.68%  | 30.56%         | -20.88%       | 40.00%                        | -1.36%                          | -36.45%        |                    2.74    |                   13.7     | 22.46%                    | 2024-08                        | -9.16%                   | 2026-03                     | 6.68%                 |         129 |
| D           | Relative Strength Top3        | weekly      |                3 | 3.85%          | 93.20%                   | 1.54%  | 30.56%         | -29.02%       | 36.67%                        | -2.00%                          | -35.17%        |                    4.34444 |                   13.0333  | 30.84%                    | 2026-02                        | -14.58%                  | 2025-03                     | 6.67%                 |         129 |
| E           | Benchmark-aware Top3          | weekly      |                3 | -2.64%         | 93.20%                   | -1.08% | 30.56%         | -31.64%       | 33.33%                        | -2.23%                          | -38.70%        |                    4.36667 |                   13.1     | 29.12%                    | 2026-02                        | -11.73%                  | 2025-03                     | 6.25%                 |         129 |
| F           | Leadership Rotation Overlay   | weekly      |                3 | -6.68%         | 93.20%                   | -2.76% | 30.56%         | -33.32%       | 36.67%                        | -2.29%                          | -42.16%        |                    4.25556 |                   12.7667  | 27.15%                    | 2026-02                        | -11.73%                  | 2024-04                     | 7.40%                 |         129 |

## Decision

- Did weekly rebalance improve excess return? Recent yes, historical no, so rejected. Historical excess CAGR delta vs baseline: -26.51%; recent excess delta: 5.54%.
- Did relative strength improve excess return? Recent yes, historical no, so rejected. Historical excess CAGR delta vs baseline: -24.10%; recent excess delta: 7.23%.
- Did benchmark-aware selection improve excess return? Recent yes, historical no, so rejected. Historical excess CAGR delta vs baseline: -26.72%; recent excess delta: 7.23%.
- Did any policy beat BIST100 robustly? No under the current acceptance filter.
- Next paper-trading candidate: none. No policy passed both historical and recent acceptance criteria.
- Current one-month fixed hold should be kept for tracking, while weekly/relative-strength variants remain research-only.

## Acceptance Rule

A policy is only eligible if it improves both historical walk-forward excess return and the recent 2026-06 counterfactual excess return. Policies that only fix June 2026 are rejected.
