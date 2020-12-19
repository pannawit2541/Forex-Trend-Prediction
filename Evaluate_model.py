import joblib
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error

file_data = ['dataset/EURUSD_features.csv','dataset/GBPUSD_features.csv','dataset/USDJPY_features.csv']
file_model = ['model/EURUSD_SVR_1.joblib','model/GBPUSD_SVR_1.joblib','model/USDJPY_SVR_1.joblib']
pair = ['EUR/USD','GBP/USD','USD/JPY']
# file = 'dataset/EURUSD_features.csv'
# filename = 'model/EURUSD_SVR_1.joblib'
# file = 'dataset/GBPUSD_features.csv'
# filename = 'model/GBPUSD_SVR_1.joblib'
# file = 'dataset/USDJPY_features.csv'
# filename = 'model/USDJPY_SVR_1.joblib'
unit = [10000,10000,100]

for i in range(3):
    file = file_data[i]
    filename = file_model[i]

    data = pd.read_csv(file)
    data.set_index('date', inplace=True, drop=True)

    ################################################
    '''
        - 4 years data
        - 4 y * 356 d * 24 hr = 34,176

    '''
    amounts = 34176
    data = data.tail(amounts+24)
    data = pd.DataFrame(data=data, dtype=np.float64)
    ##############################################

    features = data.copy(deep=False)
    features.drop(features.tail(24).index, inplace=True)
    features = features.drop(['open_24', 'close_24'], axis=1)

    labels = data[['open_24', 'close_24']].copy(deep=False)
    labels = labels.iloc[24:, :]
    ################################################
    '''
        - scale output with 1 pip
    '''
    labels = labels*unit[i]
    ################################################


    labels.reset_index(drop=True, inplace=True)
    labels.index = features.index
    #print(labels.head())
    #print(features.head())


    sc_X = StandardScaler()
    sc_y = StandardScaler()
    x = sc_X.fit_transform(features.values)
    y = sc_y.fit_transform(labels.values)

    input_train, input_test, output_train, output_test = train_test_split(
        x, y, test_size=0.05)
    #print("train shape : {:.0f}".format(input_train.shape[0]/24), "days || test shape : {:.0f}".format(input_test.shape[0]/24), "days")


    model = joblib.load(filename)

    yhat = model.predict(input_test)
    yhat = sc_y.inverse_transform(yhat)
    y_test = sc_y.inverse_transform(output_test)

    print("MAE : {}".format(pair[i]), mean_absolute_error(y_test, yhat, multioutput='raw_values'))



