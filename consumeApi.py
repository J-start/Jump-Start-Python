import requests
import json


def getApiSelic():
    request = requests.get("https://api.bcb.gov.br/dados/serie/bcdata.sgs.11/dados/ultimos/1?formato=json")
    return request

def getApiCoins(coin):
    request = requests.get(f"http://economia.awesomeapi.com.br/json/last/{coin}-BRL")
    return request

def getApiCrypto(InstrumentId):
    data = {
    "OMSId": 1,
    "InstrumentId": InstrumentId,
    "Depth": 1
    }
    headers = {'Content-type': 'application/json'}
    request = requests.post("https://api.coinext.com.br:8443/AP/GetL2Snapshot", json=data, headers=headers)
    return request