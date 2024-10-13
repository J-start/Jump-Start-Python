import mysql.connector
from mypyc.crash import catch_errors


def insertDatasSelic(dataDase,date,value):
    mydb = mysql.connector.connect(host="localhost",user="homestead",password="secret",database=dataDase)
    mycursor = mydb.cursor()
    sql = "INSERT INTO tb_selic (date, value) VALUES (%s, %s)"
    val = (date, value)
    mycursor.execute(sql, val)

    mydb.commit()


def insertDatasCrypto(dataDase,name,date,high,low,vol,last,sell,buy):
    mydb = mysql.connector.connect(host="localhost",user="homestead",password="secret",database=dataDase)
    mycursor = mydb.cursor()
    sql = "INSERT INTO tb_crypto (name, date,high,low,vol,last,sell,buy) VALUES (%s, %s,%s, %s,%s, %s,%s, %s)"
    val = (name,date,high,low,vol,last,sell,buy)
    mycursor.execute(sql, val)

    mydb.commit()


def insertDatasCoins(dataBase,name,date,high,low,bid,ask):
    mydb = mysql.connector.connect(host="localhost",user="homestead",password="secret",database=dataBase)
    mycursor = mydb.cursor()
    sql = "INSERT INTO tb_coins (name, date,high,low,bid,ask) VALUES (%s, %s,%s, %s,%s, %s)"
    val = (name,date,high,low,bid,ask)
    try:
        mycursor.execute(sql, val)
    except Exception as e:
        print("Erro inserção moedas. Erro:", e)
    mydb.commit()

def insertDatasActions(dataDase,name,date,open,high,low,close,volume):
    mydb = mysql.connector.connect(host="localhost",user="homestead",password="secret",database=dataDase)
    mycursor = mydb.cursor()
    sql = "INSERT INTO tb_acoes (name, date,open,high,low,close,volume) VALUES (%s, %s,%s, %s,%s, %s,%s)"
    val = (name,date,open,high,low,close,volume)
    mycursor.execute(sql, val)

    mydb.commit()
    
def insertNews(dataDase,news):
    mydb = mysql.connector.connect(host="localhost",user="homestead",password="secret",database=dataDase)
    mycursor = mydb.cursor()
    mycursor.execute('''
        INSERT INTO tb_news (news) VALUES (%s)
    ''', (news,))
    mydb.commit()


def main():
    insertDatasCrypto("teste","2024-04-22",5.25,5.25,5.25,5.25,5.25,5.25)

if __name__ == "__main__":
    main()