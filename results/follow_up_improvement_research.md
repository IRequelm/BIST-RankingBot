# Follow-Up Improvement Research

This is research-only. Production follow-up tracking remains fixed and still reads reports/tracking_state.json.

## Policy Summary

| policy_id   | policy_name                   | frequency   |   portfolio_size | total_return   | benchmark_total_return   | cagr   | bist100_cagr   | excess_cagr   | monthly_win_rate_vs_bist100   | average_monthly_excess_return   | max_drawdown   |   average_monthly_turnover |   average_trades_per_month | transaction_cost_impact   | worst_underperformance_month   | worst_underperformance   | best_outperformance_month   | best_outperformance   |   intervals |
|:------------|:------------------------------|:------------|-----------------:|:---------------|:-------------------------|:-------|:---------------|:--------------|:------------------------------|:--------------------------------|:---------------|---------------------------:|---------------------------:|:--------------------------|:-------------------------------|:-------------------------|:----------------------------|:----------------------|------------:|
| A           | Current baseline monthly Top3 | monthly     |                3 | 56.39%         | 52.95%                   | 16.83% | 15.93%         | 0.90%         | 44.12%                        | 0.13%                           | -19.32%        |                    1.2451  |                    3.73529 | 13.63%                    | 2024-04                        | -10.59%                  | 2025-04                     | 15.27%                |          35 |
| B           | Weekly rebalance Top3         | weekly      |                3 | -21.73%        | 52.95%                   | -8.17% | 15.93%         | -24.10%       | 40.00%                        | -1.81%                          | -42.13%        |                    3.07619 |                    9.22857 | 18.92%                    | 2024-03                        | -12.42%                  | 2025-03                     | 12.41%                |         151 |
| C           | Weekly rebalance Top5         | weekly      |                5 | 4.08%          | 52.95%                   | 1.40%  | 15.93%         | -14.53%       | 42.86%                        | -1.05%                          | -36.45%        |                    2.69143 |                   13.4571  | 21.62%                    | 2024-08                        | -9.16%                   | 2026-09                     | 6.85%                 |         151 |
| D           | Relative Strength Top3        | weekly      |                3 | -1.55%         | 52.95%                   | -0.54% | 15.93%         | -16.47%       | 40.00%                        | -1.20%                          | -39.97%        |                    4.25714 |                   12.7714  | 34.11%                    | 2026-02                        | -14.58%                  | 2026-08                     | 8.57%                 |         151 |
| E           | Benchmark-aware Top3          | weekly      |                3 | -13.21%        | 52.95%                   | -4.81% | 15.93%         | -20.74%       | 37.14%                        | -1.58%                          | -40.89%        |                    4.27619 |                   12.8286  | 30.26%                    | 2026-02                        | -11.73%                  | 2026-08                     | 8.57%                 |         151 |
| F           | Leadership Rotation Overlay   | weekly      |                3 | -15.52%        | 52.95%                   | -5.70% | 15.93%         | -21.63%       | 40.00%                        | -1.60%                          | -42.16%        |                    4.21905 |                   12.6571  | 29.05%                    | 2026-02                        | -11.73%                  | 2026-08                     | 8.44%                 |         151 |

## Decision

- Did weekly rebalance improve excess return? No. Historical excess CAGR delta vs baseline: -25.00%; recent excess delta: -1.29%.
- Did relative strength improve excess return? Recent yes, historical no, so rejected. Historical excess CAGR delta vs baseline: -17.37%; recent excess delta: 16.17%.
- Did benchmark-aware selection improve excess return? Recent yes, historical no, so rejected. Historical excess CAGR delta vs baseline: -21.64%; recent excess delta: 10.03%.
- Did any policy beat BIST100 robustly? No under the current acceptance filter.
- Next paper-trading candidate: none. No policy passed both historical and recent acceptance criteria.
- Current one-month fixed hold should be kept for tracking, while weekly/relative-strength variants remain research-only.

## Acceptance Rule

A policy is only eligible if it improves both historical walk-forward excess return and the recent 2026-06 counterfactual excess return. Policies that only fix June 2026 are rejected.
