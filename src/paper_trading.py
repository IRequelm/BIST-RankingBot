from pathlib import Path

import pandas as pd

from src.reporting import max_drawdown


def _latest_price(stock_prices: dict[str, pd.DataFrame], symbol: str) -> tuple[pd.Timestamp, float] | tuple[None, None]:
    prices = stock_prices.get(symbol)
    if prices is None or prices.empty:
        return None, None

    close = prices["Close"].dropna()
    if close.empty:
        return None, None

    latest_date = pd.Timestamp(close.index.max())
    return latest_date, float(close.loc[latest_date])


def _benchmark_value(benchmark_prices: pd.DataFrame, start_date: pd.Timestamp, current_date: pd.Timestamp, initial: float) -> float:
    close = benchmark_prices["Close"].dropna().sort_index()
    if close.empty:
        return initial

    start_series = close.loc[close.index >= start_date]
    current_series = close.loc[close.index <= current_date]
    if start_series.empty or current_series.empty:
        return initial

    start_price = float(start_series.iloc[0])
    current_price = float(current_series.iloc[-1])
    return initial * (current_price / start_price)


def _load_csv(path: Path, columns: list[str]) -> pd.DataFrame:
    if path.exists():
        return pd.read_csv(path)
    return pd.DataFrame(columns=columns)


def _active_positions(trade_log: pd.DataFrame) -> pd.DataFrame:
    if trade_log.empty:
        return pd.DataFrame()

    active = trade_log[trade_log["status"] == "OPEN"].copy()
    return active.sort_values("entry_date")


def _close_positions(
    trade_log: pd.DataFrame,
    sell_symbols: set[str],
    stock_prices: dict[str, pd.DataFrame],
    current_date: pd.Timestamp,
) -> pd.DataFrame:
    if trade_log.empty or not sell_symbols:
        return trade_log

    updated = trade_log.copy()
    for idx, row in updated[updated["status"] == "OPEN"].iterrows():
        symbol = row["symbol"]
        if symbol not in sell_symbols:
            continue

        _, exit_price = _latest_price(stock_prices, symbol)
        if exit_price is None:
            continue

        quantity = float(row["quantity"])
        entry_value = float(row["entry_value"])
        exit_value = quantity * exit_price
        updated.loc[idx, "exit_date"] = current_date.date().isoformat()
        updated.loc[idx, "exit_price"] = exit_price
        updated.loc[idx, "exit_value"] = exit_value
        updated.loc[idx, "realized_pnl"] = exit_value - entry_value
        updated.loc[idx, "return_pct"] = (exit_price / float(row["entry_price"])) - 1
        updated.loc[idx, "holding_days"] = (current_date - pd.Timestamp(row["entry_date"])).days
        updated.loc[idx, "status"] = "CLOSED"

    return updated


def _open_positions(
    trade_log: pd.DataFrame,
    symbols: list[str],
    stock_prices: dict[str, pd.DataFrame],
    current_date: pd.Timestamp,
    cash: float,
    reason: str,
) -> tuple[pd.DataFrame, float]:
    if not symbols or cash <= 0:
        return trade_log, cash

    active_symbols = set(trade_log.loc[trade_log["status"] == "OPEN", "symbol"]) if not trade_log.empty else set()
    to_open = [symbol for symbol in symbols if symbol not in active_symbols]
    if not to_open:
        return trade_log, cash

    allocation = cash / len(to_open)
    rows = []
    used_cash = 0.0
    for symbol in to_open:
        _, price = _latest_price(stock_prices, symbol)
        if price is None or price <= 0:
            continue

        quantity = allocation / price
        entry_value = quantity * price
        used_cash += entry_value
        rows.append(
            {
                "symbol": symbol,
                "entry_date": current_date.date().isoformat(),
                "entry_price": price,
                "quantity": quantity,
                "entry_value": entry_value,
                "exit_date": "",
                "exit_price": "",
                "exit_value": "",
                "realized_pnl": 0.0,
                "return_pct": 0.0,
                "holding_days": 0,
                "status": "OPEN",
                "reason": reason,
            }
        )

    if rows:
        trade_log = pd.concat([trade_log, pd.DataFrame(rows)], ignore_index=True)

    return trade_log, cash - used_cash


def _mark_to_market(trade_log: pd.DataFrame, stock_prices: dict[str, pd.DataFrame], current_date: pd.Timestamp) -> pd.DataFrame:
    active = _active_positions(trade_log)
    rows = []
    for _, row in active.iterrows():
        symbol = row["symbol"]
        _, current_price = _latest_price(stock_prices, symbol)
        if current_price is None:
            continue

        quantity = float(row["quantity"])
        entry_price = float(row["entry_price"])
        current_value = quantity * current_price
        rows.append(
            {
                "symbol": symbol,
                "entry_date": row["entry_date"],
                "entry_price": entry_price,
                "current_price": current_price,
                "quantity": quantity,
                "entry_value": float(row["entry_value"]),
                "current_value": current_value,
                "unrealized_pnl": current_value - float(row["entry_value"]),
                "return_pct": (current_price / entry_price) - 1,
                "holding_days": (current_date - pd.Timestamp(row["entry_date"])).days,
            }
        )

    return pd.DataFrame(rows)


def _append_recommendation_snapshot(current_portfolio: pd.DataFrame, snapshot_path: Path) -> None:
    snapshot = current_portfolio.copy()
    snapshot["snapshot_month"] = pd.to_datetime(snapshot["snapshot_date"]).dt.to_period("M").astype(str)

    if snapshot_path.exists():
        existing = pd.read_csv(snapshot_path)
        existing = existing[existing["snapshot_month"] != snapshot["snapshot_month"].iloc[0]]
        snapshot = pd.concat([existing, snapshot], ignore_index=True)

    snapshot.to_csv(snapshot_path, index=False)


def update_paper_trading(
    stock_prices: dict[str, pd.DataFrame],
    benchmark_prices: pd.DataFrame,
    results_dir: str,
    paper_dir: str,
    initial_capital: float,
) -> tuple[pd.DataFrame, pd.DataFrame, str]:
    """Update paper portfolio state from current_month_portfolio.csv."""
    results_path = Path(results_dir)
    paper_path = Path(paper_dir)
    paper_path.mkdir(exist_ok=True)
    results_path.mkdir(exist_ok=True)

    current_path = results_path / "current_month_portfolio.csv"
    if not current_path.exists():
        raise FileNotFoundError("current_month_portfolio.csv must be generated before paper trading update.")

    current = pd.read_csv(current_path, parse_dates=["snapshot_date"])
    current_date = pd.Timestamp(current["snapshot_date"].max())
    recommended = current[current["recommended"] == True].copy()

    trade_log_path = results_path / "paper_trade_log.csv"
    history_path = results_path / "paper_portfolio_history.csv"
    snapshot_path = paper_path / "recommendation_snapshots.csv"

    trade_columns = [
        "symbol", "entry_date", "entry_price", "quantity", "entry_value",
        "exit_date", "exit_price", "exit_value", "realized_pnl", "return_pct",
        "holding_days", "status", "reason",
    ]
    history_columns = [
        "date", "portfolio_value", "cash", "active_position_value", "realized_pnl",
        "unrealized_pnl", "total_return", "benchmark_value", "benchmark_return",
        "active_positions",
    ]

    trade_log = _load_csv(trade_log_path, trade_columns)
    history = _load_csv(history_path, history_columns)
    _append_recommendation_snapshot(current, snapshot_path)

    latest_history = history.tail(1)
    cash = float(latest_history["cash"].iloc[0]) if not latest_history.empty else initial_capital

    sell_symbols = set(current.loc[current["action"] == "SELL", "symbol"])
    before_close = trade_log.copy()
    trade_log = _close_positions(trade_log, sell_symbols, stock_prices, current_date)
    newly_closed = trade_log[(trade_log["status"] == "CLOSED") & (trade_log["exit_date"] == current_date.date().isoformat())]
    if not newly_closed.empty:
        cash += pd.to_numeric(newly_closed["exit_value"], errors="coerce").fillna(0).sum()

    if before_close.empty and trade_log.empty:
        buy_symbols = recommended["symbol"].tolist()
        open_reason = "INITIAL_RECOMMENDED"
    else:
        buy_symbols = current.loc[current["action"] == "BUY", "symbol"].tolist()
        open_reason = "BUY_SIGNAL"

    trade_log, cash = _open_positions(trade_log, buy_symbols, stock_prices, current_date, cash, open_reason)
    active_mtm = _mark_to_market(trade_log, stock_prices, current_date)

    active_position_value = active_mtm["current_value"].sum() if not active_mtm.empty else 0.0
    realized_pnl = pd.to_numeric(trade_log.loc[trade_log["status"] == "CLOSED", "realized_pnl"], errors="coerce").fillna(0).sum()
    unrealized_pnl = active_mtm["unrealized_pnl"].sum() if not active_mtm.empty else 0.0
    portfolio_value = cash + active_position_value

    first_date = current_date if history.empty else pd.Timestamp(history["date"].iloc[0])
    benchmark_value = _benchmark_value(benchmark_prices, first_date, current_date, initial_capital)
    history_row = {
        "date": current_date.date().isoformat(),
        "portfolio_value": portfolio_value,
        "cash": cash,
        "active_position_value": active_position_value,
        "realized_pnl": realized_pnl,
        "unrealized_pnl": unrealized_pnl,
        "total_return": (portfolio_value / initial_capital) - 1,
        "benchmark_value": benchmark_value,
        "benchmark_return": (benchmark_value / initial_capital) - 1,
        "active_positions": len(active_mtm),
    }

    if not history.empty:
        history = history[history["date"] != history_row["date"]]
    history = pd.concat([history, pd.DataFrame([history_row])], ignore_index=True)

    trade_log.to_csv(trade_log_path, index=False)
    history.to_csv(history_path, index=False)

    report = _build_paper_report(active_mtm, trade_log, history, current, initial_capital)
    report_path = results_path / "paper_performance_report.md"
    report_path.write_text(report, encoding="utf-8")

    return history, trade_log, report


def _build_paper_report(
    active_mtm: pd.DataFrame,
    trade_log: pd.DataFrame,
    history: pd.DataFrame,
    current: pd.DataFrame,
    initial_capital: float,
) -> str:
    latest = history.tail(1).iloc[0]
    history_sorted = history.copy()
    history_sorted["date"] = pd.to_datetime(history_sorted["date"])
    values = pd.to_numeric(history_sorted["portfolio_value"], errors="coerce")
    returns = values.pct_change().dropna()
    total_return = (float(latest["portfolio_value"]) / initial_capital) - 1

    if len(history_sorted) > 1:
        years = max((history_sorted["date"].max() - history_sorted["date"].min()).days / 365.25, 1 / 365.25)
        annualized_return = (1 + total_return) ** (1 / years) - 1
    else:
        annualized_return = 0.0

    dd = max_drawdown(values / initial_capital) if len(values) else 0.0
    closed = trade_log[trade_log["status"] == "CLOSED"].copy()
    win_rate = (pd.to_numeric(closed["realized_pnl"], errors="coerce") > 0).mean() if not closed.empty else 0.0

    active_table = active_mtm if not active_mtm.empty else pd.DataFrame(columns=[
        "symbol", "entry_date", "entry_price", "current_price", "return_pct", "holding_days", "unrealized_pnl"
    ])
    closed_table = closed.tail(20) if not closed.empty else pd.DataFrame(columns=[
        "symbol", "entry_date", "exit_date", "entry_price", "exit_price", "return_pct", "realized_pnl"
    ])

    lines = [
        "# Paper Trading Performance Report",
        "",
        "This is a research-only paper trading tracker. It does not place trades and does not call broker APIs.",
        "",
        "## Portfolio Metrics",
        "",
        f"- Portfolio value: {float(latest['portfolio_value']):.2f}",
        f"- Cash: {float(latest['cash']):.2f}",
        f"- Benchmark value: {float(latest['benchmark_value']):.2f}",
        f"- Total return: {total_return:.2%}",
        f"- Benchmark return: {float(latest['benchmark_return']):.2%}",
        f"- Annualized return: {annualized_return:.2%}",
        f"- Max drawdown: {dd:.2%}",
        f"- Win rate: {win_rate:.2%}",
        f"- Realized PnL: {float(latest['realized_pnl']):.2f}",
        f"- Unrealized PnL: {float(latest['unrealized_pnl']):.2f}",
        "",
        "## Current Recommendation Context",
        "",
        f"- Snapshot date: {pd.to_datetime(current['snapshot_date'].max()).date()}",
        f"- Active model: {current['active_model'].iloc[0]}",
        f"- Active portfolio size: {int(current['active_portfolio_size'].iloc[0])}",
        f"- Regime status: {current['regime_status'].iloc[0]}",
        "",
        "## Active Positions",
        "",
        active_table.to_markdown(index=False, floatfmt=".4f"),
        "",
        "## Closed Positions",
        "",
        closed_table.to_markdown(index=False, floatfmt=".4f"),
        "",
        "## Portfolio History",
        "",
        history.tail(24).to_markdown(index=False, floatfmt=".4f"),
        "",
    ]
    return "\n".join(lines)
