import numpy as np

def evaluate_performance(data):
    daily_return = data['Strategy_Return']
    
    # Remove NaNs
    daily_return = daily_return.dropna()

    # Basic metrics
    cumulative_return = (1 + daily_return).prod() - 1
    annualized_return = (1 + cumulative_return) ** (252 / len(daily_return)) - 1
    volatility = daily_return.std() * np.sqrt(252)
    sharpe_ratio = daily_return.mean() / daily_return.std() * np.sqrt(252)

    # Sortino Ratio
    negative_returns = daily_return[daily_return < 0]
    downside_std = negative_returns.std() * np.sqrt(252)
    sortino_ratio = daily_return.mean() / downside_std * np.sqrt(252) if downside_std != 0 else np.nan

    # Max Drawdown
    cumulative = (1 + daily_return).cumprod()
    peak = cumulative.cummax()
    drawdown = (cumulative - peak) / peak
    max_drawdown = drawdown.min()

    print("\n📊 PROFESSIONAL STRATEGY METRICS:")
    print(f"Annualized Return: {annualized_return:.2%}")
    print(f"Annualized Volatility: {volatility:.2%}")
    print(f"Sharpe Ratio: {sharpe_ratio:.2f}")
    print(f"Sortino Ratio: {sortino_ratio:.2f}")
    print(f"Maximum Drawdown: {max_drawdown:.2%}")
 
