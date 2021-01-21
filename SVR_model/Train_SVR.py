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

file = r'dataset\features\EURUSD_3.csv'
df = pd.read_csv(file)
df.set_index('date', inplace=True, drop=True)


################################################
'''
    - 4 years data
    - 4 y * 356 d * 24 hr = 34,176

'''
features = pd.read_csv(r'dataset\features\EURUSD_pca.csv')
# features = df.copy()
# features = features.drop(['open_24', 'close_24'], axis=1)
# features = features[['open','high','low','close','EMA_6','EMA_12','EMA_24','bb_bbm_6', 'bb_bbh_6', 'bb_bbl_6',
#        'bb_bbm_12', 'bb_bbh_12', 'bb_bbl_12', 'bb_bbm_24', 'bb_bbh_24',
#        'bb_bbl_24']].copy()
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


filename = 'model/test_fix2.joblib'

model = SVR(kernel='rbf', gamma='auto', C=25,
            epsilon=0.0001, verbose=2)

best_svr = MultiOutputRegressor(model)
cv = KFold(n_splits=10, shuffle=False)
scores = []
i = 1
for train_index, test_index in cv.split(input_train):
    print("K-folds at : ", i)

    X_train, X_test, y_train, y_test = input_train[train_index], input_train[
        test_index], output_train[train_index], output_train[test_index]
    best_svr.fit(X_train, y_train)

    '''
                    - Cross validate 
            '''
    scores.append(best_svr.score(X_test, y_test))
    print("scores : ", best_svr.score(X_test, y_test))

    '''
                    - MAE
            '''
    yhat = best_svr.predict(X_test)
    yhat = sc_y.inverse_transform(yhat)
    y_test = sc_y.inverse_transform(y_test)
    print("MAE : ", mean_absolute_error(
        y_test, yhat, multioutput='raw_values'))
    joblib.dump(best_svr, filename)
    i += 1

yhat = best_svr.predict(input_test)
yhat = sc_y.inverse_transform(yhat)
y_test = sc_y.inverse_transform(output_test)
mse = mean_squared_error(y_test, yhat)
sum_err = []

for i in range(len(y_test)):
    err = abs(y_test[i]-yhat[i])
    sum_err.append(err)
    #print(i,"-> Pre ",yhat[i]," vs Acc",y_test[i]," err = ",err)
print("Crossvalidation score :", np.mean(scores))
print("Abs_err = ", r2_score(yhat, y_test))
print("mse = ", mse/100
)
print("sqrt(mse) = ", np.sqrt(mse))
print("Pips err = ", mean(sum_err), "\n")
