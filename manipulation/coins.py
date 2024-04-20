from api.consumeApi import getApiCoins
from api.consumeGoogleSheets import *
from datetime import datetime





def getCoin(coin):
    request = getApiCoins(coin)

    if request.status_code == 200:
        resp = request.json()

       
        if coin != "USDT":
            return resp[f"{coin}BRL"]
        else:
            return resp["USDBRLT"]
    else:
        dateActual = datetime.now()
        dados = {
                "Data": dateActual,
                "Ativo": f"Moeda: {coin}",
                "Status": request.status_code
                }
        insertDatasCoins(dados)
        return "erro"
    
def getAllCoinsAndPrint():
    coins = ["AED","ARS","TESTEERRO","AUD","BOB","CAD","CHF","CLP","CNY","COP","DKK","EUR","GBP","HKD","ILS","INR","JPY","MXN","NOK","NZD","PEN","PLN","PYG","RUB","SAR","SEK","SGD","THB","TRY","TWD","USD","USDT","UYU","VEF","XRP","ZAR"]
    for coin in coins:
        
        response = getCoin(coin)
        if response != "erro":
            print("---------- Moedas ------------")
            print(response['high'])
            print(response['low'])
            high=response['high']
            low=response['low']
            bid=response['bid']
            ask=response['ask']
            print("high",high)
            print("high",str(high))