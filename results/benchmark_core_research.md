# Benchmark-Core Portfolio Research

Research-only. Production tracking_state.json and live follow-up behavior are unchanged.

## Policy Results

| policy_id   | policy_name                   |   months | total_return   | bist100_total_return   | cagr   | bist100_cagr   | excess_cagr   | max_drawdown   | bist100_max_drawdown   |   sharpe_proxy | monthly_win_rate_vs_bist100   | average_monthly_excess_return   | worst_month   | worst_month_return   | best_month   | best_month_return   | average_turnover   |   total_turnover | active_allocation_average   |   active_overlay_months | transaction_cost_impact   |
|:------------|:------------------------------|---------:|:---------------|:-----------------------|:-------|:---------------|:--------------|:---------------|:-----------------------|---------------:|:------------------------------|:--------------------------------|:--------------|:---------------------|:-------------|:--------------------|:-------------------|-----------------:|:----------------------------|------------------------:|:--------------------------|
| A           | BIST100 only                  |       32 | 85.36%         | 85.36%                 | 26.65% | 26.65%         | 0.00%         | -17.72%        | -17.72%                |       1.14863  | 0.00%                         | 0.00%                           | 2024-09       | -7.51%               | 2026-01      | 18.46%              | 0.00%              |          0       | 0.00%                       |                       0 | 0.00%                     |
| B           | Current active Top3 only      |       32 | 81.73%         | 85.36%                 | 25.70% | 26.65%         | -0.96%        | -19.32%        | -17.72%                |       0.985026 | 46.88%                        | 0.02%                           | 2024-08       | -10.88%              | 2026-01      | 16.86%              | 119.79%            |         38.3333  | 100.00%                     |                      32 | 7.67%                     |
| C           | 80/20 benchmark-core          |       32 | 85.85%         | 85.36%                 | 26.78% | 26.65%         | 0.13%         | -18.00%        | -17.72%                |       1.16629  | 46.88%                        | 0.00%                           | 2024-08       | -7.27%               | 2026-01      | 18.14%              | 23.96%             |          7.66667 | 20.00%                      |                      32 | 1.53%                     |
| D           | 70/30 benchmark-core          |       32 | 85.87%         | 85.36%                 | 26.78% | 26.65%         | 0.13%         | -18.15%        | -17.72%                |       1.16372  | 46.88%                        | 0.00%                           | 2024-08       | -7.72%               | 2026-01      | 17.98%              | 35.94%             |         11.5     | 30.00%                      |                      32 | 2.30%                     |
| E           | 50/50 benchmark-core          |       32 | 85.43%         | 85.36%                 | 26.67% | 26.65%         | 0.02%         | -18.46%        | -17.72%                |       1.13665  | 46.88%                        | 0.01%                           | 2024-08       | -8.63%               | 2026-01      | 17.66%              | 59.90%             |         19.1667  | 50.00%                      |                      32 | 3.83%                     |
| F           | Conditional active overlay    |       32 | 83.72%         | 85.36%                 | 26.22% | 26.65%         | -0.43%        | -18.54%        | -17.72%                |       1.12946  | 18.75%                        | -0.03%                          | 2024-09       | -7.55%               | 2026-01      | 18.14%              | 11.88%             |          3.8     | 7.50%                       |                      12 | 0.76%                     |
| G           | Drawdown-aware active overlay |       32 | 88.22%         | 85.36%                 | 27.40% | 26.65%         | 0.75%         | -18.00%        | -17.72%                |       1.18558  | 34.38%                        | 0.04%                           | 2024-08       | -7.27%               | 2026-01      | 18.46%              | 17.71%             |          5.66667 | 13.75%                      |                      22 | 1.13%                     |

## Decision

- Is pure active Top3 still worth paper trading? No. It delivered -0.96% excess CAGR versus BIST100 in this walk-forward.
- Does benchmark-core improve robustness? Yes. Core policies reduce active drawdown and tracking error mechanically, but must be checked against BIST100 drag.
- Best balance of CAGR, drawdown, and excess return: Policy G — Drawdown-aware active overlay (CAGR 27.40%, max drawdown -18.00%, excess CAGR 0.75%).
- Best fixed benchmark-core allocation if an active sleeve must be retained: Policy C — 80/20 benchmark-core (active allocation 20.00%, excess CAGR 0.13%).
- Best dynamic benchmark-core/satellite variant: Policy G — Drawdown-aware active overlay (active allocation average 13.75%, excess CAGR 0.75%).
- Next paper-trading candidate: Policy G — Drawdown-aware active overlay.
- Active stock-picking should be demoted from main strategy to satellite only unless it regains persistent benchmark-relative edge.

## Acceptance Criteria

A new candidate must improve robustness versus pure active Top3 and avoid material historical underperformance versus BIST100. June 2026 improvement alone is not sufficient.
