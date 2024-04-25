import mysql.connector

def createDataBaseTest():
    mydb = mysql.connector.connect(host="localhost",user="root",password="")
    mycursor = mydb.cursor()
    mycursor.execute("CREATE DATABASE jumpStartTest")

def deleteDataBase():
    mydb = mysql.connector.connect(host="localhost",user="root",password="")
    mycursor = mydb.cursor()
    mycursor.execute("DROP DATABASE jumpStartTest")

def countAssets(dataBase,table,asset):
    mydb = mysql.connector.connect(host="localhost",user="root",password="",database=dataBase)
    mycursor = mydb.cursor()

    mycursor.execute(f"SELECT COUNT(*) AS total FROM {table} WHERE name = '{asset}' LIMIT 1")

    countDataBase = mycursor.fetchone()
    return countDataBase[0]

def countSelic2(dataBase):
    mydb = mysql.connector.connect(host="localhost",user="root",password="",database=dataBase)
    mycursor = mydb.cursor()

    mycursor.execute("SELECT COUNT(*) AS total FROM tb_selic")

    countDataBase = mycursor.fetchone()
    return countDataBase[0]