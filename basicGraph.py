__author__ = 'Devinderjeet'
import time
import datetime
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
import matplotlib.dates as mdates
import numpy as np
import matplotlib
#from matplotlib.finance import candlestick_ohlc
from mpl_finance import candlestick_ohlc
matplotlib.rcParams.update({'font.size':9})

stocksName = 'PVR','RUSHIL','BPCL','RPOWER'
stockName = 'PVR'

class DrawGraph():
    def graphData(self, stock):
        try:
            stockFile = 'stock/1_year/'+ stock +'.txt'
            date, closep, highp , lowp, openp, volume = np.loadtxt(stockFile,delimiter=',', unpack=True,
                                                                               converters={0: mdates.strpdate2num('%Y%m%d')})
            x = 0
            y = len(date)
            candleAr = []
            while x < y:
                appendLine = date[x],openp[x],highp[x],lowp[x],closep[x],volume[x]
                candleAr.append(appendLine)
                x+=1

            fig = plt.figure()
            ax1 = plt.subplot2grid((5,4),(0,0),rowspan =4, colspan=4) #(2,3,1)
            candlestick_ohlc(ax1, candleAr, width=1, colorup='k', colordown='r')
            '''
            ax1.plot(date, openp)
            ax1.plot(date, highp)
            ax1.plot(date, lowp)
            '''
            plt.ylabel('Stock Price')
            ax1.grid(True)

            ax2 = plt.subplot2grid((5,4),(4,0), rowspan =1, colspan=4,  sharex = ax1)
            ax2.bar(date, volume)
            ax2.grid(True)
            plt.ylabel('Volume')
            ax2.axes.yaxis.set_ticklabels([])
            ax2.xaxis.set_major_locator(mticker.MaxNLocator(10))
            ax2.xaxis.set_major_formatter(mdates.DateFormatter('%d-%m'))

            for label in ax2.xaxis.get_ticklabels():
                label.set_rotation(45)

            plt.subplots_adjust(left=.15, bottom=.19, right=.93, top=.94, wspace=.20,hspace=0.00)
            plt.xlabel('Date')
            plt.suptitle(stock+ ' Stock Price')
            plt.setp(ax1.get_xticklabels(), visible=False)
            plt.setp(ax2.get_yticklabels(), visible=False)

            plt.show()
            fig.savefig('example.png')


        except Exception,e:
            print str(e)
def main():
    pvr = DrawGraph()
    pvr.graphData(stockName)
'''
rushil = DrawGraph()
rushil.graphData('RUSHIL')

'''
