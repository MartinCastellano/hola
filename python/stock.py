#! python3

from pandas_datareader import data
from pandas_datareader._utils import RemoteDataError
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from datetime import datetime
# from pandas.util.testing import assert_frame_equal


start_date  = '2005-01-01'

end_date = str(datetime.now().strftime('%Y-%m-%d'))


uk_stock = 'UU.L'

usa_stock = '^GSPC'

def get_stat(stock_data):
    return{
        'last': np.mean(stock_data.tail(1)),
        'short_mean': np.mean(stock_data.tail(20)),
        'long_mean': np.mean(stock_data.tail(200)),
        'short_rolling':stock_data.rolling(window=20).mean(),
        'long_rolling': stock_data.rolling(window=200).mean()
    }


def clean_data(stock_data,col):

    weekdays = pd.date_range(start = start_date ,end = end_date)

    clean_data = stock_data[col].reindex(weekdays)

    return clean_data.fillna(method = 'ffill')

def create_plt(stock_data,ticker):

    stats = get_stat(stock_data)

    plt.subplots(figsize = (12,8))
    plt.plot(stock_data,label = ticker)
    plt.plot(stats['short_rolling'],label = '20 days rolling')
    plt.plot(stats['long_rolling'],label = '200 days rolling')

    plt.xlabel('Date')
    plt.ylabel('Adj Close (p)')
    plt.legend()
    plt.title('stock ')
    plt.show()




def get_data(ticker):

    try :
        stock_data =data.DataReader(ticker,'yahoo',start_date,end_date)

        adj_close = clean_data(stock_data,'Adj Close')
        # print(stock_data)
        create_plt(adj_close,ticker)
    except RemoteDataError:
        print('No data from {t}'.format(t = ticker))


get_data(usa_stock)




