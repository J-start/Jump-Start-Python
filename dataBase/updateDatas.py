import mysql.connector

from common.dataBaseCredentials import HOST_DATABASE,USER_DATABASE,PASSWORD_DATABASE,NAME_DATABASE

def getCountAsset(dataBase,table,asset):
    nameTocompare = ''
    if table == "tb_crypto":
        nameTocompare = "nameCrypto"
    elif table == "tb_coins":
        nameTocompare = "nameCoin"
    elif table == 'tb_share':
        nameTocompare = "nameShare"
    else:
        return
    mydb = mysql.connector.connect(host=HOST_DATABASE,user=USER_DATABASE,password=PASSWORD_DATABASE,database=dataBase)
    mycursor = mydb.cursor()
    
    mycursor.execute(f"SELECT COUNT(*) AS total FROM {table} WHERE {nameTocompare} = '{asset}'")

    countDataBase = mycursor.fetchone()
    return countDataBase[0]

def getCountSelic(dataBase):
    mydb = mysql.connector.connect(host=HOST_DATABASE,user=USER_DATABASE,password=PASSWORD_DATABASE,database=dataBase)
    mycursor = mydb.cursor()

    mycursor.execute("SELECT COUNT(*) AS total FROM tb_selic")

    countDataBase = mycursor.fetchone()
    return countDataBase[0]


def getIdToDeleteAsset(dataBase,table,asset):
    nameTocompare = ''
    if table == "tb_crypto":
        nameTocompare = "nameCrypto"
    elif table == "tb_coins":
        nameTocompare = "nameCoin"
    elif table == 'tb_share':
        nameTocompare = "nameShare"
    else:
        return
    mydb = mysql.connector.connect(host=HOST_DATABASE,user=USER_DATABASE,password=PASSWORD_DATABASE,database=dataBase)
    mycursor = mydb.cursor()

    mycursor.execute(f"SELECT id FROM {table} WHERE {nameTocompare} = '{asset}' LIMIT 1")

    idCrypto = mycursor.fetchone()

    return idCrypto[0]

def deleteAssets(dataBase,table,asset):
    mydb = mysql.connector.connect(host=HOST_DATABASE,user=USER_DATABASE,password=PASSWORD_DATABASE,database=dataBase)
    mycursor = mydb.cursor()

    query = f"DELETE FROM {table} WHERE id IN (%s)"

    placeholders = ', '.join(['%s'] * len(asset))
    query = query % placeholders
    try:
        mycursor.execute(query, asset)
        mydb.commit()
    except Exception as e:
        message= f"Erro: ",e,"Deletando dados da tabela {table} e asset {asset}"
        print(message)

def fetchPossiblesIdsToDelete(dataBase,table,asset,idToDelete):
        N = 1
        try:
            countAsset = getCountAsset(dataBase,table,asset)
        except Exception as e:
            print("foi na contagem", e)
        if countAsset > N:
            idCrypto = getIdToDeleteAsset(dataBase,table,asset)
            idToDelete.append(idCrypto)   
        return idToDelete 

def fetchEachAsset(dataBase,table,assets):
    idToDelete = []

    for asset in assets:
        try:
            idToDelete=fetchPossiblesIdsToDelete(dataBase,table,asset,idToDelete)
        except Exception as e:
            print("foi aqui linha 85, update datas", e)
    if idToDelete != []:
        deleteAssets(dataBase,table,idToDelete)


def manipulationAcoes(dataBase):
    actions = ["PETR4.SA","BBAS3.SA","ITSA4.SA","TRPL4.SA","VALE3.SA","CMIG4.SA","SANB11.SA","USIM5.SA","ABEV3.SA","MGLU3.SA"]
    fetchEachAsset(dataBase,"tb_share",actions)

