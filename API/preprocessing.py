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

    #################################################

    # file  : name of data_set
    # s : start sample at 's'

    # return  : Heiken_Ashi OHLC candles

    #################################################
    #data = file.copy(deep=False)
    #data.set_index('date', inplace=True, drop=True)
    # data = data.iloc[s:, :]
    # data = pd.DataFrame(data=data, dtype=np.float64)

    df = file.copy(deep=False)
    df.drop(df.tail(24).index, inplace=True)

    label = file[['open', 'close']].copy(deep=False)
    label = label.iloc[24:, :]

    label.reset_index(drop=True, inplace=True)
    label.index = df.index

    label.rename(columns={"open": "open_24",
                          "close": "close_24"}, inplace=True)

    def Heiken_Ashi(prices):

        #################################################

        # prices  : dataframe of prices
        # periods : periods of which to create the candles

        # return  : Heiken_Ashi OHLC candles

        #################################################

        HA_close = prices[['open', 'high', 'low', 'close']].sum(axis=1)/4

        HA_open = HA_close.copy()

        HA_open.iloc[0] = HA_close.iloc[0]

        HA_high = HA_close.copy()

        HA_low = HA_close.copy()

        for i in range(1, len(prices)):

            HA_open.iloc[i] = (HA_open.iloc[i-1] + HA_close.iloc[i-1])/2

            HA_high.iloc[i] = np.array(
                [prices.high.iloc[i], HA_open.iloc[i], HA_close.iloc[i]]).max()

            HA_low.iloc[i] = np.array(
                [prices.low.iloc[i], HA_open.iloc[i], HA_close.iloc[i]]).min()

        return HA_open, HA_high, HA_low, HA_close

    #------------------------------------------------------------#
    # Momentum (MOM) :
    #------------------------------------------------------------#

    periods = [3, 4, 5, 8, 9, 10]
    #periods = [x+20 for x in periods]

    for i in range(0, len(periods)):
        df['MOM_{i}'.format(i=periods[i])] = talib.MOM(
            df.close.values, timeperiod=periods[i])
    print(periods)
    print("--------- Mometum Successful ---------")

    #------------------------------------------------------------#
    # Stochastic oscillator (STOCH):
    #------------------------------------------------------------#

    periods = [3, 4, 5, 8, 9, 10]
    #periods = [x+20 for x in periods]
    for i in range(0, len(periods)):
        K, D = talib.STOCH(
            close=df['close'],
            high=df['high'],
            low=df['low'],
            fastk_period=12
        )
        df['K_{i}'.format(i=periods[i])] = K
        df['D_{i}'.format(i=periods[i])] = D

    print(periods)
    print("--------- Stochastic oscillator Successful ---------")

    #------------------------------------------------------------#
    # Williams %R (WILLR) :
    #------------------------------------------------------------#

    periods = [6, 7, 8, 9, 10]
    #periods = [x+20 for x in periods]
    for i in range(len(periods)):
        df['WILLR_{i}'.format(i=periods[i])] = talib.WILLR(
            high=df['high'],
            low=df['low'],
            close=df['close'],
            timeperiod=periods[i]
        )
    print(periods)
    print("--------- Williams %R Successful ---------")

    #------------------------------------------------------------#
    #  Rate of change (PROCP) :
    #------------------------------------------------------------#

    periods = [12, 13, 14, 15]
    #periods = [x+20 for x in periods]
    for i in range(len(periods)):
        df['ROCP_{i}'.format(i=periods[i])] = talib.ROCP(
            df['close'],
            timeperiod=periods[i]
        )

    print(periods)
    print("--------- Rate of change Successful ---------")

    #------------------------------------------------------------#
    # Weighted Closing Price (WPC) :
    #------------------------------------------------------------#

    df['WPC'] = talib.WCLPRICE(
        high=df['high'],
        low=df['low'],
        close=df['close']
    )

    print("--------- Weighted Closing Price Successful ---------")

    #------------------------------------------------------------#
    # Accumulation Distribution Line (ADL) :
    #------------------------------------------------------------#

    df['ADL'] = talib.AD(
        high=df['high'],
        low=df['low'],
        close=df['close'],
        volume=df['volume']
    )

    print("--------- Accumulation Distribution Line Successful ---------")

    #------------------------------------------------------------#
    # Accumulation Distribution Oscillator (ADOSC) :
    #------------------------------------------------------------#

    periods_fast = [2, 3, 4, 5]
    #periods_fast = [x+20 for x in periods_fast]
    periods_slow = [10, 12, 14, 16]
    #periods_slow = [x+20 for x in periods_slow]
    for i in range(len(periods_fast)):
        df['ADOSC_{i},{j}'.format(i=periods_fast[i], j=periods_slow[i])] = talib.ADOSC(
            high=df['high'],
            low=df['low'],
            close=df['close'],
            volume=df['volume'],
            fastperiod=periods_fast[i],
            slowperiod=periods_slow[i]
        )

    print("--------- Accumulation Distribution Line Successful ---------")

    #------------------------------------------------------------#
    # Moving Average Convergence/Divergence (MACD) :
    #------------------------------------------------------------#

    indicator_MACD = MACD(
        close=df['close'],
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
        high=df['high'],
        low=df['low'],
        close=df['close'],
        timeperiod=15
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

    Open, High, Low, Close = Heiken_Ashi(df)
    df['HA_open'] = Open
    df['HA_high'] = High
    df['HA_low'] = Low
    df['HA_close'] = Close

    print("--------- Heikin Ashi Successful ---------")

    #------------------------------------------------------------#
    # Relative Strange index (RSI) :
    #------------------------------------------------------------#

    periods = [6, 8, 10, 12]
    #periods = [x+20 for x in periods]
    for i in range(len(periods)):
        df['RSI_{i}'.format(i=periods[i])] = talib.RSI(
            df['close'],
            timeperiod=periods[i]
        )

    print(periods)
    print("--------- Relative Strange index Successful ---------")

    #------------------------------------------------------------#
    # Slope :
    #------------------------------------------------------------#

    df['Slope_6'] = talib.LINEARREG_SLOPE(df['close'], timeperiod=6)
    df = df.fillna(method='bfill')

    print("--------- Slope Successful ---------")

    df = df.drop(['volume'], axis=1)

    # ----------- Create File .csv------------
    if create_file == True:
        _csv = pd.concat([df, label], axis=1)
        _csv.to_csv(r'dataset/USDJPY_features.csv')

    return df, label
