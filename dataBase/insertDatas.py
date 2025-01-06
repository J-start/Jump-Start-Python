import mysql.connector
from datetime import datetime
from common.dataBaseCredentials import HOST_DATABASE,USER_DATABASE,PASSWORD_DATABASE,NAME_DATABASE,PORT_DATABASE

def insertDatasActions(dataDase,name,date,open,high,low,close,volume):
    mydb = mysql.connector.connect(host=HOST_DATABASE,port=PORT_DATABASE,user=USER_DATABASE,password=PASSWORD_DATABASE,database=dataDase)
    mycursor = mydb.cursor()
    sql = "INSERT INTO tb_share (nameShare, dateShare, openShare, highShare, lowShare, closeShare, volumeShare) VALUES (%s, %s,%s, %s,%s, %s,%s)"
    val = (name,date,open,high,low,close,volume)
    mycursor.execute(sql, val)

    mydb.commit()
    
def insertNews(dataDase,news,dateNews):
    mydb = mysql.connector.connect(host=HOST_DATABASE,port=PORT_DATABASE,user=USER_DATABASE,password=PASSWORD_DATABASE,database=dataDase)
    dateActual = datetime.now()
    dateFormatedSQL = dateActual.strftime('%Y-%m-%d')
    mycursor = mydb.cursor()
    mycursor.execute('''
        INSERT INTO tb_news (news,dateNews,datePublished,isApproved) VALUES (%s,%s,%s,%s)
    ''', (news,dateFormatedSQL,dateNews,True))
    mydb.commit()

