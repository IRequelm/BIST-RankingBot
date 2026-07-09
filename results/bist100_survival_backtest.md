# BIST100 Relative Strength Survival Backtest

- Period: 2023-07-08 to 2026-07-08
- Configured BIST100 symbols: 100
- Loaded symbols: 97
- Missing/no valid data symbols: 3
- Production tracking_state.json was not modified.

## Policy Summary

| policy_id       | policy_name                              |   months | total_return   | bist100_total_return   | cagr   | bist100_cagr   | excess_cagr   | max_drawdown   | bist100_max_drawdown   |   sharpe_proxy | monthly_win_rate_vs_bist100   | average_monthly_excess_return   | worst_month   | worst_month_excess   | best_month   | best_month_excess   | average_turnover   |   average_trades_per_month |   cash_months |   average_holdings | transaction_cost_impact   |
|:----------------|:-----------------------------------------|---------:|:---------------|:-----------------------|:-------|:---------------|:--------------|:---------------|:-----------------------|---------------:|:------------------------------|:--------------------------------|:--------------|:---------------------|:-------------|:--------------------|:-------------------|---------------------------:|--------------:|-------------------:|:--------------------------|
| BENCHMARK       | BIST100 benchmark                        |       37 | 126.30%        | 126.30%                | 31.35% | 31.35%         | 0.00%         | -17.72%        | -17.72%                |        1.22856 | 0.00%                         | 0.00%                           | 2023-07       | 0.00%                | 2023-07      | 0.00%               | 0.00%              |                    0       |             0 |            0       | 0.00%                     |
| OLD_TOP3        | Old absolute-score Top3                  |       37 | 163.02%        | 126.30%                | 38.11% | 31.35%         | 6.76%         | -31.62%        | -17.72%                |        0.99792 | 51.35%                        | 0.79%                           | 2024-03       | -14.56%              | 2023-09      | 24.16%              | 132.43%            |                    3.97297 |             8 |            2.35135 | 9.80%                     |
| RS_TOP10        | BIST100 relative-strength survival Top10 |       37 | 289.91%        | 126.30%                | 57.51% | 31.35%         | 26.16%        | -14.69%        | -17.72%                |        1.44402 | 62.16%                        | 1.74%                           | 2025-06       | -11.89%              | 2023-08      | 22.18%              | 107.57%            |                   10.7568  |             8 |            7.83784 | 7.96%                     |
| RS_TOP3         | BIST100 relative-strength survival Top3  |       37 | 228.61%        | 126.30%                | 48.77% | 31.35%         | 17.42%        | -33.30%        | -17.72%                |        1.03241 | 54.05%                        | 1.66%                           | 2023-12       | -15.95%              | 2023-11      | 38.81%              | 134.23%            |                    4.02703 |             8 |            2.35135 | 9.93%                     |
| RS_TOP5         | BIST100 relative-strength survival Top5  |       37 | 219.37%        | 126.30%                | 47.36% | 31.35%         | 16.01%        | -22.51%        | -17.72%                |        1.11585 | 54.05%                        | 1.36%                           | 2023-12       | -13.80%              | 2023-08      | 28.89%              | 123.78%            |                    6.18919 |             8 |            3.91892 | 9.16%                     |
| RS_TOP5_NO_CASH | Survival Top5 without MA200 cash filter  |       37 | 441.48%        | 126.30%                | 75.76% | 31.35%         | 44.41%        | -18.81%        | -17.72%                |        1.51628 | 62.16%                        | 2.89%                           | 2023-12       | -13.80%              | 2023-08      | 28.89%              | 148.65%            |                    7.43243 |             0 |            5       | 11.00%                    |

## Decision

Selected winner: Survival Top5 without MA200 cash filter (excess CAGR 44.41%, max drawdown -18.81%).

Strict drawdown-safe candidate remains BIST100 relative-strength survival Top10 (excess CAGR 26.16%, max drawdown -14.69%).

Raw-return winner: Survival Top5 without MA200 cash filter (excess CAGR 44.41%, max drawdown -18.81%).

This selected winner is the aggressive research champion: it removes the MA200 cash filter and accepts slightly worse drawdown than BIST100 in exchange for the strongest historical excess CAGR in this run.

## Latest Survival Selections

| policy_id       | date                | symbol   |   rank |   score |   relative_strength_1m |   relative_strength_3m |   relative_strength_6m |   trend_score |   volatility |
|:----------------|:--------------------|:---------|-------:|--------:|-----------------------:|-----------------------:|-----------------------:|--------------:|-------------:|
| OLD_TOP3        | 2026-07-01 00:00:00 | EUPWR.IS |      1 |  0.8928 |                 0.0266 |                 0.9466 |                 1.2447 |        1.0000 |       0.0503 |
| OLD_TOP3        | 2026-07-01 00:00:00 | ODAS.IS  |      2 |  0.8552 |                 0.1061 |                 0.3624 |                 0.3883 |        1.0000 |       0.0363 |
| OLD_TOP3        | 2026-07-01 00:00:00 | ISGYO.IS |      3 |  0.8485 |                 0.1789 |                 0.1333 |                -0.0868 |        1.0000 |       0.0277 |
| RS_TOP10        | 2026-07-01 00:00:00 | KTLEV.IS |      1 |  0.7841 |                 0.3461 |                 1.1343 |                 7.7691 |        1.0000 |       0.0311 |
| RS_TOP10        | 2026-07-01 00:00:00 | ENERY.IS |      2 |  0.7386 |                 0.2478 |                 0.1477 |                -0.0626 |        1.0000 |       0.0272 |
| RS_TOP10        | 2026-07-01 00:00:00 | AHGAZ.IS |      3 |  0.7318 |                 0.2166 |                 0.6292 |                 0.5021 |        1.0000 |       0.0283 |
| RS_TOP10        | 2026-07-01 00:00:00 | SKBNK.IS |      4 |  0.7295 |                 0.2671 |                 0.4746 |                 0.8919 |        1.0000 |       0.0337 |
| RS_TOP10        | 2026-07-01 00:00:00 | ISGYO.IS |      5 |  0.6932 |                 0.1789 |                 0.1333 |                -0.0868 |        1.0000 |       0.0277 |
| RS_TOP10        | 2026-07-01 00:00:00 | ODAS.IS  |      6 |  0.6932 |                 0.1061 |                 0.3624 |                 0.3883 |        1.0000 |       0.0363 |
| RS_TOP10        | 2026-07-01 00:00:00 | KCAER.IS |      7 |  0.6409 |                 0.1159 |                 0.2710 |                 0.2193 |        1.0000 |       0.0318 |
| RS_TOP10        | 2026-07-01 00:00:00 | YKBNK.IS |      8 |  0.5591 |                 0.1501 |                 0.1076 |                -0.1443 |        1.0000 |       0.0307 |
| RS_TOP10        | 2026-07-01 00:00:00 | AKBNK.IS |      9 |  0.5455 |                 0.1698 |                 0.0576 |                -0.1271 |        1.0000 |       0.0312 |
| RS_TOP10        | 2026-07-01 00:00:00 | AEFES.IS |     10 |  0.5364 |                 0.0231 |                 0.1316 |                 0.0607 |        1.0000 |       0.0246 |
| RS_TOP3         | 2026-07-01 00:00:00 | KTLEV.IS |      1 |  0.7841 |                 0.3461 |                 1.1343 |                 7.7691 |        1.0000 |       0.0311 |
| RS_TOP3         | 2026-07-01 00:00:00 | ENERY.IS |      2 |  0.7386 |                 0.2478 |                 0.1477 |                -0.0626 |        1.0000 |       0.0272 |
| RS_TOP3         | 2026-07-01 00:00:00 | AHGAZ.IS |      3 |  0.7318 |                 0.2166 |                 0.6292 |                 0.5021 |        1.0000 |       0.0283 |
| RS_TOP5         | 2026-07-01 00:00:00 | KTLEV.IS |      1 |  0.7841 |                 0.3461 |                 1.1343 |                 7.7691 |        1.0000 |       0.0311 |
| RS_TOP5         | 2026-07-01 00:00:00 | ENERY.IS |      2 |  0.7386 |                 0.2478 |                 0.1477 |                -0.0626 |        1.0000 |       0.0272 |
| RS_TOP5         | 2026-07-01 00:00:00 | AHGAZ.IS |      3 |  0.7318 |                 0.2166 |                 0.6292 |                 0.5021 |        1.0000 |       0.0283 |
| RS_TOP5         | 2026-07-01 00:00:00 | SKBNK.IS |      4 |  0.7295 |                 0.2671 |                 0.4746 |                 0.8919 |        1.0000 |       0.0337 |
| RS_TOP5         | 2026-07-01 00:00:00 | ISGYO.IS |      5 |  0.6932 |                 0.1789 |                 0.1333 |                -0.0868 |        1.0000 |       0.0277 |
| RS_TOP5_NO_CASH | 2026-07-01 00:00:00 | KTLEV.IS |      1 |  0.7841 |                 0.3461 |                 1.1343 |                 7.7691 |        1.0000 |       0.0311 |
| RS_TOP5_NO_CASH | 2026-07-01 00:00:00 | ENERY.IS |      2 |  0.7386 |                 0.2478 |                 0.1477 |                -0.0626 |        1.0000 |       0.0272 |
| RS_TOP5_NO_CASH | 2026-07-01 00:00:00 | AHGAZ.IS |      3 |  0.7318 |                 0.2166 |                 0.6292 |                 0.5021 |        1.0000 |       0.0283 |
| RS_TOP5_NO_CASH | 2026-07-01 00:00:00 | SKBNK.IS |      4 |  0.7295 |                 0.2671 |                 0.4746 |                 0.8919 |        1.0000 |       0.0337 |
| RS_TOP5_NO_CASH | 2026-07-01 00:00:00 | ISGYO.IS |      5 |  0.6932 |                 0.1789 |                 0.1333 |                -0.0868 |        1.0000 |       0.0277 |

## Notes

- Strategy uses only data available at each rebalance date.
- Hard filters: stock above MA50, 20-day relative strength above BIST100, liquidity floor, volatility cap.
- Regime cash filter: no stock exposure when BIST100 is below MA200.
- Missing tickers are excluded and never substituted.
