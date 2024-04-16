import requests
import json

from API.consumeApi import *

def getCoin(coin):
    request = getApiCoins(coin)
    if request.status_code == 200:
        resp = request.json()
        
        if coin != "USDT":
            return resp[f"{coin}BRL"]
        else:
            return resp["USDBRLT"]
    else:
        return "erro"
    
def getAllCoinsAndPrint():
    coins = ["AED","ARS","AUD","BOB","CAD","CHF","CLP","CNY","COP","DKK","ETH","EUR","GBP","HKD","ILS","INR","JPY","MXN","NOK","NZD","PEN","PLN","PYG","RUB","SAR","SEK","SGD","THB","TRY","TWD","USD","USDT","UYU","VEF","XRP","ZAR"]
    for coin in coins:
        print(getCoin(coin))
        print("\n")