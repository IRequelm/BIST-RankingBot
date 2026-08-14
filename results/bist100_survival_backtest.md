# BIST100 Relative Strength Survival Backtest

- Period: 2023-08-13 to 2026-08-13
- Configured BIST100 symbols: 100
- Loaded symbols: 97
- Missing/no valid data symbols: 3
- Production tracking_state.json was not modified.

## Policy Summary

| policy_id       | policy_name                              |   months | total_return   | bist100_total_return   | cagr   | bist100_cagr   | excess_cagr   | max_drawdown   | bist100_max_drawdown   |   sharpe_proxy | monthly_win_rate_vs_bist100   | average_monthly_excess_return   | worst_month   | worst_month_excess   | best_month   | best_month_excess   | average_turnover   |   average_trades_per_month |   cash_months |   average_holdings | transaction_cost_impact   |
|:----------------|:-----------------------------------------|---------:|:---------------|:-----------------------|:-------|:---------------|:--------------|:---------------|:-----------------------|---------------:|:------------------------------|:--------------------------------|:--------------|:---------------------|:-------------|:--------------------|:-------------------|---------------------------:|--------------:|-------------------:|:--------------------------|
| BENCHMARK       | BIST100 benchmark                        |       37 | 82.65%         | 82.65%                 | 22.25% | 22.25%         | 0.00%         | -17.72%        | -17.72%                |       0.972788 | 0.00%                         | 0.00%                           | 2023-08       | 0.00%                | 2023-08      | 0.00%               | 0.00%              |                    0       |             0 |            0       | 0.00%                     |
| OLD_TOP3        | Old absolute-score Top3                  |       37 | 113.39%        | 82.65%                 | 28.77% | 22.25%         | 6.51%         | -31.62%        | -17.72%                |       0.841158 | 48.65%                        | 0.78%                           | 2024-03       | -14.56%              | 2023-09      | 24.16%              | 132.43%            |                    3.97297 |             8 |            2.35135 | 9.80%                     |
| RS_TOP10        | BIST100 relative-strength survival Top10 |       37 | 152.83%        | 82.65%                 | 36.26% | 22.25%         | 14.01%        | -20.97%        | -17.72%                |       1.11293  | 59.46%                        | 1.08%                           | 2026-07       | -12.00%              | 2026-05      | 20.05%              | 107.03%            |                   10.7027  |             8 |            7.83784 | 7.92%                     |
| RS_TOP3         | BIST100 relative-strength survival Top3  |       37 | 176.88%        | 82.65%                 | 40.45% | 22.25%         | 18.20%        | -33.30%        | -17.72%                |       0.910804 | 54.05%                        | 1.83%                           | 2023-12       | -15.95%              | 2023-11      | 38.81%              | 132.43%            |                    3.97297 |             8 |            2.35135 | 9.80%                     |
| RS_TOP5         | BIST100 relative-strength survival Top5  |       37 | 82.97%         | 82.65%                 | 22.33% | 22.25%         | 0.07%         | -27.45%        | -17.72%                |       0.708371 | 54.05%                        | 0.37%                           | 2026-07       | -17.70%              | 2023-11      | 23.75%              | 123.78%            |                    6.18919 |             8 |            3.91892 | 9.16%                     |
| RS_TOP5_NO_CASH | Survival Top5 without MA200 cash filter  |       37 | 189.39%        | 82.65%                 | 42.54% | 22.25%         | 20.28%        | -27.45%        | -17.72%                |       1.08503  | 62.16%                        | 1.69%                           | 2026-07       | -17.70%              | 2023-11      | 23.75%              | 149.73%            |                    7.48649 |             0 |            5       | 11.08%                    |

## Decision

Selected winner: Survival Top5 without MA200 cash filter (excess CAGR 20.28%, max drawdown -27.45%).

No strict drawdown-safe candidate passed both excess-return and drawdown tests.

Raw-return winner: Survival Top5 without MA200 cash filter (excess CAGR 20.28%, max drawdown -27.45%).

This selected winner is the aggressive research champion: it removes the MA200 cash filter and accepts slightly worse drawdown than BIST100 in exchange for the strongest historical excess CAGR in this run.

## Latest Survival Selections

| policy_id       | date                | symbol   |   rank |   score |   relative_strength_1m |   relative_strength_3m |   relative_strength_6m |   trend_score |   volatility |
|:----------------|:--------------------|:---------|-------:|--------:|-----------------------:|-----------------------:|-----------------------:|--------------:|-------------:|
| OLD_TOP3        | 2026-08-03 00:00:00 | AKSEN.IS |      1 |  0.8737 |                 0.1916 |                 0.1255 |                 0.2656 |        1.0000 |       0.0343 |
| OLD_TOP3        | 2026-08-03 00:00:00 | TUPRS.IS |      2 |  0.8459 |                 0.3273 |                 0.1174 |                 0.2484 |        1.0000 |       0.0244 |
| OLD_TOP3        | 2026-08-03 00:00:00 | AKFYE.IS |      3 |  0.8247 |                 0.1021 |                 0.1396 |                 0.2880 |        0.5000 |       0.0398 |
| RS_TOP10        | 2026-08-03 00:00:00 | TKFEN.IS |      1 |  0.7026 |                 0.2670 |                 0.2733 |                 1.1255 |        1.0000 |       0.0372 |
| RS_TOP10        | 2026-08-03 00:00:00 | TUPRS.IS |      2 |  0.6737 |                 0.3273 |                 0.1174 |                 0.2484 |        1.0000 |       0.0244 |
| RS_TOP10        | 2026-08-03 00:00:00 | AKSEN.IS |      3 |  0.6579 |                 0.1916 |                 0.1255 |                 0.2656 |        1.0000 |       0.0343 |
| RS_TOP10        | 2026-08-03 00:00:00 | AEFES.IS |      4 |  0.6553 |                 0.1493 |                 0.2361 |                 0.1899 |        1.0000 |       0.0225 |
| RS_TOP10        | 2026-08-03 00:00:00 | EUPWR.IS |      5 |  0.6526 |                 0.1249 |                 0.9055 |                 1.1941 |        1.0000 |       0.0561 |
| RS_TOP10        | 2026-08-03 00:00:00 | ISGYO.IS |      6 |  0.6316 |                 0.1038 |                 0.3482 |                 0.1163 |        1.0000 |       0.0302 |
| RS_TOP10        | 2026-08-03 00:00:00 | AKSA.IS  |      7 |  0.6289 |                 0.1307 |                 0.2839 |                 0.2199 |        1.0000 |       0.0287 |
| RS_TOP10        | 2026-08-03 00:00:00 | EREGL.IS |      8 |  0.5842 |                 0.0558 |                 0.2863 |                 0.4784 |        1.0000 |       0.0279 |
| RS_TOP10        | 2026-08-03 00:00:00 | AKCNS.IS |      9 |  0.5711 |                 0.1583 |                 0.1966 |                 0.2568 |        1.0000 |       0.0318 |
| RS_TOP10        | 2026-08-03 00:00:00 | CCOLA.IS |     10 |  0.5579 |                 0.0979 |                 0.2477 |                 0.2047 |        1.0000 |       0.0251 |
| RS_TOP3         | 2026-08-03 00:00:00 | TKFEN.IS |      1 |  0.7026 |                 0.2670 |                 0.2733 |                 1.1255 |        1.0000 |       0.0372 |
| RS_TOP3         | 2026-08-03 00:00:00 | TUPRS.IS |      2 |  0.6737 |                 0.3273 |                 0.1174 |                 0.2484 |        1.0000 |       0.0244 |
| RS_TOP3         | 2026-08-03 00:00:00 | AKSEN.IS |      3 |  0.6579 |                 0.1916 |                 0.1255 |                 0.2656 |        1.0000 |       0.0343 |
| RS_TOP5         | 2026-08-03 00:00:00 | TKFEN.IS |      1 |  0.7026 |                 0.2670 |                 0.2733 |                 1.1255 |        1.0000 |       0.0372 |
| RS_TOP5         | 2026-08-03 00:00:00 | TUPRS.IS |      2 |  0.6737 |                 0.3273 |                 0.1174 |                 0.2484 |        1.0000 |       0.0244 |
| RS_TOP5         | 2026-08-03 00:00:00 | AKSEN.IS |      3 |  0.6579 |                 0.1916 |                 0.1255 |                 0.2656 |        1.0000 |       0.0343 |
| RS_TOP5         | 2026-08-03 00:00:00 | AEFES.IS |      4 |  0.6553 |                 0.1493 |                 0.2361 |                 0.1899 |        1.0000 |       0.0225 |
| RS_TOP5         | 2026-08-03 00:00:00 | EUPWR.IS |      5 |  0.6526 |                 0.1249 |                 0.9055 |                 1.1941 |        1.0000 |       0.0561 |
| RS_TOP5_NO_CASH | 2026-08-03 00:00:00 | TKFEN.IS |      1 |  0.7026 |                 0.2670 |                 0.2733 |                 1.1255 |        1.0000 |       0.0372 |
| RS_TOP5_NO_CASH | 2026-08-03 00:00:00 | TUPRS.IS |      2 |  0.6737 |                 0.3273 |                 0.1174 |                 0.2484 |        1.0000 |       0.0244 |
| RS_TOP5_NO_CASH | 2026-08-03 00:00:00 | AKSEN.IS |      3 |  0.6579 |                 0.1916 |                 0.1255 |                 0.2656 |        1.0000 |       0.0343 |
| RS_TOP5_NO_CASH | 2026-08-03 00:00:00 | AEFES.IS |      4 |  0.6553 |                 0.1493 |                 0.2361 |                 0.1899 |        1.0000 |       0.0225 |
| RS_TOP5_NO_CASH | 2026-08-03 00:00:00 | EUPWR.IS |      5 |  0.6526 |                 0.1249 |                 0.9055 |                 1.1941 |        1.0000 |       0.0561 |

## Notes

- Strategy uses only data available at each rebalance date.
- Hard filters: stock above MA50, 20-day relative strength above BIST100, liquidity floor, volatility cap.
- Regime cash filter: no stock exposure when BIST100 is below MA200.
- Missing tickers are excluded and never substituted.
