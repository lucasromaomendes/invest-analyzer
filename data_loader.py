import yfinance as yf
import pandas as pd

def get_stock_data(tickers, period="5mo"):
    data = {}

    for ticker in tickers:
        if not ticker:
            continue
        try:
            ticker_yf = ticker.upper().strip() + ".SA"
            df = yf.download(ticker_yf, period=period, progress=False)
            if not df.empty and "Adj Close" in df.columns:
                data[ticker] = df["Adj Close"]
            else:
                print(f"Nenhum dado válido para ação: {ticker}")
        except Exception as e:
            print(f"Erro ao baixar ação {ticker}: {e}")

    return pd.DataFrame(data)

def get_crypto_data(tickers, period="5mo"):
    data = {}

    for ticker in tickers:
        if not ticker:
            continue
        try:
            ticker_yf = ticker.upper().strip() + "-USD"
            df = yf.download(ticker_yf, period=period, progress=False)
            if not df.empty and "Adj Close" in df.columns:
                data[ticker] = df["Adj Close"]
            else:
                print(f"Nenhum dado válido para cripto: {ticker}")
        except Exception as e:
            print(f"Erro ao baixar cripto {ticker}: {e}")

    return pd.DataFrame(data)
