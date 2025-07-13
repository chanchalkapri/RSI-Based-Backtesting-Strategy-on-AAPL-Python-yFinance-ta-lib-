import pandas as pd
from ta.momentum import RSIIndicator

def compute_rsi(data, window=14):
    rsi = RSIIndicator(close=data['Close'], window=window)
    data['RSI'] = rsi.rsi()
    return data
