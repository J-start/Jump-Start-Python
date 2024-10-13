from API.consumeApi import getApiCoins
from API.consumeGoogleSheets import *
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
    
def getAllCoinsAndPrint(dataBase):
    coins = ["ARS","AUD","BOB","CAD","CHF","CLP","CNY","COP","DKK","EUR","HKD","INR","JPY","MXN","NOK","PYG","RUB","SEK","TWD","USD","UYU","VEF"]
    for coin in coins:
        
        response = getCoin(coin)
        if response != "erro":
            high=round(float(response['high']),4)
            low=round(float(response['low']),4)
            bid=round(float(response['bid']),4)
            ask=round(float(response['ask']),4)
            date = convertDateApi(int(response['timestamp']))
        try:    
            insertDatasCoins(dataBase,coin,date,high,low,bid,ask)

        except:
            #TODO - insert log
            print("erro e")
    try:
        manipulationCoins(dataBase)
    except Exception as e:
        print("erro manipulationCoins ERRO:",e)


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