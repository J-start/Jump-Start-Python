from api.consumeApi import *
from api.consumeGoogleSheets import *
from dataBase.insertDatas import *
from dataBase.updateDatas import *

def getCripto(dataBase,crypto):

    response = getApiCrypto(crypto)
    if response.status_code == 200:
        resp = response.json()
        if resp != []:
            high = round(float(resp[0]['high']),4)
            low = round(float(resp[0]['low']),4)
            vol = round(float(resp[0]['vol']),4)
            last = round(float(resp[0]['last']),4)
            sell = round(float(resp[0]['sell']),4)
            buy = round(float(resp[0]['buy']),4)
            date = convertDateApi(resp[0]['date'])
            open = round(float(resp[0]['open']),4)

            try:
                insertDatasCrypto(dataBase,crypto,date,high,low,vol,last,sell,buy)
            except:
                 #TODO - insert log
                 print("erro insertDatasCrypto")

        else:
            manipluationErrorGetCryptos(crypto,"400")
    else:
            manipluationErrorGetCryptos(crypto,response.status_code)

def getAndPrintAllCryptos(dataBase):
    cryptos = ["BTC","LTC","ETH","XRP","BCH","USDT","LINK","DOGE","ADA","EOS","XLM","CHZ","AXS"]
    for crypto in cryptos:
        getCripto(dataBase,crypto)
    try:
        manipulationCryptos(dataBase)
    except:
        print("erro manipulationCryptos")

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