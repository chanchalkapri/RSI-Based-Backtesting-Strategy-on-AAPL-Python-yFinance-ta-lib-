# main.py

from strategy.data_loader import load_data
from strategy.indicators import compute_rsi
from strategy.signals import generate_rsi_signals
from strategy.backtest import run_backtest
from strategy.metrics import evaluate_performance
from utils.plotter import plot_price_and_rsi, plot_returns
import os

# Parameters
ticker = 'AAPL'
period = '1y'
rsi_window = 14
rsi_buy = 30
rsi_sell = 70

def main():
    # Step 1: Load historical stock data
    data = load_data(ticker, period)

    # Step 2: Compute RSI indicator
    data = compute_rsi(data, rsi_window)

    # Step 3: Generate buy/sell signals based on RSI thresholds
    data, trades = generate_rsi_signals(data, rsi_buy, rsi_sell)

    # Step 4: Run backtest using the signals
    data = run_backtest(data)

    # Step 5: Evaluate performance (metrics like returns, Sharpe, etc.)
    evaluate_performance(data)

    # Step 6: Export the trade log to CSV
    os.makedirs("trade_logs", exist_ok=True)
    trades.to_csv("trade_logs/trades.csv")
    print("✅ Trade log saved to trade_logs/trades.csv")

    # Step 7: Plot the RSI strategy and returns
    plot_price_and_rsi(data)
    plot_returns(data)

if __name__ == "__main__":
    main()
