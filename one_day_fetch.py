__author__ = 'Devinderjeet'
__author__ = 'Devinderjeet'

#http://chartapi.finance.yahoo.com/instrument/1.0/RUSHIL.NS/chartdata;type=quote;range=5d/csv
import sys
import urllib2
import time
import datetime as dt

stockPull = 'PVR'
stocksName = 'SBIN','ICICIBANK','PVR','HCLTECH'

def pullData(stock):
    try:
        print 'Currently Puling', stock
        print str(dt.datetime
                  .fromtimestamp(time
                                 .time())
                  .strftime('%d-%m-%Y %I:%M:%S'))
        urlToVisit = 'http://chartapi.finance.yahoo.com/instrument/1.0/'+stock+'.NS/chartdata;type=quote;range=1d/csv'
        saveFileLine = 'stock/1_day/'+stock+'.txt'

        try:
            readExistingData = open(saveFileLine, 'r').read()
            splitExisting = readExistingData.split('\n')
            mostRecentLine = splitExisting[-1]
            lastUnix = mostRecentLine.split(',')[0]
        except Exception, e:
            print str(e)
            lastUnix = 0



        saveFile = open(saveFileLine, 'a')
        sourceCode = urllib2.urlopen(urlToVisit).read()
        splitSource = sourceCode.split('\n')

        for eachLine in splitSource:
            if 'values' not in eachLine:
                splitLine = eachLine.split(',')
                if len(splitLine)==6:
                    if splitLine[0] > lastUnix:
                        lineToWrite  = eachLine+'\n'
                        nxtLine = lineToWrite

                        print nxtLine
                        #saveFile.write(lineToWrite)
        #saveFile.close()

        print "Pulled ", stock
        print "Sleeping"
        print str(dt.datetime
                  .fromtimestamp(time
                                 .time())
                  .strftime('%d-%m-%Y %I:%M:%S'))
        time.sleep(5)
    except Exception, e:
        print 'main loop', str(e)
        sys.exit()

def forever():
    while True:
        print "Hello"
        for eachStock in stocksName:
            pullData(eachStock)
        time.sleep(120)

def exit():
    print "Exiting Application"
    sys.exit()