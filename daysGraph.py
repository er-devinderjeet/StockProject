__author__ = 'Devinderjeet'
import time
import datetime
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
import matplotlib.dates as mdates
import numpy as np
import matplotlib
from mpl_finance import candlestick_ohlc
matplotlib.rcParams.update({'font.size':10})
matplotlib.use('Qt4Agg')
import datetime as dt

stockName='PVR','RUSHIL'

def drawStockGraph(stock):
    try:
        stockFile = 'stock/10_days/'+ stock +'.txt'
        date, close, high , low, open, volume = np.loadtxt(stockFile,delimiter=',', unpack=True)

        dateConv = np.vectorize(dt.datetime.fromtimestamp)
        date = dateConv(date)

        fig = plt.figure()
        ax1 = plt.subplot(1,1,1)

        ax1.plot(date,close,'-' ,label='Price')
        plt.ylabel('Stock PRice')
        ax1.xaxis.set_major_locator(mticker.MaxNLocator(10))
        ax1.xaxis.set_major_formatter(mdates.DateFormatter('%d %I:%M:%S'))
        for label in ax1.xaxis.get_ticklabels():
                label.set_rotation(45)
        ax1.grid(True)
        plt.subplots_adjust(left=.17,bottom=.25)

        plt.show()

    except Exception,e:
        print str(e)," error"


def forever():
        print "Opening Daily Chart"
        for eachStock in stockName:
            drawStockGraph(eachStock)

