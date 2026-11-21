# Follow-Up Improvement Research

This is research-only. Production follow-up tracking remains fixed and still reads reports/tracking_state.json.

## Policy Summary

| policy_id   | policy_name                   | frequency   |   portfolio_size | total_return   | benchmark_total_return   | cagr   | bist100_cagr   | excess_cagr   | monthly_win_rate_vs_bist100   | average_monthly_excess_return   | max_drawdown   |   average_monthly_turnover |   average_trades_per_month | transaction_cost_impact   | worst_underperformance_month   | worst_underperformance   | best_outperformance_month   | best_outperformance   |   intervals |
|:------------|:------------------------------|:------------|-----------------:|:---------------|:-------------------------|:-------|:---------------|:--------------|:------------------------------|:--------------------------------|:---------------|---------------------------:|---------------------------:|:--------------------------|:-------------------------------|:-------------------------|:----------------------------|:----------------------|------------:|
| A           | Current baseline monthly Top3 | monthly     |                3 | 48.09%         | 46.00%                   | 14.59% | 14.03%         | 0.56%         | 44.12%                        | 0.11%                           | -19.32%        |                    1.2451  |                    3.73529 | 12.93%                    | 2024-04                        | -10.59%                  | 2025-04                     | 15.27%                |          35 |
| B           | Weekly rebalance Top3         | weekly      |                3 | -25.69%        | 46.00%                   | -9.79% | 14.03%         | -23.81%       | 40.00%                        | -1.81%                          | -42.13%        |                    3.07619 |                    9.22857 | 17.96%                    | 2024-03                        | -12.42%                  | 2025-03                     | 12.41%                |         151 |
| C           | Weekly rebalance Top5         | weekly      |                5 | 1.08%          | 46.00%                   | 0.37%  | 14.03%         | -13.65%       | 45.71%                        | -1.00%                          | -36.45%        |                    2.69143 |                   13.4571  | 21.00%                    | 2024-08                        | -9.16%                   | 2026-09                     | 6.85%                 |         151 |
| D           | Relative Strength Top3        | weekly      |                3 | -2.30%         | 46.00%                   | -0.81% | 14.03%         | -14.83%       | 40.00%                        | -1.09%                          | -39.97%        |                    4.25714 |                   12.7714  | 33.84%                    | 2026-02                        | -14.58%                  | 2026-11                     | 10.33%                |         151 |
| E           | Benchmark-aware Top3          | weekly      |                3 | -13.88%        | 46.00%                   | -5.05% | 14.03%         | -19.08%       | 37.14%                        | -1.47%                          | -40.89%        |                    4.27619 |                   12.8286  | 30.03%                    | 2026-02                        | -11.73%                  | 2026-08                     | 8.57%                 |         151 |
| F           | Leadership Rotation Overlay   | weekly      |                3 | -16.17%        | 46.00%                   | -5.93% | 14.03%         | -19.96%       | 40.00%                        | -1.48%                          | -42.16%        |                    4.21905 |                   12.6571  | 28.83%                    | 2026-02                        | -11.73%                  | 2026-08                     | 8.44%                 |         151 |

## Decision

- Did weekly rebalance improve excess return? No. Historical excess CAGR delta vs baseline: -24.38%; recent excess delta: -1.02%.
- Did relative strength improve excess return? Recent yes, historical no, so rejected. Historical excess CAGR delta vs baseline: -15.40%; recent excess delta: 19.97%.
- Did benchmark-aware selection improve excess return? Recent yes, historical no, so rejected. Historical excess CAGR delta vs baseline: -19.64%; recent excess delta: 13.87%.
- Did any policy beat BIST100 robustly? No under the current acceptance filter.
- Next paper-trading candidate: none. No policy passed both historical and recent acceptance criteria.
- Current one-month fixed hold should be kept for tracking, while weekly/relative-strength variants remain research-only.

## Acceptance Rule

A policy is only eligible if it improves both historical walk-forward excess return and the recent 2026-06 counterfactual excess return. Policies that only fix June 2026 are rejected.
