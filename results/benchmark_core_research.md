# Benchmark-Core Portfolio Research

Research-only. Production tracking_state.json and live follow-up behavior are unchanged.

## Policy Results

| policy_id   | policy_name                   |   months | total_return   | bist100_total_return   | cagr   | bist100_cagr   | excess_cagr   | max_drawdown   | bist100_max_drawdown   |   sharpe_proxy | monthly_win_rate_vs_bist100   | average_monthly_excess_return   | worst_month   | worst_month_return   | best_month   | best_month_return   | average_turnover   |   total_turnover | active_allocation_average   |   active_overlay_months | transaction_cost_impact   |
|:------------|:------------------------------|---------:|:---------------|:-----------------------|:-------|:---------------|:--------------|:---------------|:-----------------------|---------------:|:------------------------------|:--------------------------------|:--------------|:---------------------|:-------------|:--------------------|:-------------------|-----------------:|:----------------------------|------------------------:|:--------------------------|
| A           | BIST100 only                  |       35 | 50.55%         | 50.55%                 | 15.50% | 15.50%         | 0.00%         | -23.72%        | -23.72%                |       0.692329 | 0.00%                         | 0.00%                           | 2026-09       | -13.92%              | 2026-01      | 18.46%              | 0.00%              |          0       | 0.00%                       |                       0 | 0.00%                     |
| B           | Current active Top3 only      |       35 | 54.14%         | 50.55%                 | 16.46% | 15.50%         | 0.96%         | -19.32%        | -23.72%                |       0.675811 | 42.86%                        | 0.13%                           | 2026-10       | -10.94%              | 2026-01      | 16.86%              | 120.95%            |         42.3333  | 100.00%                     |                      35 | 8.47%                     |
| C           | 80/20 benchmark-core          |       35 | 52.44%         | 50.55%                 | 16.01% | 15.50%         | 0.51%         | -21.76%        | -23.72%                |       0.719498 | 42.86%                        | 0.03%                           | 2026-09       | -11.99%              | 2026-01      | 18.14%              | 24.19%             |          8.46667 | 20.00%                      |                      35 | 1.69%                     |
| D           | 70/30 benchmark-core          |       35 | 53.17%         | 50.55%                 | 16.20% | 15.50%         | 0.70%         | -20.78%        | -23.72%                |       0.727139 | 42.86%                        | 0.04%                           | 2026-09       | -11.02%              | 2026-01      | 17.98%              | 36.29%             |         12.7     | 30.00%                      |                      35 | 2.54%                     |
| E           | 50/50 benchmark-core          |       35 | 54.18%         | 50.55%                 | 16.47% | 15.50%         | 0.97%         | -18.86%        | -23.72%                |       0.729674 | 42.86%                        | 0.06%                           | 2026-10       | -10.73%              | 2026-01      | 17.66%              | 60.48%             |         21.1667  | 50.00%                      |                      35 | 4.23%                     |
| F           | Conditional active overlay    |       35 | 52.83%         | 50.55%                 | 16.11% | 15.50%         | 0.61%         | -21.27%        | -23.72%                |       0.718789 | 20.00%                        | 0.04%                           | 2026-09       | -11.99%              | 2026-01      | 18.14%              | 12.19%             |          4.26667 | 7.43%                       |                      13 | 0.85%                     |
| G           | Drawdown-aware active overlay |       35 | 52.21%         | 50.55%                 | 15.95% | 15.50%         | 0.45%         | -22.86%        | -23.72%                |       0.718528 | 28.57%                        | 0.02%                           | 2026-09       | -11.98%              | 2026-01      | 18.46%              | 18.10%             |          6.33333 | 13.71%                      |                      24 | 1.27%                     |

## Decision

- Is pure active Top3 still worth paper trading? Only as a monitored sleeve. It delivered 0.96% excess CAGR versus BIST100 in this walk-forward.
- Does benchmark-core improve robustness? No. Core policies reduce active drawdown and tracking error mechanically, but must be checked against BIST100 drag.
- Best balance of CAGR, drawdown, and excess return: Policy E — 50/50 benchmark-core (CAGR 16.47%, max drawdown -18.86%, excess CAGR 0.97%).
- Best fixed benchmark-core allocation if an active sleeve must be retained: Policy E — 50/50 benchmark-core (active allocation 50.00%, excess CAGR 0.97%).
- Best dynamic benchmark-core/satellite variant: Policy E — 50/50 benchmark-core (active allocation average 50.00%, excess CAGR 0.97%).
- Next paper-trading candidate: Policy E — 50/50 benchmark-core.
- Active stock-picking should be demoted from main strategy to satellite only unless it regains persistent benchmark-relative edge.

## Acceptance Criteria

A new candidate must improve robustness versus pure active Top3 and avoid material historical underperformance versus BIST100. June 2026 improvement alone is not sufficient.
