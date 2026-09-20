# Real Return Report

This report evaluates performance in both TL and USD terms. USD performance is estimated with USDTRY.

## Cash Allocation

- Minimum BUY expected return: 0.00%
- BUY candidates meeting threshold: 3
- Active portfolio slot count: 5
- Implied CASH weight when using equal opportunity slots: 40.00%

## Paper Portfolio TL / USD

- Latest portfolio value TL: 17,257,629.55
- Portfolio TL return: 660.25%
- USDTRY return over paper period: 6.01%
- Portfolio USD return: 617.16%
- Benchmark TL return: -4.24%

## Best Model TL / USD

- Model: trend_following
- Portfolio size: 3
- Period in `best_model_results.csv`: all available rows for selected model/size

| metric             |      TL |     USD |   USDTRY |
|:-------------------|--------:|--------:|---------:|
| total_return       | 21.8344 |  1.1149 |   9.7969 |
| avg_monthly_return |  0.0368 |  0.0128 |   0.0261 |
| max_drawdown       | -0.3455 | -0.4140 |  -0.2322 |
| win_rate           |  0.6263 |  0.5051 |          |

Interpretation: USD return converts TL strategy returns by the monthly USDTRY change. When USDTRY rises faster than the TL portfolio, USD-based performance falls.

## Market Reference

- Latest BIST100 close: 13,284.40
