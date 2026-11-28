# Real Return Report

This report evaluates performance in both TL and USD terms. USD performance is estimated with USDTRY.

## Cash Allocation

- Minimum BUY expected return: 0.00%
- BUY candidates meeting threshold: 2
- Active portfolio slot count: 5
- Implied CASH weight when using equal opportunity slots: 60.00%

## Paper Portfolio TL / USD

- Latest portfolio value TL: 41,521,539.93
- Portfolio TL return: 1729.14%
- USDTRY return over paper period: 10.62%
- Portfolio USD return: 1553.48%
- Benchmark TL return: -19.90%

## Best Model TL / USD

- Model: trend_following
- Portfolio size: 3
- Period in `best_model_results.csv`: all available rows for selected model/size

| metric             |      TL |     USD |   USDTRY |
|:-------------------|--------:|--------:|---------:|
| total_return       | 18.4309 |  0.7386 |  10.1764 |
| avg_monthly_return |  0.0345 |  0.0107 |   0.0259 |
| max_drawdown       | -0.3455 | -0.4140 |  -0.2322 |
| win_rate           |  0.6139 |  0.4950 |          |

Interpretation: USD return converts TL strategy returns by the monthly USDTRY change. When USDTRY rises faster than the TL portfolio, USD-based performance falls.

## Market Reference

- Latest BIST100 close: 10,977.00
