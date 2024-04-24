import mysql.connector

def createDataBaseTest():
    mydb = mysql.connector.connect(host="localhost",user="root",password="")
    mycursor = mydb.cursor()
    mycursor.execute("CREATE DATABASE jumpStartTest")

def deleteDataBase():
    mydb = mysql.connector.connect(host="localhost",user="root",password="")
    mycursor = mydb.cursor()
    mycursor.execute("DROP DATABASE jumpStartTest")