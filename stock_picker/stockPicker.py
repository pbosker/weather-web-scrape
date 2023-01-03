import pandas as pd
import yfinance as yf
import numpy as np

def get_rolling_ret(df,n):
    return df.rolling(n).apply(np.prod)

def get_top(date):
    top_50 = ret_12.loc[date].nlargest(50).index
    top_30 = ret_6.loc[date, top_50].nlargest(30).index
    top_10 = ret_3.loc[date, top_30].nlargest(10).index
    return top_10

ticker_df = pd.read_html("http://en.wikipedia.org/wiki/Nasdaq-100")[4]
tickers = ticker_df = ticker_df.Ticker.to_list()
df = yf.download(tickers,start='2022-01-01')['Adj Close']
df = df.dropna(axis=1)
mtl = (df.pct_change() +1)[1:].resample('M').prod()
ret_12, ret_6, ret_3 = get_rolling_ret(mtl,12), get_rolling_ret(mtl,6), get_rolling_ret(mtl,3)
top_10 = get_top('2022-12-31')
print(top_10)
