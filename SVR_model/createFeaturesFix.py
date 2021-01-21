import pandas as pd
import numpy as np
from datetime import datetime

import talib

from ta.volatility import BollingerBands
from ta.trend import MACD

import plotly as py
from plotly import tools
import plotly.graph_objects as go


def preprocessing(file, s=0, create_file=False):


    data = pd.read_csv(file)
    data.set_index('date', inplace=True, drop=True)
    
    
    features = data[['open', 'high', 'low', 'close', 'volume', 'dayOfweek']].copy(deep=False)
    targets = data[['open_24', 'close_24']].copy(deep=False)
    targets = pd.DataFrame(data=targets, dtype=np.float64)

    periods = [6, 12, 18, 24, 30, 36]

    #------------------------------------------------------------#
    # Create day of week :
    #------------------------------------------------------------#

    features['isFriday'] = np.where(features['dayOfweek'] == "Friday", 1, 0)
    features['isMonday'] = np.where(features['dayOfweek'] == "Monday", 1, 0)
    features = features.drop(['dayOfweek'], axis=1)
    features = pd.DataFrame(data=features, dtype=np.float64)

    #------------------------------------------------------------#
    # Momentum (MOM) :
    #------------------------------------------------------------#

    for i in range(0, len(periods)):
        features['MOM_{i}'.format(i=periods[i])] = talib.MOM(
            features.close.values, timeperiod=periods[i])

    print("--------- Mometum Successful ---------")

    #------------------------------------------------------------#
    # Stochastic oscillator (STOCH):
    #------------------------------------------------------------#

    for i in range(0, len(periods)):
        K, D = talib.STOCH(
            close=features['close'],
            high=features['high'],
            low=features['low'],
            fastk_period=periods[i]
        )
        features['K_{i}'.format(i=periods[i])] = K
        features['D_{i}'.format(i=periods[i])] = D

    print("--------- Stochastic oscillator Successful ---------")

    #------------------------------------------------------------#
    # Moving Average Convergence/Divergence (MACD) :
    #------------------------------------------------------------#
    for i in range(0,len(periods)):
        indicator_MACD = MACD(
            close=features['close'],
            n_fast=((periods[i]/2)-1),
            n_slow=periods[i],
            n_sign=periods[i]/2.8,
            fillna=True
        )
        features['MACD_{}'.format(int((periods[i]/2)-1))] = indicator_MACD.macd()
        features['MACDsignal_{}'.format(int(periods[i]/2.8))] = indicator_MACD.macd_signal()
        features['MACDhist_{}'.format(periods[i])] = indicator_MACD.macd_diff()
    
    print("--------- Moving Average Convergence/Divergence Successful ---------")

    #------------------------------------------------------------#
    # Bollinger Bands (BBANDS) :
    #------------------------------------------------------------#

    for i in range(0,len(periods)):
        indicator_bb = BollingerBands(close=features["close"], n=periods[i], ndev=2)
        features['bb_bbm_{}'.format(periods[i])] = indicator_bb.bollinger_mavg()
        features['bb_bbh_{}'.format(periods[i])] = indicator_bb.bollinger_hband()
        features['bb_bbl_{}'.format(periods[i])] = indicator_bb.bollinger_lband()

    print("--------- Bollinger Bands Successful ---------")

    #------------------------------------------------------------#
    # Relative Strange index (RSI) :
    #------------------------------------------------------------#

    for i in range(len(periods)):
        features['RSI_{i}'.format(i=periods[i])] = talib.RSI(
           features['close'],
            timeperiod=periods[i]
        )

    print("--------- Relative Strange index Successful ---------")

    features = features.fillna(method='bfill')

    # ----------- Create File .csv------------
    if create_file == True:
        _csv = pd.concat([features, targets], axis=1)
        _csv.to_csv(r'dataset/features/EURUSD_2.csv')

    return features, targets

features,targets = preprocessing(file=r'dataset\data\finish\EURUSD\dataset_H1_EURUSD.csv',create_file=True)
print(features)