import yfinance as yf
import pandas as pd
def pull_stock_data(company_name,start_date,end_date):
    stock = yf.download(company_name,start=start_date,end=end_date)
    return stock 
def PreProcessing(stock):
    print("Before removing null values",stock.isnull().sum())
    stock.dropna(inplace=True)
    print("After removing null values",stock.isnull().sum())
    