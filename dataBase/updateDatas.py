import mysql.connector

def getCountAsset(table,crypto):
    mydb = mysql.connector.connect(host="localhost",user="root",password="",database="jumpStart")
    mycursor = mydb.cursor()

    mycursor.execute(f"SELECT COUNT(*) AS total FROM {table} WHERE name = '{crypto}'")

    countDataBase = mycursor.fetchone()
    return countDataBase[0]


def getIdToDeleteAsset(table,crypto):
    mydb = mysql.connector.connect(host="localhost",user="root",password="",database="jumpStart")
    mycursor = mydb.cursor()

    mycursor.execute(f"SELECT id FROM {table} WHERE name = '{crypto}' LIMIT 1")

    idCrypto = mycursor.fetchone()

    return idCrypto[0]

def deleteAssets(table,cryptos):
    mydb = mysql.connector.connect(host="localhost",user="root",password="",database="jumpStart")
    mycursor = mydb.cursor()

    query = f"DELETE FROM {table} WHERE id IN (%s)"

    placeholders = ', '.join(['%s'] * len(cryptos))
    query = query % placeholders
    mycursor.execute(query, cryptos)
    mydb.commit()

    print(f"{mycursor.rowcount} linhas excluídas")


def fetchPossiblesAssetsToDelete(table,asset,idToDelete):
        countCrypto = getCountAsset(table,asset)
        if countCrypto > 1:
            idCrypto = getIdToDeleteAsset(table,asset)
            idToDelete.append(idCrypto)   
        return idToDelete 

def manipulationCryptos():
    cryptos = ["BTC","LTC","ETH","XRP","BCH","USDT","LINK","DOGE","ADA","EOS","XLM","CHZ","AXS"]
    idToDelete = []
    for crypto in cryptos:
        idToDelete=fetchPossiblesAssetsToDelete(table="tb_crypto",asset=crypto,idToDelete=idToDelete)
    if idToDelete != []:
        deleteAssets("tb_crypto",idToDelete)

def main():
    manipulationCryptos()

if __name__ == "__main__":
    main()