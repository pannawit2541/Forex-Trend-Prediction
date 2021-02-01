import joblib
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error,r2_score

from preprocessing import for_evaluate
from preprocessing import slope_24
from preprocessing import to_dataFrame
from preprocessing import for_predict

import requests
import json

from collections import namedtuple

def moving_average(x, w):
    return np.convolve(x, np.ones(w), 'valid') / w

def evaluate_historical(data,c_pair):
    pip = 0
    if c_pair == "EURUSD" or c_pair == "GBPUSD":
            pip = 10000
    elif c_pair == "USDJPY":
            pip = 100
    # ----------------------------------------
    # ! Create Features
  
    features,targets = for_evaluate(data,scale=c_pair)

    # ----------------------------------------

    # ----------------------------------------
    # ! Normalization
    sc_X = StandardScaler()
    sc_y = StandardScaler()
    x = sc_X.fit_transform(features.values)
    sc_y.fit_transform(targets.values)

    # ----------------------------------------

    # ----------------------------------------
    # ! Run model & Denormalization
    model = joblib.load('model/{}_SVR_1.joblib'.format(c_pair))
    yhat = model.predict(x)
    yhat = sc_y.inverse_transform(yhat)
    # y_pre = yhat[-24:,:].copy()/pip
    # yhat = yhat[:-24,:].copy()/pip
    yhat = yhat/pip
    
    # ----------------------------------------

    # ----------------------------------------
    # ! Evaluate
    # date = data['date'].iloc[:-24].values.tolist()
    # date_24 = data['date'].iloc[-24:].values.tolist()
    # time_stamp = data['t'].iloc[:-24].values.tolist()
    # time_stamp_24 = data['t'].iloc[-24:].values.tolist()
    date = data['date'].values.tolist()
    time_stamp = data['t'].values.tolist()
    MAE = mean_absolute_error(targets.values, yhat[:-24,:])
    SMA_predict = np.around(moving_average(yhat[:,1],24),5).tolist()
    SMA_true = np.around(moving_average(targets['close'].values,24),5).tolist()
    values = np.around((yhat),decimals=5).tolist() 
    # pre_values = np.around((y_pre),decimals=5).tolist() 
    score = {
        'Date' : date,
        # 'Date_24hr' : date_24,
        'Time_stamp' : time_stamp,
        # 'Time_stamp_24hr' : time_stamp_24,
        'MAE' : MAE,
        'R2_SCORE' : r2_score(targets.values, yhat[:-24,:])*100,
        'SMA_predict' : SMA_predict,
        'SMA_true' : SMA_true,
        'Slope_acc' : slope_24(targets['close'],yhat[:-24,1]),
        'Predict_ohlc' : values,
        # 'Predict_24hr' : pre_values
    }
    # ----------------------------------------

    # score = json.dumps(score)
    # score = json.loads(score)
    
    return score


# data = pd.read_csv(r'save_data\test.csv')
# result = evaluate_historical(data,'EURUSD')
# print(result)
# print(type(result['Date']))
# from collections import namedtuple
# d_named = namedtuple("Evaluate", result.keys())(*result.values())
# print(type(d_named))
