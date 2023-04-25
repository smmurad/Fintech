from pathlib import Path
import pickle
import requests
import pandas as pd
import yfinance as yf
import bs4 as bs
import os
import datetime as dt
import ticker_util as tu

def get_data_from_yahoo(reload_sp500=False):
    if reload_sp500:
        tickers = save_sp500_tickers()
    else:
        with open("sp500tickers.pickle", "rb") as f:
            tickers = pickle.load(f)
    
    if not os.path.exists('stock_dfs'):
        os.makedirs('stock_dfs')
    
    start = dt.datetime(2000, 1, 1)
    end = dt.datetime(2023, 12, 31)
    tickers = filter_ticker_list(tickers)
    download_and_store_to_csv(tickers, start, end)

def download_and_store_to_csv(tickerStrings, start, end):
    for ticker in tickerStrings:
        data = yf.download(ticker, group_by="Ticker", start=start, end=end)
        data['ticker'] = ticker  # add this column because the dataframe doesn't contain a column with the ticker
        data.to_csv(f'stock_dfs/{ticker}.csv')
        
def get_all_tickers_from_csv():
    p = Path('C:/Users/maria/Documents/Repos/PythonProjects/Fintech/stock_dfs/')

    # find the files; this is a generator, not a list
    files = p.glob('*.csv')
    # read the files into a dataframe
    df = pd.concat([pd.read_csv(file) for file in files], ignore_index=True)
    return df

def get_ticker_from_csv(tickerString):
    p = f"C:/Users/maria/Documents/Repos/PythonProjects/Fintech/stock_dfs/{tickerString}.csv"
    df = pd.read_csv(p, parse_dates=True, index_col=0)
    return df
        
def filter_ticker_list(tickers):
    stored_tickers = get_stored_tickers()
    tickers_filtered = filter(lambda ticker: ticker not in stored_tickers, tickers)
    return list(tickers_filtered)

def get_stored_tickers():
    stored_tickers = []
    p = Path('C:/Users/maria/Documents/Repos/PythonProjects/Fintech/stock_dfs/')
    files = p.glob('*.csv')
    for file_path in files:
        stored_tickers.append(os.path.basename(file_path).rstrip('.csv'))
    return stored_tickers

def save_sp500_tickers():
    resp = requests.get('https://en.wikipedia.org/wiki/List_of_S%26P_500_companies')
    soup = bs.BeautifulSoup(resp.text, 'lxml')
    table = soup.find('table', {'class': 'wikitable sortable'})
    tickers = []
    for row in table.findAll('tr')[1:]:
        ticker = row.findAll('td')[0].text
        tickers.append(ticker.rstrip('\n'))
    
    with open("sp500tickers.pickle", "wb") as f:
        pickle.dump(tickers, f)
    
    return tickers
