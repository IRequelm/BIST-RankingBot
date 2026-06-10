# Production Candidate Validation

## Candidate Rules

- Use ranking score only
- Ignore expected_return_mid / expected_return_low / expected_return_high
- No opportunity filter
- No expected-return gating
- No forced CASH allocation
- Regime filter ON
- Fully invested
- Top3 ranked stocks only
- Equal weight

## Summary Comparison

| policy                             |   months |   cagr |   annual_return |   bist100_cagr |   excess_cagr |   win_rate_vs_bist100 |   max_drawdown |   average_monthly_return |   average_excess_return |   volatility |   sharpe_proxy | worst_month   |   worst_month_return | best_month   |   best_month_return |   number_of_trades |   average_cash_weight |
|:-----------------------------------|---------:|-------:|----------------:|---------------:|--------------:|----------------------:|---------------:|-------------------------:|------------------------:|-------------:|---------------:|:--------------|---------------------:|:-------------|--------------------:|-------------------:|----------------------:|
| Policy_D_Production_Candidate_Top3 |       30 | 0.2679 |          0.2679 |         0.2286 |        0.0393 |                0.4667 |        -0.1517 |                   0.0229 |                  0.0035 |       0.0789 |         1.0059 | 2024-03       |              -0.0952 | 2025-03      |              0.1149 |                 90 |                0.0000 |
| Stress_Top3                        |       30 | 0.2679 |          0.2679 |         0.2286 |        0.0393 |                0.4667 |        -0.1517 |                   0.0229 |                  0.0035 |       0.0789 |         1.0059 | 2024-03       |              -0.0952 | 2025-03      |              0.1149 |                 90 |                0.0000 |
| Stress_Top5                        |       30 | 0.2295 |          0.2295 |         0.2286 |        0.0009 |                0.4000 |        -0.1380 |                   0.0198 |                  0.0004 |       0.0718 |         0.9544 | 2024-02       |              -0.0432 | 2025-01      |              0.0880 |                150 |                0.0000 |
| Ranking Only                       |       30 | 0.1877 |          0.1877 |         0.2286 |       -0.0409 |                0.4667 |        -0.1679 |                   0.0165 |                 -0.0029 |       0.0668 |         0.8558 | 2024-11       |               0.0571 | 2025-01      |              0.0186 |                300 |                0.0000 |
| Stress_Top10                       |       30 | 0.1877 |          0.1877 |         0.2286 |       -0.0409 |                0.4667 |        -0.1679 |                   0.0165 |                 -0.0029 |       0.0668 |         0.8558 | 2024-11       |               0.0571 | 2025-01      |              0.0186 |                300 |                0.0000 |
| Current Production                 |       30 | 0.1117 |          0.1117 |         0.2286 |       -0.1169 |                0.3667 |        -0.0961 |                   0.0095 |                 -0.0099 |       0.0370 |         0.8909 | 2025-06       |               0.0213 | 2024-09      |             -0.0219 |                131 |                0.4933 |

## Stress Test: Top3 vs Top5 vs Top10

| policy       |   cagr |   excess_cagr |   win_rate_vs_bist100 |   max_drawdown |   volatility |   sharpe_proxy |   number_of_trades |
|:-------------|-------:|--------------:|----------------------:|---------------:|-------------:|---------------:|-------------------:|
| Stress_Top3  | 0.2679 |        0.0393 |                0.4667 |        -0.1517 |       0.0789 |         1.0059 |                 90 |
| Stress_Top5  | 0.2295 |        0.0009 |                0.4000 |        -0.1380 |       0.0718 |         0.9544 |                150 |
| Stress_Top10 | 0.1877 |       -0.0409 |                0.4667 |        -0.1679 |       0.0668 |         0.8558 |                300 |

## Recommendation

Best configuration by CAGR is **Policy_D_Production_Candidate_Top3**.

Production candidate Top3 CAGR: 26.79%
Current production CAGR: 11.17%
Candidate excess CAGR vs BIST100: 3.93%
Candidate win rate vs BIST100: 46.67%
Candidate max drawdown: -15.17%

Among Top3 / Top5 / Top10 stress tests, Top3 is the strongest CAGR configuration. Top5 has lower CAGR but higher win rate and lower volatility. Top10 dilutes the edge.

## Should expected_return_mid be removed?

**Yes, from production action/gating.**

Evidence:

- Current production with expected-return gating: 11.17% CAGR
- Production candidate without expected-return gating: 26.79% CAGR
- CAGR improvement: 15.62%
- Prior predictive-power audit found expected_return_mid has negative forward correlation with next-month return.
- Prior ranking-action audit showed expected_return_mid creates contradictory Rank #1 + SELL cases.

## Final Conclusion

The next production version should be validated as **Top3 ranking-only, fully invested, regime ON, equal weight**. This does not mean deploy immediately; it means this is the best candidate from the controlled replay validation.
