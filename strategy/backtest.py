def run_backtest(data):
    data['Shifted_Signal'] = data['RSI_Signal'].shift(1)
    data['Daily_Return'] = data['Close'].pct_change()
    data['Strategy_Return'] = data['Daily_Return'] * data['Shifted_Signal']
    
    # Calculate cumulative returns
    data['Cumulative Market Return'] = (1 + data['Daily_Return']).cumprod()
    data['Cumulative Strategy Return'] = (1 + data['Strategy_Return']).cumprod()
    
    return data
