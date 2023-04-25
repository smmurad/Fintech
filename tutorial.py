import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt
from matplotlib import style
from pathlib import Path
import ticker_util as tu

style.use('ggplot')

## TUTORIAL 4


## TUTORIAL 3
# df = tu.get_ticker_from_csv('MSFT')
# df['100ma'] = df['Adj Close'].rolling(window=100, min_periods=0).mean()
# print(df.head())

# ax1 = plt.subplot2grid((6,1), (0,0), rowspan=5, colspan=1)
# ax2 = plt.subplot2grid((6,1), (5,0), rowspan=1, colspan=1, sharex=ax1)

# ax1.plot(df.index, df['Adj Close'])
# ax1.plot(df.index, df['100ma'])
# ax2.bar(df.index, df['Volume'])

# plt.show()


## TUTORIAL 2
# df = pd.read_csv('test.csv', parse_dates=True, index_col=0, skip_blank_lines=0)
# df = yf.download("GOOGL", start="2017-01-01", end="2017-04-30")
# df['Adj Close'].plot()
# print(df[['Open', 'Close']])
# plt.show()

## TUTORIAL 1
# ticker = yf.Ticker('GOOGL').info
# print(ticker)
# market_price = ticker['regularMarketPrice']
# previous_close_price = ticker['regularMarketPreviousClose']
# print('Ticker: GOOGL')
# print('Market Price:', market_price)
# print('Previous Close Price:', previous_close_price)

# data = yf.download("SPY AAPL", start="2017-01-01", end="2017-04-30")
# data.tp_csv('test.csv')
# df = pd.read_csv('test.csv', parse_dates=True, index_col=0, skip_blank_lines=0)

