# Ranking-Action Consistency Audit

## Executive Answer

EREGL.IS can be Rank #1 and Recommended=True but Action=SELL because the system has two conflicting decision layers. The ranking layer says EREGL belongs in the active Top10 portfolio. The expected-return/action layer then overrides that ranking because expected_return_mid is negative.

This behavior is best classified as: **B) design flaw**.

It is not a simple implementation crash/bug because the code is doing exactly what it was written to do. But it is a flawed design because `recommended=True` and `SELL` communicate opposite portfolio instructions for the same stock.

## EREGL.IS Decision Trace

- Symbol: EREGL.IS
- Rank: 1
- Active model: volume_heavy
- Active portfolio size: 10
- Recommended portfolio member: True
- Score: 0.8735
- expected_return_low: -4.21%
- expected_return_mid: -0.52%
- expected_return_high: 11.56%
- Opportunity threshold: 1.50%
- Action: SELL

## Raw And Normalized Factor Values

| factor             |   raw_value | higher_is_better   |   weight |   normalized_percentile |   weighted_contribution |
|:-------------------|------------:|:-------------------|---------:|------------------------:|------------------------:|
| momentum_1m        |      0.1862 | True               |   0.1500 |                  1.0000 |                  0.1500 |
| momentum_3m        |      0.2539 | True               |   0.2000 |                  0.9412 |                  0.1882 |
| momentum_6m        |      0.6764 | True               |   0.1500 |                  0.9412 |                  0.1412 |
| volume_increase    |      0.0413 | True               |   0.3500 |                  0.8235 |                  0.2882 |
| above_ma           |      1.0000 | True               |   0.1000 |                  0.9412 |                  0.0941 |
| volatility_penalty |      0.0307 | False              |   0.0500 |                  0.2353 |                  0.0118 |

Score calculation:

```text
score = sum(weighted_contribution)
score = 0.1500 + 0.1882 + 0.1412 + 0.2882 + 0.0941 + 0.0118
score = 0.8735
```

## Action Assignment Logic

Current logic from `src/current_portfolio.py`:

```text
if expected_return_mid is missing:
    HOLD if recommended else EXCLUDE
if expected_return_mid >= opportunity_threshold:
    BUY if recommended else EXCLUDE
if expected_return_mid < 0:
    SELL
else:
    HOLD if recommended else EXCLUDE
```

For EREGL.IS:

- recommended=True because Rank #1 is inside active Top10.
- expected_return_mid=-0.52%, which is below zero.
- Therefore the action layer returns SELL.

## Why Rank #1 And SELL Can Happen

The two fields answer different questions:

- `recommended=True`: ranking layer says the stock is inside the active ranked portfolio.
- `action=SELL`: expected-return layer says the historical expected-return estimate is negative.

The inconsistency exists because the system does not reconcile those two layers into one final portfolio instruction.

## Top 20 Diagnostic Table

|   rank | symbol   |   score |   expected_return_mid | action   | recommended   | flag             |
|-------:|:---------|--------:|----------------------:|:---------|:--------------|:-----------------|
|      1 | EREGL.IS |  0.8735 |               -0.0052 | SELL     | True          | High rank + SELL |
|      2 | SISE.IS  |  0.7971 |                0.0573 | BUY      | True          |                  |
|      3 | BIMAS.IS |  0.6971 |                0.0150 | BUY      | True          |                  |
|      4 | TOASO.IS |  0.6265 |                0.0360 | BUY      | True          |                  |
|      5 | TCELL.IS |  0.5412 |               -0.0056 | SELL     | True          | High rank + SELL |
|      6 | PETKM.IS |  0.5382 |               -0.0293 | SELL     | True          |                  |
|      7 | ASELS.IS |  0.5029 |                0.0149 | HOLD     | True          |                  |
|      8 | FROTO.IS |  0.5000 |                0.1135 | BUY      | True          |                  |
|      9 | ARCLK.IS |  0.4941 |                0.0319 | BUY      | True          |                  |
|     10 | THYAO.IS |  0.4882 |               -0.0071 | SELL     | True          |                  |
|     11 | KCHOL.IS |  0.4882 |                0.0070 | EXCLUDE  | False         |                  |
|     12 | GARAN.IS |  0.4588 |                0.0063 | EXCLUDE  | False         |                  |
|     13 | TUPRS.IS |  0.4382 |                0.0180 | EXCLUDE  | False         |                  |
|     14 | SAHOL.IS |  0.4235 |               -0.0223 | SELL     | False         |                  |
|     15 | AKBNK.IS |  0.4176 |               -0.0047 | SELL     | False         |                  |
|     16 | YKBNK.IS |  0.3765 |               -0.0310 | SELL     | False         |                  |
|     17 | PGSUS.IS |  0.3382 |                0.0408 | EXCLUDE  | False         |                  |

## Mismatch Flags

|   rank | symbol   |   score |   expected_return_mid | action   | recommended   | flag             |
|-------:|:---------|--------:|----------------------:|:---------|:--------------|:-----------------|
|      1 | EREGL.IS |  0.8735 |               -0.0052 | SELL     | True          | High rank + SELL |
|      5 | TCELL.IS |  0.5412 |               -0.0056 | SELL     | True          | High rank + SELL |

## Alternative Policy Simulation

| Policy | Meaning |
|:--|:--|
| A_expected_return_only | BUY names whose expected_return_mid passes threshold, regardless of recommended flag, capped at active portfolio size |
| B_ranking_only | BUY active TopN ranked names; ignore expected_return_mid |
| C_ranking_and_expected_return | Current production-style policy: BUY only if ranked and expected return passes threshold |

|   cagr |   bist100_cagr |   excess_cagr |   avg_excess_return |   win_rate_vs_bist100 |   max_drawdown |   avg_selected_count |   avg_cash_weight | policy                        |
|-------:|---------------:|--------------:|--------------------:|----------------------:|---------------:|---------------------:|------------------:|:------------------------------|
| 0.2191 |         0.2286 |       -0.0095 |             -0.0005 |                0.4667 |        -0.1361 |               8.6667 |            0.0000 | B_ranking_only                |
| 0.1117 |         0.2286 |       -0.1169 |             -0.0099 |                0.3667 |        -0.0961 |               4.3667 |            0.4933 | C_ranking_and_expected_return |
| 0.0824 |         0.2286 |       -0.1462 |             -0.0116 |                0.3000 |        -0.1815 |               7.0000 |            0.1700 | A_expected_return_only        |

## Estimated Impact

- Current policy C CAGR: 11.17%
- Ranking-only policy B CAGR: 21.91%
- CAGR impact of trusting ranking instead of expected-return gate: 10.74%
- Win-rate impact: 10.00%

Stock selection quality also improves under ranking-only in this diagnostic if CAGR/excess return improve versus policy C. This matches earlier predictive-power audits showing expected_return_mid is not reliable.

## Is This Intentional?

Partly intentional, but not performance-justified.

The code intentionally lets expected_return_mid override ranking. However, prior audits show expected_return_mid has weak/negative forward predictive power, so the override does not currently have evidence that it improves performance.

## Which Layer Should Be Trusted More?

**Trust ranking score more than the expected-return engine.**

Reason: the expected-return layer creates contradictory instructions and materially reduces replay performance. The ranking score is imperfect, but the current expected_return_mid engine is worse as a gating/action layer.

## Recommendation

Do not modify production logic in this audit. Next controlled experiment should remove expected_return_mid from action assignment and make action follow ranking/portfolio membership first.
