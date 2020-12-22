import requests
import json

#response = requests.get("https://fcsapi.com/api-v2/forex/history?symbol=EUR/USD&period=1h&access_key=62fshe1xJ6ejIAFmICbhv&level=3")
#response = requests.get("https://marketdata.tradermade.com/api/v1/timeseries?api_key=iGv_aQZoc7huEAchcPOV&currency=GBPUSD&start_date=2020-11-21-00:00&end_date=2020-12-21-08:00&format=records&interval=hourly")
def jprint(obj):
    # create a formatted string of the Python JSON object
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)

#jprint(response.json())

a = {
    "EURUSD" : "EURUSD",
    "USDJPY" : "USDJPY",
    "GBPUSD" : "GBPUSD"
}
print(a.get("EURUSD"))

