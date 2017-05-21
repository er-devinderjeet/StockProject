__author__ = 'Devinderjeet'
from numpy import log, polyfit, sqrt, std, subtract
import statsmodels.tsa.stattools as ts
import statsmodels.api as sm
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import numpy as np
import time
import seaborn as sns
import pprint
import basicGraph
import pandas as pd
stockName = "PVR","RUSHIL"

def stat():

        '''
        for sl in stockName:
            stockFile_1 = 'stock/1_year/'+ stock +'.txt'
            date, close, high , low, open, volume = np.loadtxt(stockFile_1,delimiter=',', unpack=True,
                                                            converters={0: mdates.strpdate2num('%Y%m%d')})


        print close[-1:]
        print close[-2:-1]
        '''
        stockFile_X = 'stock/1_year/PVR.txt'

        date_X, close_X, high_X , low_X, open_X, volume_X = np.loadtxt(stockFile_X,delimiter=',', unpack=True,
                                                            converters={0: mdates.strpdate2num('%Y%m%d')})
        stockFile_Y = 'stock/1_year/RUSHIL.txt'

        date_Y, close_Y, high_Y , low_X, open_y, volume_y = np.loadtxt(stockFile_Y,delimiter=',', unpack=True,
                                                            converters={0: mdates.strpdate2num('%Y%m%d')})
        print close_X[-1:]  #close[n]
        print close_Y[-2:-1] #close[n-1]
        '''
        print date_X[0],date_X[-1]
        print date_Y
        plt.plot(date_X,close_X,label="PVR")
        plt.plot(date_X,close_Y,label="RUSHIL")
        plt.xlabel('Date')
        plt.ylabel('Price')
        plt.legend()
        sns.jointplot(close_Y, close_X ,color='b')

        plt.show()
        '''

        df1 = pd.DataFrame({'y':close_Y,'x':close_X})
        est = sm.OLS(df1.y,df1.x)
        est = est.fit()
        df1['hr'] = -est.params[0]
        df1['spread'] = df1.x + (df1.y * df1.hr)
        '''
        plt.plot(df1.spread)
        plt.show()
        '''
        cadf = ts.adfuller(df1.spread)
        print 'Augmented Dickey Fuller test statistic =',cadf[0]
        print 'Augmented Dickey Fuller p-value =',cadf[1]
        print 'Augmented Dickey Fuller 1%, 5% and 10% test statistics =',cadf[4]
stat()