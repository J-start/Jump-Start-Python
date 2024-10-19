from dataBase.manipulationDataBase import *  # Importa módulos do pacote dataBase
from teste.dataBaseTests.manipulationDataBase import *
from manipulation.selic import *  # Importa módulos do pacote manipulation
from manipulation.acoes import *
from manipulation.coins import *
from manipulation.cryptocurrency import *
from colorama import Fore, Style
from teste.enumAssets import *


def shouldInsertOneDataSelic():
    createDataBaseTest()
    createTableSelic("jumpStartTest")
    insertNValues(Asset.SELIC,3)
    count=countSelic2("jumpStartTest")
    result=verifyTest(count,"selic")
    deleteDataBase()
    return result

def shouldInsertOneDataAcoes():
    createDataBaseTest()
    createTableActions("jumpStartTest")
    insertNValues(Asset.ACAO,3)
    count=countAcoes()
    result = verifyTest(count,"acao")
    deleteDataBase()
    return result

def shouldInsertOneDataCoins():
    createDataBaseTest()
    createTableCoins("jumpStartTest")
    insertNValues(Asset.COIN,3)
    count=countCoins()
    result=verifyTest(count,"coin")
    deleteDataBase()
    return result

def shouldInsertOneDataCrypto():
    createDataBaseTest()
    createTableCryptos("jumpStartTest")
    insertNValues(Asset.CRYPTO,3)
    count=countCrypto()
    result=verifyTest(count,"crypto")
    deleteDataBase()
    return result


def verifyTest(count,asset):
    try:
        assert count == 1, "Should be 1"
        print("\n")
        print(Fore.GREEN+f"Passou-{asset}"+Style.RESET_ALL)
        return True
    except AssertionError:
        print("\n")
        print(Fore.RED+f"Falhou-{asset}"+Style.RESET_ALL)
        return False
    
def insertNValues(asset,N):
    
        if asset == Asset.SELIC:
            for i in range(N):
                manipulationSelic("jumpStartTest")
        elif asset == Asset.ACAO:
            for i in range(N):
                fetchAllInformationActions("jumpStartTest")
        elif asset == Asset.COIN:
            for i in range(N):
                getAllCoinsAndPrint("jumpStartTest")
        elif asset == Asset.CRYPTO:
            for i in range(N):
                getAndPrintAllCryptos("jumpStartTest")

def countCrypto():
    cryptos = ["BTC","LTC","ETH","XRP","BCH","USDT","LINK","DOGE","ADA","EOS","XLM","CHZ","AXS"]
    return verifyCountAsset(cryptos,"tb_crypto")
    
def countCoins():
    coins = ["ARS","AUD","BOB","CAD","CHF","CLP","CNY","COP","DKK","EUR","HKD","INR","JPY","MXN","NOK","PYG","RUB","SEK","TWD","USD","UYU","VEF"]
    return verifyCountAsset(coins,"tb_coins")

def countAcoes():
    actions = ["PETR4.SA","BBAS3.SA","ITSA4.SA","TRPL4.SA","VALE3.SA","CMIG4.SA","SANB11.SA","USIM5.SA","ABEV3.SA","MGLU3.SA"]
    return verifyCountAsset(actions,"tb_share")

def verifyCountAsset(listAssets,table):
    count = []
    N = 1
    for asset in listAssets:
        countAssetActual = countAssets("jumpStartTest",table,asset)
        if countAssetActual != N:
            count.append(countAssetActual)
    if count == []:
        return 1
    else:
        return 0    

