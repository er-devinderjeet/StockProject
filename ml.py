import quandl, math
import pandas as pd
from sklearn import preprocessing, cross_validation, svm
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import style
import datetime,time
import pickle

style.use('ggplot')

df = quandl.get("NSE/NCC")
'''
print df.tail()
df['Close'].plot()
plt.show()

'''
df = df[['Open',  'High',  'Low',  'Close', 'Total Trade Quantity']]
#df['HL_PCT'] = (df['High'] - df['Low']) / df['Close'] * 100.0
#df['PCT_change'] = (df['Close'] - df['Open']) / df['Open'] * 100.0
df=df[['Close']]
forecast_col = 'Close'
df.fillna(value=-99999, inplace=True)
forecast_out =int(math.ceil(0.01 * len(df)))

df['label'] = df[forecast_col]

X = np.array(df.drop(['label'], 1))
X = preprocessing.scale(X)
X_lately = X[-forecast_out:]
X = X[:-forecast_out]

df.dropna(inplace=True)

y = np.array(df['label'])
print(forecast_out,df)
print X
print "value of y"
print X_lately

'''
X_train, X_test, y_train, y_test = cross_validation.train_test_split(X, y, test_size=0.2)
'''
#COMMENTED OUT:
#clf = svm.SVR(kernel='linear')
'''
clf = LinearRegression(n_jobs=-1)
clf.fit(X_train, y_train)


#writing pickle file as f

with open('linearregression.pickle','wb') as f:
	pickle.dump(clf, f)


#read  pickle file

pickle_in = open('linearregression.pickle','rb')
clf = pickle.load(pickle_in)

confidence = clf.score(X_test, y_test)

forecast_set = clf.predict(X_lately)

#print (forecast_set,confidence,forecast_out)

df['Forecast'] = np.nan


last_date = df.iloc[-1].name
print(df,last_date)

last_unix = time.mktime(last_date.timetuple())
#>>> >>> datetime.datetime.fromtimestamp(time.time()).strftime('%d-%m-%Y %H:%M:%S') , time.time()
#last_unix = last_date.datetime.now()
#print (last_date, last_unix)
one_day = 86400
next_unix = last_unix + one_day
print next_unix
for i in forecast_set:
    next_date = datetime.datetime.fromtimestamp(next_unix)
    next_unix += 86400
    df.loc[next_date] = [np.nan for _ in range(len(df.columns)-1)]+[i]



df['Close'].plot()
df['Forecast'].plot()
plt.legend(loc=4)
plt.xlabel('Date')
plt.ylabel('Price')
plt.show()
'''