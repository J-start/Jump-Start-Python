import mysql.connector

def getCountCrypto(crypto):
    mydb = mysql.connector.connect(host="localhost",user="root",password="",database="jumpStart")
    mycursor = mydb.cursor()
    mycursor.execute(f"SELECT COUNT(*) AS total FROM tb_crypto WHERE name = '{crypto}'")

    countDataBase = mycursor.fetchone()
    return countDataBase[0]


def getIdCryptoToDelete(crypto):
    mydb = mysql.connector.connect(host="localhost",user="root",password="",database="jumpStart")
    mycursor = mydb.cursor()
    mycursor.execute(f"SELECT id FROM tb_crypto WHERE name = '{crypto}' LIMIT 1")

    idCrypto = mycursor.fetchone()
    print("idCrypto[0]",idCrypto[0])
    return idCrypto[0]

def deleteCryptos(cryptos):
    mydb = mysql.connector.connect(host="localhost",user="root",password="",database="jumpStart")
    mycursor = mydb.cursor()

    query = "DELETE FROM tb_crypto WHERE id IN (%s)"
    placeholders = ', '.join(['%s'] * len(cryptos))
    query = query % placeholders

    mycursor.execute(query, cryptos)

    mydb.commit()

    print(f"{mycursor.rowcount} linhas excluídas")



def manipulationCryptos():
    cryptos = ["BTC","LTC","ETH","XRP","BCH","USDT","LINK","DOGE","ADA","EOS","XLM","CHZ","AXS"]
    idToDelete = []
    for crypto in cryptos:
        countCrypto = getCountCrypto(crypto)
        if countCrypto > 1:
            idCrypto = getIdCryptoToDelete(crypto)
            idToDelete.append(idCrypto)
    if idToDelete != []:
        deleteCryptos(idToDelete)

def main():
    manipulationCryptos()

if __name__ == "__main__":
    main()