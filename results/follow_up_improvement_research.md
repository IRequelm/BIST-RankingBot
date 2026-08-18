# Follow-Up Improvement Research

This is research-only. Production follow-up tracking remains fixed and still reads reports/tracking_state.json.

## Policy Summary

| policy_id   | policy_name                   | frequency   |   portfolio_size | total_return   | benchmark_total_return   | cagr   | bist100_cagr   | excess_cagr   | monthly_win_rate_vs_bist100   | average_monthly_excess_return   | max_drawdown   |   average_monthly_turnover |   average_trades_per_month | transaction_cost_impact   | worst_underperformance_month   | worst_underperformance   | best_outperformance_month   | best_outperformance   |   intervals |
|:------------|:------------------------------|:------------|-----------------:|:---------------|:-------------------------|:-------|:---------------|:--------------|:------------------------------|:--------------------------------|:---------------|---------------------------:|---------------------------:|:--------------------------|:-------------------------------|:-------------------------|:----------------------------|:----------------------|------------:|
| A           | Current baseline monthly Top3 | monthly     |                3 | 73.34%         | 85.88%                   | 23.42% | 26.76%         | -3.34%        | 45.16%                        | -0.16%                          | -19.32%        |                    1.21505 |                    3.64516 | 13.31%                    | 2024-04                        | -10.59%                  | 2025-04                     | 15.27%                |          32 |
| B           | Weekly rebalance Top3         | weekly      |                3 | -8.29%         | 85.88%                   | -3.26% | 26.76%         | -30.01%       | 37.50%                        | -2.08%                          | -42.13%        |                    3.11458 |                    9.34375 | 20.32%                    | 2024-03                        | -12.42%                  | 2025-03                     | 12.41%                |         137 |
| C           | Weekly rebalance Top5         | weekly      |                5 | 10.86%         | 85.88%                   | 4.02%  | 26.76%         | -22.74%       | 40.62%                        | -1.53%                          | -36.45%        |                    2.71875 |                   13.5938  | 21.10%                    | 2024-08                        | -9.16%                   | 2026-03                     | 6.68%                 |         137 |
| D           | Relative Strength Top3        | weekly      |                3 | -4.07%         | 85.88%                   | -1.58% | 26.76%         | -28.34%       | 34.38%                        | -2.00%                          | -38.81%        |                    4.26042 |                   12.7812  | 30.00%                    | 2026-02                        | -14.58%                  | 2025-03                     | 6.67%                 |         137 |
| E           | Benchmark-aware Top3          | weekly      |                3 | -10.07%        | 85.88%                   | -3.98% | 26.76%         | -30.74%       | 31.25%                        | -2.21%                          | -39.49%        |                    4.28125 |                   12.8438  | 28.31%                    | 2026-02                        | -11.73%                  | 2025-03                     | 6.25%                 |         137 |
| F           | Leadership Rotation Overlay   | weekly      |                3 | -11.45%        | 85.88%                   | -4.54% | 26.76%         | -31.30%       | 37.50%                        | -2.19%                          | -42.16%        |                    4.13542 |                   12.4062  | 26.85%                    | 2026-02                        | -11.73%                  | 2024-04                     | 7.40%                 |         137 |

## Decision

- Did weekly rebalance improve excess return? Recent yes, historical no, so rejected. Historical excess CAGR delta vs baseline: -26.67%; recent excess delta: 5.26%.
- Did relative strength improve excess return? Recent yes, historical no, so rejected. Historical excess CAGR delta vs baseline: -24.99%; recent excess delta: 5.39%.
- Did benchmark-aware selection improve excess return? Recent yes, historical no, so rejected. Historical excess CAGR delta vs baseline: -27.40%; recent excess delta: 5.39%.
- Did any policy beat BIST100 robustly? No under the current acceptance filter.
- Next paper-trading candidate: none. No policy passed both historical and recent acceptance criteria.
- Current one-month fixed hold should be kept for tracking, while weekly/relative-strength variants remain research-only.

## Acceptance Rule

A policy is only eligible if it improves both historical walk-forward excess return and the recent 2026-06 counterfactual excess return. Policies that only fix June 2026 are rejected.
