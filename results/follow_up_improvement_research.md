# Follow-Up Improvement Research

This is research-only. Production follow-up tracking remains fixed and still reads reports/tracking_state.json.

## Policy Summary

| policy_id   | policy_name                   | frequency   |   portfolio_size | total_return   | benchmark_total_return   | cagr   | bist100_cagr   | excess_cagr   | monthly_win_rate_vs_bist100   | average_monthly_excess_return   | max_drawdown   |   average_monthly_turnover |   average_trades_per_month | transaction_cost_impact   | worst_underperformance_month   | worst_underperformance   | best_outperformance_month   | best_outperformance   |   intervals |
|:------------|:------------------------------|:------------|-----------------:|:---------------|:-------------------------|:-------|:---------------|:--------------|:------------------------------|:--------------------------------|:---------------|---------------------------:|---------------------------:|:--------------------------|:-------------------------------|:-------------------------|:----------------------------|:----------------------|------------:|
| A           | Current baseline monthly Top3 | monthly     |                3 | 77.27%         | 56.70%                   | 23.21% | 17.79%         | 5.42%         | 46.88%                        | 0.44%                           | -19.32%        |                    1.21875 |                    3.65625 | 14.13%                    | 2024-04                        | -10.59%                  | 2026-09                     | 19.75%                |          33 |
| B           | Weekly rebalance Top3         | weekly      |                3 | -8.21%         | 56.70%                   | -3.07% | 17.79%         | -20.86%       | 39.39%                        | -1.53%                          | -42.13%        |                    3.10101 |                    9.30303 | 20.94%                    | 2024-03                        | -12.42%                  | 2025-03                     | 12.41%                |         144 |
| C           | Weekly rebalance Top5         | weekly      |                5 | 6.97%          | 56.70%                   | 2.49%  | 17.79%         | -15.30%       | 42.42%                        | -1.12%                          | -36.45%        |                    2.78182 |                   13.9091  | 21.60%                    | 2024-08                        | -9.16%                   | 2026-09                     | 10.55%                |         144 |
| D           | Relative Strength Top3        | weekly      |                3 | -3.97%         | 56.70%                   | -1.47% | 17.79%         | -19.26%       | 36.36%                        | -1.45%                          | -38.81%        |                    4.31313 |                   12.9394  | 31.56%                    | 2026-02                        | -14.58%                  | 2026-09                     | 11.12%                |         144 |
| E           | Benchmark-aware Top3          | weekly      |                3 | -9.32%         | 56.70%                   | -3.50% | 17.79%         | -21.29%       | 33.33%                        | -1.63%                          | -39.49%        |                    4.31313 |                   12.9394  | 29.83%                    | 2026-02                        | -11.73%                  | 2026-09                     | 11.81%                |         144 |
| F           | Leadership Rotation Overlay   | weekly      |                3 | -12.24%        | 56.70%                   | -4.65% | 17.79%         | -22.44%       | 39.39%                        | -1.66%                          | -42.16%        |                    4.19192 |                   12.5758  | 28.01%                    | 2026-02                        | -11.73%                  | 2026-09                     | 10.41%                |         144 |

## Decision

- Did weekly rebalance improve excess return? Recent yes, historical no, so rejected. Historical excess CAGR delta vs baseline: -26.28%; recent excess delta: 3.97%.
- Did relative strength improve excess return? Recent yes, historical no, so rejected. Historical excess CAGR delta vs baseline: -24.67%; recent excess delta: 4.12%.
- Did benchmark-aware selection improve excess return? Recent yes, historical no, so rejected. Historical excess CAGR delta vs baseline: -26.71%; recent excess delta: 4.86%.
- Did any policy beat BIST100 robustly? No under the current acceptance filter.
- Next paper-trading candidate: none. No policy passed both historical and recent acceptance criteria.
- Current one-month fixed hold should be kept for tracking, while weekly/relative-strength variants remain research-only.

## Acceptance Rule

A policy is only eligible if it improves both historical walk-forward excess return and the recent 2026-06 counterfactual excess return. Policies that only fix June 2026 are rejected.
