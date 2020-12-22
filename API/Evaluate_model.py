import joblib
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error

import preprocessing as ps
import requests
import json

response = requests.get("https://fcsapi.com/api-v3/forex/history?symbol=EUR/USD&period=1h&access_key=62fshe1xJ6ejIAFmICbhv&level=3")
#response = requests.get("https://marketdata.tradermade.com/api/v1/timeseries?api_key=iGv_aQZoc7huEAchcPOV&currency=GBPUSD&start_date=2020-11-21-00:00&end_date=2020-12-21-08:00&format=records&interval=hourly")

# def to_pandas(data):

print(response.Response())
