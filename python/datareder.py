import pandas_datareader.data as web

symbol = 'AAPL'  # or 'AAPL.US'

df = web.DataReader(symbol, 'yahoo', '2015-01-01', '2015-01-05')

print(df.loc['2015-01-02'])