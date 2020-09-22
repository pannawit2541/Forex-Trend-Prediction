import pandas as pd
import numpy as np 
from datetime import datetime
from ta import add_all_ta_features
from ta.utils import dropna
from ta.volatility import BollingerBands
import numpy
import talib

if __name__ == "__main__":
    df = pd.read_csv('dataset/EURUSD_H1.csv')
    df.set_index('Date', inplace=True, drop=True)
    df = df.iloc[85000:]
    df = dropna(df)
    #print(df)
    #df = add_all_ta_features(df, open="Open", high="High", low="Low", close="Close", volume="Volume")
    bb = BollingerBands(close=df['Close'], n=20 ,ndev=2)
    df['bb_bbm'] = bb.bollinger_mavg()
    df['bb_bbh'] = bb.bollinger_hband()
    df['bb_bbl'] = bb.bollinger_lband()
    #print(df)
    close = numpy.random.random(100)
    output = talib.SMA(close)
    print(close)
