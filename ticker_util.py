from pathlib import Path
import pandas as pd
import yfinance as yf


def download_and_store_to_csv(tickerStrings, start, end):
    for ticker in tickerStrings:
        data = yf.download(ticker, group_by="Ticker", start="2017-01-01", end="2017-04-30")
        data['ticker'] = ticker  # add this column because the dataframe doesn't contain a column with the ticker
        data.to_csv(f'ticker_{ticker}.csv')  # ticker_AAPL.csv for example
        
def get_all_tickers_from_csv():
    p = Path('C:/Users/maria/Documents/Repos/PythonProjects/Fintech')

    # find the files; this is a generator, not a list
    files = p.glob('ticker_*.csv')
    # read the files into a dataframe
    df = pd.concat([pd.read_csv(file) for file in files], ignore_index=True)
    return df

def get_ticker_from_csv(tickerString):
    p = "C:/Users/maria/Documents/Repos/PythonProjects/Fintech/ticker_{tickerName}.csv".format(tickerName = tickerString)
    df = pd.read_csv(p, parse_dates=True, index_col=0)
    return df