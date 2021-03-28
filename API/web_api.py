from apscheduler.schedulers.background import BackgroundScheduler
from flask import Flask, request, jsonify, make_response
import requests
import json
# from pymongo import MongoClient
# from flask_pymongo import PyMongo
from flask_cors import CORS

import pandas as pd

from preprocessing import to_dataFrame
from Evaluate_model import evaluate_historical
from preprocessing import for_evaluate


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
    "EURUSD": requests.get("https://fcsapi.com/api-v3/forex/history?symbol=EUR/USD&period=1h&access_key=62fshe1xJ6ejIAFmICbhv&level=3"),
    "GBPUSD": requests.get("https://fcsapi.com/api-v3/forex/history?symbol=GBP/USD&period=1h&access_key=62fshe1xJ6ejIAFmICbhv&level=3"),
    "USDJPY": requests.get("https://fcsapi.com/api-v3/forex/history?symbol=USD/JPY&period=1h&access_key=62fshe1xJ6ejIAFmICbhv&level=3"),
}


def forex_historical():
    API_historical = {
        "EURUSD": requests.get("https://fcsapi.com/api-v3/forex/history?symbol=EUR/USD&period=1h&access_key=62fshe1xJ6ejIAFmICbhv&level=3"),
        "GBPUSD": requests.get("https://fcsapi.com/api-v3/forex/history?symbol=GBP/USD&period=1h&access_key=62fshe1xJ6ejIAFmICbhv&level=3"),
        "USDJPY": requests.get("https://fcsapi.com/api-v3/forex/history?symbol=USD/JPY&period=1h&access_key=62fshe1xJ6ejIAFmICbhv&level=3"),
    }
    evaluate = {
        # "EURUSD" : evaluate_historical(data,"EURUSD")
        "EURUSD": create_feature("EURUSD"),
        "GBPUSD": create_feature("GBPUSD"),
        "USDJPY": create_feature("USDJPY"),
    }


def create_feature(c_pair):
    response = API_historical.get("{}".format(c_pair))
    data = response.json().get('response')
    data = to_dataFrame(data)
    return evaluate_historical(data, c_pair)


# data = pd.read_csv(r'save_data\test.csv')
evaluate = {
    # "EURUSD" : evaluate_historical(data,"EURUSD")
    "EURUSD": create_feature("EURUSD"),
    "GBPUSD": create_feature("GBPUSD"),
    "USDJPY": create_feature("USDJPY"),
}


sched = BackgroundScheduler(daemon=True)
sched.add_job(forex_historical, 'interval', minutes=60)
sched.start()


@app.route('/<string:c_pair>/historical', methods=['GET'])
def data_historical(c_pair):
    response = API_historical.get("{}".format(c_pair))
    if request.method == 'GET':
        result = response.json()
        return make_response(jsonify(result), 200)
    else:
        return make_response("", 404)


@app.route('/<string:c_pair>/evaluate', methods=['GET'])
def data_evaluate(c_pair):
    if request.method == 'GET':
        result = evaluate.get("{}".format(c_pair))
        return make_response(jsonify(result), 200)
    else:
        return make_response("", 404)


if __name__ == '__main__':
    app.run()
