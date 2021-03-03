import pandas as pd
import numpy as np
from datetime import datetime

import talib

from ta.volatility import BollingerBands
from ta.trend import MACD


def create_features(file, create_file=False): 
    
    features = pd.read_csv(file)
    # features.set_index('date', inplace=True, drop=True)
    print("Size of datas : ",len(features))

    # features = features.iloc[:-tf, :].copy()

    periods = [12, 24, 48, 60, 120]
    print(">> Periods : ",periods)
    
    #------------------------------------------------------------#
    # Moving Average Convergence/Divergence (MACD) :
    #------------------------------------------------------------#

    for i in range(len(periods)):
        features['SMA_{i}'.format(i=periods[i])] = talib.SMA(
            features['close'],
            timeperiod=periods[i]
        )

    print("--------- Moving Average Convergence/Divergence Successful ---------")

    #------------------------------------------------------------#
    # Relative Strange index (RSI) :
    #------------------------------------------------------------#

    #periods = [x+20 for x in periods]
    for i in range(len(periods)):
        features['RSI_{i}'.format(i=periods[i])] = talib.RSI(
            features['close'],
            timeperiod=periods[i]
        )

    print("--------- Relative Strange index Successful ---------")

    # #------------------------------------------------------------#
    # # Slope :
    # #------------------------------------------------------------#
    # for i in range(len(periods)):
    #     try :
    #         features['Slope_{}'.format(i=periods[i])] = talib.LINEARREG_SLOPE(
    #             features['close'], timeperiod=periods[i])
    #     except IndexError:
    #         pass

    # print("--------- Slope Successful ---------")

    features = features.fillna(method='bfill')

    return features


features_H1 = create_features(r'data\EURUSD_H1.csv')
features_M15 = create_features(r'data\EURUSD_M15.csv')
i=15000
# print(features_M15.iloc[i*4])
# print(features_H1.iloc[i])

# features_M15["time"]= features_M15["date"].str.split(" ",expand = True)[1] 
# print(features_M15.head(2))
np_M15 =  features_M15.values
data_sequences = []
data = []
hr_before = 0
day_before = 0
for index,value in enumerate(np_M15[:,0]):
    (d,t) = value.split(' ')
    hr = int(t.split(':')[0])
    day = int(d.split('/')[0])
    print(day_before,hr, " +1 : " , day,hr)
    if (len(data) == 0 and hr_before ==0 and day_before==0):
        data = np.concatenate((data,np_M15[index]), axis=None)
        hr_before = hr
        day_before = day
    elif (hr_before == hr) and (day_before == day):
        data = np.concatenate((data,np_M15[index,1:]), axis=None)
    else:
        
        if data.shape[0] < 46 :
            for _ in range(int((46-data.shape[0])/15)):
                data = np.concatenate((data,np_M15[index,1:]), axis=None)
        elif data.shape[0] > 46:
            data = np.delete(data,range(1,16))
            
        
        data_sequences.append(data.tolist().copy())
        hr_before= 0
        day_before = 0
        data = []
        
    # print(data)

# print(len(data_sequences[1]))
data_sequences = np.array(data_sequences)
print(data_sequences.shape)
