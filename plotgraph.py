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



def create_candlestick(df) :
    ma = df.Close.rolling(center=False,window=30).mean()

    detrend = Detrend(df,method="linear")

    line = wadl(df,[15])[15]
    
    mm = momentum(df,[10])[10]

    trace_0 = go.Ohlc(x=df.index,
                    open=df['Open'],
                    high=df['High'],
                    low=df['Low'],
                    close=df['Close'],
                    name='Currency Quote')

    trace_1 = go.Scatter(x=df.index,y=ma)

    #trace_2 = go.Scatter(x=df.index,y=detrend)
    #trace_2 = go.Scatter(x=line.index,y=line.Close)
    trace_2 = go.Scatter(x=mm.index,y=mm.Close)
    
    #data = [trace_0,trace_1,trace_2]
    fig = tools.make_subplots(rows=2,cols=1,shared_xaxes=True,shared_yaxes=True)
    fig.append_trace(trace_0,1,1)
    #fig.append_trace(trace_1,1,1)
    fig.append_trace(trace_2,2,1)

    py.offline.plot(fig,filename='Candlestick_chart')
    '''
    fig = go.Figure(data=[go.Candlestick(x=df['Date'],
                    open=df['Open'],
                    high=df['High'],
                    low=df['Low'],
                    close=df['Close'])])

    fig.show()
'''

def Heiken_Ashi(prices):
 
    #################################################

    #prices  : dataframe of prices
    #periods : periods of which to create the candles

    #return  : Heiken_Ashi OHLC candles

    #################################################


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

    return df
    
def Detrend(prices,method='difference'):

    #################################################

    #prices : dataframe of prices
    #method : method by which to detrend 'linear' or 'difference'

    #return : the detrended price series

    #################################################

    if method == 'difference' :

        detrended = prices.Close[1:] - prices.Close[:-1].values

    elif method == 'linear':
        x = np.arange(0,len(prices))

        y = prices.Close.values

        model = LinearRegression()
    
        model.fit(x.reshape(-1,1),y.reshape(-1,1))

        trend = model.predict(x.reshape(-1,1))

        trend = trend.reshape((len(prices),))

        detrended = prices.Close - trend
        

    else :
        print('You did not input a valid method for detrending! Options are liner or difference')

    return detrended

def fseries(x,a0,a1,b1,w):
    #################################################

    #x  : the hours (independent variable)
    #a0 : first fourier series coefficient
    #a1 : second fourier series coefficient
    #b1 : third fourier series coefficient
    #w  : fourier series frequency
    #return  : the value of the fourier function

    #################################################

    f = a0 + a1*np.cos(w*x) + b1*np.sin(w*x)

    return f

def sseries(x,a0,b1,w):
    #################################################

    #x  : the hours (independent variable)
    #a0 : first sine series coefficient
    #b1 : third sine series coefficient
    #w  : sine series frequency
    #return  : the value of the fourier function

    #################################################

    f = a0 + b1*np.sin(w*x)

    return f

def fourier(prices,periods,method='difference'):
    #################################################

    #prices  : OHCL dataframe
    #periods : list of periods for which to compute coefficients [3,5,10,...]
    #method  : method by which to detrend the data
    #return  : dict of dataframes containing coefficients for said periods

    #################################################

    plot = False
    dict = {}

    detrended = Detrend(prices,method)

    for i in range(0,len(periods)):

        coeffs = []

        for j in range(periods[i],len(prices)-periods[i]):

            x = np.arange(0,periods[i])
            y = detrended.iloc[j-periods[i]:j]

            with warnings.catch_warnings():
                warnings.simplefilter('error',OptimizeWarning)

                try:
                    res = scipy.optimize.curve_fit(fseries,x,y)

                except (RuntimeError,OptimizeWarning):
                    res = np.empty((1,4))
                    res[0:] = np.nan
        
            if plot == True:
                xt = np.linspace(0,periods[i],100)
                yt = fseries(xt,res[0][0],res[0][1],res[0][2],res[0][3])

                plt.plot(x,y)
                plt.plot(xt,yt,'r')

                plt.show()
            
            coeffs.extend([res[0]])

        warnings.filterwarnings('ignore',category=np.VisibleDeprecationWarning)

        coeffs = np.array(coeffs)

        df = pd.DataFrame(coeffs, index=prices.iloc[periods[i]:-periods[i]].index)
        df.columns = [['a0','a1','b1','w']]
        df = df.fillna(method='bfill')

        dict[periods[i]] = df
    return dict
            
def wadl(prices,periods):

    #################################################

    #prices  : dataframe of OHLC prices
    #periods : (list) periods for which to calculate the function [5,10,15,...]
    #return  : william accumulation distribution lines for each period

    #################################################

    dict = {}
    for i in range(0,len(periods)):
        
        WAD = []

        for j in range(periods[i],len(prices)-periods[i]):

            TRH = np.array([prices.High.iloc[j],prices.Close.iloc[j-1]]).max()
            TRL = np.array([prices.Low.iloc[j],prices.Close.iloc[j-1]]).min()

            if prices.Close.iloc[j] > prices.Close.iloc[j-1] : 
                PM = prices.Close.iloc[j] - TRL
            elif prices.Close.iloc[j] < prices.Close.iloc[j-1] : 
                PM = prices.Close.iloc[j] - TRH
            elif prices.Close.iloc[j] == prices.Close.iloc[j-1] : 
                PM = 0
            else:
                print("Unknown error ocurred")

            AD = PM*prices.Volume.iloc[j]

            WAD = np.append(WAD,AD)
        
        WAD = WAD.cumsum()
        WAD = pd.DataFrame(list(zip(WAD)),index=prices.iloc[periods[i]:-periods[i]].index,columns=['Close'])
        dict[periods[i]] = WAD

    return dict

def OHLCresample(DataFrame,TimeFrame):

     #################################################

    #DataFrame  : dataframe containing data the we want to resample
    #TimeFrame  : timeframe that we want for resampling  
    #return     : resampled OHCLdata for the given timeframe

    #################################################

    grouped = DataFrame.groupby('Symbol')

    Open    = grouped('Open').resample(TimeFrame).ohlc()
    Close   = grouped('Close').resample(TimeFrame).ohlc()
    High    = grouped('High').resample(TimeFrame).ohlc()
    Low     = grouped('Low').resample(TimeFrame).ohlc()
    Volume  = grouped('Volume').resample(TimeFrame).ohlc()

    resampled = pd.DataFrame(Open)
    resampled['High'] = High
    resampled['Low'] = Low
    resampled['Close'] = Close
    resampled['Volume'] = Volume

    resampled = resampled.dropna()

    return resampled

def momentum(prices,periods):

    #################################################

    #prices  : dataframe of OHLC prices
    #periods : (list) periods for which to calculate the function value
    #return  : momentum indicator

    #################################################

    Open = {}
    Close = {}
    dict = {}

    for i in range(0,len(periods)):
        
        Open[periods[i]] = pd.DataFrame(prices.Open.iloc[periods[i]:]-prices.Open.iloc[:-periods[i]].values,
                                        index = prices.iloc[periods[i]:].index,columns=['Open'])

        Close[periods[i]] = pd.DataFrame(prices.Close.iloc[periods[i]:]-prices.Close.iloc[:-periods[i]].values,
                                        index = prices.iloc[periods[i]:].index,columns=['Close'])

        df = pd.concat([Open[periods[i]], Close[periods[i]]], axis=1)
        dict[periods[i]] = df
    
    return dict
        


if __name__ == "__main__":
    df = pd.read_csv('dataset/EURUSD_H1.csv')
    df.set_index('Date', inplace=True, drop=True)
    #print(df)
    create_candlestick(df.iloc[85000:])
    
    #f = fourier(df.iloc[85000:],[10,15],method='difference')


  

  