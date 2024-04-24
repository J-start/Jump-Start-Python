import mysql.connector


def createConnection():
    mydb = mysql.connector.connect(host="localhost",user="root",password="")
    return mydb.cursor()

def createDataBase():
    mydb = mysql.connector.connect(host="localhost",user="root",password="")
    mycursor = mydb.cursor()
    mycursor.execute("CREATE DATABASE jumpStart")

def createTableSelic(database):
    mydb = mysql.connector.connect(host="localhost",user="root",password="",database=database)
    mycursor = mydb.cursor()
    mycursor.execute("CREATE TABLE tb_selic (id INT AUTO_INCREMENT PRIMARY KEY, date DATE, value FLOAT)")

def createTableCryptos(database):
    mydb = mysql.connector.connect(host="localhost",user="root",password="",database=database)
    mycursor = mydb.cursor()
    mycursor.execute("CREATE TABLE tb_crypto (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), date DATE, high FLOAT, low FLOAT, vol FLOAT, last FLOAT, sell FLOAT, buy FLOAT)")

def createTableCoins(database):
    mydb = mysql.connector.connect(host="localhost",user="root",password="",database=database)
    mycursor = mydb.cursor()
    mycursor.execute("CREATE TABLE tb_coins (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), date DATE, high FLOAT, low FLOAT, bid FLOAT, ask FLOAT)")

def createTableActions(database):
    mydb = mysql.connector.connect(host="localhost",user="root",password="",database=database)
    mycursor = mydb.cursor()
    mycursor.execute("CREATE TABLE tb_acoes (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), date DATE,open FLOAT, high FLOAT, low FLOAT, close FLOAT, volume FLOAT)")    

