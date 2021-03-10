import joblib
from joblib import dump, load

import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error
from sklearn.metrics import r2_score

file_data = ['dataset/2020update/EURUSD_features.csv','dataset/2020update/GBPUSD_features.csv','dataset/2020update/USDJPY_features.csv']
file_model = ['model/2020_EURUSD.joblib','model/2020_GBPUSD.joblib','model/2020_USDJPY.joblib']
pair = ['EURUSD','GBPUSD','USDJPY']
# file = r'dataset\2020update\EURUSD_features.csv'
# file_model = 'model\2020_EURUSD.joblib'
unit = [10000,10000,100]

for i in range(len(file_data)):
    file = file_data[i]
    filename = file_model[i]

    data = pd.read_csv(file)
    data.set_index('date', inplace=True, drop=True)

    ################################################
    '''
        - 4 years data
        - 4 y * 356 d * 24 hr = 34,176

    '''
    # amounts = 34176
    # data = data.tail(amounts+24)
    # data = data.iloc[87428:,:].copy()
    data = pd.DataFrame(data=data, dtype=np.float64)
    ##############################################

    features = data.copy(deep=False)
    # features.drop(features.tail(24).index, inplace=True)
    features = features.drop(['open_24', 'close_24'], axis=1)

    labels = data[['open_24', 'close_24']].copy(deep=False)
    # labels = labels.iloc[24:, :]
    ################################################
    '''
        - scale output with 1 pip
    '''
    labels = labels*unit[i]
    ################################################


    # labels.reset_index(drop=True, inplace=True)
    # labels.index = features.index
    #print(labels.head())
    #print(features.head())


    sc_X = StandardScaler()
    sc_y = StandardScaler()
    x = sc_X.fit_transform(features.values)
    y = sc_y.fit_transform(labels.values)
    dump(sc_X, 'model/scaler/x_scaler.bin', compress=True)
    # dump(x, open('model/scaler/x_scaler.pkl', 'wb'))
    dump(sc_y, 'model/scaler/y_scaler.bin', compress=True)
    # input_train, input_test, output_train, output_test = train_test_split(
        # x, y, test_size=0.05)
    #print("train shape : {:.0f}".format(input_train.shape[0]/24), "days || test shape : {:.0f}".format(input_test.shape[0]/24), "days")
    if pair[i] == "EURUSD":
        x =  x[87428:,:]
        y = y[87428:,:]
    elif pair[i] == "GBPUSD":
        x =  x[87420:,:]
        y = y[87420:,:]
    else:
        x = x[87092:,:]
        y = y[87092:,:]
    model = joblib.load(filename)

    yhat = model.predict(x)
    yhat = sc_y.inverse_transform(yhat)
    y_test = sc_y.inverse_transform(y)

    print("{}".format(pair[i]))
    print("MAE : ", mean_absolute_error(y_test, yhat, multioutput='raw_values'))
    print("R2_score : ", r2_score(yhat, y_test))



