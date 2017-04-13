__author__ = 'Devinderjeet'

#http://chartapi.finance.yahoo.com/instrument/1.0/RUSHIL.NS/chartdata;type=quote;range=5d/csv
import urllib2
import time
import datetime

stockPull = 'PVR'
stocksName = 'PVR','RUSHIL','BPCL','RPOWER'
def pullData(stock):
    try:
        fileLine = 'stock/'+stock+'.NS.txt'
        urlToVisit = 'http://chartapi.finance.yahoo.com/instrument/1.0/'+stock+'.NS/chartdata;type=quote;range=10d/csv'
        sourceCode = urllib2.urlopen(urlToVisit).read()
        splitSource = sourceCode.split('\n')

        for eachLine in splitSource:
            splitLine = eachLine.split(',')
            if len(splitLine)==6:
                if 'values' not in eachLine:
                    saveFile = open(fileLine, 'a')
                    lineToWrite  = eachLine+'\n'
                    saveFile.write(lineToWrite)

        print 'Pulled',stock
        print 'Sleep'

    except Exception, e:
        print 'main loop', str(e)

for eachStock in stocksName:
    pullData(eachStock)