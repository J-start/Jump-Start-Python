import mysql.connector

def insertDatasSelic(date,value):
    mydb = mysql.connector.connect(host="localhost",user="root",password="",database="jumpStart")
    mycursor = mydb.cursor()
    sql = "INSERT INTO tb_selic (date, value) VALUES (%s, %s)"
    val = (date, value)
    mycursor.execute(sql, val)

    mydb.commit()


def insertDatasCrypto(name,date,high,low,vol,last,sell,buy):
    mydb = mysql.connector.connect(host="localhost",user="root",password="",database="jumpStart")
    mycursor = mydb.cursor()
    sql = "INSERT INTO tb_crypto (name, date,high,low,vol,last,sell,buy) VALUES (%s, %s,%s, %s,%s, %s,%s, %s)"
    val = (name,date,high,low,vol,last,sell,buy)
    mycursor.execute(sql, val)

    mydb.commit()


def insertDatasCoins(name,date,high,low,bid,ask):
    mydb = mysql.connector.connect(host="localhost",user="root",password="",database="jumpStart")
    mycursor = mydb.cursor()
    sql = "INSERT INTO tb_coins (name, date,high,low,bid,ask) VALUES (%s, %s,%s, %s,%s, %s)"
    val = (name,date,high,low,bid,ask)
    mycursor.execute(sql, val)

    mydb.commit()

def insertDatasActions(name,date,open,high,low,close,volume):
    mydb = mysql.connector.connect(host="localhost",user="root",password="",database="jumpStart")
    mycursor = mydb.cursor()
    sql = "INSERT INTO tb_acoes (name, date,open,high,low,close,volume) VALUES (%s, %s,%s, %s,%s, %s,%s)"
    val = (name,date,open,high,low,close,volume)
    mycursor.execute(sql, val)

    mydb.commit()


def main():
    insertDatasCrypto("teste","2024-04-22",5.25,5.25,5.25,5.25,5.25,5.25)

if __name__ == "__main__":
    main()