import joblib
from pickle import load

import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error,r2_score

from preprocessing import for_evaluate
from preprocessing import slope_acc
from preprocessing import to_dataFrame
from preprocessing import smooth_candlestick

import requests
import json

from collections import namedtuple

def moving_average(x, w):
    return np.convolve(x, np.ones(w), 'valid') / w

def slope(predict):
    predict_pd = pd.DataFrame(predict)

    def calc_slope(x):
        slope = np.polyfit(range(len(x)), x, 1)[0]
        return slope
    pre_slope = predict_pd.rolling(48).apply(calc_slope,raw=False).values

    return pre_slope

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
    # print(targets)
    # ----------------------------------------
    # ! Normalization
    # sc_X = joblib.load('model/scaler/x_scaler.bin')

    # print(sc_X)
    sc_X = StandardScaler()
    sc_y = StandardScaler()

    f_train = pd.read_csv('save_data\{}_features.csv'.format(c_pair))
    f_train.set_index('date', inplace=True, drop=True)

    labels = f_train[['open_24', 'close_24']].copy(deep=False)
    labels = labels*pip

    f_train = f_train.drop(['open_24', 'close_24'], axis=1)

    
    sc_X.fit_transform(f_train.values)
    sc_y.fit_transform(labels.values)
    # sc_y = joblib.load('model/scaler/y_scaler.bin')
    x = sc_X.transform(features.values)
    sc_y.transform(targets.values)
    
    # ----------------------------------------

    # ----------------------------------------
    # ! Run model & Denormalization
    # model = joblib.load('model/{}_SVR_1.joblib'.format(c_pair))
    model = joblib.load('model/2020_{}.joblib'.format(c_pair))
    yhat = model.predict(x)
    yhat = sc_y.inverse_transform(yhat)
    # y_pre = yhat[-24:,:].copy()/pip
    # yhat = yhat[:-24,:].copy()/pip
    # yhat = yhat
    # ----------------------------------------
    # print(yhat)
    # ----------------------------------------
    # ! Evaluate

    date = data['date'].values.tolist()
    # date = data['date'].iloc[-240:].str.split(n=1,expand=True).values[:,0].tolist()

    time_stamp = data['t'].values.tolist()
    MAE = int(mean_absolute_error(targets.values, yhat[:-24,:]))
    SMA_predict = (np.around(moving_average(yhat[:,1],24),4)/pip)
    SMA_true = (np.around(moving_average(targets['close'].values,24),4)/pip)
    trend_acc = slope_acc(SMA_predict[:-24],SMA_true,48)
    slope_values = slope(yhat[:,1])[-24:].tolist()
    slope_values = [item for sublist in slope_values for item in sublist]

    yhat_smooth = smooth_candlestick(yhat)
    values = np.around((yhat_smooth/pip),decimals=5).tolist() 
    # pre_values = np.around((y_pre),decimals=5).tolist() 

    score = {
        'Date' : date,
        # 'Date_24hr' : date_24,
        'Time_stamp' : time_stamp,
        # 'Time_stamp_24hr' : time_stamp_24,
        'MAE' : MAE,
        'R2_SCORE' : int(r2_score(targets.values, yhat[:-24,:])*100),
        'SMA_predict' : SMA_predict.tolist(),
        'SMA_true' : SMA_true.tolist(),
        'Slope_acc' : int(trend_acc),
        'Predict_ohlc' : values,
        'Slope_values' : slope_values
        # 'Predict_24hr' : pre_values
    }
    # ----------------------------------------

    # score = json.dumps(score)
    # score = json.loads(score)
    
    return score


# data = pd.read_csv(r'save_data\test_EUR.csv')
# result = evaluate_historical(data,'EURUSD')
# print((result["R2_SCORE"]))
# print(type(result['Date']))
# from collections import namedtuple
# d_named = namedtuple("Evaluate", result.keys())(*result.values())
# print(type(d_named))
