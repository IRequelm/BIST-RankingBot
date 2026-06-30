# Benchmark-Core Portfolio Research

Research-only. Production tracking_state.json and live follow-up behavior are unchanged.

## Policy Results

| policy_id   | policy_name                   |   months | total_return   | bist100_total_return   | cagr   | bist100_cagr   | excess_cagr   | max_drawdown   | bist100_max_drawdown   |   sharpe_proxy | monthly_win_rate_vs_bist100   | average_monthly_excess_return   | worst_month   | worst_month_return   | best_month   | best_month_return   | average_turnover   |   total_turnover | active_allocation_average   |   active_overlay_months | transaction_cost_impact   |
|:------------|:------------------------------|---------:|:---------------|:-----------------------|:-------|:---------------|:--------------|:---------------|:-----------------------|---------------:|:------------------------------|:--------------------------------|:--------------|:---------------------|:-------------|:--------------------|:-------------------|-----------------:|:----------------------------|------------------------:|:--------------------------|
| A           | BIST100 only                  |       30 | 86.03%         | 86.03%                 | 28.33% | 28.33%         | 0.00%         | -17.72%        | -17.72%                |       1.22839  | 0.00%                         | 0.00%                           | 2024-09       | -7.51%               | 2026-01      | 18.46%              | 0.00%              |          0       | 0.00%                       |                       0 | 0.00%                     |
| B           | Current active Top3 only      |       30 | 73.99%         | 86.03%                 | 24.92% | 28.33%         | -3.40%        | -19.32%        | -17.72%                |       0.982466 | 43.33%                        | -0.15%                          | 2024-08       | -10.88%              | 2026-01      | 16.86%              | 118.89%            |         35.6667  | 100.00%                     |                      30 | 7.13%                     |
| C           | 80/20 benchmark-core          |       30 | 84.69%         | 86.03%                 | 27.96% | 28.33%         | -0.37%        | -18.00%        | -17.72%                |       1.23102  | 43.33%                        | -0.03%                          | 2024-08       | -7.27%               | 2026-01      | 18.14%              | 23.78%             |          7.13333 | 20.00%                      |                      30 | 1.43%                     |
| D           | 70/30 benchmark-core          |       30 | 83.81%         | 86.03%                 | 27.71% | 28.33%         | -0.62%        | -18.15%        | -17.72%                |       1.22019  | 43.33%                        | -0.05%                          | 2024-08       | -7.72%               | 2026-01      | 17.98%              | 35.67%             |         10.7     | 30.00%                      |                      30 | 2.14%                     |
| E           | 50/50 benchmark-core          |       30 | 81.65%         | 86.03%                 | 27.10% | 28.33%         | -1.22%        | -18.46%        | -17.72%                |       1.17576  | 43.33%                        | -0.08%                          | 2024-08       | -8.63%               | 2026-01      | 17.66%              | 59.44%             |         17.8333  | 50.00%                      |                      30 | 3.57%                     |
| F           | Conditional active overlay    |       30 | 83.16%         | 86.03%                 | 27.53% | 28.33%         | -0.80%        | -18.54%        | -17.72%                |       1.1982   | 16.67%                        | -0.05%                          | 2024-09       | -7.55%               | 2026-01      | 18.14%              | 11.33%             |          3.4     | 7.33%                       |                      11 | 0.68%                     |
| G           | Drawdown-aware active overlay |       30 | 87.05%         | 86.03%                 | 28.61% | 28.33%         | 0.28%         | -18.00%        | -17.72%                |       1.25163  | 30.00%                        | 0.01%                           | 2024-08       | -7.27%               | 2026-01      | 18.46%              | 17.11%             |          5.13333 | 13.33%                      |                      20 | 1.03%                     |

## Decision

- Is pure active Top3 still worth paper trading? No. It delivered -3.40% excess CAGR versus BIST100 in this walk-forward.
- Does benchmark-core improve robustness? Yes. Core policies reduce active drawdown and tracking error mechanically, but must be checked against BIST100 drag.
- Best balance of CAGR, drawdown, and excess return: Policy G — Drawdown-aware active overlay (CAGR 28.61%, max drawdown -18.00%, excess CAGR 0.28%).
- Best fixed benchmark-core allocation if an active sleeve must be retained: Policy C — 80/20 benchmark-core (active allocation 20.00%, excess CAGR -0.37%).
- Best dynamic benchmark-core/satellite variant: Policy G — Drawdown-aware active overlay (active allocation average 13.33%, excess CAGR 0.28%).
- Next paper-trading candidate: Policy G — Drawdown-aware active overlay.
- Active stock-picking should be demoted from main strategy to satellite only unless it regains persistent benchmark-relative edge.

## Acceptance Criteria

A new candidate must improve robustness versus pure active Top3 and avoid material historical underperformance versus BIST100. June 2026 improvement alone is not sufficient.
