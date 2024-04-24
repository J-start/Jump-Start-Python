import mysql.connector



def getCountAsset(table,asset):
    mydb = mysql.connector.connect(host="localhost",user="root",password="",database="jumpStart")
    mycursor = mydb.cursor()
    
    mycursor.execute(f"SELECT COUNT(*) AS total FROM {table} WHERE name = '{asset}'")

    countDataBase = mycursor.fetchone()
    return countDataBase[0]

def getCountSelic():
    mydb = mysql.connector.connect(host="localhost",user="root",password="",database="jumpStart")
    mycursor = mydb.cursor()

    mycursor.execute("SELECT COUNT(*) AS total FROM tb_selic")

    countDataBase = mycursor.fetchone()
    return countDataBase[0]

def getIdToDeleteSelic():
    mydb = mysql.connector.connect(host="localhost",user="root",password="",database="jumpStart")
    mycursor = mydb.cursor()

    mycursor.execute("SELECT id FROM tb_selic LIMIT 1")

    idCrypto = mycursor.fetchone()

    return idCrypto[0]

def getIdToDeleteAsset(table,asset):
    mydb = mysql.connector.connect(host="localhost",user="root",password="",database="jumpStart")
    mycursor = mydb.cursor()

    mycursor.execute(f"SELECT id FROM {table} WHERE name = '{asset}' LIMIT 1")

    idCrypto = mycursor.fetchone()

    return idCrypto[0]

def deleteAssets(table,asset):
    mydb = mysql.connector.connect(host="localhost",user="root",password="",database="jumpStart")
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

def fetchPossiblesIdsToDelete(table,asset,idToDelete):
        N = 1
        countCrypto = getCountAsset(table,asset)
        if countCrypto > N:
            idCrypto = getIdToDeleteAsset(table,asset)
            idToDelete.append(idCrypto)   
        return idToDelete 

def fetchEachAsset(table,assets):
    idToDelete = []
    for asset in assets:
        idToDelete=fetchPossiblesIdsToDelete(table,asset,idToDelete)
    if idToDelete != []:
        deleteAssets(table,idToDelete)

def manipulationCryptos():
    cryptos = ["BTC","LTC","ETH","XRP","BCH","USDT","LINK","DOGE","ADA","EOS","XLM","CHZ","AXS"]
    fetchEachAsset("tb_crypto",cryptos)

def manipulationAcoes():
    actions = ["PETR4.SA","BBAS3.SA","ITSA4.SA","TRPL4.SA","VALE3.SA","CMIG4.SA","SANB11.SA","USIM5.SA","ABEV3.SA","MGLU3.SA"]
    fetchEachAsset("tb_acoes",actions)

def manipulationCoins():
    coins = ["AED","ARS","AUD","BOB","CAD","CHF","CLP","CNY","COP","DKK","EUR","GBP","HKD","ILS","INR","JPY","MXN","NOK","NZD","PEN","PLN","PYG","RUB","SAR","SEK","SGD","THB","TRY","TWD","USD","USDT","UYU","VEF","XRP","ZAR"]
    fetchEachAsset("tb_coins",coins)

def manipulationSelicDeleteDatas():
    N = 1
    countSelic = getCountSelic()
    if countSelic > N:
        idToDelete = getIdToDeleteSelic()
        deleteAssets("tb_selic",[idToDelete])

def main():
    manipulationSelicDeleteDatas()

if __name__ == "__main__":
    main()