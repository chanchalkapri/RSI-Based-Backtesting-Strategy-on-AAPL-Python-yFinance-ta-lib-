\# 📈 RSI Backtesting Strategy



This project backtests a simple \*\*Relative Strength Index (RSI)\*\* strategy on historical stock data using Python.



\## 📌 Strategy Logic



\- \*\*Indicator\*\*: RSI (14-day)

\- \*\*Buy\*\*: RSI < 30 (oversold)

\- \*\*Sell\*\*: RSI > 70 (overbought)

\- Positions are entered on signal crossover, held until opposite signal.



\## 📊 Key Features



\- Data loaded from \*\*Yahoo Finance\*\* via `yfinance`

\- Strategy signals based on `ta` technical analysis library

\- Vectorized \*\*backtesting engine\*\*

\- Professional-grade metrics:

&nbsp; - Annualized Return

&nbsp; - Volatility

&nbsp; - Sharpe \& Sortino Ratios

&nbsp; - Max Drawdown

\- Visualizations: Price + RSI, Returns comparison

\- Clean modular code structure

\- Exportable trade logs



\## 📁 Project Structure





