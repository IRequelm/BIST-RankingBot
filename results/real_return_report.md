# Real Return Report

This report evaluates performance in both TL and USD terms. USD performance is estimated with USDTRY.

## Cash Allocation

- Minimum BUY expected return: 0.00%
- BUY candidates meeting threshold: 3
- Active portfolio slot count: 5
- Implied CASH weight when using equal opportunity slots: 40.00%

## Paper Portfolio TL / USD

- Latest portfolio value TL: 42,203,213.72
- Portfolio TL return: 1759.17%
- USDTRY return over paper period: 10.19%
- Portfolio USD return: 1587.20%
- Benchmark TL return: -18.97%

## Best Model TL / USD

- Model: trend_following
- Portfolio size: 3
- Period in `best_model_results.csv`: all available rows for selected model/size

| metric             |      TL |     USD |   USDTRY |
|:-------------------|--------:|--------:|---------:|
| total_return       | 18.9486 |  0.7849 |  10.1764 |
| avg_monthly_return |  0.0348 |  0.0110 |   0.0259 |
| max_drawdown       | -0.3455 | -0.4140 |  -0.2322 |
| win_rate           |  0.6139 |  0.4950 |          |

Interpretation: USD return converts TL strategy returns by the monthly USDTRY change. When USDTRY rises faster than the TL portfolio, USD-based performance falls.

## Market Reference

- Latest BIST100 close: 11,104.40
