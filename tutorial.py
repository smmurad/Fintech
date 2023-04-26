import numpy as np
import pickle
import requests
import datetime as dt
import os
import pandas as pd

import matplotlib.pyplot as plt
from matplotlib import style

style.use('ggplot')

## TUTORIAL 8
def visualize_data():
    df = pd.read_csv('sp500_joined_closes.csv')
    df_corr = df.corr(numeric_only=True)
    
    data = df_corr.values
    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)
    heatmap = ax.pcolor(data, cmap=plt.cm.RdYlGn)
    fig.colorbar(heatmap)
    
    ax.set_xticks(np.arange(data.shape[0]) + 0.5, minor=False)
    ax.set_yticks(np.arange(data.shape[1]) + 0.5, minor=False)
    ax.invert_yaxis()
    ax.xaxis.tick_top()
    
    coloumn_labels = df_corr.columns
    row_labels = df_corr.index
    ax.set_xticklabels(coloumn_labels)
    ax.set_yticklabels(row_labels)
    plt.xticks(rotation=90)
    heatmap.set_clim(-1, 1)
    plt.tight_layout()
    plt.show()
    
## TUTORIAL 7
def compile_data():
    with open('sp500tickers.pickle', 'rb') as f:
        tickers = pickle.load(f)
    main_df = pd.DataFrame()
    
    for count, ticker in enumerate(tickers):
        df = pd.read_csv(f'stock_dfs/{ticker}.csv')
        df.set_index('Date', inplace=True)
        df.rename(columns= {'Adj Close': ticker}, inplace=True)
        df.drop(['Open','High','Close','Volume','Low', 'ticker'], axis=1, inplace=True)
        if main_df.empty:
            main_df = df
        else:
            main_df = main_df.join(df, on='Date')
        
        if count % 10 == 0:
            print(count)
            
    main_df.to_csv('sp500_joined_closes.csv')
        
        
## TUTORIAL 5 & 6

# tu.get_data_from_yahoo()

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

