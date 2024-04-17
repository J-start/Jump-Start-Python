
from API.consumeApi import *

def cripto(crypto):

    response = getApiCrypto(crypto)

    resp = response.json()
    print("------------------ \n")
    print(resp)
    print("------------------ \n")

def getAndPrintAllCryptos():
    cryptos = [1,2,4,6,8,10,12,14,16,18,20,22,28]
    index =1
    for crypto in cryptos:
        print(index)
        index +=1
        cripto(crypto)