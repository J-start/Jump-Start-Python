from dataBase.manipulationDataBase import *  # Importa módulos do pacote dataBase
from teste.dataBaseTests.manipulationDataBase import *
from manipulation.selic import *  # Importa módulos do pacote manipulation
from manipulation.acoes import *
from manipulation.coins import *
from manipulation.cryptocurrency import *

def insertDatas():
    createDataBaseTest()
    createTableSelic("jumpStartTest")
    deleteDataBase()

def shouldInsertOneDataSelic():
    createDataBaseTest()
    createTableSelic("jumpStartTest")
    insertNValuesSelic()
    count=countSelic2("jumpStartTest")
    try:
        assert count == 1, "Should be 1"
        print("Passou!!!!!-Selic")
    except AssertionError:
            print("Falhou!!!!!")
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

def shouldInsertOneDataCoins():
    createDataBaseTest()
    createTableCryptos("jumpStartTest")
    insertNValuesCoins()
    count=countAssets("jumpStartTest","tb_coins","CAD")
    verifyTest(count,"coin")
    deleteDataBase()

def verifyTest(count,asset):
    try:
        assert count == 2, "Should be 1"
        print(f"Passou!!!!!-{asset}")
    except AssertionError:
            print("Falhou!!!!!")
    
def insertNValuesSelic():
    for i in range(5):
        manipulationSelic("jumpStartTest")

def insertNValuesAcoes():
    for i in range(5):
        fetchAllInformationActions("jumpStartTest")

def insertNValuesCoins():
    for i in range(5):
        getAllCoinsAndPrint("jumpStartTest")


def insertNValuesCoins():
    for i in range(5):
        getAllCoinsAndPrint("jumpStartTest")

