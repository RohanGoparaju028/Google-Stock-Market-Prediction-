import yfinance as yf
import pandas as pd
import sys

def pull_stock_data(company_name, start_date, end_date):
    stock = yf.download(company_name, start=start_date, end=end_date)
    return stock

def PreProcessing(stock):
    print("Before removing null values", stock.isnull().sum())
    stock.dropna(inplace=True)
    print("After removing null values", stock.isnull().sum())

    if isinstance(stock.columns, pd.MultiIndex):
        stock.columns = stock.columns.get_level_values(0)
    new_names = {
        'Close': 'Close',
        'High': 'High',
        'Low': 'Low',
        'Open': 'Open',
        'Volume': 'Volume'
    }
    stock.rename(columns=new_names, inplace=True)

    stock['Target'] = (stock['Close'].shift(-1) > stock['Close']).astype(int)

    stock.dropna(inplace=True)

    return stock