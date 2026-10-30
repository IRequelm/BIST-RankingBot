# Follow-Up Improvement Research

This is research-only. Production follow-up tracking remains fixed and still reads reports/tracking_state.json.

## Policy Summary

| policy_id   | policy_name                   | frequency   |   portfolio_size | total_return   | benchmark_total_return   | cagr   | bist100_cagr   | excess_cagr   | monthly_win_rate_vs_bist100   | average_monthly_excess_return   | max_drawdown   |   average_monthly_turnover |   average_trades_per_month | transaction_cost_impact   | worst_underperformance_month   | worst_underperformance   | best_outperformance_month   | best_outperformance   |   intervals |
|:------------|:------------------------------|:------------|-----------------:|:---------------|:-------------------------|:-------|:---------------|:--------------|:------------------------------|:--------------------------------|:---------------|---------------------------:|---------------------------:|:--------------------------|:-------------------------------|:-------------------------|:----------------------------|:----------------------|------------:|
| A           | Current baseline monthly Top3 | monthly     |                3 | 54.12%         | 46.45%                   | 16.58% | 14.49%         | 2.09%         | 45.45%                        | 0.19%                           | -19.32%        |                    1.24242 |                    3.72727 | 13.00%                    | 2024-04                        | -10.59%                  | 2025-04                     | 15.27%                |          34 |
| B           | Weekly rebalance Top3         | weekly      |                3 | -22.44%        | 46.45%                   | -8.62% | 14.49%         | -23.10%       | 38.24%                        | -1.75%                          | -42.13%        |                    3.10784 |                    9.32353 | 18.37%                    | 2024-03                        | -12.42%                  | 2025-03                     | 12.41%                |         148 |
| C           | Weekly rebalance Top5         | weekly      |                5 | -1.49%         | 46.45%                   | -0.53% | 14.49%         | -15.02%       | 44.12%                        | -1.11%                          | -36.45%        |                    2.71176 |                   13.5588  | 20.00%                    | 2024-08                        | -9.16%                   | 2026-09                     | 6.85%                 |         148 |
| D           | Relative Strength Top3        | weekly      |                3 | -14.10%        | 46.45%                   | -5.25% | 14.49%         | -19.73%       | 38.24%                        | -1.51%                          | -40.16%        |                    4.32353 |                   12.9706  | 29.32%                    | 2026-02                        | -14.58%                  | 2026-08                     | 8.57%                 |         148 |
| E           | Benchmark-aware Top3          | weekly      |                3 | -19.82%        | 46.45%                   | -7.53% | 14.49%         | -22.02%       | 35.29%                        | -1.72%                          | -41.08%        |                    4.30392 |                   12.9118  | 27.26%                    | 2026-02                        | -11.73%                  | 2026-08                     | 8.57%                 |         148 |
| F           | Leadership Rotation Overlay   | weekly      |                3 | -21.94%        | 46.45%                   | -8.41% | 14.49%         | -22.90%       | 38.24%                        | -1.74%                          | -42.16%        |                    4.2451  |                   12.7353  | 26.17%                    | 2026-02                        | -11.73%                  | 2026-08                     | 8.44%                 |         148 |

## Decision

- Did weekly rebalance improve excess return? Recent yes, historical no, so rejected. Historical excess CAGR delta vs baseline: -25.20%; recent excess delta: 1.32%.
- Did relative strength improve excess return? Recent yes, historical no, so rejected. Historical excess CAGR delta vs baseline: -21.82%; recent excess delta: 6.44%.
- Did benchmark-aware selection improve excess return? Recent yes, historical no, so rejected. Historical excess CAGR delta vs baseline: -24.11%; recent excess delta: 6.04%.
- Did any policy beat BIST100 robustly? No under the current acceptance filter.
- Next paper-trading candidate: none. No policy passed both historical and recent acceptance criteria.
- Current one-month fixed hold should be kept for tracking, while weekly/relative-strength variants remain research-only.

## Acceptance Rule

A policy is only eligible if it improves both historical walk-forward excess return and the recent 2026-06 counterfactual excess return. Policies that only fix June 2026 are rejected.
