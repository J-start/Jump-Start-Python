import mysql.connector

from common.dataBaseCredentials import HOST_DATABASE,USER_DATABASE,PASSWORD_DATABASE,NAME_DATABASE,PORT_DATABASE

def getNameAsset(dataBase):
    mydb = mysql.connector.connect(host=HOST_DATABASE,port=PORT_DATABASE,user=USER_DATABASE,password=PASSWORD_DATABASE,database=dataBase)
    mycursor = mydb.cursor()

    mycursor.execute("SELECT nameAsset,typeAsset FROM list_asset")

    countDataBase = mycursor.fetchall()   
    return countDataBase


def main():
    getNameAsset(NAME_DATABASE)

if __name__ == "__main__":
    main()

