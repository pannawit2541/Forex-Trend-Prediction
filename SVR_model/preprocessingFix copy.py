import pandas as pd
import numpy as np
from datetime import datetime

import talib

from ta.volatility import BollingerBands
from ta.trend import MACD

import plotly as py
from plotly import tools
import plotly.graph_objects as go

import re

file = r'dataset\data\USDJPY_H1.csv'

data = pd.read_csv(file)
data.columns = ['date', 'open', 'high', 'low', 'close', 'volume']

# --------------------------------------------------------------------------------

# Select Row by year

years = data['date'].str.split("-", expand=True)[0]
years = pd.DataFrame({'year': years.values})
years['month'] = data['date'].str.split("-", expand=True)[1]
years['day'] = data['date'].str.split("-", expand=True)[2]
years['day'] = years['day'].str.split(" ", expand=True)[0]


data = pd.concat([years, data], axis=1)
data["year"] = pd.to_numeric(data["year"])
data["day"] = pd.to_numeric(data["day"])
data["month"] = pd.to_numeric(data["month"])


data = data.loc[(data['year'] >= 2015) & (data['year'] <= 2020)]

# --------------------------------------------------------------------------------

#  Clean data

grouped = data.groupby(data.year)
df = pd.DataFrame()

for y in range(2015, 2021):
    month_grouped = grouped.get_group(y)
    day_grouped = month_grouped.groupby(month_grouped.month)
    for m in range(1, 13):
        day = day_grouped.get_group(m)
        counts = day['day'].value_counts()
        del_rows = counts[counts <= 12].index.values
        temp_df = day[~day['day'].isin(del_rows)]
        if m == 1 and y == 2015:
            temp_df.reset_index
            df = temp_df.copy()
        else:
            df = pd.concat([df, temp_df], ignore_index=True)

# df.drop(['year', 'month', 'day'], axis=1, inplace=True)
df = df.reset_index(drop=True)
data = df.copy()
for y in range(2015,2021):
    df = data.copy()
    df = df.reset_index(drop=True)
    df = df.loc[df['year'] == y]
    # df.to_csv(r'dataset\data\test.csv')
    # --------------------------------------------------------------------------------

    df['dayOfweek'] = pd.to_datetime(df['date'].str.split(
        " ", expand=True)[0], errors='coerce').dt.day_name()
    # df['isMonday'] = pd.to_datetime(df['date'].str.split(" ", expand=True)[0], errors='coerce').dt.day_name()
    # df['isFriday'] = np.where(df['isFriday'] == "Friday", 1, 0)
    # df['isMonday'] = np.where(df['isMonday'] == "Monday", 1, 0)
    df['time'] = df['date'].str.split(" ", expand=True)[1]
    df['time'] = pd.to_numeric(df['time'].str.split(":", expand=True)[0])

    # df = df.loc[~((df['isMonday'] == 1) & (df['time'] > 21))]


    # cond = ~((df['dayOfweek'] == "Thursday") & (df['time'] > 21))
    # features = df.loc[cond].copy()
    features = df.copy()
    max_firstM = -1
    for i in range(24):
        if max_firstM < features['time'].iloc[i]:
            max_firstM = i
        else:
            break
    print(max_firstM)


    # cond = ~((df['dayOfweek'] == "Monday") & (df['time'] > 21))
    # targets = df.loc[cond].copy()
    targets = df.copy()
    max_lastM = targets['time'].iloc[-1]

    features.drop(features.tail(max_lastM+1).index, inplace=True)
    targets.drop(targets.head(max_firstM+1).index, inplace=True)

    print(features)
    print(targets)

    # features = features.loc[ features['date'] != "2015-03-12 21:00"].copy()
    # targets = targets.loc[ targets['date'] != "2015-03-16 21:00"].copy()
    # features = features.loc[ features['date'] != "2015-03-19 21:00"].copy()
    # targets = targets.loc[ targets['date'] != "2015-03-23 21:00"].copy()
    # features = features.loc[ features['date'] != "2015-03-26 21:00"].copy()
    features = features.reset_index(drop=True)
    targets = targets.reset_index(drop=True)

    i = 0
    while i < len(targets):
        print("INDEX = ", i)
        print("Size : ", len(features), len(targets))

        target_date = targets['date'].iloc[i]
        target_time = targets['time'].iloc[i]
        feature_date = features['date'].iloc[i]
        feature_time = features['time'].iloc[i]
        target_dayOfweek = targets['dayOfweek'].iloc[i]
        feature_dayOfweek = features['dayOfweek'].iloc[i]

        feature_month = features['month'].iloc[i]
        target_month = targets['month'].iloc[i]

        if target_time != feature_time:
            print("Date : " , feature_date , " // " , target_date)
            print("DayOfWeek : " , feature_dayOfweek , " // " ,  target_dayOfweek)

            if target_time > feature_time:
                print("---- Targets was remove")
                targets = targets.loc[targets['date'] != target_date].copy()
            elif target_time < feature_time:
                print("---- Features was remove")
                features = features.loc[features['date'] != feature_date].copy()
            else:
                print("Method was BREAKING !!")
                break
            i = i-3
            features = features.reset_index(drop=True)
            targets = targets.reset_index(drop=True)
            print("--------------------------")
            
        if (len(targets) > len(features) and (len(targets)-i <= 2 or len(features)-i <= 2)):
            print("---- **Targets was remove")
            targets = targets.loc[targets['date'] != target_date].copy()
        elif (len(targets) < len(features) and (len(targets)-i <= 2 or len(features)-i <= 2)):
            print("---- **Features was remove")
            features = features.loc[features['date'] != feature_date].copy()
        i += 1
    features = features.reset_index(drop=True)
    targets = targets.reset_index(drop=True)
    features.to_csv(r'dataset\data\finish\features{}.csv'.format(y))
    targets.to_csv(r'dataset\data\finish\targets{}.csv'.format(y))
    print(len(features) == len(targets))
