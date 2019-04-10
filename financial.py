# -*- coding: utf-8 -*-
"""
Created on Wed Apr 10 22:58:41 2019

Financial Ananlysis Project

@author: Rishabh
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

%matplotlib inline
import pandas_datareader.data as web 
import datetime
start=datetime.datetime(2015,1,1)
end=datetime.datetime(2019,1,1)
tesla= web.DataReader('TSLA','iex',start,end)
tesla.head()
ford=web.DataReader('F','iex',start,end)
gm= web.DataReader('GM','iex',start,end)
ford.head()
gm.head()
""""
Data Visualization
""""
# Opening price of all stocks
tesla['open'].plot(label='Tesla',figsize=(12,8),title='Opening Prices')
gm['open'].plot(label='GM')
ford['open'].plot(label='Ford')
plt.legend()
# Volume of Stocks for each day
tesla['volume'].plot(label='Tesla',figsize=(16,8),title='Volume of Stocks Traded each day')
gm['volume'].plot(label='GM')
ford['volume'].plot(label='Ford')
plt.legend();
# date of max trading
ford['volume'].argmax()
ford['open'].plot(figsize=(20,6))


tesla['Total Traded']=tesla['volume']*tesla['open']
ford['Total Traded']= ford['volume']*ford['open']
gm['Total Traded']= gm['volume']*gm['open']

tesla['Total Traded'].plot(label='Tesla',figsize=(16,8))
ford['Total Traded'].plot(label='Ford')
gm['Total Traded'].plot(label='GM')
plt.legend();

tesla['Total Traded'].argmax()

gm['MA50'] = gm['open'].rolling(50).mean()
gm['MA200'] = gm['open'].rolling(200).mean()
gm[['open','MA50','MA200']].plot(figsize=(16,8))


from pandas.plotting import scatter_matrix
car_comp= pd.concat([tesla['open'],ford['open'],gm['open']],axis=1)
car_comp.columns = ['Tesla Open','Ford Open','GM Open']
car_comp.head()
scatter_matrix(car_comp,figsize=(8,8),alpha=0.2,hist_kwds={'bins':50});

""""
Candlestick Graph
""""

import mpl_finance
from matplotlib.dates import DateFormatter, date2num, WeekdayLocator, DayLocator, MONDAY
from mpl_finance import candlestick_ohlc

ford_reset = ford.loc['2015-01-01':'2015-01-31'].reset_index()
ford_reset.head()
ford_reset.info()
ford_reset['date_ax']= ford_reset['date'].apply(lambda date: date2num(date))
