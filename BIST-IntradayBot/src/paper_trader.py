from __future__ import annotations

from dataclasses import dataclass

import pandas as pd

import config


@dataclass
class PaperTradeResult:
    trades: pd.DataFrame
    portfolio_return: float
    portfolio_pnl: float
    ending_value: float
    benchmark_return: float
    excess_return: float
    best_trade: str
    worst_trade: str


def _benchmark_return(benchmark_session: pd.DataFrame) -> float:
    if benchmark_session.empty or len(benchmark_session) < 2:
        return 0.0
    return float(benchmark_session["Close"].iloc[-1] / benchmark_session["Open"].iloc[0] - 1.0)


def simulate_day(
    selected_signals: pd.DataFrame,
    session_prices: dict[str, pd.DataFrame],
    benchmark_session: pd.DataFrame,
) -> PaperTradeResult:
    benchmark_return = _benchmark_return(benchmark_session)
    if selected_signals.empty:
        return PaperTradeResult(
            trades=pd.DataFrame(),
            portfolio_return=0.0,
            portfolio_pnl=0.0,
            ending_value=config.STARTING_CAPITAL,
            benchmark_return=benchmark_return,
            excess_return=-benchmark_return,
            best_trade="Yok",
            worst_trade="Yok",
        )

    position_count = min(len(selected_signals), config.MAX_ACTIVE_POSITIONS)
    position_size = config.STARTING_CAPITAL / config.MAX_ACTIVE_POSITIONS
    rows = []

    for _, signal in selected_signals.head(config.MAX_ACTIVE_POSITIONS).iterrows():
        symbol = signal["symbol"]
        frame = session_prices[symbol]
        entry_time = signal["signal_time"]
        entry_price = float(signal["entry_price"])
        exit_time = frame.index[-1]
        exit_price = float(frame["Close"].iloc[-1])
        gross_return = exit_price / entry_price - 1.0
        cost_drag = 2.0 * (config.TRANSACTION_COST_RATE + config.SLIPPAGE_RATE)
        net_return = gross_return - cost_drag
        pnl = position_size * net_return
        rows.append(
            {
                "Hisse": symbol,
                "Entry Time": entry_time,
                "Exit Time": exit_time,
                "Entry Price": entry_price,
                "Exit Price": exit_price,
                "Return %": net_return,
                "PnL TL": pnl,
                "Reason": signal["reason"],
            }
        )

    trades = pd.DataFrame(rows)
    portfolio_pnl = float(trades["PnL TL"].sum())
    invested_capital = position_size * position_count
    cash = config.STARTING_CAPITAL - invested_capital
    ending_value = cash + invested_capital + portfolio_pnl
    portfolio_return = ending_value / config.STARTING_CAPITAL - 1.0
    excess_return = portfolio_return - benchmark_return

    best_row = trades.sort_values("Return %", ascending=False).iloc[0]
    worst_row = trades.sort_values("Return %", ascending=True).iloc[0]
    return PaperTradeResult(
        trades=trades,
        portfolio_return=portfolio_return,
        portfolio_pnl=portfolio_pnl,
        ending_value=ending_value,
        benchmark_return=benchmark_return,
        excess_return=excess_return,
        best_trade=f"{best_row['Hisse']} ({best_row['Return %']:.2%})",
        worst_trade=f"{worst_row['Hisse']} ({worst_row['Return %']:.2%})",
    )
