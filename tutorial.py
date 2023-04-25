import bs4 as bs
import pickle
import requests
import datetime as dt
import os
import pandas as pd
import ticker_util as tu
from pathlib import Path



## TUTORIAL 5 & 6

tu.get_data_from_yahoo()

## TUTORIAL 4
# import mplfinance as mpf
# df = tu.get_ticker_from_csv('MSFT')
# mpf.plot(df, type='candle', style='charles',
#             title='Title',
#             ylabel='Ylabel',
#             ylabel_lower='Ylabel_lower',
#             figratio=(25,10),
#             figscale=1,
#             mav=50,
#             volume=True
#             )


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

