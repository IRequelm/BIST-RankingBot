# Follow-Up Improvement Research

This is research-only. Production follow-up tracking remains fixed and still reads reports/tracking_state.json.

## Policy Summary

| policy_id   | policy_name                   | frequency   |   portfolio_size | total_return   | benchmark_total_return   | cagr   | bist100_cagr   | excess_cagr   | monthly_win_rate_vs_bist100   | average_monthly_excess_return   | max_drawdown   |   average_monthly_turnover |   average_trades_per_month | transaction_cost_impact   | worst_underperformance_month   | worst_underperformance   | best_outperformance_month   | best_outperformance   |   intervals |
|:------------|:------------------------------|:------------|-----------------:|:---------------|:-------------------------|:-------|:---------------|:--------------|:------------------------------|:--------------------------------|:---------------|---------------------------:|---------------------------:|:--------------------------|:-------------------------------|:-------------------------|:----------------------------|:----------------------|------------:|
| A           | Current baseline monthly Top3 | monthly     |                3 | 68.26%         | 85.07%                   | 22.07% | 26.61%         | -4.54%        | 41.94%                        | -0.24%                          | -19.32%        |                    1.21505 |                    3.64516 | 12.93%                    | 2024-04                        | -10.59%                  | 2025-04                     | 15.27%                |          32 |
| B           | Weekly rebalance Top3         | weekly      |                3 | -11.38%        | 85.07%                   | -4.53% | 26.61%         | -31.13%       | 34.38%                        | -2.18%                          | -42.13%        |                    3.11458 |                    9.34375 | 19.64%                    | 2024-03                        | -12.42%                  | 2025-03                     | 12.41%                |         137 |
| C           | Weekly rebalance Top5         | weekly      |                5 | 6.15%          | 85.07%                   | 2.32%  | 26.61%         | -24.29%       | 37.50%                        | -1.66%                          | -36.45%        |                    2.71875 |                   13.5938  | 20.21%                    | 2024-08                        | -9.16%                   | 2026-03                     | 6.68%                 |         137 |
| D           | Relative Strength Top3        | weekly      |                3 | -7.27%         | 85.07%                   | -2.85% | 26.61%         | -29.46%       | 34.38%                        | -2.10%                          | -38.77%        |                    4.26042 |                   12.7812  | 29.00%                    | 2026-02                        | -14.58%                  | 2025-03                     | 6.67%                 |         137 |
| E           | Benchmark-aware Top3          | weekly      |                3 | -13.07%        | 85.07%                   | -5.23% | 26.61%         | -31.83%       | 31.25%                        | -2.31%                          | -39.45%        |                    4.28125 |                   12.8438  | 27.37%                    | 2026-02                        | -11.73%                  | 2025-03                     | 6.25%                 |         137 |
| F           | Leadership Rotation Overlay   | weekly      |                3 | -13.57%        | 85.07%                   | -5.44% | 26.61%         | -32.04%       | 37.50%                        | -2.26%                          | -42.16%        |                    4.13542 |                   12.4062  | 26.20%                    | 2026-02                        | -11.73%                  | 2024-04                     | 7.40%                 |         137 |

## Decision

- Did weekly rebalance improve excess return? Recent yes, historical no, so rejected. Historical excess CAGR delta vs baseline: -26.59%; recent excess delta: 2.50%.
- Did relative strength improve excess return? Recent yes, historical no, so rejected. Historical excess CAGR delta vs baseline: -24.92%; recent excess delta: 2.67%.
- Did benchmark-aware selection improve excess return? Recent yes, historical no, so rejected. Historical excess CAGR delta vs baseline: -27.30%; recent excess delta: 2.67%.
- Did any policy beat BIST100 robustly? No under the current acceptance filter.
- Next paper-trading candidate: none. No policy passed both historical and recent acceptance criteria.
- Current one-month fixed hold should be kept for tracking, while weekly/relative-strength variants remain research-only.

## Acceptance Rule

A policy is only eligible if it improves both historical walk-forward excess return and the recent 2026-06 counterfactual excess return. Policies that only fix June 2026 are rejected.
