from API.consumeGoogleSheets import insertErrorGoogleSheets
import mysql.connector
from common.listShares import *
from common.dataBaseCredentials import HOST_DATABASE,USER_DATABASE,PASSWORD_DATABASE,NAME_DATABASE,PORT_DATABASE

def getCountAsset(table,asset):
    print("getCountAsset")
    nameTocompare = 'nameShare'
    if table == "tb_crypto":
        nameTocompare = 'nameCrypto'
    try:
        mydb = mysql.connector.connect(host=HOST_DATABASE,port=PORT_DATABASE,user=USER_DATABASE,password=PASSWORD_DATABASE,database=NAME_DATABASE)
        mycursor = mydb.cursor()
    
        mycursor.execute(f"SELECT COUNT(*) AS total FROM {table} WHERE {nameTocompare} = '{asset}'")

        countDataBase = mycursor.fetchone()
        print("countDataBase: ",countDataBase)
        return countDataBase[0]
    except Exception as e:
        print("Erro na contagem de ações: ",e)
        return -1


def getIdToDeleteAsset(table,asset):
    nameTocompare = 'nameShare'
    if table == "tb_crypto":
        nameTocompare = 'nameCrypto'
    print("nameTocompare ",nameTocompare)
    print("asset ",asset)
    try:
        mydb = mysql.connector.connect(host=HOST_DATABASE,port=PORT_DATABASE,user=USER_DATABASE,password=PASSWORD_DATABASE,database=NAME_DATABASE)
        mycursor = mydb.cursor()
        sql = f"SELECT id FROM {table} WHERE {nameTocompare} = '{asset}' LIMIT 1"
        print("sql: ",sql)
        mycursor.execute(sql)

        idCrypto = mycursor.fetchone()

        return idCrypto[0]
    except Exception as e:
        return -1
    


def deleteAssets(table,asset):

    try:
        mydb = mysql.connector.connect(host=HOST_DATABASE,port=PORT_DATABASE,user=USER_DATABASE,password=PASSWORD_DATABASE,database=NAME_DATABASE)
        mycursor = mydb.cursor()

        query = f"DELETE FROM {table} WHERE id IN (%s)"

        placeholders = ', '.join(['%s'] * len(asset))
        query = query % placeholders
        mycursor.execute(query, asset)
        mydb.commit()
    except Exception as e:
        print("Erro deletando dados da tabela ",table," e assets ",asset, e)
        message= f"Erro deletando dados da tabela {table} e assets {asset}"
        manipluationError(asset, message)


def fetchPossiblesIdsToDelete(table,asset):
        MAX_INSERTS = 10
        if table == "tb_share":
            MAX_INSERTS = 320
        elif table == "tb_crypto":
            MAX_INSERTS = 31
        try:
            countAsset = getCountAsset(table,asset)
        except Exception as e:
            manipluationError(asset, f"Erro na contagem de ações: ${str(e)}")
            return 
        if countAsset > MAX_INSERTS:
            idCrypto = getIdToDeleteAsset(table,asset)
            print("idCrypto2: ",idCrypto)
            if idCrypto != -1: 
                return idCrypto
        return -1

def fetchEachAsset(table,assets):
    idToDelete = []

    for asset in assets:
        try:
            id=fetchPossiblesIdsToDelete(table,asset)
            if id != -1:
                idToDelete.append(id)
            print("idToDelete: ",idToDelete)
        except Exception as e:
            print("Erro ao buscar possiveis ids para deletar: ",e)
            manipluationError(asset, f"Erro ao buscar possiveis ids para deletar: ${str(e)}")
    if idToDelete != []:
        deleteAssets(table,idToDelete)


def manipulationAcoes():

    actions = searchListShares()
    fetchEachAsset("tb_share",actions)

def manipulationCrypto():
    print("dataBase tb_crypto ",NAME_DATABASE)
    actions = searchListCrypto()
    print("actions: ",actions)
    fetchEachAsset("tb_crypto",actions)    



def manipluationError(share,status):
     datas = {
            "Data": "",
            "Ativo": share,
            "Status": status
             }
     insertErrorGoogleSheets(datas) 