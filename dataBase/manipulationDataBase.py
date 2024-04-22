import mysql.connector


def createConnection():
    mydb = mysql.connector.connect(host="localhost",user="root",password="")
    return mydb.cursor()

def createDataBase():
    mydb = mysql.connector.connect(host="localhost",user="root",password="")
    mycursor = mydb.cursor()
    mycursor.execute("CREATE DATABASE jumpStart")

def createTableSelic():
    mydb = mysql.connector.connect(host="localhost",user="root",password="",database="jumpStart")
    mycursor = mydb.cursor()
    mycursor.execute("CREATE TABLE tb_selic (id INT AUTO_INCREMENT PRIMARY KEY, date DATE, value FLOAT)")

def createTableCryptos():
    mydb = mysql.connector.connect(host="localhost",user="root",password="",database="jumpStart")
    mycursor = mydb.cursor()
    mycursor.execute("CREATE TABLE tb_crypto (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), date DATE, high FLOAT, low FLOAT, vol FLOAT, last FLOAT, sell FLOAT, buy FLOAT)")

def createTableCoins():
    mydb = mysql.connector.connect(host="localhost",user="root",password="",database="jumpStart")
    mycursor = mydb.cursor()
    mycursor.execute("CREATE TABLE tb_coins (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), date DATE, high FLOAT, low FLOAT, bid FLOAT, ask FLOAT)")

def createTableActions():
    mydb = mysql.connector.connect(host="localhost",user="root",password="",database="jumpStart")
    mycursor = mydb.cursor()
    mycursor.execute("CREATE TABLE tb_acoes (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), date DATE,open FLOAT, high FLOAT, low FLOAT, close FLOAT, volume FLOAT)")    

def main():
    createTableActions()

if __name__ == "__main__":
    main()