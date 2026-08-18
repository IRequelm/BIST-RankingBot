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
| OLD_TOP3        | Old absolute-score Top3                  |       37 | 118.49%        | 83.17%                 | 29.75% | 22.35%         | 7.40%         | -31.62%        | -17.72%                |       0.861721 | 48.65%                        | 0.84%                           | 2024-03       | -14.56%              | 2023-09      | 24.16%              | 132.43%            |                    3.97297 |             8 |            2.35135 | 9.80%                     |
| RS_TOP10        | BIST100 relative-strength survival Top10 |       37 | 151.73%        | 83.17%                 | 36.02% | 22.35%         | 13.68%        | -20.97%        | -17.72%                |       1.10845  | 59.46%                        | 1.06%                           | 2026-07       | -12.00%              | 2026-05      | 20.05%              | 107.03%            |                   10.7027  |             8 |            7.83784 | 7.92%                     |
| RS_TOP3         | BIST100 relative-strength survival Top3  |       37 | 189.85%        | 83.17%                 | 42.57% | 22.35%         | 20.22%        | -33.30%        | -17.72%                |       0.93464  | 54.05%                        | 1.97%                           | 2023-12       | -15.95%              | 2023-11      | 38.81%              | 132.43%            |                    3.97297 |             8 |            2.35135 | 9.80%                     |
| RS_TOP5         | BIST100 relative-strength survival Top5  |       37 | 89.29%         | 83.17%                 | 23.70% | 22.35%         | 1.35%         | -27.45%        | -17.72%                |       0.734845 | 54.05%                        | 0.47%                           | 2026-07       | -17.70%              | 2023-11      | 23.75%              | 123.78%            |                    6.18919 |             8 |            3.91892 | 9.16%                     |
| RS_TOP5_NO_CASH | Survival Top5 without MA200 cash filter  |       37 | 199.38%        | 83.17%                 | 44.11% | 22.35%         | 21.77%        | -27.45%        | -17.72%                |       1.10894  | 62.16%                        | 1.78%                           | 2026-07       | -17.70%              | 2023-11      | 23.75%              | 149.73%            |                    7.48649 |             0 |            5       | 11.08%                    |

## Decision

Selected winner: Survival Top5 without MA200 cash filter (excess CAGR 21.77%, max drawdown -27.45%).

No strict drawdown-safe candidate passed both excess-return and drawdown tests.

Raw-return winner: Survival Top5 without MA200 cash filter (excess CAGR 21.77%, max drawdown -27.45%).

This selected winner is the aggressive research champion: it removes the MA200 cash filter and accepts slightly worse drawdown than BIST100 in exchange for the strongest historical excess CAGR in this run.

## Latest Survival Selections

| policy_id       | date                | symbol   |   rank |   score |   relative_strength_1m |   relative_strength_3m |   relative_strength_6m |   trend_score |   volatility |
|:----------------|:--------------------|:---------|-------:|--------:|-----------------------:|-----------------------:|-----------------------:|--------------:|-------------:|
| OLD_TOP3        | 2026-08-03 00:00:00 | AKSEN.IS |      1 |  0.8804 |                 0.1821 |                 0.1785 |                 0.2685 |        1.0000 |       0.0352 |
| OLD_TOP3        | 2026-08-03 00:00:00 | TUPRS.IS |      2 |  0.8428 |                 0.2949 |                 0.1434 |                 0.2479 |        1.0000 |       0.0240 |
| OLD_TOP3        | 2026-08-03 00:00:00 | AKFYE.IS |      3 |  0.8340 |                 0.1200 |                 0.1317 |                 0.3075 |        0.5000 |       0.0411 |
| RS_TOP10        | 2026-08-03 00:00:00 | TKFEN.IS |      1 |  0.6663 |                 0.2213 |                 0.2215 |                 1.1926 |        1.0000 |       0.0367 |
| RS_TOP10        | 2026-08-03 00:00:00 | EUPWR.IS |      2 |  0.6537 |                 0.1243 |                 0.7909 |                 1.1756 |        1.0000 |       0.0520 |
| RS_TOP10        | 2026-08-03 00:00:00 | TUPRS.IS |      3 |  0.6513 |                 0.2949 |                 0.1434 |                 0.2479 |        1.0000 |       0.0240 |
| RS_TOP10        | 2026-08-03 00:00:00 | CCOLA.IS |      4 |  0.6487 |                 0.1271 |                 0.2507 |                 0.2588 |        1.0000 |       0.0247 |
| RS_TOP10        | 2026-08-03 00:00:00 | PASEU.IS |      5 |  0.6438 |                 0.8596 |                 0.3518 |                 0.0553 |        1.0000 |       0.0583 |
| RS_TOP10        | 2026-08-03 00:00:00 | AKSEN.IS |      6 |  0.6288 |                 0.1821 |                 0.1785 |                 0.2685 |        1.0000 |       0.0352 |
| RS_TOP10        | 2026-08-03 00:00:00 | AEFES.IS |      7 |  0.6287 |                 0.1240 |                 0.2445 |                 0.2147 |        1.0000 |       0.0225 |
| RS_TOP10        | 2026-08-03 00:00:00 | ISGYO.IS |      8 |  0.6212 |                 0.1079 |                 0.3580 |                 0.0986 |        1.0000 |       0.0300 |
| RS_TOP10        | 2026-08-03 00:00:00 | AKSA.IS  |      9 |  0.6013 |                 0.1150 |                 0.2518 |                 0.2594 |        1.0000 |       0.0278 |
| RS_TOP10        | 2026-08-03 00:00:00 | ANHYT.IS |     10 |  0.5587 |                 0.1895 |                 0.1093 |                 0.0882 |        1.0000 |       0.0224 |
| RS_TOP3         | 2026-08-03 00:00:00 | TKFEN.IS |      1 |  0.6663 |                 0.2213 |                 0.2215 |                 1.1926 |        1.0000 |       0.0367 |
| RS_TOP3         | 2026-08-03 00:00:00 | EUPWR.IS |      2 |  0.6537 |                 0.1243 |                 0.7909 |                 1.1756 |        1.0000 |       0.0520 |
| RS_TOP3         | 2026-08-03 00:00:00 | TUPRS.IS |      3 |  0.6513 |                 0.2949 |                 0.1434 |                 0.2479 |        1.0000 |       0.0240 |
| RS_TOP5         | 2026-08-03 00:00:00 | TKFEN.IS |      1 |  0.6663 |                 0.2213 |                 0.2215 |                 1.1926 |        1.0000 |       0.0367 |
| RS_TOP5         | 2026-08-03 00:00:00 | EUPWR.IS |      2 |  0.6537 |                 0.1243 |                 0.7909 |                 1.1756 |        1.0000 |       0.0520 |
| RS_TOP5         | 2026-08-03 00:00:00 | TUPRS.IS |      3 |  0.6513 |                 0.2949 |                 0.1434 |                 0.2479 |        1.0000 |       0.0240 |
| RS_TOP5         | 2026-08-03 00:00:00 | CCOLA.IS |      4 |  0.6487 |                 0.1271 |                 0.2507 |                 0.2588 |        1.0000 |       0.0247 |
| RS_TOP5         | 2026-08-03 00:00:00 | PASEU.IS |      5 |  0.6438 |                 0.8596 |                 0.3518 |                 0.0553 |        1.0000 |       0.0583 |
| RS_TOP5_NO_CASH | 2026-08-03 00:00:00 | TKFEN.IS |      1 |  0.6663 |                 0.2213 |                 0.2215 |                 1.1926 |        1.0000 |       0.0367 |
| RS_TOP5_NO_CASH | 2026-08-03 00:00:00 | EUPWR.IS |      2 |  0.6537 |                 0.1243 |                 0.7909 |                 1.1756 |        1.0000 |       0.0520 |
| RS_TOP5_NO_CASH | 2026-08-03 00:00:00 | TUPRS.IS |      3 |  0.6513 |                 0.2949 |                 0.1434 |                 0.2479 |        1.0000 |       0.0240 |
| RS_TOP5_NO_CASH | 2026-08-03 00:00:00 | CCOLA.IS |      4 |  0.6487 |                 0.1271 |                 0.2507 |                 0.2588 |        1.0000 |       0.0247 |
| RS_TOP5_NO_CASH | 2026-08-03 00:00:00 | PASEU.IS |      5 |  0.6438 |                 0.8596 |                 0.3518 |                 0.0553 |        1.0000 |       0.0583 |

## Notes

- Strategy uses only data available at each rebalance date.
- Hard filters: stock above MA50, 20-day relative strength above BIST100, liquidity floor, volatility cap.
- Regime cash filter: no stock exposure when BIST100 is below MA200.
- Missing tickers are excluded and never substituted.
