__author__ = 'Devinderjeet'
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
import matplotlib.dates as mdates
import matplotlib.figure as mfigure
import numpy as np


def drawGraph():
    date, bid, ask = np.loadtxt('E:\Devinderjeet\developer\python\sentdex\Machine Learning for Forex and Stock analysis and algorithmic trading\GBPUSD\GBPUSD1d.txt', unpack=True,
                              delimiter=',',
                              converters={0:mdates.strpdate2num('%Y%m%d%H%M%S')})
    fig = plt.Figure(figsize=(10,7))
    ax1 =plt.subplot2grid((40,40),(0,0),rowspan=40,colspan=40)

    ax1.plot(date,bid)
    ax1.plot(date,ask)

    ax1.xaxis.set_major_formatter(mdates.DateFormatter('%d-%m-%Y %I:%M:%S'))
    plt.grid(True)
    plt.show()

drawGraph()