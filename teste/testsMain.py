from dataBase.manipulationDataBase import *  # Importa módulos do pacote dataBase
from teste.dataBaseTests.manipulationDataBase import *
from manipulation.selic import *  # Importa módulos do pacote manipulation
from manipulation.acoes import *
from manipulation.coins import *
from manipulation.cryptocurrency import *


def shouldInsertOneDataSelic():
    createDataBaseTest()
    createTableSelic("jumpStartTest")
    insertNValuesSelic()
    count=countSelic2("jumpStartTest")
    result=verifyTest(count,"selic")
    deleteDataBase()
    return result

def shouldInsertOneDataAcoes():
    createDataBaseTest()
    createTableActions("jumpStartTest")
    insertNValuesAcoes()
    count=countAssets("jumpStartTest","tb_acoes","TRPL4.SA")
    result = verifyTest(count,"acao")
    deleteDataBase()
    return result

def shouldInsertOneDataCoins():
    createDataBaseTest()
    createTableCoins("jumpStartTest")
    insertNValuesCoins()
    count=countAssets("jumpStartTest","tb_coins","CAD")
    result=verifyTest(count,"coin")
    deleteDataBase()
    return result

def shouldInsertOneDataCrypto():
    createDataBaseTest()
    createTableCryptos("jumpStartTest")
    insertNValuesCrypto()
    count=countAssets("jumpStartTest","tb_crypto","BTC")
    result=verifyTest(count,"crypto")
    deleteDataBase()
    return result


def verifyTest(count,asset):
    try:
        assert count == 1, "Should be 1"
        print("\n")
        print(f"Passou!!!!!-{asset}")
        print("\n")
        return True
    except AssertionError:
        print("\n")
        print(f"Falhou!!!!!-{asset}")
        print("\n")
        return False
    
def insertNValuesSelic():
    for i in range(3):
        manipulationSelic("jumpStartTest")

def insertNValuesAcoes():
    for i in range(3):
        fetchAllInformationActions("jumpStartTest")

def insertNValuesCoins():
    for i in range(3):
        getAllCoinsAndPrint("jumpStartTest")

def insertNValuesCrypto():
    for i in range(3):
        getAndPrintAllCryptos("jumpStartTest")

