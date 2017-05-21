__author__ = 'Devinderjeet'

#http://chartapi.finance.yahoo.com/instrument/1.0/RUSHIL.NS/chartdata;type=quote;range=5d/csv
import sys
import urllib2
import time
import datetime as dt

stockPull = 'PVR'
stocksName = 'CNXMEDIA','NSEI','NSEBANK','CNXIT'

def  fifteenDays(stock):
        urlToVisit = 'http://chartapi.finance.yahoo.com/instrument/1.0/%5E'+stock+'/chartdata;type=quote;range=15d/csv'
        #urlToVisit = 'http://chartapi.finance.yahoo.com/instrument/1.0/%5E'+stock+'.NS/chartdata;type=quote;range=1d/csv'
        saveFileLine = 'stock/15_days/'+stock+'.csv'
def  tenDays(stock):
        urlToVisit = 'http://chartapi.finance.yahoo.com/instrument/1.0/%5E'+stock+'/chartdata;type=quote;range=15d/csv'
        #urlToVisit = 'http://chartapi.finance.yahoo.com/instrument/1.0/%5E'+stock+'.NS/chartdata;type=quote;range=1d/csv'



def pullData(stock):
    try:
        print 'Currently Puling', stock
        print str(dt.datetime
                  .fromtimestamp(time
                                 .time())
                  .strftime('%d-%m-%Y %I:%M:%S'))
        urlToVisit = 'http://chartapi.finance.yahoo.com/instrument/1.0/%5E'+stock+'/chartdata;type=quote;range=10d/csv'

        saveFileLine = 'stock/10_days/'+stock+'.csv'


        try:
            readExistingData = open(saveFileLine, 'r').read()
            splitExisting = readExistingData.split('\n')
            mostRecentLine = splitExisting[-2]
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
                    if int(splitLine[0]) > int(lastUnix):
                        lineToWrite  = eachLine+'\n'
                        saveFile.write(lineToWrite)
        saveFile.close()

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
        time.sleep(300)

def exit():
    print "Exiting Application"
    sys.exit()