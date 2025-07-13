# utils/plotter.py
import matplotlib.pyplot as plt

def plot_price_and_rsi(data):
    plt.figure(figsize=(14, 7))

    # Price and RSI
    ax1 = plt.subplot(2, 1, 1)
    ax1.plot(data['Close'], label='Close Price')
    ax1.set_title('Price Chart with Buy/Sell Signals')
    ax1.set_ylabel('Price')
    ax1.legend()

    # Plot Buy/Sell Signals
    buy_signals = data[data['RSI_Signal'] == 1]
    sell_signals = data[data['RSI_Signal'] == -1]
    ax1.plot(buy_signals.index, buy_signals['Close'], '^', markersize=10, color='green', label='Buy')
    ax1.plot(sell_signals.index, sell_signals['Close'], 'v', markersize=10, color='red', label='Sell')
    ax1.legend()

    ax2 = plt.subplot(2, 1, 2)
    ax2.plot(data['RSI'], label='RSI (14)', color='orange')
    ax2.axhline(70, color='red', linestyle='--', label='Overbought (70)')
    ax2.axhline(30, color='green', linestyle='--', label='Oversold (30)')
    ax2.set_ylabel('RSI')
    ax2.set_title('Relative Strength Index (RSI)')
    ax2.legend()

    plt.tight_layout()
    plt.show()


def plot_returns(data):
    plt.figure(figsize=(12, 6))
    plt.plot(data['Cumulative Market Return'], label='Market Return')
    plt.plot(data['Cumulative Strategy Return'], label='Strategy Return')
    plt.title('Cumulative Returns')
    plt.xlabel('Date')
    plt.ylabel('Growth of $1')
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()
