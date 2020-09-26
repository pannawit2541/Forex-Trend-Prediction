import pandas as pd
import numpy as np 
from datetime import datetime

import talib
#from finta import TA 
from ta.volatility import BollingerBands
from ta.trend import MACD

import plotly as py
from plotly import tools
import plotly.graph_objects as go


def create_candlestick(df) :

    trace_0 = go.Ohlc(x=df.index,
                    open=df['Open'],
                    high=df['High'],
                    low=df['Low'],
                    close=df['Close'],
                    name='Currency Quote')

    fig = tools.make_subplots(rows=1,cols=1,shared_xaxes=True)
    fig.append_trace(trace_0,1,1)

    py.offline.plot(fig,filename='Candlestick_chart')


def Heiken_Ashi(prices):
 
    #################################################

    #prices  : dataframe of prices
    #periods : periods of which to create the candles

    #return  : Heiken_Ashi OHLC candles

    #################################################


    HA_close = prices[['open','high','low','close']].sum(axis = 1)/4

    HA_open = HA_close.copy()

    HA_open.iloc[0] = HA_close.iloc[0]

    HA_high = HA_close.copy()

    HA_low = HA_close.copy()

    for i in range(1,len(prices)):
        
        HA_open.iloc[i] = (HA_open.iloc[i-1] + HA_close.iloc[i-1])/2

        HA_high.iloc[i] = np.array([prices.high.iloc[i], HA_open.iloc[i], HA_close.iloc[i]]).max()

        HA_low.iloc[i] = np.array([prices.low.iloc[i], HA_open.iloc[i], HA_close.iloc[i]]).min()

    return HA_open,HA_high,HA_low,HA_close
    

if __name__ == "__main__":
    
    data = pd.read_csv('dataset/EURUSD_H1.csv')
    data.set_index('date', inplace=True, drop=True)
    data = data.iloc[60000:,:]
    data = pd.DataFrame(data=data, dtype=np.float64) 

    df = data.copy(deep=False)
    df.drop(df.tail(24).index,inplace=True)

    label = data[['open','close']].copy(deep=False)
    #label = data[['open'].copy(deep=False)
    label = label.iloc[24:,:]
    label.reset_index(drop=True,inplace=True)
    label.index = df.index


    #------------------------------------------------------------#
    # Momentum (MOM) :
    #------------------------------------------------------------#

    periods = [12,24,48,60,72,84]

    for i in range(0,len(periods)):
        df['MOM_{i}'.format(i=periods[i])] = talib.MOM(df.close.values,timeperiod = periods[i])

    print("--------- Mometum Successful ---------")

    #------------------------------------------------------------#
    # Stochastic oscillator (STOCH):
    #------------------------------------------------------------#

    periods = [12,24,48,60,72,84]
    for i in range(0,len(periods)):
        K,D = talib.STOCH(
            close = df['close'],
            high = df['high'],
            low = df['low'],
            fastk_period=12
            )
        df['K_{i}'.format(i=periods[i])] = K
        df['D_{i}'.format(i=periods[i])] = D

    print("--------- Stochastic oscillator Successful ---------")

    #------------------------------------------------------------#
    # Williams %R (WILLR) :
    #------------------------------------------------------------#
    
    periods = [8,9,10,11,12]
    for i in range(len(periods)):
        df['WILLR_{i}'.format(i=periods[i])] = talib.WILLR(
            high = df['high'],
            low = df['low'],
            close = df['close'],
            timeperiod = periods[i]
            )

    print("--------- Williams %R Successful ---------")

    #------------------------------------------------------------#
    #  Rate of change (PROCP) :
    #------------------------------------------------------------#

    periods = [12,13,14,15]
    for i in range(len(periods)):
        df['ROCP_{i}'.format(i=periods[i])] = talib.ROCP(
            df['close'],
            timeperiod = periods[i]
        )

    print("--------- Rate of change Successful ---------")

    #------------------------------------------------------------#
    # Weighted Closing Price (WPC) :
    #------------------------------------------------------------#

    df['WPC'] = talib.WCLPRICE(
            high = df['high'],
            low = df['low'],
            close = df['close']
        )

    print("--------- Weighted Closing Price Successful ---------")

    #------------------------------------------------------------#
    # Accumulation Distribution Line (ADL) :
    #------------------------------------------------------------#

    df['ADL'] = talib.AD(
        high = df['high'],
        low = df['low'],
        close = df['close'],
        volume = df['volume']
    )

    print("--------- Accumulation Distribution Line Successful ---------")

    #------------------------------------------------------------#
    # Accumulation Distribution Oscillator (ADOSC) :
    #------------------------------------------------------------#

    periods_fast = [3,6,9,12]
    periods_slow = [10,13,16,19]
    for i in range(len(periods_fast)):
        df['ADOSC_{i},{j}'.format(i=periods_fast[i],j=periods_slow[i])] = talib.ADOSC(
            high = df['high'],
            low = df['low'],
            close = df['close'],
            volume = df['volume'],
            fastperiod = periods_fast[i],
            slowperiod = periods_slow[i]
        )
    
    print("--------- Accumulation Distribution Line Successful ---------")

    #------------------------------------------------------------#
    # Moving Average Convergence/Divergence (MACD) :
    #------------------------------------------------------------#
    
    indicator_MACD = MACD(
        close = df['close'],
        n_fast=12,
        n_slow=26,
        n_sign=9,
        fillna=True
    )

    df['MACD_12,26'] = indicator_MACD.macd()
    df['MACD_his_12,26'] = indicator_MACD.macd_diff()
    df['MACD_signal_12,26'] = indicator_MACD.macd_signal()

    print("--------- Moving Average Convergence/Divergence Successful ---------")
    
    #------------------------------------------------------------#
    # Commodity Channel Index (CCI) :
    #------------------------------------------------------------#

    df['CCI_15'] = talib.CCI(
        high = df['high'],
        low = df['low'],
        close = df['close'],
        timeperiod = 15        
    )

    print("--------- Commodity Channel Index Successful ---------")

    #------------------------------------------------------------#
    # Bollinger Bands (BBANDS) :
    #------------------------------------------------------------#

    indicator_bb = BollingerBands(close=df["close"], n=15, ndev=2)
    df['bb_bbm_15'] = indicator_bb.bollinger_mavg()
    df['bb_bbh_15'] = indicator_bb.bollinger_hband()
    df['bb_bbl_15'] = indicator_bb.bollinger_lband()

    print("--------- Bollinger Bands Successful ---------")

    #------------------------------------------------------------#
    # Heikin Ashi :
    #------------------------------------------------------------#

    Open,High,Low,Close = Heiken_Ashi(df)
    df['HA_open'] = Open
    df['HA_high'] = High
    df['HA_low'] = Low
    df['HA_close'] = Close

    print("--------- Heikin Ashi Successful ---------")

    #------------------------------------------------------------#
    # Relative Strange index (RSI) :
    #------------------------------------------------------------#

    periods = [12,24,48,60]
    for i in range(len(periods)):
        df['RSI_{i}'.format(i=periods[i])] = talib.RSI(
            df['close'],
            timeperiod = periods[i]
        )
    
    print("--------- Relative Strange index Successful ---------")

    #------------------------------------------------------------#
    # Slope :
    #------------------------------------------------------------#

    df['Slope_4'] = talib.LINEARREG_SLOPE(df['close'], timeperiod=4)
    df = df.fillna(method='bfill')

    print("--------- Slope Successful ---------")

    ###################################################################################


    from sklearn.preprocessing import StandardScaler
    import matplotlib.pyplot as plt
    from sklearn.datasets import make_regression
    from sklearn.svm import LinearSVR
    from sklearn.svm import SVR
    from sklearn.multioutput import MultiOutputRegressor
    from sklearn.model_selection import cross_val_score
    from sklearn.model_selection import RepeatedKFold
    from numpy import mean
    from numpy import std
    from numpy import absolute
    from sklearn.metrics import r2_score,mean_squared_error
    from sklearn.model_selection import train_test_split

    sc_X = StandardScaler()
    sc_y = StandardScaler()
    x = sc_X.fit_transform(df.values)
    y = sc_y.fit_transform(label.values)

    x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.05)
   # print(len(x_train))
   # print((x_test))


    model = SVR(kernel='rbf',gamma=0.1)
    wrapper = MultiOutputRegressor(model)
    wrapper.fit(x_train,y_train)

    yhat = wrapper.predict(x_test)

    mse = mean_squared_error(y_test,yhat)
    print(r2_score(yhat,y_test))
    yhat = sc_y.inverse_transform(yhat)
    y_test = sc_y.inverse_transform(y_test)
    print("mse = ",mse)
    print("sqrt(mse) = ",np.sqrt(mse))
    for i in range(len(y_test)):
        err = abs(y_test[i]-yhat[i])
        print(i,"-> Pre ",yhat[i]," vs Acc",y_test[i]," err = ",err)
        #print("Acc ",y_test[:5,:])



    