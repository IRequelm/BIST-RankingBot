# Real Return Report

This report evaluates performance in both TL and USD terms. USD performance is estimated with USDTRY.

## Cash Allocation

- Minimum BUY expected return: 0.00%
- BUY candidates meeting threshold: 3
- Active portfolio slot count: 5
- Implied CASH weight when using equal opportunity slots: 40.00%

## Paper Portfolio TL / USD

- Latest portfolio value TL: 41,407,853.51
- Portfolio TL return: 1724.13%
- USDTRY return over paper period: 9.02%
- Portfolio USD return: 1573.21%
- Benchmark TL return: -17.30%

## Best Model TL / USD

- Model: trend_following
- Portfolio size: 3
- Period in `best_model_results.csv`: all available rows for selected model/size

| metric             |      TL |     USD |   USDTRY |
|:-------------------|--------:|--------:|---------:|
| total_return       | 19.1131 |  0.7996 |  10.1764 |
| avg_monthly_return |  0.0349 |  0.0111 |   0.0259 |
| max_drawdown       | -0.3455 | -0.4140 |  -0.2322 |
| win_rate           |  0.6139 |  0.4950 |          |

Interpretation: USD return converts TL strategy returns by the monthly USDTRY change. When USDTRY rises faster than the TL portfolio, USD-based performance falls.

## Market Reference

- Latest BIST100 close: 11,482.60
