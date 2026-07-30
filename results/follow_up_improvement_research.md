# Follow-Up Improvement Research

This is research-only. Production follow-up tracking remains fixed and still reads reports/tracking_state.json.

## Policy Summary

| policy_id   | policy_name                   | frequency   |   portfolio_size | total_return   | benchmark_total_return   | cagr   | bist100_cagr   | excess_cagr   | monthly_win_rate_vs_bist100   | average_monthly_excess_return   | max_drawdown   |   average_monthly_turnover |   average_trades_per_month | transaction_cost_impact   | worst_underperformance_month   | worst_underperformance   | best_outperformance_month   | best_outperformance   |   intervals |
|:------------|:------------------------------|:------------|-----------------:|:---------------|:-------------------------|:-------|:---------------|:--------------|:------------------------------|:--------------------------------|:---------------|---------------------------:|---------------------------:|:--------------------------|:-------------------------------|:-------------------------|:----------------------------|:----------------------|------------:|
| A           | Current baseline monthly Top3 | monthly     |                3 | 64.72%         | 77.09%                   | 21.42% | 24.89%         | -3.47%        | 43.33%                        | -0.16%                          | -19.32%        |                    1.23333 |                    3.7     | 12.42%                    | 2024-04                        | -10.59%                  | 2025-04                     | 15.27%                |          31 |
| B           | Weekly rebalance Top3         | weekly      |                3 | -12.59%        | 77.09%                   | -5.10% | 24.89%         | -29.99%       | 35.48%                        | -2.15%                          | -42.13%        |                    3.19355 |                    9.58065 | 19.23%                    | 2024-03                        | -12.42%                  | 2025-03                     | 12.41%                |         135 |
| C           | Weekly rebalance Top5         | weekly      |                5 | 7.84%          | 77.09%                   | 2.98%  | 24.89%         | -21.91%       | 38.71%                        | -1.52%                          | -36.45%        |                    2.76774 |                   13.8387  | 20.22%                    | 2024-08                        | -9.16%                   | 2026-03                     | 6.68%                 |         135 |
| D           | Relative Strength Top3        | weekly      |                3 | -8.83%         | 77.09%                   | -3.53% | 24.89%         | -28.43%       | 32.26%                        | -2.08%                          | -37.13%        |                    4.37634 |                   13.129   | 28.35%                    | 2026-02                        | -14.58%                  | 2025-03                     | 6.67%                 |         135 |
| E           | Benchmark-aware Top3          | weekly      |                3 | -14.53%        | 77.09%                   | -5.93% | 24.89%         | -30.82%       | 29.03%                        | -2.30%                          | -38.70%        |                    4.39785 |                   13.1935  | 26.76%                    | 2026-02                        | -11.73%                  | 2025-03                     | 6.25%                 |         135 |
| F           | Leadership Rotation Overlay   | weekly      |                3 | -15.84%        | 77.09%                   | -6.49% | 24.89%         | -31.38%       | 38.71%                        | -2.28%                          | -42.16%        |                    4.24731 |                   12.7419  | 25.38%                    | 2026-02                        | -11.73%                  | 2024-04                     | 7.40%                 |         135 |

## Decision

- Did weekly rebalance improve excess return? No. Historical excess CAGR delta vs baseline: -26.52%; recent excess delta: -6.98%.
- Did relative strength improve excess return? No. Historical excess CAGR delta vs baseline: -24.96%; recent excess delta: -7.13%.
- Did benchmark-aware selection improve excess return? No. Historical excess CAGR delta vs baseline: -27.35%; recent excess delta: -7.13%.
- Did any policy beat BIST100 robustly? No under the current acceptance filter.
- Next paper-trading candidate: none. No policy passed both historical and recent acceptance criteria.
- Current one-month fixed hold should be kept for tracking, while weekly/relative-strength variants remain research-only.

## Acceptance Rule

A policy is only eligible if it improves both historical walk-forward excess return and the recent 2026-06 counterfactual excess return. Policies that only fix June 2026 are rejected.
