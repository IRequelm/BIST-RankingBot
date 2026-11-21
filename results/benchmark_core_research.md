# Benchmark-Core Portfolio Research

Research-only. Production tracking_state.json and live follow-up behavior are unchanged.

## Policy Results

| policy_id   | policy_name                   |   months | total_return   | bist100_total_return   | cagr   | bist100_cagr   | excess_cagr   | max_drawdown   | bist100_max_drawdown   |   sharpe_proxy | monthly_win_rate_vs_bist100   | average_monthly_excess_return   | worst_month   | worst_month_return   | best_month   | best_month_return   | average_turnover   |   total_turnover | active_allocation_average   |   active_overlay_months | transaction_cost_impact   |
|:------------|:------------------------------|---------:|:---------------|:-----------------------|:-------|:---------------|:--------------|:---------------|:-----------------------|---------------:|:------------------------------|:--------------------------------|:--------------|:---------------------|:-------------|:--------------------|:-------------------|-----------------:|:----------------------------|------------------------:|:--------------------------|
| A           | BIST100 only                  |       35 | 46.00%         | 46.00%                 | 14.03% | 14.03%         | 0.00%         | -23.72%        | -23.72%                |       0.650217 | 0.00%                         | 0.00%                           | 2026-09       | -13.92%              | 2026-01      | 18.46%              | 0.00%              |          0       | 0.00%                       |                       0 | 0.00%                     |
| B           | Current active Top3 only      |       35 | 48.09%         | 46.00%                 | 14.59% | 14.03%         | 0.56%         | -19.32%        | -23.72%                |       0.624821 | 42.86%                        | 0.10%                           | 2026-10       | -10.94%              | 2026-01      | 16.86%              | 120.95%            |         42.3333  | 100.00%                     |                      35 | 8.47%                     |
| C           | 80/20 benchmark-core          |       35 | 47.56%         | 46.00%                 | 14.45% | 14.03%         | 0.42%         | -21.76%        | -23.72%                |       0.673681 | 42.86%                        | 0.02%                           | 2026-09       | -11.99%              | 2026-01      | 18.14%              | 24.19%             |          8.46667 | 20.00%                      |                      35 | 1.69%                     |
| D           | 70/30 benchmark-core          |       35 | 48.13%         | 46.00%                 | 14.60% | 14.03%         | 0.57%         | -20.78%        | -23.72%                |       0.679759 | 42.86%                        | 0.03%                           | 2026-09       | -11.02%              | 2026-01      | 17.98%              | 36.29%             |         12.7     | 30.00%                      |                      35 | 2.54%                     |
| E           | 50/50 benchmark-core          |       35 | 48.83%         | 46.00%                 | 14.79% | 14.03%         | 0.76%         | -18.86%        | -23.72%                |       0.679926 | 42.86%                        | 0.05%                           | 2026-10       | -10.73%              | 2026-01      | 17.66%              | 60.48%             |         21.1667  | 50.00%                      |                      35 | 4.23%                     |
| F           | Conditional active overlay    |       35 | 48.21%         | 46.00%                 | 14.62% | 14.03%         | 0.60%         | -21.27%        | -23.72%                |       0.676249 | 20.00%                        | 0.04%                           | 2026-09       | -11.99%              | 2026-01      | 18.14%              | 12.19%             |          4.26667 | 7.43%                       |                      13 | 0.85%                     |
| G           | Drawdown-aware active overlay |       35 | 47.34%         | 46.00%                 | 14.39% | 14.03%         | 0.36%         | -22.86%        | -23.72%                |       0.672607 | 28.57%                        | 0.02%                           | 2026-09       | -11.98%              | 2026-01      | 18.46%              | 18.10%             |          6.33333 | 13.71%                      |                      24 | 1.27%                     |

## Decision

- Is pure active Top3 still worth paper trading? Only as a monitored sleeve. It delivered 0.56% excess CAGR versus BIST100 in this walk-forward.
- Does benchmark-core improve robustness? No. Core policies reduce active drawdown and tracking error mechanically, but must be checked against BIST100 drag.
- Best balance of CAGR, drawdown, and excess return: Policy E — 50/50 benchmark-core (CAGR 14.79%, max drawdown -18.86%, excess CAGR 0.76%).
- Best fixed benchmark-core allocation if an active sleeve must be retained: Policy E — 50/50 benchmark-core (active allocation 50.00%, excess CAGR 0.76%).
- Best dynamic benchmark-core/satellite variant: Policy E — 50/50 benchmark-core (active allocation average 50.00%, excess CAGR 0.76%).
- Next paper-trading candidate: Policy E — 50/50 benchmark-core.
- Active stock-picking should be demoted from main strategy to satellite only unless it regains persistent benchmark-relative edge.

## Acceptance Criteria

A new candidate must improve robustness versus pure active Top3 and avoid material historical underperformance versus BIST100. June 2026 improvement alone is not sufficient.
