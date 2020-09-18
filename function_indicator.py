import pandas as pd
import warnings
import numpy as np 
from datetime import datetime
import plotly as py
import matplotlib.pyplot as plt
from plotly import tools
import plotly.graph_objects as go
from sklearn.linear_model import LinearRegression
from scipy.optimize import OptimizeWarning
import scipy

class indicator:

    def __init__(self,prices):

        self.prices = prices
        self.Heiken_Ashi = {}
    
    def Heiken_Ashi(self):
    
        #################################################

        #prices  : dataframe of prices
        #periods : periods of which to create the candles
        #return  : Heiken_Ashi OHLC candles

        #################################################

        prices = self.prices

        HA_close = prices[['Open','High','Low','Close']].sum(axis = 1)/4

        HA_open = HA_close.copy()

        HA_open.iloc[0] = HA_close.iloc[0]

        HA_high = HA_close.copy()

        HA_low = HA_close.copy()

        for i in range(1,len(prices)):
            
            HA_open.iloc[i] = (HA_open.iloc[i-1] + HA_close.iloc[i-1])/2

            HA_high.iloc[i] = np.array([prices.High.iloc[i], HA_open.iloc[i], HA_close.iloc[i]]).max()

            HA_low.iloc[i] = np.array([prices.Low.iloc[i], HA_open.iloc[i], HA_close.iloc[i]]).min()

        df = pd.concat((HA_open,HA_high,HA_low,HA_close),axis = 1)
        df.columns = [['Open','High','Low','Close']]

        self.result = df
        return self.result
   

if __name__ == "__main__":
    df = pd.read_csv('dataset/EURUSD_H1.csv')
    df.set_index('Date', inplace=True, drop=True)

    A = indicator(df.iloc[5000:])
    print(A.Heiken_Ashi)