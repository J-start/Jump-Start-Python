import mysql.connector

from common.dataBaseCredentials import HOST_DATABASE,USER_DATABASE,PASSWORD_DATABASE,NAME_DATABASE,PORT_DATABASE

def getNameAsset(dataBase):
    mydb = mysql.connector.connect(host=HOST_DATABASE,port=PORT_DATABASE,user=USER_DATABASE,password=PASSWORD_DATABASE,database=dataBase)
    mycursor = mydb.cursor()

    mycursor.execute("SELECT nameAsset,typeAsset FROM list_asset")

    countDataBase = mycursor.fetchall()   
    return countDataBase

def getCountNews():
   
    try:
        mydb = mysql.connector.connect(host=HOST_DATABASE,port=PORT_DATABASE,user=USER_DATABASE,password=PASSWORD_DATABASE,database=NAME_DATABASE)
        mycursor = mydb.cursor()
    
        mycursor.execute(f"SELECT COUNT(*) AS total FROM tb_news")

        countDataBase = mycursor.fetchone()
        return countDataBase[0]
    except Exception as e:
        print("Erro na contagem de noticias: ",e)
        return -1
    
def deleteNewsById(id):
   
    try:
        mydb = mysql.connector.connect(host=HOST_DATABASE,port=PORT_DATABASE,user=USER_DATABASE,password=PASSWORD_DATABASE,database=NAME_DATABASE)
        mycursor = mydb.cursor()
    
        mycursor.execute(f"DELETE FROM tb_news WHERE id={id}")
        mydb.commit()
    except Exception as e:
        print("Erro na contagem de noticias: ",e)
    
def getOldestNews():
   
    try:
        mydb = mysql.connector.connect(host=HOST_DATABASE,port=PORT_DATABASE,user=USER_DATABASE,password=PASSWORD_DATABASE,database=NAME_DATABASE)
        mycursor = mydb.cursor()
    
        mycursor.execute("SELECT id FROM tb_news LIMIT 1")

        countDataBase = mycursor.fetchone()
        return countDataBase[0]
    except Exception as e:
        print("Erro na contagem de noticias: ",e)
        return -1



