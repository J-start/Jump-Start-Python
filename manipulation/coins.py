from api.consumeApi import getApiCoins
from api.consumeGoogleSheets import *
from dataBase.insertDatas import *
from dataBase.updateDatas import *

def getCoin(coin):
    request = getApiCoins(coin)

    if request.status_code == 200:
        resp = request.json()
        if coin != "USDT":
            return resp[f"{coin}BRL"]
        else:
            return resp["USDBRLT"]
    else:
        manipluationErrorGetCryptos(coin,request.status_code)
        return "erro"
    
def getAllCoinsAndPrint():
    coins = ["AED","ARS","AUD","BOB","CAD","CHF","CLP","CNY","COP","DKK","EUR","GBP","HKD","ILS","INR","JPY","MXN","NOK","NZD","PEN","PLN","PYG","RUB","SAR","SEK","SGD","THB","TRY","TWD","USD","USDT","UYU","VEF","XRP","ZAR"]
    #,"ARS","AUD","BOB","CAD","CHF","CLP","CNY","COP","DKK","EUR","GBP","HKD","ILS","INR","JPY","MXN","NOK","NZD","PEN","PLN","PYG","RUB","SAR","SEK","SGD","THB","TRY","TWD","USD","USDT","UYU","VEF","XRP","ZAR"
    for coin in coins:
        
        response = getCoin(coin)
        if response != "erro":
            high=round(float(response['high']),4)
            low=round(float(response['low']),4)
            bid=round(float(response['bid']),4)
            ask=round(float(response['ask']),4)
            date = convertDateApi(int(response['timestamp']))
        try:    
            insertDatasCoins(coin,date,high,low,bid,ask)

        except:
            #TODO - insert log
            print("erro")
    try:
        manipulationCoins()
    except:
        print("erro manipulationCoins")


def manipluationErrorGetCryptos(crypto,status):
     datas = {
            "Data": "",
            "Crypto": "Crypto: "+crypto,
            "Status": status
             }
     insertErrorGoogleSheets(datas) 

def convertDateApi(dateApi):
    dateFormated = datetime.fromtimestamp(dateApi).strftime('%Y-%m-%d')

    return dateFormated