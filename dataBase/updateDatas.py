from API.consumeGoogleSheets import insertErrorGoogleSheets
import mysql.connector
from common.listShares import *
from common.dataBaseCredentials import HOST_DATABASE,USER_DATABASE,PASSWORD_DATABASE,NAME_DATABASE

def getCountAsset(dataBase,table,asset):
    nameTocompare = 'nameShare'
    try:
        mydb = mysql.connector.connect(host=HOST_DATABASE,user=USER_DATABASE,password=PASSWORD_DATABASE,database=dataBase)
        mycursor = mydb.cursor()
    
        mycursor.execute(f"SELECT COUNT(*) AS total FROM {table} WHERE {nameTocompare} = '{asset}'")

        countDataBase = mycursor.fetchone()
        return countDataBase[0]
    except Exception as e:
        return -1


def getIdToDeleteAsset(dataBase,table,asset):
    nameTocompare = 'nameShare'
    try:
        mydb = mysql.connector.connect(host=HOST_DATABASE,user=USER_DATABASE,password=PASSWORD_DATABASE,database=dataBase)
        mycursor = mydb.cursor()

        mycursor.execute(f"SELECT id FROM {table} WHERE {nameTocompare} = '{asset}' LIMIT 1")

        idCrypto = mycursor.fetchone()

        return idCrypto[0]
    except Exception as e:
        return -1
    


def deleteAssets(dataBase,table,asset):

    try:
        mydb = mysql.connector.connect(host=HOST_DATABASE,user=USER_DATABASE,password=PASSWORD_DATABASE,database=dataBase)
        mycursor = mydb.cursor()

        query = f"DELETE FROM {table} WHERE id IN (%s)"

        placeholders = ', '.join(['%s'] * len(asset))
        query = query % placeholders
        mycursor.execute(query, asset)
        mydb.commit()
    except Exception as e:
        message= f"Erro deletando dados da tabela {table} e assets {asset}"
        manipluationError(asset, message)


def fetchPossiblesIdsToDelete(dataBase,table,asset,idToDelete):
        MAX_SHARE = 320
        try:
            countAsset = getCountAsset(dataBase,table,asset)
        except Exception as e:
            manipluationError(asset, f"Erro na contagem de ações: ${str(e)}")
            return 
        if countAsset > MAX_SHARE:
            idCrypto = getIdToDeleteAsset(dataBase,table,asset)
            if idCrypto != -1:
                idToDelete.append(idCrypto)   
                return idToDelete
        return -1

def fetchEachAsset(dataBase,table,assets):
    idToDelete = []

    for asset in assets:
        try:
            idToDelete=fetchPossiblesIdsToDelete(dataBase,table,asset,idToDelete)
        except Exception as e:
            manipluationError(asset, f"Erro ao buscar possiveis ids para deletar: ${str(e)}")
    if idToDelete != []:
        deleteAssets(dataBase,table,idToDelete)


def manipulationAcoes(dataBase):
    actions = searchListShares()
    fetchEachAsset(dataBase,"tb_share",actions)

def manipluationError(share,status):
     datas = {
            "Data": "",
            "Ativo": share,
            "Status": status
             }
     insertErrorGoogleSheets(datas) 