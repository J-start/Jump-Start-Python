from dataBase.manipulationDataBase import *  # Importa módulos do pacote dataBase
from tests.dataBaseTests.manipulationDataBase import *  # Importa módulos do pacote dataBaseTests

def insertDatas():
    createDataBaseTest()
    createTableSelic("jumpStartTest")
    deleteDataBase()
