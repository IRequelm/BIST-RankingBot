# BIST100 Relative Strength Survival Backtest

- Period: 2023-08-14 to 2026-08-14
- Configured BIST100 symbols: 100
- Loaded symbols: 97
- Missing/no valid data symbols: 3
- Production tracking_state.json was not modified.

## Policy Summary

| policy_id       | policy_name                              |   months | total_return   | bist100_total_return   | cagr   | bist100_cagr   | excess_cagr   | max_drawdown   | bist100_max_drawdown   |   sharpe_proxy | monthly_win_rate_vs_bist100   | average_monthly_excess_return   | worst_month   | worst_month_excess   | best_month   | best_month_excess   | average_turnover   |   average_trades_per_month |   cash_months |   average_holdings | transaction_cost_impact   |
|:----------------|:-----------------------------------------|---------:|:---------------|:-----------------------|:-------|:---------------|:--------------|:---------------|:-----------------------|---------------:|:------------------------------|:--------------------------------|:--------------|:---------------------|:-------------|:--------------------|:-------------------|---------------------------:|--------------:|-------------------:|:--------------------------|
| BENCHMARK       | BIST100 benchmark                        |       37 | 83.17%         | 83.17%                 | 22.35% | 22.35%         | 0.00%         | -17.72%        | -17.72%                |       0.976357 | 0.00%                         | 0.00%                           | 2023-08       | 0.00%                | 2023-08      | 0.00%               | 0.00%              |                    0       |             0 |            0       | 0.00%                     |
| OLD_TOP3        | Old absolute-score Top3                  |       37 | 113.99%        | 83.17%                 | 28.86% | 22.35%         | 6.51%         | -31.62%        | -17.72%                |       0.843617 | 48.65%                        | 0.78%                           | 2024-03       | -14.56%              | 2023-09      | 24.16%              | 132.43%            |                    3.97297 |             8 |            2.35135 | 9.80%                     |
| RS_TOP10        | BIST100 relative-strength survival Top10 |       37 | 150.45%        | 83.17%                 | 35.79% | 22.35%         | 13.45%        | -20.97%        | -17.72%                |       1.1032   | 59.46%                        | 1.05%                           | 2026-07       | -12.00%              | 2026-05      | 20.05%              | 107.03%            |                   10.7027  |             8 |            7.83784 | 7.92%                     |
| RS_TOP3         | BIST100 relative-strength survival Top3  |       37 | 178.80%        | 83.17%                 | 40.73% | 22.35%         | 18.39%        | -33.30%        | -17.72%                |       0.91462  | 54.05%                        | 1.84%                           | 2023-12       | -15.95%              | 2023-11      | 38.81%              | 132.43%            |                    3.97297 |             8 |            2.35135 | 9.80%                     |
| RS_TOP5         | BIST100 relative-strength survival Top5  |       37 | 79.47%         | 83.17%                 | 21.52% | 22.35%         | -0.83%        | -27.45%        | -17.72%                |       0.692511 | 54.05%                        | 0.31%                           | 2026-07       | -17.70%              | 2023-11      | 23.75%              | 123.78%            |                    6.18919 |             8 |            3.91892 | 9.16%                     |
| RS_TOP5_NO_CASH | Survival Top5 without MA200 cash filter  |       37 | 183.85%        | 83.17%                 | 41.58% | 22.35%         | 19.23%        | -27.45%        | -17.72%                |       1.07022  | 62.16%                        | 1.63%                           | 2026-07       | -17.70%              | 2023-11      | 23.75%              | 149.73%            |                    7.48649 |             0 |            5       | 11.08%                    |

## Decision

Selected winner: Survival Top5 without MA200 cash filter (excess CAGR 19.23%, max drawdown -27.45%).

No strict drawdown-safe candidate passed both excess-return and drawdown tests.

Raw-return winner: Survival Top5 without MA200 cash filter (excess CAGR 19.23%, max drawdown -27.45%).

This selected winner is the aggressive research champion: it removes the MA200 cash filter and accepts slightly worse drawdown than BIST100 in exchange for the strongest historical excess CAGR in this run.

## Latest Survival Selections

| policy_id       | date                | symbol   |   rank |   score |   relative_strength_1m |   relative_strength_3m |   relative_strength_6m |   trend_score |   volatility |
|:----------------|:--------------------|:---------|-------:|--------:|-----------------------:|-----------------------:|-----------------------:|--------------:|-------------:|
| OLD_TOP3        | 2026-08-03 00:00:00 | AKSEN.IS |      1 |  0.8686 |                 0.1704 |                 0.1573 |                 0.2353 |        1.0000 |       0.0352 |
| OLD_TOP3        | 2026-08-03 00:00:00 | TUPRS.IS |      2 |  0.8392 |                 0.3273 |                 0.1174 |                 0.2484 |        1.0000 |       0.0244 |
| OLD_TOP3        | 2026-08-03 00:00:00 | AKFYE.IS |      3 |  0.8119 |                 0.1046 |                 0.0849 |                 0.2929 |        0.5000 |       0.0407 |
| RS_TOP10        | 2026-08-03 00:00:00 | TKFEN.IS |      1 |  0.7026 |                 0.2670 |                 0.2733 |                 1.1255 |        1.0000 |       0.0372 |
| RS_TOP10        | 2026-08-03 00:00:00 | EUPWR.IS |      2 |  0.6947 |                 0.1598 |                 0.6916 |                 1.2020 |        1.0000 |       0.0519 |
| RS_TOP10        | 2026-08-03 00:00:00 | TUPRS.IS |      3 |  0.6816 |                 0.3273 |                 0.1174 |                 0.2484 |        1.0000 |       0.0244 |
| RS_TOP10        | 2026-08-03 00:00:00 | AEFES.IS |      4 |  0.6447 |                 0.1493 |                 0.2361 |                 0.1899 |        1.0000 |       0.0225 |
| RS_TOP10        | 2026-08-03 00:00:00 | AKSEN.IS |      5 |  0.6211 |                 0.1704 |                 0.1573 |                 0.2353 |        1.0000 |       0.0352 |
| RS_TOP10        | 2026-08-03 00:00:00 | AKSA.IS  |      6 |  0.6184 |                 0.1307 |                 0.2839 |                 0.2199 |        1.0000 |       0.0287 |
| RS_TOP10        | 2026-08-03 00:00:00 | ISGYO.IS |      7 |  0.6105 |                 0.1197 |                 0.3720 |                 0.1159 |        1.0000 |       0.0301 |
| RS_TOP10        | 2026-08-03 00:00:00 | ANHYT.IS |      8 |  0.5895 |                 0.1952 |                 0.1103 |                 0.0272 |        1.0000 |       0.0223 |
| RS_TOP10        | 2026-08-03 00:00:00 | EREGL.IS |      9 |  0.5842 |                 0.0558 |                 0.2863 |                 0.4784 |        1.0000 |       0.0279 |
| RS_TOP10        | 2026-08-03 00:00:00 | AKCNS.IS |     10 |  0.5684 |                 0.1583 |                 0.1966 |                 0.2568 |        1.0000 |       0.0318 |
| RS_TOP3         | 2026-08-03 00:00:00 | TKFEN.IS |      1 |  0.7026 |                 0.2670 |                 0.2733 |                 1.1255 |        1.0000 |       0.0372 |
| RS_TOP3         | 2026-08-03 00:00:00 | EUPWR.IS |      2 |  0.6947 |                 0.1598 |                 0.6916 |                 1.2020 |        1.0000 |       0.0519 |
| RS_TOP3         | 2026-08-03 00:00:00 | TUPRS.IS |      3 |  0.6816 |                 0.3273 |                 0.1174 |                 0.2484 |        1.0000 |       0.0244 |
| RS_TOP5         | 2026-08-03 00:00:00 | TKFEN.IS |      1 |  0.7026 |                 0.2670 |                 0.2733 |                 1.1255 |        1.0000 |       0.0372 |
| RS_TOP5         | 2026-08-03 00:00:00 | EUPWR.IS |      2 |  0.6947 |                 0.1598 |                 0.6916 |                 1.2020 |        1.0000 |       0.0519 |
| RS_TOP5         | 2026-08-03 00:00:00 | TUPRS.IS |      3 |  0.6816 |                 0.3273 |                 0.1174 |                 0.2484 |        1.0000 |       0.0244 |
| RS_TOP5         | 2026-08-03 00:00:00 | AEFES.IS |      4 |  0.6447 |                 0.1493 |                 0.2361 |                 0.1899 |        1.0000 |       0.0225 |
| RS_TOP5         | 2026-08-03 00:00:00 | AKSEN.IS |      5 |  0.6211 |                 0.1704 |                 0.1573 |                 0.2353 |        1.0000 |       0.0352 |
| RS_TOP5_NO_CASH | 2026-08-03 00:00:00 | TKFEN.IS |      1 |  0.7026 |                 0.2670 |                 0.2733 |                 1.1255 |        1.0000 |       0.0372 |
| RS_TOP5_NO_CASH | 2026-08-03 00:00:00 | EUPWR.IS |      2 |  0.6947 |                 0.1598 |                 0.6916 |                 1.2020 |        1.0000 |       0.0519 |
| RS_TOP5_NO_CASH | 2026-08-03 00:00:00 | TUPRS.IS |      3 |  0.6816 |                 0.3273 |                 0.1174 |                 0.2484 |        1.0000 |       0.0244 |
| RS_TOP5_NO_CASH | 2026-08-03 00:00:00 | AEFES.IS |      4 |  0.6447 |                 0.1493 |                 0.2361 |                 0.1899 |        1.0000 |       0.0225 |
| RS_TOP5_NO_CASH | 2026-08-03 00:00:00 | AKSEN.IS |      5 |  0.6211 |                 0.1704 |                 0.1573 |                 0.2353 |        1.0000 |       0.0352 |

## Notes

- Strategy uses only data available at each rebalance date.
- Hard filters: stock above MA50, 20-day relative strength above BIST100, liquidity floor, volatility cap.
- Regime cash filter: no stock exposure when BIST100 is below MA200.
- Missing tickers are excluded and never substituted.
