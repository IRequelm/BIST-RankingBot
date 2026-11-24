# Follow-Up Improvement Research

This is research-only. Production follow-up tracking remains fixed and still reads reports/tracking_state.json.

## Policy Summary

| policy_id   | policy_name                   | frequency   |   portfolio_size | total_return   | benchmark_total_return   | cagr   | bist100_cagr   | excess_cagr   | monthly_win_rate_vs_bist100   | average_monthly_excess_return   | max_drawdown   |   average_monthly_turnover |   average_trades_per_month | transaction_cost_impact   | worst_underperformance_month   | worst_underperformance   | best_outperformance_month   | best_outperformance   |   intervals |
|:------------|:------------------------------|:------------|-----------------:|:---------------|:-------------------------|:-------|:---------------|:--------------|:------------------------------|:--------------------------------|:---------------|---------------------------:|---------------------------:|:--------------------------|:-------------------------------|:-------------------------|:----------------------------|:----------------------|------------:|
| A           | Current baseline monthly Top3 | monthly     |                3 | 47.49%         | 45.65%                   | 14.39% | 13.89%         | 0.50%         | 44.12%                        | 0.11%                           | -19.32%        |                    1.2451  |                    3.73529 | 12.88%                    | 2024-04                        | -10.59%                  | 2025-04                     | 15.27%                |          35 |
| B           | Weekly rebalance Top3         | weekly      |                3 | -25.22%        | 45.65%                   | -9.56% | 13.89%         | -23.45%       | 40.00%                        | -1.79%                          | -42.13%        |                    3.07619 |                    9.22857 | 18.08%                    | 2024-03                        | -12.42%                  | 2025-03                     | 12.41%                |         151 |
| C           | Weekly rebalance Top5         | weekly      |                5 | 0.38%          | 45.65%                   | 0.13%  | 13.89%         | -13.76%       | 42.86%                        | -1.02%                          | -36.45%        |                    2.69143 |                   13.4571  | 20.85%                    | 2024-08                        | -9.16%                   | 2026-09                     | 6.85%                 |         151 |
| D           | Relative Strength Top3        | weekly      |                3 | -3.67%         | 45.65%                   | -1.28% | 13.89%         | -15.17%       | 40.00%                        | -1.12%                          | -39.97%        |                    4.25714 |                   12.7714  | 33.37%                    | 2026-02                        | -14.58%                  | 2026-11                     | 9.04%                 |         151 |
| E           | Benchmark-aware Top3          | weekly      |                3 | -15.09%        | 45.65%                   | -5.50% | 13.89%         | -19.39%       | 37.14%                        | -1.50%                          | -40.89%        |                    4.27619 |                   12.8286  | 29.61%                    | 2026-02                        | -11.73%                  | 2026-08                     | 8.57%                 |         151 |
| F           | Leadership Rotation Overlay   | weekly      |                3 | -17.34%        | 45.65%                   | -6.37% | 13.89%         | -20.26%       | 40.00%                        | -1.52%                          | -42.16%        |                    4.21905 |                   12.6571  | 28.43%                    | 2026-02                        | -11.73%                  | 2026-08                     | 8.44%                 |         151 |

## Decision

- Did weekly rebalance improve excess return? Recent yes, historical no, so rejected. Historical excess CAGR delta vs baseline: -23.95%; recent excess delta: 0.12%.
- Did relative strength improve excess return? Recent yes, historical no, so rejected. Historical excess CAGR delta vs baseline: -15.67%; recent excess delta: 19.18%.
- Did benchmark-aware selection improve excess return? Recent yes, historical no, so rejected. Historical excess CAGR delta vs baseline: -19.88%; recent excess delta: 13.16%.
- Did any policy beat BIST100 robustly? No under the current acceptance filter.
- Next paper-trading candidate: none. No policy passed both historical and recent acceptance criteria.
- Current one-month fixed hold should be kept for tracking, while weekly/relative-strength variants remain research-only.

## Acceptance Rule

A policy is only eligible if it improves both historical walk-forward excess return and the recent 2026-06 counterfactual excess return. Policies that only fix June 2026 are rejected.
