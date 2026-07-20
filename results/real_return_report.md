# Real Return Report

This report evaluates performance in both TL and USD terms. USD performance is estimated with USDTRY.

## Cash Allocation

- Minimum BUY expected return: 0.00%
- BUY candidates meeting threshold: 5
- Active portfolio slot count: 10
- Implied CASH weight when using equal opportunity slots: 50.00%

## Paper Portfolio TL / USD

- Latest portfolio value TL: 10,242,586.08
- Portfolio TL return: 351.22%
- USDTRY return over paper period: 2.48%
- Portfolio USD return: 340.29%
- Benchmark TL return: 3.99%

## Best Model TL / USD

- Model: trend_following
- Portfolio size: 3
- Period in `best_model_results.csv`: all available rows for selected model/size

| metric             |      TL |     USD |   USDTRY |
|:-------------------|--------:|--------:|---------:|
| total_return       | 21.3988 |  1.1460 |   9.4374 |
| avg_monthly_return |  0.0373 |  0.0132 |   0.0263 |
| max_drawdown       | -0.3455 | -0.4140 |  -0.2322 |
| win_rate           |  0.6392 |  0.5155 |          |

Interpretation: USD return converts TL strategy returns by the monthly USDTRY change. When USDTRY rises faster than the TL portfolio, USD-based performance falls.

## Market Reference

- Latest BIST100 close: 13,981.10
