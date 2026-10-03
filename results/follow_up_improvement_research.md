# Follow-Up Improvement Research

This is research-only. Production follow-up tracking remains fixed and still reads reports/tracking_state.json.

## Policy Summary

| policy_id   | policy_name                   | frequency   |   portfolio_size | total_return   | benchmark_total_return   | cagr   | bist100_cagr   | excess_cagr   | monthly_win_rate_vs_bist100   | average_monthly_excess_return   | max_drawdown   |   average_monthly_turnover |   average_trades_per_month | transaction_cost_impact   | worst_underperformance_month   | worst_underperformance   | best_outperformance_month   | best_outperformance   |   intervals |
|:------------|:------------------------------|:------------|-----------------:|:---------------|:-------------------------|:-------|:---------------|:--------------|:------------------------------|:--------------------------------|:---------------|---------------------------:|---------------------------:|:--------------------------|:-------------------------------|:-------------------------|:----------------------------|:----------------------|------------:|
| A           | Current baseline monthly Top3 | monthly     |                3 | 77.00%         | 60.94%                   | 23.09% | 18.90%         | 4.19%         | 48.48%                        | 0.34%                           | -19.32%        |                    1.20202 |                    3.60606 | 14.36%                    | 2024-04                        | -10.59%                  | 2025-04                     | 15.27%                |          34 |
| B           | Weekly rebalance Top3         | weekly      |                3 | -8.99%         | 60.94%                   | -3.37% | 18.90%         | -22.27%       | 41.18%                        | -1.56%                          | -42.13%        |                    3.0098  |                    9.02941 | 20.77%                    | 2024-03                        | -12.42%                  | 2025-03                     | 12.41%                |         144 |
| C           | Weekly rebalance Top5         | weekly      |                5 | 5.03%          | 60.94%                   | 1.80%  | 18.90%         | -17.10%       | 41.18%                        | -1.20%                          | -36.45%        |                    2.7     |                   13.5     | 21.21%                    | 2024-08                        | -9.16%                   | 2026-09                     | 7.20%                 |         144 |
| D           | Relative Strength Top3        | weekly      |                3 | -7.00%         | 60.94%                   | -2.61% | 18.90%         | -21.51%       | 35.29%                        | -1.55%                          | -38.81%        |                    4.18627 |                   12.5588  | 30.57%                    | 2026-02                        | -14.58%                  | 2026-08                     | 8.57%                 |         144 |
| E           | Benchmark-aware Top3          | weekly      |                3 | -12.18%        | 60.94%                   | -4.61% | 18.90%         | -23.51%       | 32.35%                        | -1.73%                          | -39.49%        |                    4.18627 |                   12.5588  | 28.90%                    | 2026-02                        | -11.73%                  | 2026-08                     | 8.57%                 |         144 |
| F           | Leadership Rotation Overlay   | weekly      |                3 | -14.02%        | 60.94%                   | -5.35% | 18.90%         | -24.25%       | 38.24%                        | -1.73%                          | -42.16%        |                    4.06863 |                   12.2059  | 27.45%                    | 2026-02                        | -11.73%                  | 2026-08                     | 8.44%                 |         144 |

## Decision

- Did weekly rebalance improve excess return? Recent yes, historical no, so rejected. Historical excess CAGR delta vs baseline: -26.46%; recent excess delta: 5.11%.
- Did relative strength improve excess return? Recent yes, historical no, so rejected. Historical excess CAGR delta vs baseline: -25.69%; recent excess delta: 2.95%.
- Did benchmark-aware selection improve excess return? Recent yes, historical no, so rejected. Historical excess CAGR delta vs baseline: -27.70%; recent excess delta: 3.66%.
- Did any policy beat BIST100 robustly? No under the current acceptance filter.
- Next paper-trading candidate: none. No policy passed both historical and recent acceptance criteria.
- Current one-month fixed hold should be kept for tracking, while weekly/relative-strength variants remain research-only.

## Acceptance Rule

A policy is only eligible if it improves both historical walk-forward excess return and the recent 2026-06 counterfactual excess return. Policies that only fix June 2026 are rejected.
