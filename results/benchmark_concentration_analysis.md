# Benchmark Concentration Analysis

## Scope Note

This analysis uses the project's available cached BIST universe, not the full official BIST100 constituent and free-float market-cap history. Market-cap groups are therefore proxies built from the large-cap names available in the bot data cache.

- Top 5 proxy stocks: GARAN.IS, ASELS.IS, THYAO.IS, KCHOL.IS, AKBNK.IS
- Top 10 proxy stocks: GARAN.IS, ASELS.IS, THYAO.IS, KCHOL.IS, AKBNK.IS, ISCTR.IS, BIMAS.IS, TUPRS.IS, TCELL.IS, YKBNK.IS
- Remaining proxy stocks: FROTO.IS, SAHOL.IS, EREGL.IS, SISE.IS, PGSUS.IS, TOASO.IS, ARCLK.IS, PETKM.IS

## Direct Answer

B) benchmark returns are materially influenced by mega-cap leadership, but A) strategy selection is also weak versus the large-cap basket.

The strategy underperforms because it misses large-cap/index leadership. The benchmark is not simply unbeatable because of one or two names, but the large-cap proxy beats the strategy and tracks BIST100 better than the bot portfolio.

## Portfolio Comparison

| portfolio                         |   months |   cagr |   bist100_cagr |   excess_cagr |   avg_monthly_return |   avg_excess |   win_rate_vs_bist100 |   max_drawdown |   correlation_to_bist100 | best_month   |   best_excess | worst_month   |   worst_excess |
|:----------------------------------|---------:|-------:|---------------:|--------------:|---------------------:|-------------:|----------------------:|---------------:|-------------------------:|:-------------|--------------:|:--------------|---------------:|
| Top 5 market-cap proxy            |       30 | 0.4121 |         0.2286 |        0.1835 |               0.0321 |       0.0127 |                0.5667 |        -0.1835 |                   0.9024 | 2024-03      |        0.1338 | 2025-10       |        -0.0378 |
| Top 10 market-cap proxy           |       30 | 0.3600 |         0.2286 |        0.1314 |               0.0288 |       0.0094 |                0.5667 |        -0.2038 |                   0.9110 | 2024-03      |        0.1050 | 2024-02       |        -0.0377 |
| Cap-weight proxy BIST100          |       30 | 0.2864 |         0.2286 |        0.0578 |               0.0236 |       0.0041 |                0.4667 |        -0.2001 |                   0.9506 | 2024-03      |        0.0649 | 2026-04       |        -0.0401 |
| Equal weight available BIST proxy |       30 | 0.2512 |         0.2286 |        0.0226 |               0.0210 |       0.0016 |                0.5000 |        -0.1984 |                   0.9614 | 2024-03      |        0.0455 | 2026-04       |        -0.0424 |
| Remaining available stocks        |       30 | 0.1186 |         0.2286 |       -0.1100 |               0.0114 |      -0.0081 |                0.3667 |        -0.2054 |                   0.9187 | 2025-03      |        0.0387 | 2025-11       |        -0.0523 |
| Strategy baseline replay          |       30 | 0.1117 |         0.2286 |       -0.1169 |               0.0095 |      -0.0099 |                0.3667 |        -0.0879 |                   0.7756 | 2024-09      |        0.0866 | 2025-06       |        -0.1097 |

## Market-Cap Group Contribution Proxy

| group                      |   cagr |   avg_monthly_return |   correlation_to_cap_weight_proxy |   return_share_vs_proxy_avg |
|:---------------------------|-------:|---------------------:|----------------------------------:|----------------------------:|
| Top 5 market-cap proxy     | 0.4121 |               0.0321 |                            0.9692 |                      1.3611 |
| Top 10 market-cap proxy    | 0.3600 |               0.0288 |                            0.9864 |                      1.2220 |
| Remaining available stocks | 0.1186 |               0.0114 |                            0.8874 |                      0.4819 |

## Top 5 / Top 10 Market-Cap Portfolio Test

- Top 5 proxy CAGR: 41.21%
- Top 5 proxy drawdown: -18.35%
- Top 5 win rate vs BIST100: 56.67%
- Top 10 proxy CAGR: 36.00%
- Top 10 proxy drawdown: -20.38%
- Top 10 win rate vs BIST100: 56.67%

## Interpretation

If the top market-cap proxy portfolios outperform the strategy, the bot is not merely fighting an abstract benchmark; it is failing to own enough of the names that explain index strength. In the current replay window, the strategy's baseline CAGR is below BIST100, while the large-cap proxy baskets are competitive with or stronger than the strategy.

## What This Means For The Bot

- The ranking model should be tested against a large-cap leadership benchmark, not only XU100.
- Avoiding or underweighting banks, ASELS, THYAO, KCHOL, and similar index leaders can explain a large part of underperformance.
- The next replay optimization should test index-relative momentum and a minimum large-cap/index-leader sleeve before adding any new features.
