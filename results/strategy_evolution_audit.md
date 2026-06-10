# Strategy Evolution Audit

## Question

Why did historical backtests show very high CAGR while current batch replay shows only 11.17% CAGR?

## Short Answer

The high historical numbers were mostly produced by the older classic backtest/validation view, not by the current production replay rules. The current replay CAGR fell because the production recommendation layer added expected-return gating, opportunity filtering, and cash allocation on top of the ranking system. Those rules cut exposure aggressively during a strong BIST100 period.

The biggest direct CAGR reducers are:

1. Opportunity filter / expected-return gating
2. Cash allocation caused by the same gating
3. Using current production replay rules instead of classic full-invested backtest rules
4. Model/portfolio selection changes
5. Regime filter, which has only a small isolated impact in the current baseline

## Version Comparison

| Area | Original high-performing configuration | Current production configuration |
|:--|:--|:--|
| Ranking formula | Cross-sectional weighted score from 1m momentum, 3m momentum, 6m momentum, volume increase, MA trend, and volatility penalty | Same factor family and weighted score |
| Filters | No expected-return buy gate in the classic backtest; buy TopN directly | Expected-return gate and opportunity threshold control BUY eligibility |
| Cash allocation | Fully invested equal-weight TopN | Unqualified names become CASH; current batch replay average cash is 49.33% |
| Model selection | Classic backtest compares all factor models and portfolio sizes; best validation rows can be very high | Production replay uses active regime framework: risk-on volume_heavy Top10, defensive low_volatility Top5 |
| Portfolio size | Tested Top3 / Top5 / Top10 / Top15; high validation rows were often Top3/Top5 | Risk-on Top10, defensive Top5; actual selected BUY count often lower because of gating |
| Expected return gating | None in backtest execution; expected return bands were descriptive | expected_return_mid must pass threshold/opportunity filter to become BUY |
| Regime filter | Backtest tables are fixed-model, no live MA200 switch | MA200 regime chooses risk-on or defensive model/size |
| Opportunity filter | None | Active; percentile/floor threshold filters opportunities |
| Replay methodology | Month-end backtest on known historical ranking table; often judged on validation period | Rolling replay from 2024-01 onward, using only data available at each replay date, then measuring subsequent 30-day realized return |

## Historical Numbers vs Current Replay

| Measurement | CAGR / result | Interpretation |
|:--|--:|:--|
| Best validation classic backtest: trend_following Top3 | 152.44% CAGR | Very strong 2022-2023 validation regime; not a current out-of-sample replay result |
| Best current-period classic out-of-sample row: mixed_model Top15 | 23.23% CAGR | Full-invested classic backtest in 2024+ is close to BIST100, not 40-60%+ |
| Current batch replay production baseline | 11.17% CAGR | Production rules plus cash/gating materially reduce exposure |
| Current BIST100 in batch replay | 22.86% CAGR | Benchmark doubled the production replay CAGR |

## Impact Estimate: If Only This Feature Were Reverted

| Reverted feature / test | Estimated current replay CAGR | Impact vs 11.17% baseline | Evidence |
|:--|--:|--:|:--|
| Remove opportunity filter / expected-return gate | 21.91% | +10.74 pp | `H_Disable_opportunity_filter` diagnostic |
| Remove cash allocation by fully investing selected BUY names | 21.34% | +10.17 pp | `A_No_cash_allocation` diagnostic |
| Cap cash at 25% | 16.25% | +5.08 pp | `B_Max_cash_25pct` diagnostic |
| Cap cash at 50% | 11.26% | +0.09 pp | `C_Max_cash_50pct` diagnostic |
| Use out-of-sample winner / robust model | 14.87% | +3.70 pp | `F_Out_of_sample_winner` and `G_Most_robust_model` diagnostics |
| Disable regime filter only | 11.45% | +0.28 pp | `I_Disable_regime_filter` diagnostic |
| Revert to full-invested Top3 with opportunity filter removed and regime ON | 26.79% | +15.62 pp | final performance gap grid |
| Revert to classic current-period best full-invested backtest | 23.23% | +12.06 pp | `summary_report.csv`, mixed_model Top15 out-of-sample |

## Which Changes Reduced CAGR The Most?

### 1. Opportunity filter and expected-return gating

This is the largest direct reducer. Current production gating turns many ranked stocks into HOLD/EXCLUDE instead of BUY. In batch replay, the current system held 49.33% average cash and produced 11.17% CAGR. Removing the opportunity filter raised estimated CAGR to 21.91%.

Estimated reverted CAGR today: **21.91%**

### 2. Cash allocation

Cash allocation is not an independent alpha model; it is mostly the mechanical result of expected-return gating. Fully investing only the selected BUY names raised CAGR to 21.34%. This means the system was often selecting some reasonable names but then leaving too much capital idle.

Estimated reverted CAGR today: **21.34%**

### 3. Replay methodology and evaluation window

The apparent 40-60%+ or higher historical performance came from validation-period classic backtests. The strongest validation row is trend_following Top3 at 152.44% CAGR. But when the same classic style is judged on the current 2024+ out-of-sample window, the best row is around 23.23% CAGR, close to BIST100.

This means the biggest “drop” is not only code evolution. It is also regime/evaluation drift: validation-era results did not survive cleanly into current replay.

Estimated current CAGR under classic full-invested best row: **23.23%**

### 4. Model selection changes

Current production uses volume_heavy in risk-on and low_volatility in defensive periods. Diagnostics show that using the out-of-sample/robust winner improves CAGR to 14.87%, but this is far smaller than removing cash/gating.

Estimated reverted CAGR today: **14.87%**

### 5. Regime filter

Disabling the regime filter alone only moved CAGR from 11.17% to 11.45%. In isolation, it is not the main damage. However, regime plus TopN choice matters: Top3 with regime ON and no opportunity filter reached 26.79%, while Top5 regime OFF reached 25.39%.

Estimated reverted CAGR today if only disabled: **11.45%**

## Why Current Batch Replay Is So Much Lower

Current production replay is not equivalent to the old backtest. It adds multiple live-decision constraints:

- It decides using only data available at the replay date.
- It applies expected-return gating.
- It converts unqualified opportunities into cash.
- It uses regime-based model/size switching.
- It evaluates 30-day realized forward return.

The old high backtests were full-invested monthly TopN simulations. They did not ask: “Would the live recommendation system have actually bought this stock on that historical date after gating and cash rules?”

## Bottom Line

The main CAGR killer is not the raw ranking formula changing. The main CAGR killer is the recommendation layer added after the ranking formula:

- expected_return_mid gating
- opportunity filter
- cash allocation

If only one thing is reverted, revert the opportunity filter / expected-return gating first. Expected current replay CAGR rises from **11.17%** to about **21.91%**. If the system is further simplified to concentrated full-invested Top3 with regime ON, replay CAGR rises to about **26.79%**, but monthly consistency remains weak.

## Recommendation

Do not add new features. The next experiment should be:

**Production candidate replay: Top3, fully invested, regime ON, no expected_return_mid gating, no opportunity filter, no forced CASH.**

This is the smallest change set that directly targets the measured CAGR loss.
