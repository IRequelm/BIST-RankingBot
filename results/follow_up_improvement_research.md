# Follow-Up Improvement Research

This is research-only. Production follow-up tracking remains fixed and still reads reports/tracking_state.json.

## Policy Summary

| policy_id   | policy_name                   | frequency   |   portfolio_size | total_return   | benchmark_total_return   | cagr   | bist100_cagr   | excess_cagr   | monthly_win_rate_vs_bist100   | average_monthly_excess_return   | max_drawdown   |   average_monthly_turnover |   average_trades_per_month | transaction_cost_impact   | worst_underperformance_month   | worst_underperformance   | best_outperformance_month   | best_outperformance   |   intervals |
|:------------|:------------------------------|:------------|-----------------:|:---------------|:-------------------------|:-------|:---------------|:--------------|:------------------------------|:--------------------------------|:---------------|---------------------------:|---------------------------:|:--------------------------|:-------------------------------|:-------------------------|:----------------------------|:----------------------|------------:|
| A           | Current baseline monthly Top3 | monthly     |                3 | 57.04%         | 46.26%                   | 17.37% | 14.45%         | 2.93%         | 45.45%                        | 0.24%                           | -19.32%        |                    1.24242 |                    3.72727 | 13.24%                    | 2024-04                        | -10.59%                  | 2025-04                     | 15.27%                |          34 |
| B           | Weekly rebalance Top3         | weekly      |                3 | -20.35%        | 46.26%                   | -7.76% | 14.45%         | -22.21%       | 41.18%                        | -1.67%                          | -42.13%        |                    3.10784 |                    9.32353 | 18.86%                    | 2024-03                        | -12.42%                  | 2025-03                     | 12.41%                |         148 |
| C           | Weekly rebalance Top5         | weekly      |                5 | 1.08%          | 46.26%                   | 0.38%  | 14.45%         | -14.06%       | 44.12%                        | -1.04%                          | -36.45%        |                    2.71176 |                   13.5588  | 20.51%                    | 2024-08                        | -9.16%                   | 2026-09                     | 6.85%                 |         148 |
| D           | Relative Strength Top3        | weekly      |                3 | -11.42%        | 46.26%                   | -4.21% | 14.45%         | -18.66%       | 38.24%                        | -1.43%                          | -38.81%        |                    4.32353 |                   12.9706  | 30.23%                    | 2026-02                        | -14.58%                  | 2026-08                     | 8.57%                 |         148 |
| E           | Benchmark-aware Top3          | weekly      |                3 | -17.32%        | 46.26%                   | -6.53% | 14.45%         | -20.98%       | 35.29%                        | -1.64%                          | -40.42%        |                    4.30392 |                   12.9118  | 28.11%                    | 2026-02                        | -11.73%                  | 2026-08                     | 8.57%                 |         148 |
| F           | Leadership Rotation Overlay   | weekly      |                3 | -19.51%        | 46.26%                   | -7.42% | 14.45%         | -21.86%       | 38.24%                        | -1.66%                          | -42.16%        |                    4.2451  |                   12.7353  | 26.98%                    | 2026-02                        | -11.73%                  | 2026-08                     | 8.44%                 |         148 |

## Decision

- Did weekly rebalance improve excess return? Recent yes, historical no, so rejected. Historical excess CAGR delta vs baseline: -25.13%; recent excess delta: 2.66%.
- Did relative strength improve excess return? Recent yes, historical no, so rejected. Historical excess CAGR delta vs baseline: -21.59%; recent excess delta: 8.29%.
- Did benchmark-aware selection improve excess return? Recent yes, historical no, so rejected. Historical excess CAGR delta vs baseline: -23.90%; recent excess delta: 7.89%.
- Did any policy beat BIST100 robustly? No under the current acceptance filter.
- Next paper-trading candidate: none. No policy passed both historical and recent acceptance criteria.
- Current one-month fixed hold should be kept for tracking, while weekly/relative-strength variants remain research-only.

## Acceptance Rule

A policy is only eligible if it improves both historical walk-forward excess return and the recent 2026-06 counterfactual excess return. Policies that only fix June 2026 are rejected.
