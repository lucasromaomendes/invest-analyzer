import yfinance as yf
import pandas as pd

def get_stock_data(tickers, period="5mo"):
    data = {}

    for ticker in tickers:
        if not ticker:
            continue
        try:
            df = yf.download(ticker + ".SA", period=period, progress=False)
            if not df.empty:
                if "Adj Close" in df.columns:
                    data[ticker] = df["Adj Close"]
                elif isinstance(df.columns, pd.MultiIndex):
                    data[ticker] = df[("Adj Close", ticker + ".SA")]
        except Exception as e:
            print(f"Erro ao baixar {ticker}: {e}")

    return pd.DataFrame(data)

def get_crypto_data(tickers, period="150d"):
    data = {}
    for ticker in tickers:
        if not ticker:
            continue
        try:
            df = yf.download(ticker + "-USD", period=period, progress=False)
            if not df.empty:
                if "Adj Close" in df.columns:
                    data[ticker] = df["Adj Close"]
        except Exception as e:
            print(f"Erro ao baixar {ticker}: {e}")
    return pd.DataFrame(data)
