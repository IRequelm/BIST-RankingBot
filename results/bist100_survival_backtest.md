# BIST100 Relative Strength Survival Backtest

- Period: 2023-10-19 to 2026-10-19
- Configured BIST100 symbols: 100
- Loaded symbols: 97
- Missing/no valid data symbols: 3
- Production tracking_state.json was not modified.

## Policy Summary

| policy_id       | policy_name                              |   months | total_return   | bist100_total_return   | cagr   | bist100_cagr   | excess_cagr   | max_drawdown   | bist100_max_drawdown   |   sharpe_proxy | monthly_win_rate_vs_bist100   | average_monthly_excess_return   | worst_month   | worst_month_excess   | best_month   | best_month_excess   | average_turnover   |   average_trades_per_month |   cash_months |   average_holdings | transaction_cost_impact   |
|:----------------|:-----------------------------------------|---------:|:---------------|:-----------------------|:-------|:---------------|:--------------|:---------------|:-----------------------|---------------:|:------------------------------|:--------------------------------|:--------------|:---------------------|:-------------|:--------------------|:-------------------|---------------------------:|--------------:|-------------------:|:--------------------------|
| BENCHMARK       | BIST100 benchmark                        |       37 | 47.13%         | 47.13%                 | 13.73% | 13.73%         | 0.00%         | -20.46%        | -20.46%                |       0.641432 | 0.00%                         | 0.00%                           | 2023-10       | 0.00%                | 2023-10      | 0.00%               | 0.00%              |                    0       |             0 |            0       | 0.00%                     |
| OLD_TOP3        | Old absolute-score Top3                  |       37 | 43.27%         | 47.13%                 | 12.73% | 13.73%         | -1.00%        | -31.62%        | -20.46%                |       0.512249 | 48.65%                        | 0.16%                           | 2024-03       | -14.56%              | 2026-05      | 22.66%              | 127.93%            |                    3.83784 |             9 |            2.27027 | 9.47%                     |
| RS_TOP10        | BIST100 relative-strength survival Top10 |       37 | 46.80%         | 47.13%                 | 13.65% | 13.73%         | -0.08%        | -26.80%        | -20.46%                |       0.568277 | 56.76%                        | 0.10%                           | 2025-06       | -11.89%              | 2026-05      | 13.30%              | 106.49%            |                   10.6486  |             9 |            7.56757 | 7.88%                     |
| RS_TOP3         | BIST100 relative-strength survival Top3  |       37 | 33.27%         | 47.13%                 | 10.05% | 13.73%         | -3.69%        | -38.25%        | -20.46%                |       0.429267 | 51.35%                        | 0.61%                           | 2026-07       | -28.85%              | 2023-11      | 38.94%              | 126.13%            |                    3.78378 |             9 |            2.27027 | 9.33%                     |
| RS_TOP5         | BIST100 relative-strength survival Top5  |       37 | -3.51%         | 47.13%                 | -1.18% | 13.73%         | -14.92%       | -42.64%        | -20.46%                |       0.186693 | 48.65%                        | -0.61%                          | 2026-09       | -17.81%              | 2023-11      | 23.75%              | 120.00%            |                    6       |             9 |            3.78378 | 8.88%                     |
| RS_TOP5_NO_CASH | Survival Top5 without MA200 cash filter  |       37 | 45.56%         | 47.13%                 | 13.33% | 13.73%         | -0.40%        | -45.28%        | -20.46%                |       0.500027 | 56.76%                        | 0.58%                           | 2026-09       | -17.81%              | 2023-11      | 23.75%              | 146.49%            |                    7.32432 |             0 |            5       | 10.84%                    |

## Decision

Selected winner: Survival Top5 without MA200 cash filter (excess CAGR -0.40%, max drawdown -45.28%).

No strict drawdown-safe candidate passed both excess-return and drawdown tests.

Raw-return winner: BIST100 relative-strength survival Top10 (excess CAGR -0.08%, max drawdown -26.80%).

This selected winner is the aggressive research champion: it removes the MA200 cash filter and accepts slightly worse drawdown than BIST100 in exchange for the strongest historical excess CAGR in this run.

## Latest Survival Selections

| policy_id       | date                | symbol   |   rank |   score |   relative_strength_1m |   relative_strength_3m |   relative_strength_6m |   trend_score |   volatility |
|:----------------|:--------------------|:---------|-------:|--------:|-----------------------:|-----------------------:|-----------------------:|--------------:|-------------:|
| OLD_TOP3        | 2026-09-01 00:00:00 | TKFEN.IS |      1 |  0.8943 |                 0.2457 |                 0.4051 |                 1.7546 |        1.0000 |       0.0384 |
| OLD_TOP3        | 2026-09-01 00:00:00 | TUPRS.IS |      2 |  0.8670 |                 0.3254 |                 0.6741 |                 0.8955 |        1.0000 |       0.0271 |
| OLD_TOP3        | 2026-09-01 00:00:00 | KCHOL.IS |      3 |  0.8649 |                 0.0305 |                 0.1195 |                 0.0583 |        1.0000 |       0.0191 |
| RS_TOP10        | 2026-09-01 00:00:00 | TUPRS.IS |      1 |  0.8425 |                 0.3254 |                 0.6741 |                 0.8955 |        1.0000 |       0.0271 |
| RS_TOP10        | 2026-09-01 00:00:00 | TKFEN.IS |      2 |  0.8042 |                 0.2457 |                 0.4051 |                 1.7546 |        1.0000 |       0.0384 |
| RS_TOP10        | 2026-09-01 00:00:00 | KTLEV.IS |      3 |  0.7792 |                 0.3042 |                 0.3992 |                 3.9477 |        1.0000 |       0.0448 |
| RS_TOP10        | 2026-09-01 00:00:00 | PASEU.IS |      4 |  0.7742 |                 0.2236 |                 0.9913 |                 0.7261 |        1.0000 |       0.0588 |
| RS_TOP10        | 2026-09-01 00:00:00 | BRSAN.IS |      5 |  0.7242 |                 0.2679 |                 0.2204 |                 0.0010 |        1.0000 |       0.0342 |
| RS_TOP10        | 2026-09-01 00:00:00 | AHGAZ.IS |      6 |  0.6975 |                 0.1359 |                 0.1970 |                 0.5753 |        1.0000 |       0.0270 |
| RS_TOP10        | 2026-09-01 00:00:00 | KCHOL.IS |      7 |  0.6625 |                 0.0305 |                 0.1195 |                 0.0583 |        1.0000 |       0.0191 |
| RS_TOP10        | 2026-09-01 00:00:00 | KRDMD.IS |      8 |  0.6008 |                 0.0429 |                 0.0780 |                 0.3900 |        1.0000 |       0.0281 |
| RS_TOP10        | 2026-09-01 00:00:00 | ENERY.IS |      9 |  0.5992 |                 0.0929 |                 0.1390 |                 0.0355 |        1.0000 |       0.0322 |
| RS_TOP10        | 2026-09-01 00:00:00 | SOKM.IS  |     10 |  0.5658 |                 0.0655 |                 0.1338 |                -0.2108 |        1.0000 |       0.0232 |
| RS_TOP3         | 2026-09-01 00:00:00 | TUPRS.IS |      1 |  0.8425 |                 0.3254 |                 0.6741 |                 0.8955 |        1.0000 |       0.0271 |
| RS_TOP3         | 2026-09-01 00:00:00 | TKFEN.IS |      2 |  0.8042 |                 0.2457 |                 0.4051 |                 1.7546 |        1.0000 |       0.0384 |
| RS_TOP3         | 2026-09-01 00:00:00 | KTLEV.IS |      3 |  0.7792 |                 0.3042 |                 0.3992 |                 3.9477 |        1.0000 |       0.0448 |
| RS_TOP5         | 2026-09-01 00:00:00 | TUPRS.IS |      1 |  0.8425 |                 0.3254 |                 0.6741 |                 0.8955 |        1.0000 |       0.0271 |
| RS_TOP5         | 2026-09-01 00:00:00 | TKFEN.IS |      2 |  0.8042 |                 0.2457 |                 0.4051 |                 1.7546 |        1.0000 |       0.0384 |
| RS_TOP5         | 2026-09-01 00:00:00 | KTLEV.IS |      3 |  0.7792 |                 0.3042 |                 0.3992 |                 3.9477 |        1.0000 |       0.0448 |
| RS_TOP5         | 2026-09-01 00:00:00 | PASEU.IS |      4 |  0.7742 |                 0.2236 |                 0.9913 |                 0.7261 |        1.0000 |       0.0588 |
| RS_TOP5         | 2026-09-01 00:00:00 | BRSAN.IS |      5 |  0.7242 |                 0.2679 |                 0.2204 |                 0.0010 |        1.0000 |       0.0342 |
| RS_TOP5_NO_CASH | 2026-10-01 00:00:00 | ENERY.IS |      1 |  0.8025 |                 0.4168 |                 0.5654 |                 0.6098 |        1.0000 |       0.0298 |
| RS_TOP5_NO_CASH | 2026-10-01 00:00:00 | TKFEN.IS |      2 |  0.7975 |                 0.3322 |                 0.9440 |                 1.6467 |        1.0000 |       0.0421 |
| RS_TOP5_NO_CASH | 2026-10-01 00:00:00 | AHGAZ.IS |      3 |  0.7625 |                 0.2807 |                 0.3998 |                 1.1176 |        1.0000 |       0.0254 |
| RS_TOP5_NO_CASH | 2026-10-01 00:00:00 | TUPRS.IS |      4 |  0.6775 |                 0.1325 |                 0.7376 |                 0.6248 |        1.0000 |       0.0274 |
| RS_TOP5_NO_CASH | 2026-10-01 00:00:00 | BIMAS.IS |      5 |  0.5375 |                 0.1386 |                 0.3002 |                 0.2488 |        1.0000 |       0.0194 |

## Notes

- Strategy uses only data available at each rebalance date.
- Hard filters: stock above MA50, 20-day relative strength above BIST100, liquidity floor, volatility cap.
- Regime cash filter: no stock exposure when BIST100 is below MA200.
- Missing tickers are excluded and never substituted.
