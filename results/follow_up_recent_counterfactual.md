# Follow-Up Recent Counterfactual

Period: 2026-06-01 to latest available BIST100 close. Signals use only data available at each rebalance date.

## Cumulative Results

| policy_id   | policy_name                   | cumulative_return   | cumulative_benchmark_return   | cumulative_excess_return   | selected_symbols                                 |
|:------------|:------------------------------|:--------------------|:------------------------------|:---------------------------|:-------------------------------------------------|
| A           | Current fixed follow-up state | 1.73%               | 4.16%                         | -2.43%                     | EREGL.IS, SISE.IS, BIMAS.IS                      |
| B           | Weekly rebalance Top3         | 1.85%               | 4.16%                         | -2.31%                     | AKBNK.IS, YKBNK.IS, BIMAS.IS                     |
| C           | Weekly rebalance Top5         | 2.15%               | 4.16%                         | -2.01%                     | AKBNK.IS, YKBNK.IS, BIMAS.IS, ASELS.IS, TOASO.IS |
| D           | Relative Strength Top3        | 3.00%               | 4.16%                         | -1.16%                     | YKBNK.IS, AKBNK.IS, TOASO.IS                     |
| E           | Benchmark-aware Top3          | 3.00%               | 4.16%                         | -1.16%                     | YKBNK.IS, AKBNK.IS, TOASO.IS                     |
| F           | Leadership Rotation Overlay   | 3.68%               | 4.16%                         | -0.48%                     | YKBNK.IS, AKBNK.IS, GARAN.IS                     |

## Rebalance Paths

| policy_id   | policy_name                   | start_date          | end_date            | selected_symbols                                 | gross_return   | net_return   | benchmark_return   | excess_return   | cumulative_return   | cumulative_excess_return   | turnover   |   trades |
|:------------|:------------------------------|:--------------------|:--------------------|:-------------------------------------------------|:---------------|:-------------|:-------------------|:----------------|:--------------------|:---------------------------|:-----------|---------:|
| A           | Current fixed follow-up state | 2026-06-01 00:00:00 | 2026-06-26 00:00:00 | EREGL.IS, SISE.IS, BIMAS.IS                      | 1.93%          | 1.73%        | 4.16%              | -2.43%          | 1.73%               | -2.43%                     | 100.00%    |        3 |
| B           | Weekly rebalance Top3         | 2026-06-01 00:00:00 | 2026-06-08 00:00:00 | EREGL.IS, SISE.IS, BIMAS.IS                      | -0.19%         | -0.39%       | 1.14%              | -1.53%          | -0.39%              | -1.53%                     | 100.00%    |        3 |
| B           | Weekly rebalance Top3         | 2026-06-08 00:00:00 | 2026-06-15 00:00:00 | BIMAS.IS, EREGL.IS, SISE.IS                      | 3.51%          | 3.51%        | 4.23%              | -0.72%          | 3.11%               | -2.31%                     | 0.00%      |        0 |
| B           | Weekly rebalance Top3         | 2026-06-15 00:00:00 | 2026-06-22 00:00:00 | BIMAS.IS, YKBNK.IS, AKBNK.IS                     | 3.96%          | 3.70%        | 1.96%              | 1.74%           | 6.92%               | -0.56%                     | 133.33%    |        4 |
| B           | Weekly rebalance Top3         | 2026-06-22 00:00:00 | 2026-06-26 00:00:00 | AKBNK.IS, YKBNK.IS, BIMAS.IS                     | -4.74%         | -4.74%       | -3.09%             | -1.65%          | 1.85%               | -2.31%                     | 0.00%      |        0 |
| C           | Weekly rebalance Top5         | 2026-06-01 00:00:00 | 2026-06-08 00:00:00 | EREGL.IS, SISE.IS, BIMAS.IS, TOASO.IS, TCELL.IS  | 0.49%          | 0.29%        | 1.14%              | -0.86%          | 0.29%               | -0.86%                     | 100.00%    |        5 |
| C           | Weekly rebalance Top5         | 2026-06-08 00:00:00 | 2026-06-15 00:00:00 | BIMAS.IS, EREGL.IS, SISE.IS, TCELL.IS, TOASO.IS  | 5.17%          | 5.17%        | 4.23%              | 0.94%           | 5.47%               | 0.05%                      | 0.00%      |        0 |
| C           | Weekly rebalance Top5         | 2026-06-15 00:00:00 | 2026-06-22 00:00:00 | BIMAS.IS, YKBNK.IS, AKBNK.IS, THYAO.IS, SAHOL.IS | 2.38%          | 2.06%        | 1.96%              | 0.09%           | 7.64%               | 0.15%                      | 160.00%    |        8 |
| C           | Weekly rebalance Top5         | 2026-06-22 00:00:00 | 2026-06-26 00:00:00 | AKBNK.IS, YKBNK.IS, BIMAS.IS, ASELS.IS, TOASO.IS | -4.94%         | -5.10%       | -3.09%             | -2.00%          | 2.15%               | -2.01%                     | 80.00%     |        4 |
| D           | Relative Strength Top3        | 2026-06-01 00:00:00 | 2026-06-08 00:00:00 | EREGL.IS, SISE.IS, TOASO.IS                      | -1.29%         | -1.49%       | 1.14%              | -2.63%          | -1.49%              | -2.63%                     | 100.00%    |        3 |
| D           | Relative Strength Top3        | 2026-06-08 00:00:00 | 2026-06-15 00:00:00 | BIMAS.IS, EREGL.IS, GARAN.IS                     | 5.50%          | 5.24%        | 4.23%              | 1.01%           | 3.67%               | -1.75%                     | 133.33%    |        4 |
| D           | Relative Strength Top3        | 2026-06-15 00:00:00 | 2026-06-22 00:00:00 | YKBNK.IS, AKBNK.IS, SAHOL.IS                     | 5.16%          | 4.76%        | 1.96%              | 2.80%           | 8.61%               | 1.12%                      | 200.00%    |        6 |
| D           | Relative Strength Top3        | 2026-06-22 00:00:00 | 2026-06-26 00:00:00 | YKBNK.IS, AKBNK.IS, TOASO.IS                     | -5.03%         | -5.16%       | -3.09%             | -2.07%          | 3.00%               | -1.16%                     | 66.67%     |        2 |
| E           | Benchmark-aware Top3          | 2026-06-01 00:00:00 | 2026-06-08 00:00:00 | EREGL.IS, SISE.IS, TOASO.IS                      | -1.29%         | -1.49%       | 1.14%              | -2.63%          | -1.49%              | -2.63%                     | 100.00%    |        3 |
| E           | Benchmark-aware Top3          | 2026-06-08 00:00:00 | 2026-06-15 00:00:00 | BIMAS.IS, EREGL.IS, GARAN.IS                     | 5.50%          | 5.24%        | 4.23%              | 1.01%           | 3.67%               | -1.75%                     | 133.33%    |        4 |
| E           | Benchmark-aware Top3          | 2026-06-15 00:00:00 | 2026-06-22 00:00:00 | YKBNK.IS, AKBNK.IS, SAHOL.IS                     | 5.16%          | 4.76%        | 1.96%              | 2.80%           | 8.61%               | 1.12%                      | 200.00%    |        6 |
| E           | Benchmark-aware Top3          | 2026-06-22 00:00:00 | 2026-06-26 00:00:00 | YKBNK.IS, AKBNK.IS, TOASO.IS                     | -5.03%         | -5.16%       | -3.09%             | -2.07%          | 3.00%               | -1.16%                     | 66.67%     |        2 |
| F           | Leadership Rotation Overlay   | 2026-06-01 00:00:00 | 2026-06-08 00:00:00 | EREGL.IS, SISE.IS, BIMAS.IS                      | -0.19%         | -0.39%       | 1.14%              | -1.53%          | -0.39%              | -1.53%                     | 100.00%    |        3 |
| F           | Leadership Rotation Overlay   | 2026-06-08 00:00:00 | 2026-06-15 00:00:00 | BIMAS.IS, EREGL.IS, GARAN.IS                     | 5.50%          | 5.37%        | 4.23%              | 1.14%           | 4.96%               | -0.45%                     | 66.67%     |        2 |
| F           | Leadership Rotation Overlay   | 2026-06-15 00:00:00 | 2026-06-22 00:00:00 | YKBNK.IS, AKBNK.IS, SAHOL.IS                     | 5.16%          | 4.76%        | 1.96%              | 2.80%           | 9.96%               | 2.48%                      | 200.00%    |        6 |
| F           | Leadership Rotation Overlay   | 2026-06-22 00:00:00 | 2026-06-26 00:00:00 | YKBNK.IS, AKBNK.IS, GARAN.IS                     | -5.58%         | -5.71%       | -3.09%             | -2.62%          | 3.68%               | -0.48%                     | 66.67%     |        2 |

## Rotation Check

Use the selected_symbols column to inspect whether the weekly policies rotated away from the original EREGL/SISE/BIMAS basket and into the stronger bank or large-cap leadership names.
