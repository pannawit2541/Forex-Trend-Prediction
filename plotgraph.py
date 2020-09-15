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

    ss = stochastic(df,[14,15])[14]

    ww = williams(df,[15])[15]

    AD = adosc(df,[30])[30]

    p = proc(df,[30])[30]

    m = macd(df,[15,30])

    c = cci(df,[30])[30]

    b = bollinger(df,[20],2)[20]

    avs = paverage(df,[20])[20]

    s = slopes(df,[20])[20]

    trace_0 = go.Ohlc(x=df.index,
                    open=df['Open'],
                    high=df['High'],
                    low=df['Low'],
                    close=df['Close'],
                    name='Currency Quote')

    trace_1 = go.Scatter(x=df.index,y=ma)

    #trace_2 = go.Scatter(x=df.index,y=detrend)
    #trace_2 = go.Scatter(x=line.index,y=line.Close)
    #trace_2 = go.Scatter(x=mm.index,y=mm.Close)
    #trace_2 = go.Scatter(x=ss.index,y=ss.K)
    #trace_2 = go.Scatter(x=ww.index,y=ww.R)
    #trace_2 = go.Scatter(x=p.index,y=p.Close)
    #trace_2 = go.Scatter(x=AD.index,y=AD.AD)
    #trace_2 = go.Scatter(x=m.index,y=m.L)
    #trace_2 = go.Scatter(x=c.index,y=c.Close)
    #trace_2 = go.Scatter(x=b.index,y=b.Upper)
    #trace_2 = go.Scatter(x=avs.index,y=avs.Close)
    trace_2 = go.Scatter(x=s.index,y=s.High)
    
    #data = [trace_0,trace_1,trace_2]
    fig = tools.make_subplots(rows=2,cols=1,shared_xaxes=True)
    fig.append_trace(trace_0,1,1)
    fig.append_trace(trace_1,1,1)
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
    Result = {}

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

        Result[periods[i]] = df
    return Result
            
def wadl(prices,periods):

    #################################################

    #prices  : dataframe of OHLC prices
    #periods : (list) periods for which to calculate the function [5,10,15,...]
    #return  : william accumulation distribution lines for each period

    #################################################

    Result = {}
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
        Result[periods[i]] = WAD

    return Result

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
    Result = {}

    for i in range(0,len(periods)):
        
        Open[periods[i]] = pd.DataFrame(prices.Open.iloc[periods[i]:]-prices.Open.iloc[:-periods[i]].values,
                                        index = prices.iloc[periods[i]:].index,columns=['Open'])

        Close[periods[i]] = pd.DataFrame(prices.Close.iloc[periods[i]:]-prices.Close.iloc[:-periods[i]].values,
                                        index = prices.iloc[periods[i]:].index,columns=['Close'])

        df = pd.concat([Open[periods[i]], Close[periods[i]]], axis=1)
        Result[periods[i]] = df
    
    return Result
        
def stochastic(prices,periods):

    #################################################

    #prices  : dataframe of OHLC prices
    #periods : periods for which to calculate the function value
    #return  : oscillator function valuse

    #################################################

    Result = {}

    for i in range(0,len(periods)):
        Ks = []

        for j in range(periods[i],len(prices)-periods[i]):

            C = prices.Close.iloc[j+1]
            H = prices.High.iloc[j-periods[i]:j].max()
            L = prices.Low.iloc[j - periods[i]:j].min()

            if H == L:
                K = 0
            else:
                K = 100*(C-L)/(H-L)
            Ks = np.append(Ks,K)
        df = pd.DataFrame(Ks,index = prices.iloc[periods[i]+1:-periods[i]+1].index,columns=['K'])
        df['D'] = df.K.rolling(3).mean()
        df = df.dropna()

        Result[periods[i]] = df

    return Result

    #################################################

    #prices  : dataframe of OHLC prices
    #periods : (list) periods for which to calculate the function value
    #return  : momentum indicator

    #################################################
    #################################################

    #prices  : dataframe of OHLC prices
    #periods : (list) periods for which to calculate the function value
    #return  : momentum indicator

    #################################################

    #################################################

    #prices  : dataframe of OHLC prices
    #periods : (list) periods for which to calculate the function value
    #return  : momentum indicator

    #################################################

     #################################################

    #prices  : dataframe of OHLC prices
    #periods : (list) periods for which to calculate the function value
    #return  : momentum indicator

    #################################################

def williams(prices,periods):

    #################################################

    #prices  : dataframe of OHLC prices
    #periods : (list) periods for which to calculate the function value
    #return  : values of williams osc function

    #################################################

    Result ={}

    for i in range(0,len(periods)):
        Rs = []
        for j in range(periods[i],len(prices)-periods[i]):
            C = prices.Close.iloc[j+1]
            H = prices.High.iloc[j-periods[i]:j].max()
            L = prices.Low.iloc[j - periods[i]:j].min()

            if H == L:
                R = 0
            else:
                R = -100*(H-C) / (H-L)
            
            Rs = np.append(Rs,R)
        df = pd.DataFrame(Rs,index = prices.iloc[periods[i]+1:-periods[i]+1].index,columns = ['R'])
        df = df.dropna()

        Result[periods[i]] = df

    return Result

def proc(prices,periods):

    #################################################

    #prices  : dataframe of OHLC prices
    #periods : (list) periods for which to calculate PROC
    #return  : PROC for indicated periods

    #################################################

    Result = {}
    for i in range(0,len(periods)):
        Result[periods[i]] = pd.DataFrame((prices.Close.iloc[periods[i]:]-prices.Close.iloc[:-periods[i]].values)/prices.Close.iloc[:-periods[i]].values,columns = ['Close'])

    return Result
    
def adosc(prices,periods):
   
    #################################################

    #prices  : dataframe of OHLC prices
    #periods : (list) periods for which to calculate 
    #return  : indicator values for indicated periods

    #################################################

    Result = {}

    for i in range(0,len(periods)):

        AD = []

        for j in range(periods[i],len(prices)-periods[i]):

            C = prices.Close.iloc[j+1]
            H = prices.High.iloc[j-periods[i]:j].max()
            L = prices.Low.iloc[j - periods[i]:j].min()
            V = prices.Volume.iloc[j+1]

            if H==L:
                CLV = 0
            else:
                CLV = ((C-L)-(H-C))/(H-L)
            AD = np.append(AD,CLV*V)
        
        AD = AD.cumsum()
        AD = pd.DataFrame(AD,index = prices.iloc[periods[i]+1:-periods[i]+1].index,columns = ['AD'])

        Result[periods[i]] = AD

    return Result 

def macd(prices,periods):
    
    #################################################

    #prices  : dataframe of OHLC prices
    #periods : 1x2 array containing values for the EMAS
    #return  : MACD for given periods

    #################################################

    Result = {}

    EMA1 = prices.Close.ewm(span=periods[0]).mean()
    EMA2 = prices.Close.ewm(span=periods[1]).mean()

    MACD = pd.DataFrame(EMA1- EMA2)
    MACD.columns = ['L']

    SigMACD = MACD.rolling(3).mean()
    SigMACD.columns = ['SL']

    Result = pd.concat([MACD, SigMACD], axis=1)

    return Result

def bollinger(prices,periods,deviations):

    #################################################

    #prices     : dataframe of OHLC prices
    #periods    : periods for which to compute the bollinger bands
    #deviations : deviations to use when calculating bands (upper & lower)
    #return     : bollinger bands

    #################################################

    Result = {}

    for i in range(0,len(periods)):

        mid = prices.Close.rolling(periods[i]).mean()
        Mid = pd.DataFrame(mid)
        Mid.columns = ['Mid']

        std = prices.Close.rolling(periods[i]).std()

        upper = mid+deviations*std
        Upper = pd.DataFrame(upper)
        Upper.columns = ['Upper']

        lower = mid-deviations*std
        Lower = pd.DataFrame(lower)
        Lower.columns = ['Lower']
        
        df = pd.concat((Upper,Mid,Lower),axis = 1)
        
        Result[periods[i]] = df

    return Result

def cci(prices,periods):
    #################################################

    #prices  : dataframe of OHLC prices
    #periods : periods for which to compute the indicator
    #return  : CCI for the given periods

    #################################################

    Result = {}

    for i in range(0,len(periods)):
        
        MA = prices.Close.rolling(periods[i]).mean()
        std = prices.Close.rolling(periods[i]).std()

        D = (prices.Close - MA)/std

        Result[periods[i]] = pd.DataFrame(((prices.Close - MA))/(0.015*D), index = prices.iloc[periods[i]:].index,columns=['Close'])

    return Result

def paverage(prices,periods):
    #################################################

    #prices  : dataframe of OHLC prices
    #periods : periods for which to compute the indicator
    #return  : averages over the given periods

    #################################################

    Result = {}
    
    for i in range(0,len(periods)):
        Result[periods[i]] = pd.DataFrame(prices[['Open','High','Low','Close']].rolling(periods[i]).mean())
    
    return Result

def slopes(prices,periods):
    #################################################

    #prices  : dataframe of OHLC prices
    #periods : periods for which to compute the indicator
    #return  : slopes over given periods

    #################################################

    Result = {}

    for i in range(0,len(periods)):

        ms = []

        for j in range(periods[i],len(prices)-periods[i]):

            y = prices.High.iloc[j - periods[i]:j].values
            x = np.arange(0,len(y))

            res = scipy.stats.linregress(x,y=y)
            m = res.slope

            ms = np.append(ms,m)   
        
        ms = pd.DataFrame(ms, index = prices.iloc[periods[i]:-periods[i]].index,columns = ['High'])

        #ms.columns = [['High']]

        Result[periods[i]] = ms
    
    return Result 


if __name__ == "__main__":
    df = pd.read_csv('dataset/EURUSD_H1.csv')
    df.set_index('Date', inplace=True, drop=True)
    #print(df)
    create_candlestick(df.iloc[85000:])
    
    #f = fourier(df.iloc[85000:],[10,15],method='difference')


  

  