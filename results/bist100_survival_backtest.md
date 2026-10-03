# BIST100 Relative Strength Survival Backtest

- Period: 2023-10-02 to 2026-10-02
- Configured BIST100 symbols: 100
- Loaded symbols: 97
- Missing/no valid data symbols: 3
- Production tracking_state.json was not modified.

## Policy Summary

| policy_id       | policy_name                              |   months | total_return   | bist100_total_return   | cagr   | bist100_cagr   | excess_cagr   | max_drawdown   | bist100_max_drawdown   |   sharpe_proxy | monthly_win_rate_vs_bist100   | average_monthly_excess_return   | worst_month   | worst_month_excess   | best_month   | best_month_excess   | average_turnover   |   average_trades_per_month |   cash_months |   average_holdings | transaction_cost_impact   |
|:----------------|:-----------------------------------------|---------:|:---------------|:-----------------------|:-------|:---------------|:--------------|:---------------|:-----------------------|---------------:|:------------------------------|:--------------------------------|:--------------|:---------------------|:-------------|:--------------------|:-------------------|---------------------------:|--------------:|-------------------:|:--------------------------|
| BENCHMARK       | BIST100 benchmark                        |       37 | 44.58%         | 44.58%                 | 13.07% | 13.07%         | 0.00%         | -17.72%        | -17.72%                |       0.609636 | 0.00%                         | 0.00%                           | 2023-10       | 0.00%                | 2023-10      | 0.00%               | 0.00%              |                    0       |             0 |            0       | 0.00%                     |
| OLD_TOP3        | Old absolute-score Top3                  |       37 | 46.70%         | 44.58%                 | 13.62% | 13.07%         | 0.55%         | -31.62%        | -17.72%                |       0.539449 | 45.95%                        | 0.25%                           | 2024-03       | -14.56%              | 2026-05      | 22.66%              | 129.73%            |                    3.89189 |             9 |            2.27027 | 9.60%                     |
| RS_TOP10        | BIST100 relative-strength survival Top10 |       37 | 56.33%         | 44.58%                 | 16.06% | 13.07%         | 2.98%         | -29.04%        | -17.72%                |       0.62816  | 56.76%                        | 0.34%                           | 2026-07       | -12.00%              | 2026-05      | 20.05%              | 107.57%            |                   10.7568  |             9 |            7.56757 | 7.96%                     |
| RS_TOP3         | BIST100 relative-strength survival Top3  |       37 | 91.97%         | 44.58%                 | 24.28% | 13.07%         | 11.20%        | -33.30%        | -17.72%                |       0.656859 | 51.35%                        | 1.48%                           | 2023-12       | -15.95%              | 2023-11      | 38.81%              | 127.93%            |                    3.83784 |             9 |            2.27027 | 9.47%                     |
| RS_TOP5         | BIST100 relative-strength survival Top5  |       37 | 7.42%          | 44.58%                 | 2.41%  | 13.07%         | -10.66%       | -42.64%        | -17.72%                |       0.26855  | 48.65%                        | -0.30%                          | 2026-09       | -17.81%              | 2023-11      | 23.75%              | 120.00%            |                    6       |             9 |            3.78378 | 8.88%                     |
| RS_TOP5_NO_CASH | Survival Top5 without MA200 cash filter  |       37 | 69.82%         | 44.58%                 | 19.30% | 13.07%         | 6.23%         | -42.66%        | -17.72%                |       0.616746 | 56.76%                        | 1.02%                           | 2026-09       | -17.81%              | 2023-11      | 23.75%              | 146.49%            |                    7.32432 |             0 |            5       | 10.84%                    |

## Decision

Selected winner: Survival Top5 without MA200 cash filter (excess CAGR 6.23%, max drawdown -42.66%).

No strict drawdown-safe candidate passed both excess-return and drawdown tests.

Raw-return winner: BIST100 relative-strength survival Top3 (excess CAGR 11.20%, max drawdown -33.30%).

This selected winner is the aggressive research champion: it removes the MA200 cash filter and accepts slightly worse drawdown than BIST100 in exchange for the strongest historical excess CAGR in this run.

## Latest Survival Selections

| policy_id       | date                | symbol   |   rank |   score |   relative_strength_1m |   relative_strength_3m |   relative_strength_6m |   trend_score |   volatility |
|:----------------|:--------------------|:---------|-------:|--------:|-----------------------:|-----------------------:|-----------------------:|--------------:|-------------:|
| OLD_TOP3        | 2026-09-01 00:00:00 | TKFEN.IS |      1 |  0.8948 |                 0.2457 |                 0.4051 |                 1.9714 |        1.0000 |       0.0384 |
| OLD_TOP3        | 2026-09-01 00:00:00 | TUPRS.IS |      2 |  0.8660 |                 0.3254 |                 0.6741 |                 0.7989 |        1.0000 |       0.0271 |
| OLD_TOP3        | 2026-09-01 00:00:00 | KCHOL.IS |      3 |  0.8655 |                 0.0305 |                 0.1195 |                 0.0737 |        1.0000 |       0.0191 |
| RS_TOP10        | 2026-09-01 00:00:00 | TUPRS.IS |      1 |  0.8450 |                 0.3254 |                 0.6741 |                 0.7989 |        1.0000 |       0.0271 |
| RS_TOP10        | 2026-09-01 00:00:00 | TKFEN.IS |      2 |  0.8067 |                 0.2457 |                 0.4051 |                 1.9714 |        1.0000 |       0.0384 |
| RS_TOP10        | 2026-09-01 00:00:00 | KTLEV.IS |      3 |  0.7883 |                 0.3042 |                 0.2634 |                 2.5615 |        1.0000 |       0.0431 |
| RS_TOP10        | 2026-09-01 00:00:00 | PASEU.IS |      4 |  0.7733 |                 0.2236 |                 0.9913 |                 0.6875 |        1.0000 |       0.0588 |
| RS_TOP10        | 2026-09-01 00:00:00 | BRSAN.IS |      5 |  0.7617 |                 0.2679 |                 0.2204 |                 0.1455 |        1.0000 |       0.0342 |
| RS_TOP10        | 2026-09-01 00:00:00 | AHGAZ.IS |      6 |  0.7000 |                 0.1359 |                 0.1970 |                 0.5275 |        1.0000 |       0.0270 |
| RS_TOP10        | 2026-09-01 00:00:00 | KCHOL.IS |      7 |  0.6650 |                 0.0305 |                 0.1195 |                 0.0737 |        1.0000 |       0.0191 |
| RS_TOP10        | 2026-09-01 00:00:00 | KRDMD.IS |      8 |  0.6033 |                 0.0429 |                 0.0780 |                 0.3034 |        1.0000 |       0.0281 |
| RS_TOP10        | 2026-09-01 00:00:00 | ENERY.IS |      9 |  0.5917 |                 0.0929 |                 0.1390 |                -0.0135 |        1.0000 |       0.0322 |
| RS_TOP10        | 2026-09-01 00:00:00 | AYDEM.IS |     10 |  0.5733 |                 0.0805 |                -0.0104 |                -0.0099 |        1.0000 |       0.0268 |
| RS_TOP3         | 2026-09-01 00:00:00 | TUPRS.IS |      1 |  0.8450 |                 0.3254 |                 0.6741 |                 0.7989 |        1.0000 |       0.0271 |
| RS_TOP3         | 2026-09-01 00:00:00 | TKFEN.IS |      2 |  0.8067 |                 0.2457 |                 0.4051 |                 1.9714 |        1.0000 |       0.0384 |
| RS_TOP3         | 2026-09-01 00:00:00 | KTLEV.IS |      3 |  0.7883 |                 0.3042 |                 0.2634 |                 2.5615 |        1.0000 |       0.0431 |
| RS_TOP5         | 2026-09-01 00:00:00 | TUPRS.IS |      1 |  0.8450 |                 0.3254 |                 0.6741 |                 0.7989 |        1.0000 |       0.0271 |
| RS_TOP5         | 2026-09-01 00:00:00 | TKFEN.IS |      2 |  0.8067 |                 0.2457 |                 0.4051 |                 1.9714 |        1.0000 |       0.0384 |
| RS_TOP5         | 2026-09-01 00:00:00 | KTLEV.IS |      3 |  0.7883 |                 0.3042 |                 0.2634 |                 2.5615 |        1.0000 |       0.0431 |
| RS_TOP5         | 2026-09-01 00:00:00 | PASEU.IS |      4 |  0.7733 |                 0.2236 |                 0.9913 |                 0.6875 |        1.0000 |       0.0588 |
| RS_TOP5         | 2026-09-01 00:00:00 | BRSAN.IS |      5 |  0.7617 |                 0.2679 |                 0.2204 |                 0.1455 |        1.0000 |       0.0342 |
| RS_TOP5_NO_CASH | 2026-10-01 00:00:00 | ENERY.IS |      1 |  0.8175 |                 0.4168 |                 0.5654 |                 0.6563 |        1.0000 |       0.0298 |
| RS_TOP5_NO_CASH | 2026-10-01 00:00:00 | TKFEN.IS |      2 |  0.7975 |                 0.3322 |                 0.9440 |                 1.5345 |        1.0000 |       0.0421 |
| RS_TOP5_NO_CASH | 2026-10-01 00:00:00 | AHGAZ.IS |      3 |  0.7625 |                 0.2807 |                 0.3998 |                 1.1204 |        1.0000 |       0.0254 |
| RS_TOP5_NO_CASH | 2026-10-01 00:00:00 | TUPRS.IS |      4 |  0.6625 |                 0.1325 |                 0.7376 |                 0.6003 |        1.0000 |       0.0274 |
| RS_TOP5_NO_CASH | 2026-10-01 00:00:00 | BIMAS.IS |      5 |  0.5375 |                 0.1386 |                 0.3002 |                 0.2601 |        1.0000 |       0.0194 |

## Notes

- Strategy uses only data available at each rebalance date.
- Hard filters: stock above MA50, 20-day relative strength above BIST100, liquidity floor, volatility cap.
- Regime cash filter: no stock exposure when BIST100 is below MA200.
- Missing tickers are excluded and never substituted.
