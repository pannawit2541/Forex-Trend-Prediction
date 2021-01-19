import pandas as pd
import numpy as np
from datetime import datetime
from statistics import mean
import matplotlib.pyplot as plt

file = r"dataset\data\GBPUSD_D1.csv"

data = pd.read_csv(file)
data.columns = ['date','open','high','low','close','volumn']
years = data['date'].str.split("-",expand=True)
data_visualize = pd.concat([years[0],data['close']],axis=1)
data_visualize.columns = ['year','close']
years = []
for i in range(2007,2021):
    years.append(str(i))

min_close = []
max_close = []

grouped = data_visualize.groupby(data_visualize.year)

for i in years:
    max = grouped.get_group(i).max().values
    min = grouped.get_group(i).min().values
    min_close.append(round(min[1],4))
    max_close.append(round(max[1],4))

plt.plot(years, min_close, label = "min")
plt.plot(years, max_close, label = "max")
plt.xlabel('years')
plt.ylabel('close')
plt.title('min max close')
plt.legend()
plt.show()