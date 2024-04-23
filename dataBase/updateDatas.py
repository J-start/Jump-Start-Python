import mysql.connector

def getCountAsset(table,asset):
    mydb = mysql.connector.connect(host="localhost",user="root",password="",database="jumpStart")
    mycursor = mydb.cursor()

    mycursor.execute(f"SELECT COUNT(*) AS total FROM {table} WHERE name = '{asset}'")

    countDataBase = mycursor.fetchone()
    return countDataBase[0]


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
    mycursor.execute(query, asset)
    mydb.commit()

    print(f"{mycursor.rowcount} linhas excluídas")


def fetchPossiblesIdsToDelete(table,asset,idToDelete):
        countCrypto = getCountAsset(table,asset)
        if countCrypto > 1:
            idCrypto = getIdToDeleteAsset(table,asset)
            idToDelete.append(idCrypto)   
        return idToDelete 

def manipulationCryptos():
    cryptos = ["BTC","LTC","ETH","XRP","BCH","USDT","LINK","DOGE","ADA","EOS","XLM","CHZ","AXS"]
    idToDelete = []
    for crypto in cryptos:
        idToDelete=fetchPossiblesIdsToDelete(table="tb_crypto",asset=crypto,idToDelete=idToDelete)
    if idToDelete != []:
        deleteAssets("tb_crypto",idToDelete)

def manipulationAcoes():
    actions = ["PETR4.SA","BBAS3.SA","ITSA4.SA","TRPL4.SA","VALE3.SA","CMIG4.SA","SANB11.SA","USIM5.SA","ABEV3.SA","MGLU3.SA"]
    idToDelete = []
    for action in actions:
        idToDelete=fetchPossiblesIdsToDelete(table="tb_acoes",asset=action,idToDelete=idToDelete)
    if idToDelete != []:
        deleteAssets("tb_acoes",idToDelete)

def manipulationCoins():
    coins = ["AED","ARS","AUD","BOB","CAD","CHF","CLP","CNY","COP","DKK","EUR","GBP","HKD","ILS","INR","JPY","MXN","NOK","NZD","PEN","PLN","PYG","RUB","SAR","SEK","SGD","THB","TRY","TWD","USD","USDT","UYU","VEF","XRP","ZAR"]
    idToDelete = []
    for coin in coins:
        idToDelete=fetchPossiblesIdsToDelete(table="tb_coins",asset=coin,idToDelete=idToDelete)
    if idToDelete != []:
        deleteAssets("tb_coins",idToDelete)


def main():
    manipulationCoins()

if __name__ == "__main__":
    main()