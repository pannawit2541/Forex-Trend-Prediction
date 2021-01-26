import joblib
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error,r2_score

import talib

from preprocessing import for_evaluate
from preprocessing import slope_24
from preprocessing import to_dataFrame
from preprocessing import for_predict

import requests
import json

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
    y = sc_y.fit_transform(targets.values)

    # ----------------------------------------

    # ----------------------------------------
    # ! Run model & Denormalization
    model = joblib.load('model/{}_SVR_1.joblib'.format(c_pair))
    yhat = model.predict(x)
    yhat = sc_y.inverse_transform(yhat)
    y_pre = yhat[-24:,:].copy()
    yhat = yhat[:-24,:].copy()
    
    # ----------------------------------------

    # ----------------------------------------
    # ! Evaluate
    date = data['date'].iloc[:-24].values.tolist()
    date_24 = data['date'].iloc[-24:].values.tolist()
    time_stamp = data['t'].iloc[:-24].values.tolist()
    time_stamp_24 = data['t'].iloc[-24:].values.tolist()
    MAE = mean_absolute_error(targets.values, yhat)
    SMA_predict = talib.SMA(yhat[:,1],timeperiod=24).tolist()
    SMA_true = talib.SMA(targets['close'].values,timeperiod=24).tolist()
    values = np.around((yhat/pip),decimals=5).tolist() 
    pre_values = np.around((y_pre/pip),decimals=5).tolist() 
    score = {
        'Date' : date,
        'Date_24hr' : date_24,
        'Time_stamp' : time_stamp,
        'Time_stamp_24hr' : time_stamp_24,
        'MAE' : MAE,
        'R2_SCORE' : r2_score(targets.values, yhat)*100,
        'SMA_predict' : SMA_predict,
        'SMA_true' : SMA_true,
        'Slope_acc' : slope_24(targets['close'],yhat[:,1]),
        'Predict_ohlc' : values,
        'Predict_24hr' : pre_values
    }
    # ----------------------------------------

    score = json.dumps(score)
    score = json.loads(score)
    return score
