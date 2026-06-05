# Batch Replay Diagnostics

## Diagnosis

- Baseline average cash allocation: 49.33%
- Cash/excess return correlation: -0.19
- Negative excess months: 60.00% of replay months
- Worst 5 months explain 60.61% of total negative excess return.
- Risk ON average excess: -0.96%
- Defensive regime average excess: -1.06%
- Months with 3 or fewer selected stocks: 8 / 30

## Cause Checks

- Excessive CASH allocation: Yes
- Wrong model selection: Likely
- Top3 portfolio size: No; baseline is not Top3-only.
- Opportunity filter: Likely
- Regime filter: Likely
- Transaction cost: No. Batch replay holding returns do not deduct transaction cost, so transaction cost is not the measured cause here.
- Few bad months or broad weakness: Broad weakness

## Policy Comparison

| policy                       |   months |   cagr |   bist100_cagr |   excess_cagr |   win_rate_vs_bist100 |   max_drawdown |   average_cash_weight | worst_month   |   worst_month_excess | best_month   |   best_month_excess |
|:-----------------------------|---------:|-------:|---------------:|--------------:|----------------------:|---------------:|----------------------:|:--------------|---------------------:|:-------------|--------------------:|
| H_Disable_opportunity_filter |       30 | 0.2191 |         0.2286 |       -0.0095 |                0.4667 |        -0.1361 |                0.0000 | 2025-04       |              -0.0510 | 2025-03      |              0.0840 |
| A_No_cash_allocation         |       30 | 0.2134 |         0.2286 |       -0.0152 |                0.4000 |        -0.1577 |                0.0000 | 2025-06       |              -0.0776 | 2025-03      |              0.0967 |
| B_Max_cash_25pct             |       30 | 0.1625 |         0.2286 |       -0.0661 |                0.3667 |        -0.1194 |                0.2500 | 2025-06       |              -0.0910 | 2025-03      |              0.0823 |
| F_Out_of_sample_winner       |       30 | 0.1487 |         0.2286 |       -0.0799 |                0.5333 |        -0.0966 |                0.4667 | 2026-01       |              -0.1120 | 2024-09      |              0.0642 |
| G_Most_robust_model          |       30 | 0.1487 |         0.2286 |       -0.0799 |                0.5333 |        -0.0966 |                0.4667 | 2026-01       |              -0.1120 | 2024-09      |              0.0642 |
| I_Disable_regime_filter      |       30 | 0.1145 |         0.2286 |       -0.1141 |                0.3667 |        -0.1143 |                0.5000 | 2026-01       |              -0.0991 | 2024-09      |              0.0866 |
| C_Max_cash_50pct             |       30 | 0.1126 |         0.2286 |       -0.1160 |                0.3667 |        -0.0961 |                0.4833 | 2025-06       |              -0.1043 | 2024-09      |              0.0866 |
| Baseline                     |       30 | 0.1117 |         0.2286 |       -0.1169 |                0.3667 |        -0.0961 |                0.4933 | 2025-06       |              -0.1097 | 2024-09      |              0.0866 |
| E_Always_Top10               |       30 | 0.0849 |         0.2286 |       -0.1437 |                0.3667 |        -0.0954 |                0.5033 | 2026-01       |              -0.0991 | 2024-09      |              0.0866 |
| D_Always_Top5                |       30 | 0.0834 |         0.2286 |       -0.1452 |                0.3333 |        -0.1004 |                0.4200 | 2025-06       |              -0.1097 | 2025-01      |              0.0941 |

## Best Next Experiment

Test `H_Disable_opportunity_filter` as the next controlled experiment, because it has the strongest excess CAGR (-0.95%) and win rate (46.67%) in this diagnostic replay. Keep it outside production until validated on a longer replay window and with trading costs.
