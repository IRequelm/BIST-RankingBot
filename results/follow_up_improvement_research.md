# Follow-Up Improvement Research

This is research-only. Production follow-up tracking remains fixed and still reads reports/tracking_state.json.

## Policy Summary

| policy_id   | policy_name                   | frequency   |   portfolio_size | total_return   | benchmark_total_return   | cagr   | bist100_cagr   | excess_cagr   | monthly_win_rate_vs_bist100   | average_monthly_excess_return   | max_drawdown   |   average_monthly_turnover |   average_trades_per_month | transaction_cost_impact   | worst_underperformance_month   | worst_underperformance   | best_outperformance_month   | best_outperformance   |   intervals |
|:------------|:------------------------------|:------------|-----------------:|:---------------|:-------------------------|:-------|:---------------|:--------------|:------------------------------|:--------------------------------|:---------------|---------------------------:|---------------------------:|:--------------------------|:-------------------------------|:-------------------------|:----------------------------|:----------------------|------------:|
| A           | Current baseline monthly Top3 | monthly     |                3 | 54.52%         | 46.45%                   | 16.69% | 14.49%         | 2.20%         | 45.45%                        | 0.20%                           | -19.32%        |                    1.24242 |                    3.72727 | 13.03%                    | 2024-04                        | -10.59%                  | 2025-04                     | 15.27%                |          34 |
| B           | Weekly rebalance Top3         | weekly      |                3 | -21.88%        | 46.45%                   | -8.38% | 14.49%         | -22.87%       | 38.24%                        | -1.73%                          | -42.13%        |                    3.10784 |                    9.32353 | 18.50%                    | 2024-03                        | -12.42%                  | 2025-03                     | 12.41%                |         148 |
| C           | Weekly rebalance Top5         | weekly      |                5 | -0.66%         | 46.45%                   | -0.23% | 14.49%         | -14.72%       | 44.12%                        | -1.09%                          | -36.45%        |                    2.71176 |                   13.5588  | 20.16%                    | 2024-08                        | -9.16%                   | 2026-09                     | 6.85%                 |         148 |
| D           | Relative Strength Top3        | weekly      |                3 | -12.59%        | 46.45%                   | -4.66% | 14.49%         | -19.14%       | 38.24%                        | -1.47%                          | -39.10%        |                    4.32353 |                   12.9706  | 29.84%                    | 2026-02                        | -14.58%                  | 2026-08                     | 8.57%                 |         148 |
| E           | Benchmark-aware Top3          | weekly      |                3 | -18.41%        | 46.45%                   | -6.96% | 14.49%         | -21.45%       | 35.29%                        | -1.68%                          | -40.42%        |                    4.30392 |                   12.9118  | 27.74%                    | 2026-02                        | -11.73%                  | 2026-08                     | 8.57%                 |         148 |
| F           | Leadership Rotation Overlay   | weekly      |                3 | -20.57%        | 46.45%                   | -7.84% | 14.49%         | -22.33%       | 38.24%                        | -1.70%                          | -42.16%        |                    4.2451  |                   12.7353  | 26.63%                    | 2026-02                        | -11.73%                  | 2026-08                     | 8.44%                 |         148 |

## Decision

- Did weekly rebalance improve excess return? Recent yes, historical no, so rejected. Historical excess CAGR delta vs baseline: -25.07%; recent excess delta: 2.00%.
- Did relative strength improve excess return? Recent yes, historical no, so rejected. Historical excess CAGR delta vs baseline: -21.34%; recent excess delta: 8.07%.
- Did benchmark-aware selection improve excess return? Recent yes, historical no, so rejected. Historical excess CAGR delta vs baseline: -23.65%; recent excess delta: 7.67%.
- Did any policy beat BIST100 robustly? No under the current acceptance filter.
- Next paper-trading candidate: none. No policy passed both historical and recent acceptance criteria.
- Current one-month fixed hold should be kept for tracking, while weekly/relative-strength variants remain research-only.

## Acceptance Rule

A policy is only eligible if it improves both historical walk-forward excess return and the recent 2026-06 counterfactual excess return. Policies that only fix June 2026 are rejected.
