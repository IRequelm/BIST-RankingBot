# Follow-Up Improvement Research

This is research-only. Production follow-up tracking remains fixed and still reads reports/tracking_state.json.

## Policy Summary

| policy_id   | policy_name                   | frequency   |   portfolio_size | total_return   | benchmark_total_return   | cagr   | bist100_cagr   | excess_cagr   | monthly_win_rate_vs_bist100   | average_monthly_excess_return   | max_drawdown   |   average_monthly_turnover |   average_trades_per_month | transaction_cost_impact   | worst_underperformance_month   | worst_underperformance   | best_outperformance_month   | best_outperformance   |   intervals |
|:------------|:------------------------------|:------------|-----------------:|:---------------|:-------------------------|:-------|:---------------|:--------------|:------------------------------|:--------------------------------|:---------------|---------------------------:|---------------------------:|:--------------------------|:-------------------------------|:-------------------------|:----------------------------|:----------------------|------------:|
| A           | Current baseline monthly Top3 | monthly     |                3 | 53.60%         | 50.54%                   | 16.08% | 15.28%         | 0.81%         | 44.12%                        | 0.13%                           | -19.32%        |                    1.2451  |                    3.73529 | 13.39%                    | 2024-04                        | -10.59%                  | 2025-04                     | 15.27%                |          35 |
| B           | Weekly rebalance Top3         | weekly      |                3 | -23.34%        | 50.54%                   | -8.82% | 15.28%         | -24.10%       | 40.00%                        | -1.82%                          | -42.13%        |                    3.07619 |                    9.22857 | 18.53%                    | 2024-03                        | -12.42%                  | 2025-03                     | 12.41%                |         151 |
| C           | Weekly rebalance Top5         | weekly      |                5 | 2.40%          | 50.54%                   | 0.83%  | 15.28%         | -14.45%       | 42.86%                        | -1.05%                          | -36.45%        |                    2.69143 |                   13.4571  | 21.27%                    | 2024-08                        | -9.16%                   | 2026-09                     | 6.85%                 |         151 |
| D           | Relative Strength Top3        | weekly      |                3 | -2.84%         | 50.54%                   | -1.00% | 15.28%         | -16.27%       | 40.00%                        | -1.19%                          | -39.97%        |                    4.25714 |                   12.7714  | 33.66%                    | 2026-02                        | -14.58%                  | 2026-08                     | 8.57%                 |         151 |
| E           | Benchmark-aware Top3          | weekly      |                3 | -14.36%        | 50.54%                   | -5.24% | 15.28%         | -20.52%       | 37.14%                        | -1.57%                          | -40.89%        |                    4.27619 |                   12.8286  | 29.86%                    | 2026-02                        | -11.73%                  | 2026-08                     | 8.57%                 |         151 |
| F           | Leadership Rotation Overlay   | weekly      |                3 | -16.63%        | 50.54%                   | -6.13% | 15.28%         | -21.40%       | 40.00%                        | -1.59%                          | -42.16%        |                    4.21905 |                   12.6571  | 28.67%                    | 2026-02                        | -11.73%                  | 2026-08                     | 8.44%                 |         151 |

## Decision

- Did weekly rebalance improve excess return? No. Historical excess CAGR delta vs baseline: -24.91%; recent excess delta: -1.66%.
- Did relative strength improve excess return? Recent yes, historical no, so rejected. Historical excess CAGR delta vs baseline: -17.08%; recent excess delta: 16.21%.
- Did benchmark-aware selection improve excess return? Recent yes, historical no, so rejected. Historical excess CAGR delta vs baseline: -21.33%; recent excess delta: 10.14%.
- Did any policy beat BIST100 robustly? No under the current acceptance filter.
- Next paper-trading candidate: none. No policy passed both historical and recent acceptance criteria.
- Current one-month fixed hold should be kept for tracking, while weekly/relative-strength variants remain research-only.

## Acceptance Rule

A policy is only eligible if it improves both historical walk-forward excess return and the recent 2026-06 counterfactual excess return. Policies that only fix June 2026 are rejected.
