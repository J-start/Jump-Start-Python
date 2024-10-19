import mysql.connector

def createDataBaseTest():
    mydb = mysql.connector.connect(host="localhost",user="homestead",password="secret")
    mycursor = mydb.cursor()
    mycursor.execute("CREATE DATABASE jumpStartTest")

def deleteDataBase():
    mydb = mysql.connector.connect(host="localhost",user="homestead",password="secret")
    mycursor = mydb.cursor()
    mycursor.execute("DROP DATABASE jumpStartTest")

def countAssets(dataBase,table,asset):
    nameTocompare = ''
    if table == "tb_crypto":
        nameTocompare = "nameCrypto"
    elif table == "tb_coins":
        nameTocompare = "nameCoin"
    elif table == 'tb_share':
        nameTocompare = "nameShare"
    else:
        return
    mydb = mysql.connector.connect(host="localhost",user="homestead",password="secret",database=dataBase)
    mycursor = mydb.cursor()

    mycursor.execute(f"SELECT COUNT(*) AS total FROM {table} WHERE {nameTocompare} = '{asset}' LIMIT 1")

    countDataBase = mycursor.fetchone()
    return countDataBase[0]

def countSelic2(dataBase):
    mydb = mysql.connector.connect(host="localhost",user="homestead",password="secret",database=dataBase)
    mycursor = mydb.cursor()

    mycursor.execute("SELECT COUNT(*) AS total FROM tb_selic")

    countDataBase = mycursor.fetchone()
    return countDataBase[0]