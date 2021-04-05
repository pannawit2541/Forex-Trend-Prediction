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

file = r'dataset\2020update\USDJPY_features.csv'
df = pd.read_csv(file)
df.set_index('date', inplace=True, drop=True)
# df = df.drop(df.columns[[0]], axis=1)
# df = df.iloc[49704:87092,:].copy()
# print(df.shape)

################################################
'''
    - 4 years data
    - 4 y * 356 d * 24 hr = 34,176

'''
features = df.copy()

features = features.drop(['open_24', 'close_24'], axis=1)
targets = df[['open_24', 'close_24']].copy()
################################################
'''
    - scale output with 1 pip
'''
targets = targets*100
################################################
# print(features.head(2))
# print(features.tail(2))
# print(targets.tail(2))
# print("train :",features.iloc[50038]," to ",features.iloc[87428])
# print("test :",features.iloc[87428]," to ",features.iloc[-1])
sc_X = StandardScaler()
sc_y = StandardScaler()
x = sc_X.fit_transform(features.values)
y = sc_y.fit_transform(targets.values)
input_train = x[49704:87092,:]
output_train = y[49704:87092,:]

input_test =  x[87092:,:]
output_test = y[87092:,:]

# input_train, input_test, output_train, output_test = train_test_split(
#     x, y, test_size=0.05)
# print("train shape : {:.0f}".format(input_train.shape[0]/24), "days || test shape : {:.0f}".format(input_test.shape[0]/24), "days")



# result = []
# C = np.arange(20, 50, 10)
# # C = [1,10,]
# gamma = [0.001]
# epsilon = [0.0001]

# for c in C:
#     for g in gamma:
#         for e in epsilon:
#             model = SVR(kernel='rbf', gamma=g, C=c,
#                         epsilon=e, verbose=1,max_iter=100000)
#             best_svr = MultiOutputRegressor(model)
#             best_svr.fit(input_train, output_train)

#             yhat = best_svr.predict(input_test)
#             yhat = sc_y.inverse_transform(yhat)
#             y_test = sc_y.inverse_transform(output_test)
#             mse = mean_squared_error(y_test, yhat)
#             r2 = r2_score(yhat, y_test)
#             print("-------------------------------------------------")
#             print("R2_score = ", r2)
#             print("mse = ", mse/100
#                   )
#             print("sqrt(mse) = ", np.sqrt(mse))
#             print("Pips err = ", mean_absolute_error(yhat, y_test), "\n")
#             mae = mean_absolute_error(yhat, y_test)
#             result.append([c, g, mae, r2])
#             _csv = pd.DataFrame(result,columns=["C","gamma","MAE","R2"])
#             _csv.to_csv(r'dataset\2020update\bestParamGBPUSD.csv',index=False)
#             print("-------------------------------------------------")


filename = 'model/2020_USDJPY.joblib'
model = SVR(kernel='rbf', gamma=0.001, C=1,
            epsilon=0.0001, verbose=1)

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

# yhat = best_svr.predict(input_test)
# yhat = sc_y.inverse_transform(yhat) 
# y_test = sc_y.inverse_transform(output_test)
# mse = mean_squared_error(y_test, yhat)
# sum_err = []

# for i in range(len(y_test)):
#     err = abs(y_test[i]-yhat[i])
#     sum_err.append(err)
#     #print(i,"-> Pre ",yhat[i]," vs Acc",y_test[i]," err = ",err)
# print("Crossvalidation score :", np.mean(scores))
# print("Abs_err = ", r2_score(yhat, y_test))
# print("mse = ", mse/100
#       )
# print("sqrt(mse) = ", np.sqrt(mse))
# print("Pips err = ", mean(sum_err), "\n")
