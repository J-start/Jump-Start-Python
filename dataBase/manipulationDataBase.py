import mysql.connector


def createConnection():
    mydb = mysql.connector.connect(host="localhost",user="homestead",password="secret")
    myCursor = mydb.cursor()
    return "sucesso"

def createDataBase():
    mydb = mysql.connector.connect(host="localhost",user="homestead",password="secret")
    mycursor = mydb.cursor()
    mycursor.execute("CREATE DATABASE jumpStart")


def createTableSelic(database):
    mydb = mysql.connector.connect(host="localhost",user="homestead",password="secret",database=database)
    mycursor = mydb.cursor()
    mycursor.execute("CREATE TABLE tb_selic  (id INT AUTO_INCREMENT PRIMARY KEY, dateSelic DATE, valueSelic FLOAT)")

def createTableCryptos(database):
    mydb = mysql.connector.connect(host="localhost",user="homestead",password="secret",database=database)
    mycursor = mydb.cursor()
    mycursor.execute("CREATE TABLE tb_crypto (id INT AUTO_INCREMENT PRIMARY KEY, nameCrypto VARCHAR(255), date DATE, highCrypto FLOAT, lowCrypto FLOAT, volCrypto FLOAT, lastCrypto FLOAT, sellCrypto FLOAT, buyCrypto FLOAT)")

def createTableCoins(database):
    mydb = mysql.connector.connect(host="localhost",user="homestead",password="secret",database=database)
    mycursor = mydb.cursor()
    mycursor.execute("CREATE TABLE tb_coins  (id INT AUTO_INCREMENT PRIMARY KEY, nameCoin VARCHAR(255), dateCoin DATE, highCoin FLOAT, lowCoin FLOAT, bidCoin FLOAT, askCoin FLOAT)")

def createTableActions(database):
    mydb = mysql.connector.connect(host="localhost",user="homestead",password="secret",database=database)
    mycursor = mydb.cursor()
    mycursor.execute("CREATE TABLE tb_share  (id INT AUTO_INCREMENT PRIMARY KEY, nameShare VARCHAR(255), dateShare DATE,openShare FLOAT, highShare FLOAT, lowShare FLOAT, closeShare FLOAT, volumeShare FLOAT)")

def createTableNews(database):
    mydb = mysql.connector.connect(host="localhost",user="homestead",password="secret",database=database)
    mycursor = mydb.cursor()
    mycursor.execute("CREATE TABLE tb_news (id INT AUTO_INCREMENT PRIMARY KEY, news VARCHAR(300), dateNews DATE, isApproved BOOLEAN)")

def main():
    createTableSelic("jumpStart")
    createTableCryptos("jumpStart")
    createTableCoins("jumpStart")
    createTableActions("jumpStart")
    createTableNews("jumpStart")

if __name__ == "__main__":
    main()