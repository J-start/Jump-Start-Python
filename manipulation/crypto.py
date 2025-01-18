from API.consumeGoogleSheets import insertErrorGoogleSheets
from common.listShares import searchListCrypto
import dataBase
from dataBase.insertDatas import insertCrypto
from dataBase.updateDatas import manipulationCrypto
import requests
from datetime import datetime

def getValuesCrypto(crypto):
    url = f"https://api.mercadobitcoin.net/api/v4/tickers?symbols={crypto}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return None

def insertCryptoDb(database,name,value,date):
    try:
        insertCrypto(database,name,value,date)
    except Exception as e:
        print("erro: ", e)
        manipluationError(e,"Erro ao manipular crypto")

def mainCrypto(database):
    cryptos = searchListCrypto()
    for crypto in cryptos:
        responseCrypto = getValuesCrypto(crypto)
        if responseCrypto != None:
            name = responseCrypto[0]['pair']
            value = float(responseCrypto[0]['last'])
            dateDb = convertTimesTamp(responseCrypto[0]['date'])
        insertCryptoDb(database,name,value,dateDb)
    try:
        print("aaaa")
        manipulationCrypto()
        print()
    except Exception as e:
        print("erro crypto", e)
        manipluationError(crypto, f"Erro ao manipular crypto, verificação de exclusão: ${str(e)}")     

def convertTimesTamp(timestamp):
    date = datetime.fromtimestamp(timestamp)
    dateDb = date.strftime('%Y-%m-%d')
    return dateDb

def manipluationError(share,status):
     datas = {
            "Data": "",
            "Acao": "Crypto",
            "Status": status
             }
     insertErrorGoogleSheets(datas) 