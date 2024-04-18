import requests
import json


def getApiSelic():
    request = requests.get("https://api.bcb.gov.br/dados/serie/bcdata.sgs.11/dados/ultimos/1?formato=json")
    return request

def getApiCoins(coin):
    request = requests.get(f"http://economia.awesomeapi.com.br/json/last/{coin}-BRL")
    return request

def getApiCrypto(cripto):
    request = requests.get(f"https://api.mercadobitcoin.net/api/v4/tickers?symbols={cripto}-BRL")
    return request