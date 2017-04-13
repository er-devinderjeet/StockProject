from PyQt4 import QtCore, QtGui
import sys
import MySQLdb
import pandas as pd
import time
from datetime import datetime
from time import mktime

def backtest():
    #trade rules
    #Buy everytime you are not invested and
    #stock Price Drops
    #sell every time the sell the stock price is .2% higher than when you bought
    investing  = 'none'
    buyPrice   = 0
    sellPrice  = 0
    previousPrice = 0

    totalProfit = 0


    conn   = MySQLdb.connect(host='localhost',user='root',passwd='12345678', db='icici')
    cursor = conn.cursor()
    cursor.execute("SELECT close,timestamp FROM fivemin ORDER BY timestamp ASC")
    #query  = ("SELECT close,timestamp FROM fivemin ORDER BY timestamp DESC")
    #data   =  pd.read_sql_query(query, con=conn)

    #data_b = pd.read_sql_query(query, con=conn, index_col='timestamp')
    #data_c = data.astype(float)
    data = cursor.fetchall()
    for row in data :
        stockPrice =float(row[0])
        date = row[1]
        dateStamp  = time.strftime('%d/%m/%Y %H:%M:%S',time.localtime(date))

        reFormat =  dateStamp, stockPrice
        saveFormat = str(reFormat).replace('\'','').replace('(','').replace(')','')

        if investing == 'none':
            if stockPrice < previousPrice:
                print 'buy triggered'
                buyPrice = stockPrice
                print 'bought stock for',buyPrice
                investing = 'holding'

        elif investing  == 'holding':
            if stockPrice > buyPrice * .005 + buyPrice:
                print 'sell Triggered'
                sellPrice = stockPrice
                print 'Finished trade. Sold for',sellPrice
                investing = 'none'
                tradeProfit = sellPrice- buyPrice
                totalProfit += tradeProfit
                print totalProfit

        previousPrice = stockPrice
        time.sleep(1)
        '''
        writeData =  open('icicidata.txt','a')
        writeData.write(saveFormat)
        writeData.write("\n")
        writeData.close()
        '''
    conn.commit()
    conn.rollback()

    conn.close()
    print 'we are complete, Here is Total Profit'
    print totalProfit
    time.sleep(50)
backtest()