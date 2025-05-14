import yfinance as yf
import pandas as pd

def get_stock_data(tickers, period="5mo"):
    data = {}
    for ticker in tickers:
        df = yf.download(ticker + ".SA", period=period)
        if not df.empty:
            data[ticker] = df['Adj Close']
    return pd.DataFrame(data)

def get_crypto_data(tickers, period="150d"):
    data = {}
    for ticker in tickers:
        df = yf.download(ticker + "-USD", period=period)
        if not df.empty:
            data[ticker] = df['Adj Close']
    return pd.DataFrame(data)
