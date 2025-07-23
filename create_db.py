import pymysql
mydatabase = pymysql.connect(
    host="localhost",
    user="root",
    password="1234"
)
mycursor = mydatabase.cursor()
mycursor.execute("CREATE DATABASE IF NOT EXISTS students_db")
mycursor.execute("SHOW DATABASES")
for db in mycursor:
    print(db)
