# Benchmark-Core Portfolio Research

Research-only. Production tracking_state.json and live follow-up behavior are unchanged.

## Policy Results

| policy_id   | policy_name                   |   months | total_return   | bist100_total_return   | cagr   | bist100_cagr   | excess_cagr   | max_drawdown   | bist100_max_drawdown   |   sharpe_proxy | monthly_win_rate_vs_bist100   | average_monthly_excess_return   | worst_month   | worst_month_return   | best_month   | best_month_return   | average_turnover   |   total_turnover | active_allocation_average   |   active_overlay_months | transaction_cost_impact   |
|:------------|:------------------------------|---------:|:---------------|:-----------------------|:-------|:---------------|:--------------|:---------------|:-----------------------|---------------:|:------------------------------|:--------------------------------|:--------------|:---------------------|:-------------|:--------------------|:-------------------|-----------------:|:----------------------------|------------------------:|:--------------------------|
| A           | BIST100 only                  |       34 | 59.37%         | 59.37%                 | 18.28% | 18.28%         | 0.00%         | -17.72%        | -17.72%                |       0.809278 | 0.00%                         | 0.00%                           | 2026-09       | -13.92%              | 2026-01      | 18.46%              | 0.00%              |          0       | 0.00%                       |                       0 | 0.00%                     |
| B           | Current active Top3 only      |       34 | 66.01%         | 59.37%                 | 20.03% | 18.28%         | 1.75%         | -19.32%        | -17.72%                |       0.80048  | 44.12%                        | 0.18%                           | 2024-08       | -10.88%              | 2026-01      | 16.86%              | 120.59%            |         41       | 100.00%                     |                      34 | 8.20%                     |
| C           | 80/20 benchmark-core          |       34 | 61.93%         | 59.37%                 | 18.96% | 18.28%         | 0.68%         | -18.00%        | -17.72%                |       0.846808 | 44.12%                        | 0.04%                           | 2026-09       | -11.99%              | 2026-01      | 18.14%              | 24.12%             |          8.2     | 20.00%                      |                      34 | 1.64%                     |
| D           | 70/30 benchmark-core          |       34 | 62.98%         | 59.37%                 | 19.24% | 18.28%         | 0.96%         | -18.15%        | -17.72%                |       0.857981 | 44.12%                        | 0.05%                           | 2026-09       | -11.02%              | 2026-01      | 17.98%              | 36.18%             |         12.3     | 30.00%                      |                      34 | 2.46%                     |
| E           | 50/50 benchmark-core          |       34 | 64.63%         | 59.37%                 | 19.67% | 18.28%         | 1.39%         | -18.46%        | -17.72%                |       0.863779 | 44.12%                        | 0.09%                           | 2026-09       | -9.10%               | 2026-01      | 17.66%              | 60.29%             |         20.5     | 50.00%                      |                      34 | 4.10%                     |
| F           | Conditional active overlay    |       34 | 61.79%         | 59.37%                 | 18.92% | 18.28%         | 0.64%         | -18.54%        | -17.72%                |       0.83954  | 20.59%                        | 0.04%                           | 2026-09       | -11.99%              | 2026-01      | 18.14%              | 12.55%             |          4.26667 | 7.65%                       |                      13 | 0.85%                     |
| G           | Drawdown-aware active overlay |       34 | 61.69%         | 59.37%                 | 18.90% | 18.28%         | 0.62%         | -18.00%        | -17.72%                |       0.846167 | 29.41%                        | 0.03%                           | 2026-09       | -11.98%              | 2026-01      | 18.46%              | 17.84%             |          6.06667 | 13.53%                      |                      23 | 1.21%                     |

## Decision

- Is pure active Top3 still worth paper trading? Only as a monitored sleeve. It delivered 1.75% excess CAGR versus BIST100 in this walk-forward.
- Does benchmark-core improve robustness? No. Core policies reduce active drawdown and tracking error mechanically, but must be checked against BIST100 drag.
- Best balance of CAGR, drawdown, and excess return: Policy E — 50/50 benchmark-core (CAGR 19.67%, max drawdown -18.46%, excess CAGR 1.39%).
- Best fixed benchmark-core allocation if an active sleeve must be retained: Policy E — 50/50 benchmark-core (active allocation 50.00%, excess CAGR 1.39%).
- Best dynamic benchmark-core/satellite variant: Policy E — 50/50 benchmark-core (active allocation average 50.00%, excess CAGR 1.39%).
- Next paper-trading candidate: Policy E — 50/50 benchmark-core.
- Active stock-picking should be demoted from main strategy to satellite only unless it regains persistent benchmark-relative edge.

## Acceptance Criteria

A new candidate must improve robustness versus pure active Top3 and avoid material historical underperformance versus BIST100. June 2026 improvement alone is not sufficient.
