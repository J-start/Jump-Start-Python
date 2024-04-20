import mysql.connector


def createConnection():
    mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="testfronta"
    )

