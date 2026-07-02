# Benchmark-Core Portfolio Research

Research-only. Production tracking_state.json and live follow-up behavior are unchanged.

## Policy Results

| policy_id   | policy_name                   |   months | total_return   | bist100_total_return   | cagr   | bist100_cagr   | excess_cagr   | max_drawdown   | bist100_max_drawdown   |   sharpe_proxy | monthly_win_rate_vs_bist100   | average_monthly_excess_return   | worst_month   | worst_month_return   | best_month   | best_month_return   | average_turnover   |   total_turnover | active_allocation_average   |   active_overlay_months | transaction_cost_impact   |
|:------------|:------------------------------|---------:|:---------------|:-----------------------|:-------|:---------------|:--------------|:---------------|:-----------------------|---------------:|:------------------------------|:--------------------------------|:--------------|:---------------------|:-------------|:--------------------|:-------------------|-----------------:|:----------------------------|------------------------:|:--------------------------|
| A           | BIST100 only                  |       30 | 88.22%         | 88.22%                 | 28.86% | 28.86%         | 0.00%         | -17.72%        | -17.72%                |       1.24802  | 0.00%                         | 0.00%                           | 2024-09       | -7.51%               | 2026-01      | 18.46%              | 0.00%              |          0       | 0.00%                       |                       0 | 0.00%                     |
| B           | Current active Top3 only      |       30 | 71.77%         | 88.22%                 | 24.22% | 28.86%         | -4.64%        | -19.32%        | -17.72%                |       0.961307 | 43.33%                        | -0.24%                          | 2024-08       | -10.88%              | 2026-01      | 16.86%              | 118.89%            |         35.6667  | 100.00%                     |                      30 | 7.13%                     |
| C           | 80/20 benchmark-core          |       30 | 85.99%         | 88.22%                 | 28.25% | 28.86%         | -0.62%        | -18.00%        | -17.72%                |       1.24331  | 43.33%                        | -0.05%                          | 2024-08       | -7.27%               | 2026-01      | 18.14%              | 23.78%             |          7.13333 | 20.00%                      |                      30 | 1.43%                     |
| D           | 70/30 benchmark-core          |       30 | 84.65%         | 88.22%                 | 27.88% | 28.86%         | -0.99%        | -18.15%        | -17.72%                |       1.22836  | 43.33%                        | -0.07%                          | 2024-08       | -7.72%               | 2026-01      | 17.98%              | 35.67%             |         10.7     | 30.00%                      |                      30 | 2.14%                     |
| E           | 50/50 benchmark-core          |       30 | 81.59%         | 88.22%                 | 27.02% | 28.86%         | -1.84%        | -18.46%        | -17.72%                |       1.17517  | 43.33%                        | -0.12%                          | 2024-08       | -8.63%               | 2026-01      | 17.66%              | 59.44%             |         17.8333  | 50.00%                      |                      30 | 3.57%                     |
| F           | Conditional active overlay    |       30 | 84.44%         | 88.22%                 | 27.82% | 28.86%         | -1.04%        | -18.54%        | -17.72%                |       1.21029  | 16.67%                        | -0.07%                          | 2024-09       | -7.55%               | 2026-01      | 18.14%              | 11.33%             |          3.4     | 7.33%                       |                      11 | 0.68%                     |
| G           | Drawdown-aware active overlay |       30 | 88.36%         | 88.22%                 | 28.90% | 28.86%         | 0.04%         | -18.00%        | -17.72%                |       1.26391  | 30.00%                        | -0.00%                          | 2024-08       | -7.27%               | 2026-01      | 18.46%              | 17.11%             |          5.13333 | 13.33%                      |                      20 | 1.03%                     |

## Decision

- Is pure active Top3 still worth paper trading? No. It delivered -4.64% excess CAGR versus BIST100 in this walk-forward.
- Does benchmark-core improve robustness? Yes. Core policies reduce active drawdown and tracking error mechanically, but must be checked against BIST100 drag.
- Best balance of CAGR, drawdown, and excess return: Policy A — BIST100 only (CAGR 28.86%, max drawdown -17.72%, excess CAGR 0.00%).
- Best fixed benchmark-core allocation if an active sleeve must be retained: Policy C — 80/20 benchmark-core (active allocation 20.00%, excess CAGR -0.62%).
- Best dynamic benchmark-core/satellite variant: Policy G — Drawdown-aware active overlay (active allocation average 13.33%, excess CAGR 0.04%).
- Next paper-trading candidate: Policy A — BIST100 only.
- Active stock-picking should be demoted from main strategy to satellite only unless it regains persistent benchmark-relative edge.

## Acceptance Criteria

A new candidate must improve robustness versus pure active Top3 and avoid material historical underperformance versus BIST100. June 2026 improvement alone is not sufficient.
