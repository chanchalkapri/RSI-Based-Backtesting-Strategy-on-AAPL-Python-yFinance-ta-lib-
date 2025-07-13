import yfinance as yf
import pandas as pd

def load_data(ticker: str, period: str = '1y') -> pd.DataFrame:
    data = yf.download(ticker, period=period, auto_adjust=True)

    # Reset column if multi-indexed
    if isinstance(data.columns, pd.MultiIndex):
        data.columns = data.columns.get_level_values(0)

    # Make sure 'Close' is a Series
    data['Close'] = data['Close'].astype(float)

    return data
