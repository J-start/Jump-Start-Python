import mysql.connector
from datetime import datetime


def insertDatasSelic(dataDase,date,value):
    mydb = mysql.connector.connect(host="localhost",user="homestead",password="secret",database=dataDase)
    mycursor = mydb.cursor()
    sql = "INSERT INTO tb_selic (dateSelic, valueSelic) VALUES (%s, %s)"
    val = (date, value)
    mycursor.execute(sql, val)

    mydb.commit()


def insertDatasCrypto(dataDase,name,date,high,low,vol,last,sell,buy):
    mydb = mysql.connector.connect(host="localhost",user="homestead",password="secret",database=dataDase)
    mycursor = mydb.cursor()
    sql = "INSERT INTO tb_crypto (nameCrypto, date, highCrypto, lowCrypto, volCrypto, lastCrypto, sellCrypto, buyCrypto) VALUES (%s, %s,%s, %s,%s, %s,%s, %s)"
    val = (name,date,high,low,vol,last,sell,buy)
    mycursor.execute(sql, val)

    mydb.commit()


def insertDatasCoins(dataBase,name,date,high,low,bid,ask):
    mydb = mysql.connector.connect(host="localhost",user="homestead",password="secret",database=dataBase)
    mycursor = mydb.cursor()
    sql = "INSERT INTO tb_coins (nameCoin, dateCoin, highCoin, lowCoin, bidCoin, askCoin) VALUES (%s, %s,%s, %s,%s, %s)"
    val = (name,date,high,low,bid,ask)
    try:
        mycursor.execute(sql, val)
    except Exception as e:
        print("Erro inserção moedas. Erro:", e)
    mydb.commit()

def insertDatasActions(dataDase,name,date,open,high,low,close,volume):
    mydb = mysql.connector.connect(host="localhost",user="homestead",password="secret",database=dataDase)
    mycursor = mydb.cursor()
    sql = "INSERT INTO tb_share (nameShare, dateShare, openShare, highShare, lowShare, closeShare, volumeShare) VALUES (%s, %s,%s, %s,%s, %s,%s)"
    val = (name,date,open,high,low,close,volume)
    mycursor.execute(sql, val)

    mydb.commit()
    
def insertNews(dataDase,news):
    dateActual = datetime.now()
    dateFormatedSQL = dateActual.strftime('%Y-%m-%d')
    mydb = mysql.connector.connect(host="localhost",user="homestead",password="secret",database=dataDase)
    mycursor = mydb.cursor()
    mycursor.execute('''
        INSERT INTO tb_news (news,dateNews,isApproved) VALUES (%s,%s,%s)
    ''', (news,dateFormatedSQL,False))
    mydb.commit()


def main():
    insertDatasCrypto("teste","2024-04-22",5.25,5.25,5.25,5.25,5.25,5.25)

if __name__ == "__main__":
    main()