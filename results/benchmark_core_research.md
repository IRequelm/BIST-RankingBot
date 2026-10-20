# Benchmark-Core Portfolio Research

Research-only. Production tracking_state.json and live follow-up behavior are unchanged.

## Policy Results

| policy_id   | policy_name                   |   months | total_return   | bist100_total_return   | cagr   | bist100_cagr   | excess_cagr   | max_drawdown   | bist100_max_drawdown   |   sharpe_proxy | monthly_win_rate_vs_bist100   | average_monthly_excess_return   | worst_month   | worst_month_return   | best_month   | best_month_return   | average_turnover   |   total_turnover | active_allocation_average   |   active_overlay_months | transaction_cost_impact   |
|:------------|:------------------------------|---------:|:---------------|:-----------------------|:-------|:---------------|:--------------|:---------------|:-----------------------|---------------:|:------------------------------|:--------------------------------|:--------------|:---------------------|:-------------|:--------------------|:-------------------|-----------------:|:----------------------------|------------------------:|:--------------------------|
| A           | BIST100 only                  |       34 | 49.92%         | 49.92%                 | 15.59% | 15.59%         | 0.00%         | -20.46%        | -20.46%                |       0.707968 | 0.00%                         | 0.00%                           | 2026-09       | -13.92%              | 2026-01      | 18.46%              | 0.00%              |          0       | 0.00%                       |                       0 | 0.00%                     |
| B           | Current active Top3 only      |       34 | 60.42%         | 49.92%                 | 18.42% | 15.59%         | 2.83%         | -19.32%        | -20.46%                |       0.750976 | 47.06%                        | 0.26%                           | 2024-08       | -10.88%              | 2026-01      | 16.86%              | 120.59%            |         41       | 100.00%                     |                      34 | 8.20%                     |
| C           | 80/20 benchmark-core          |       34 | 53.15%         | 49.92%                 | 16.47% | 15.59%         | 0.89%         | -18.00%        | -20.46%                |       0.751496 | 47.06%                        | 0.05%                           | 2026-09       | -11.99%              | 2026-01      | 18.14%              | 24.12%             |          8.2     | 20.00%                      |                      34 | 1.64%                     |
| D           | 70/30 benchmark-core          |       34 | 54.57%         | 49.92%                 | 16.86% | 15.59%         | 1.27%         | -18.15%        | -20.46%                |       0.766938 | 47.06%                        | 0.08%                           | 2026-09       | -11.02%              | 2026-01      | 17.98%              | 36.18%             |         12.3     | 30.00%                      |                      34 | 2.46%                     |
| E           | 50/50 benchmark-core          |       34 | 56.97%         | 49.92%                 | 17.50% | 15.59%         | 1.92%         | -18.46%        | -20.46%                |       0.783361 | 47.06%                        | 0.13%                           | 2026-09       | -9.10%               | 2026-01      | 17.66%              | 60.29%             |         20.5     | 50.00%                      |                      34 | 4.10%                     |
| F           | Conditional active overlay    |       34 | 52.19%         | 49.92%                 | 16.21% | 15.59%         | 0.62%         | -18.54%        | -20.46%                |       0.735917 | 20.59%                        | 0.04%                           | 2026-09       | -11.99%              | 2026-01      | 18.14%              | 12.55%             |          4.26667 | 7.65%                       |                      13 | 0.85%                     |
| G           | Drawdown-aware active overlay |       34 | 52.92%         | 49.92%                 | 16.41% | 15.59%         | 0.82%         | -19.06%        | -20.46%                |       0.750592 | 32.35%                        | 0.05%                           | 2026-09       | -11.98%              | 2026-01      | 18.46%              | 17.84%             |          6.06667 | 13.53%                      |                      23 | 1.21%                     |

## Decision

- Is pure active Top3 still worth paper trading? Only as a monitored sleeve. It delivered 2.83% excess CAGR versus BIST100 in this walk-forward.
- Does benchmark-core improve robustness? No. Core policies reduce active drawdown and tracking error mechanically, but must be checked against BIST100 drag.
- Best balance of CAGR, drawdown, and excess return: Policy E — 50/50 benchmark-core (CAGR 17.50%, max drawdown -18.46%, excess CAGR 1.92%).
- Best fixed benchmark-core allocation if an active sleeve must be retained: Policy E — 50/50 benchmark-core (active allocation 50.00%, excess CAGR 1.92%).
- Best dynamic benchmark-core/satellite variant: Policy E — 50/50 benchmark-core (active allocation average 50.00%, excess CAGR 1.92%).
- Next paper-trading candidate: Policy E — 50/50 benchmark-core.
- Active stock-picking should be demoted from main strategy to satellite only unless it regains persistent benchmark-relative edge.

## Acceptance Criteria

A new candidate must improve robustness versus pure active Top3 and avoid material historical underperformance versus BIST100. June 2026 improvement alone is not sufficient.
