import yfinance as yf
import pandas as pd

def fetch_stock_data(ticker='AAPL', start='2023-01-01', end='2025-01-01'):
    data = yf.download(ticker, start=start, end=end)
    data = data[['Open', 'Close', 'High', 'Low', 'Volume']]
    data['Returns'] = data['Close'].pct_change()
    data.dropna(inplace=True)
    return data

def label_market_condition(data, threshold=0.0025):
    conditions = []
    for r in data['Returns']:
        if r > threshold:
            conditions.append('Bullish')
        elif r < -threshold:
            conditions.append('Bearish')
        else:
            conditions.append('Consolidation')
    data['Market_Condition'] = conditions
    return data
