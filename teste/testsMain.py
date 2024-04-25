from dataBase.manipulationDataBase import *  # Importa módulos do pacote dataBase
from teste.dataBaseTests.manipulationDataBase import *
from manipulation.selic import *  # Importa módulos do pacote manipulation

def insertDatas():
    createDataBaseTest()
    createTableSelic("jumpStartTest")
    deleteDataBase()

def shouldInsertOneDataSelic():
    createDataBaseTest()
    createTableSelic("jumpStartTest")
    insertNValuesSelic()
    countSelic=countSelic2("jumpStartTest")
    try:
        assert countSelic == 1, "Should be 1"
        print("Passou!!!!!-Selic")
    except AssertionError:
            print("Falhou!!!!!")
    deleteDataBase()

def insertNValuesSelic():
    for i in range(5):
        manipulationSelic("jumpStartTest")