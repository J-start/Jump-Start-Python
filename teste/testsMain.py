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
    verifyTest(count,"selic")
    deleteDataBase()

def shouldInsertOneDataAcoes():
    createDataBaseTest()
    createTableActions("jumpStartTest")
    insertNValuesAcoes()
    count=countAssets("jumpStartTest","tb_acoes","TRPL4.SA")
    verifyTest(count,"acao")
    deleteDataBase()

def shouldInsertOneDataCoins():
    createDataBaseTest()
    createTableCoins("jumpStartTest")
    insertNValuesCoins()
    count=countAssets("jumpStartTest","tb_coins","CAD")
    verifyTest(count,"coin")
    deleteDataBase()

def shouldInsertOneDataCrypto():
    createDataBaseTest()
    createTableCryptos("jumpStartTest")
    insertNValuesCrypto()
    count=countAssets("jumpStartTest","tb_crypto","BTC")
    verifyTest(count,"crypto")
    deleteDataBase()


def verifyTest(count,asset):
    try:
        assert count == 1, "Should be 1"
        print(f"Passou!!!!!-{asset}")
    except AssertionError:
            print(f"Falhou!!!!!-{asset}")
    
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

