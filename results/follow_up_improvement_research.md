# Follow-Up Improvement Research

This is research-only. Production follow-up tracking remains fixed and still reads reports/tracking_state.json.

## Policy Summary

| policy_id   | policy_name                   | frequency   |   portfolio_size | total_return   | benchmark_total_return   | cagr   | bist100_cagr   | excess_cagr   | monthly_win_rate_vs_bist100   | average_monthly_excess_return   | max_drawdown   |   average_monthly_turnover |   average_trades_per_month | transaction_cost_impact   | worst_underperformance_month   | worst_underperformance   | best_outperformance_month   | best_outperformance   |   intervals |
|:------------|:------------------------------|:------------|-----------------:|:---------------|:-------------------------|:-------|:---------------|:--------------|:------------------------------|:--------------------------------|:---------------|---------------------------:|---------------------------:|:--------------------------|:-------------------------------|:-------------------------|:----------------------------|:----------------------|------------:|
| A           | Current baseline monthly Top3 | monthly     |                3 | 63.37%         | 80.67%                   | 21.09% | 25.93%         | -4.85%        | 43.33%                        | -0.26%                          | -19.32%        |                    1.23333 |                    3.7     | 12.33%                    | 2024-04                        | -10.59%                  | 2025-04                     | 15.27%                |          31 |
| B           | Weekly rebalance Top3         | weekly      |                3 | -12.87%        | 80.67%                   | -5.23% | 25.93%         | -31.16%       | 35.48%                        | -2.23%                          | -42.13%        |                    3.19355 |                    9.58065 | 19.17%                    | 2024-03                        | -12.42%                  | 2025-03                     | 12.41%                |         134 |
| C           | Weekly rebalance Top5         | weekly      |                5 | 8.39%          | 80.67%                   | 3.19%  | 25.93%         | -22.74%       | 38.71%                        | -1.57%                          | -36.45%        |                    2.74194 |                   13.7097  | 20.11%                    | 2024-08                        | -9.16%                   | 2026-03                     | 6.68%                 |         134 |
| D           | Relative Strength Top3        | weekly      |                3 | -6.08%         | 80.67%                   | -2.42% | 25.93%         | -28.35%       | 32.26%                        | -2.05%                          | -36.49%        |                    4.35484 |                   13.0645  | 29.04%                    | 2026-02                        | -14.58%                  | 2025-03                     | 6.67%                 |         134 |
| E           | Benchmark-aware Top3          | weekly      |                3 | -11.95%        | 80.67%                   | -4.84% | 25.93%         | -30.77%       | 29.03%                        | -2.27%                          | -38.70%        |                    4.37634 |                   13.129   | 27.41%                    | 2026-02                        | -11.73%                  | 2025-03                     | 6.25%                 |         134 |
| F           | Leadership Rotation Overlay   | weekly      |                3 | -15.88%        | 80.67%                   | -6.52% | 25.93%         | -32.45%       | 35.48%                        | -2.34%                          | -42.16%        |                    4.24731 |                   12.7419  | 25.37%                    | 2026-02                        | -11.73%                  | 2024-04                     | 7.40%                 |         134 |

## Decision

- Did weekly rebalance improve excess return? No. Historical excess CAGR delta vs baseline: -26.32%; recent excess delta: -6.64%.
- Did relative strength improve excess return? No. Historical excess CAGR delta vs baseline: -23.50%; recent excess delta: -3.60%.
- Did benchmark-aware selection improve excess return? No. Historical excess CAGR delta vs baseline: -25.93%; recent excess delta: -3.60%.
- Did any policy beat BIST100 robustly? No under the current acceptance filter.
- Next paper-trading candidate: none. No policy passed both historical and recent acceptance criteria.
- Current one-month fixed hold should be kept for tracking, while weekly/relative-strength variants remain research-only.

## Acceptance Rule

A policy is only eligible if it improves both historical walk-forward excess return and the recent 2026-06 counterfactual excess return. Policies that only fix June 2026 are rejected.
