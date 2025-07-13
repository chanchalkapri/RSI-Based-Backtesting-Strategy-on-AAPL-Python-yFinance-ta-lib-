import pandas as pd

def generate_rsi_signals(data, rsi_buy=30, rsi_sell=70):
    data['RSI_Signal'] = 0

    # Buy when RSI < rsi_buy, Sell when RSI > rsi_sell
    data.loc[data['RSI'] < rsi_buy, 'RSI_Signal'] = 1
    data.loc[data['RSI'] > rsi_sell, 'RSI_Signal'] = -1

    # Identify positions (where signal changes)
    data['Position'] = data['RSI_Signal'].diff()

    # Create trade log
    trades = data[data['Position'].isin([2, -2])][['Close']]
    trades['Trade'] = data['Position'].map({2: 'Buy', -2: 'Sell'})
    trades = trades[['Trade', 'Close']]

    return data, trades
