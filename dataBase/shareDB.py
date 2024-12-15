import mysql.connector

from common.dataBaseCredentials import HOST_DATABASE,USER_DATABASE,PASSWORD_DATABASE,NAME_DATABASE

def getListShare(dataBase):
    mydb = mysql.connector.connect(host=HOST_DATABASE,user=USER_DATABASE,password=PASSWORD_DATABASE,database=dataBase)
    mycursor = mydb.cursor()

    mycursor.execute("SELECT acronymAsset FROM list_asset WHERE typeAsset = 'SHARE'")

    countDataBase = mycursor.fetchall()   
    return countDataBase


