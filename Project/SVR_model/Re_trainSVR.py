from sklearn.metrics import r2_score, mean_squared_error
import joblib  # save model
from sklearn.metrics import mean_absolute_error
from sklearn.model_selection import train_test_split
from numpy import absolute
from numpy import std
from numpy import mean
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import KFold
from sklearn.multioutput import MultiOutputRegressor
from sklearn.svm import SVR
from sklearn.svm import LinearSVR
from sklearn.datasets import make_regression
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
import pandas as pd
import numpy as np

file = r'dataset\features\EURUSD.csv'
df = pd.read_csv(file)
df.set_index('date', inplace=True, drop=True)


################################################
'''
    - 4 years data
    - 4 y * 356 d * 24 hr = 34,176

'''
features = df.copy()
# features = features.drop(['open_24', 'close_24'], axis=1)
features = features[['open',
                     'high',
                     'low',
                     'close',
                     'WPC',
                     'HA_open',
                     'HA_high',
                     'HA_low',
                     'HA_close',
                     'EMA_4',
                     'EMA_8',
                     'EMA_16',
                     'EMA_32',
                     'bb_bbm_4',
                     'bb_bbh_4',
                     'bb_bbl_4',
                     'bb_bbm_8',
                     'bb_bbh_8',
                     'bb_bbl_8',
                     'bb_bbm_16',
                     'bb_bbh_16',
                     'bb_bbl_16',
                     'bb_bbm_32',
                     'bb_bbh_32',
                     'bb_bbl_32']].copy()
print(features.shape)
targets = df[['open_24', 'close_24']].copy()
################################################
'''
    - scale output with 1 pip
'''
targets = targets*10000
################################################


sc_X = StandardScaler()
sc_y = StandardScaler()
x = sc_X.fit_transform(features.values)
y = sc_y.fit_transform(targets.values)

input_train, input_test, output_train, output_test = train_test_split(
    x, y, test_size=0.05)
print("train shape : {:.0f}".format(
    input_train.shape[0]/24), "days || test shape : {:.0f}".format(input_test.shape[0]/24), "days")

result = []
C = np.arange(10, 15, 1)
gamma = np.arange(10, 15, 1)
epsilon = [0.0001]

for c in C:
    for g in gamma:
        for e in epsilon:
            model = SVR(kernel='rbf', gamma=g, C=c,
                        epsilon=e, verbose=2,)
            best_svr = MultiOutputRegressor(model)
            best_svr.fit(input_train, output_train)

            yhat = best_svr.predict(input_test)
            yhat = sc_y.inverse_transform(yhat)
            y_test = sc_y.inverse_transform(output_test)
            mse = mean_squared_error(y_test, yhat)

            print("-------------------------------------------------")
            print("R2_score = ", r2_score(yhat, y_test))
            print("mse = ", mse/100
                  )
            print("sqrt(mse) = ", np.sqrt(mse))
            print("Pips err = ", mean_absolute_error(yhat, y_test), "\n")
            mae = mean_absolute_error(yhat, y_test)
            result.append([c, g, e, mae])
            _csv = pd.DataFrame(result,columns=["C","gamma","epsilon","MAE"])
            _csv.to_csv(r'dataset/features/bestParam.csv',index=False)
            print("-------------------------------------------------")
