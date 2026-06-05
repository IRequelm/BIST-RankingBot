# Final Performance Gap Analysis

## Question

What is preventing the strategy from beating BIST100?

## Short Answer

The current production-style replay is losing mostly because the opportunity filter creates too much CASH during strong BIST100 rallies. When the opportunity filter is removed and the bot is forced into a concentrated Top3 portfolio with the regime filter ON, the strategy does beat BIST100 in this 30-month replay window. The remaining issue is consistency: the best policy has higher CAGR than BIST100, but wins only 46.67% of months and depends on concentrated upside months.

## Current Baseline

- Replay months: 30
- Strategy CAGR: 11.17%
- BIST100 CAGR: 22.86%
- Excess CAGR: -11.69%
- Average excess return: -0.99%
- Win rate vs BIST100: 36.67%
- Average cash allocation: 49.33%

## Research Grid

Opportunity filter was removed completely for all tests. The grid tested Top3 / Top5 / Top10, fixed cash caps of 0%, 10%, 20%, 30%, and regime filter ON/OFF.

|   top_n |   cash_cap | regime   |   strategy_cagr |   bist100_cagr |   excess_cagr |   avg_excess |   win_rate |   max_drawdown |   avg_cash | best_month   |   best_excess | worst_month   |   worst_excess |
|--------:|-----------:|:---------|----------------:|---------------:|--------------:|-------------:|-----------:|---------------:|-----------:|:-------------|--------------:|:--------------|---------------:|
|       3 |     0.0000 | ON       |          0.2679 |         0.2286 |        0.0393 |       0.0035 |     0.4667 |        -0.1517 |     0.0000 | 2025-03      |        0.1540 | 2024-03       |        -0.1019 |
|       3 |     0.1000 | ON       |          0.2679 |         0.2286 |        0.0393 |       0.0035 |     0.4667 |        -0.1517 |     0.0000 | 2025-03      |        0.1540 | 2024-03       |        -0.1019 |
|       3 |     0.2000 | ON       |          0.2679 |         0.2286 |        0.0393 |       0.0035 |     0.4667 |        -0.1517 |     0.0000 | 2025-03      |        0.1540 | 2024-03       |        -0.1019 |
|       3 |     0.3000 | ON       |          0.2679 |         0.2286 |        0.0393 |       0.0035 |     0.4667 |        -0.1517 |     0.0000 | 2025-03      |        0.1540 | 2024-03       |        -0.1019 |
|       5 |     0.0000 | OFF      |          0.2539 |         0.2286 |        0.0253 |       0.0021 |     0.5000 |        -0.1827 |     0.0000 | 2025-01      |        0.1068 | 2024-02       |        -0.0734 |
|       5 |     0.1000 | OFF      |          0.2539 |         0.2286 |        0.0253 |       0.0021 |     0.5000 |        -0.1827 |     0.0000 | 2025-01      |        0.1068 | 2024-02       |        -0.0734 |
|       5 |     0.2000 | OFF      |          0.2539 |         0.2286 |        0.0253 |       0.0021 |     0.5000 |        -0.1827 |     0.0000 | 2025-01      |        0.1068 | 2024-02       |        -0.0734 |
|       5 |     0.3000 | OFF      |          0.2539 |         0.2286 |        0.0253 |       0.0021 |     0.5000 |        -0.1827 |     0.0000 | 2025-01      |        0.1068 | 2024-02       |        -0.0734 |
|       5 |     0.0000 | ON       |          0.2295 |         0.2286 |        0.0009 |       0.0004 |     0.4000 |        -0.1380 |     0.0000 | 2025-01      |        0.1068 | 2024-02       |        -0.0734 |
|       5 |     0.1000 | ON       |          0.2295 |         0.2286 |        0.0009 |       0.0004 |     0.4000 |        -0.1380 |     0.0000 | 2025-01      |        0.1068 | 2024-02       |        -0.0734 |
|       5 |     0.2000 | ON       |          0.2295 |         0.2286 |        0.0009 |       0.0004 |     0.4000 |        -0.1380 |     0.0000 | 2025-01      |        0.1068 | 2024-02       |        -0.0734 |
|       5 |     0.3000 | ON       |          0.2295 |         0.2286 |        0.0009 |       0.0004 |     0.4000 |        -0.1380 |     0.0000 | 2025-01      |        0.1068 | 2024-02       |        -0.0734 |
|       3 |     0.0000 | OFF      |          0.2273 |         0.2286 |       -0.0013 |       0.0005 |     0.5000 |        -0.1934 |     0.0000 | 2025-01      |        0.1018 | 2024-03       |        -0.1019 |
|       3 |     0.1000 | OFF      |          0.2273 |         0.2286 |       -0.0013 |       0.0005 |     0.5000 |        -0.1934 |     0.0000 | 2025-01      |        0.1018 | 2024-03       |        -0.1019 |
|       3 |     0.2000 | OFF      |          0.2273 |         0.2286 |       -0.0013 |       0.0005 |     0.5000 |        -0.1934 |     0.0000 | 2025-01      |        0.1018 | 2024-03       |        -0.1019 |
|       3 |     0.3000 | OFF      |          0.2273 |         0.2286 |       -0.0013 |       0.0005 |     0.5000 |        -0.1934 |     0.0000 | 2025-01      |        0.1018 | 2024-03       |        -0.1019 |
|      10 |     0.0000 | OFF      |          0.2100 |         0.2286 |       -0.0186 |      -0.0010 |     0.5333 |        -0.1866 |     0.0000 | 2025-01      |        0.0373 | 2024-10       |        -0.0358 |
|      10 |     0.1000 | OFF      |          0.2100 |         0.2286 |       -0.0186 |      -0.0010 |     0.5333 |        -0.1866 |     0.0000 | 2025-01      |        0.0373 | 2024-10       |        -0.0358 |
|      10 |     0.2000 | OFF      |          0.2100 |         0.2286 |       -0.0186 |      -0.0010 |     0.5333 |        -0.1866 |     0.0000 | 2025-01      |        0.0373 | 2024-10       |        -0.0358 |
|      10 |     0.3000 | OFF      |          0.2100 |         0.2286 |       -0.0186 |      -0.0010 |     0.5333 |        -0.1866 |     0.0000 | 2025-01      |        0.0373 | 2024-10       |        -0.0358 |
|      10 |     0.0000 | ON       |          0.1877 |         0.2286 |       -0.0409 |      -0.0029 |     0.4667 |        -0.1679 |     0.0000 | 2025-01      |        0.0373 | 2024-11       |        -0.0325 |
|      10 |     0.1000 | ON       |          0.1877 |         0.2286 |       -0.0409 |      -0.0029 |     0.4667 |        -0.1679 |     0.0000 | 2025-01      |        0.0373 | 2024-11       |        -0.0325 |
|      10 |     0.2000 | ON       |          0.1877 |         0.2286 |       -0.0409 |      -0.0029 |     0.4667 |        -0.1679 |     0.0000 | 2025-01      |        0.0373 | 2024-11       |        -0.0325 |
|      10 |     0.3000 | ON       |          0.1877 |         0.2286 |       -0.0409 |      -0.0029 |     0.4667 |        -0.1679 |     0.0000 | 2025-01      |        0.0373 | 2024-11       |        -0.0325 |

## Best Tested Policy

- TopN: Top3
- Cash cap: 0.00%
- Regime filter: ON
- Strategy CAGR: 26.79%
- BIST100 CAGR: 22.86%
- Excess CAGR: 3.93%
- Win rate: 46.67%
- Max drawdown: -15.17%

## Findings

- Removing the opportunity filter is the key improvement. It turns the best tested policy from underperforming to beating BIST100 by CAGR.
- With opportunity filter removed, cash caps do not matter because TopN is always fully invested; average cash remains 0%.
- Top3 with regime filter ON is the best tested policy: 26.79% CAGR vs 22.86% for BIST100.
- Top5 with regime filter OFF also beats BIST100, but by a smaller margin: 25.39% CAGR vs 22.86%.
- Top10 underperforms, so adding more names dilutes the strongest ranking signals in this replay window.
- Cash caps are irrelevant once the opportunity filter is removed, because the tested TopN portfolios stay fully invested.

## What Is Preventing BIST100 Outperformance?

The opportunity filter/cash layer is the main blocker in the current strategy. It cuts exposure too aggressively, leaving roughly half the capital in cash while BIST100 rallies. Once that layer is removed, the ranking signal has enough edge only in a concentrated Top3 form. The strategy still does not beat BIST100 consistently month by month, so the next bottleneck is signal reliability: the bot needs a rule that keeps Top3 upside while reducing the large losing months.
