from flask import Flask, request, jsonify, make_response
import requests
import json
from pymongo import MongoClient
from flask_pymongo import PyMongo
from flask_cors import CORS


app = Flask(__name__)
CORS(app)

#client = MongoClient('mongodb+srv://test1:1234@cluster0.5k4up.mongodb.net/Forex_historical?retryWrites=true&w=majority')
"""
DB_URI = 'mongodb+srv://test1:1234@cluster0.5k4up.mongodb.net/Forex_historical?retryWrites=true&w=majority'
app.config["MONGODB_HOST"] = DB_URI

#client = MongoClient('mongodb+srv://test1:1234@cluster0.5k4up.mongodb.net/Forex_historical?retryWrites=true&w=majority')
client = MongoClient(DB_URI)
db = client['Forex_historical']
"""
API_historical = {
    "EURUSD" : requests.get("https://marketdata.tradermade.com/api/v1/timeseries?api_key=iGv_aQZoc7huEAchcPOV&currency=EURUSD&start_date=2020-11-21-00:00&end_date=2020-12-21-08:00&format=records&interval=hourly"),
    "USDJPY" : requests.get("https://marketdata.tradermade.com/api/v1/timeseries?api_key=iGv_aQZoc7huEAchcPOV&currency=USDJPY&start_date=2020-11-21-00:00&end_date=2020-12-21-08:00&format=records&interval=hourly"),
    "GBPUSD" : requests.get("https://marketdata.tradermade.com/api/v1/timeseries?api_key=iGv_aQZoc7huEAchcPOV&currency=GBPUSD&start_date=2020-11-21-00:00&end_date=2020-12-21-08:00&format=records&interval=hourly")
}

def to_json(data):
    return{
        "index": data['index'],
        "date": data['date'],
        "open": data['open'],
        "high": data['high'],
        "low": data['low'],
        "close": data['close'],
        "volume": data['volume']
    }

@app.route('/<string:c_pair>/historical', methods=['GET'])
def data_historical(c_pair):
    #response = requests.get("https://fcsapi.com/api-v3/forex/history?id=1&period=1h&access_key=62fshe1xJ6ejIAFmICbhv&level=3")
    response = API_historical.get("{}".format(c_pair))
    if request.method == 'GET':
        return make_response(jsonify(response.json()), 200)
    else:
        return make_response("", 404)

# @app.route('/<string:c_pair>/predict', methods=['GET'])
# def predict_historical(c_pair):
#     #ollection = db['{}_predict'.format(c_pair)]
#     if request.method == 'GET':
        
#         return make_response(jsonify(data), 200)
#     else:
#         return make_response("", 404)


if __name__ == '__main__': 
    app.run()
