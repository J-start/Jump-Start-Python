import mysql.connector

def insertDatasSelic(date,value):
    mydb = mysql.connector.connect(host="localhost",user="root",password="",database="jumpStart")
    mycursor = mydb.cursor()
    sql = "INSERT INTO tb_selic (date, value) VALUES (%s, %s)"
    val = (date, value)
    mycursor.execute(sql, val)

    mydb.commit()

    print(mycursor.rowcount, "record inserted.")

def main():
    insertDatasSelic("2024-04-22",5.25)

if __name__ == "__main__":
    main()