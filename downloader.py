import yfinance as yf

from datetime import date

def getData(stock_name):
    today = date.today().strftime("%Y-%m-%d")
    print("Downloading [" + stock_name +"]")  
    data = yf.Ticker(stock_name).history(period='1y')
    return data
