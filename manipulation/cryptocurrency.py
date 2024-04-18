
from api.consumeApi import *

def cripto(crypto):

    response = getApiCrypto(crypto)

    resp = response.json()
    print("------------------ \n")
    high = round(float(resp[0]['high']),4)
    low = round(float(resp[0]['low']),4)
    vol = round(float(resp[0]['vol']),4)
    last = round(float(resp[0]['last']),4)
    sell = round(float(resp[0]['sell']),4)
    buy = round(float(resp[0]['buy']),4)
    date = resp[0]['date']
    open = round(float(resp[0]['open']),4)

    print("coin: ",crypto,"high :",high,"low :",low,"vol :",vol,"last :",last,"buy :",buy,"sell :",sell,"date :",date,"open :",open)

def getAndPrintAllCryptos():
    cryptos = ["BTC","LTC","ETH","XRP","BCH","USDT","LINK","DOGE","ADA","EOS","XLM","CHZ","AXS"]
    index =1
    for crypto in cryptos:
        index +=1
        print("--------Crypto-------")
        cripto(crypto)
        print("--------Crypto-------")