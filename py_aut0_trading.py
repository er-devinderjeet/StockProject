__author__ = 'Devinderjeet'
import numpy as np
import pandas as pd
import oandapy as opy
#import seaborn as sns; sns.net()
import warnings
warnings.simplefilter('ignore')
path = "./data/"
#%matplotlib inline
import matplotlib
import pickle

import configparser
import oandapy as opy
import pickle

config = configparser.ConfigParser()
oanda_creds = config.read('oanda.cfg')
print oanda_creds['oanda']['accountId']
'''
oanda = opy.API(environment='practice',
                access_token=oanda['access_token'])
print oanda
accountId = oanda_creds['account_id']
token = oanda_creds['access_token']

#Third step , connection to oanda

oanda = opy.API(environment='practice', access_token=token)
'''

ins = oanda.get_instruments(account_id=config['oanda']['account_id'])['instruments']

for i in ins:
    print i['instruments'],
