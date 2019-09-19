import mysql.connector

mydb=mysql.connector.connect(host="localhost", user="admin", passwd="root", database="books")

mycursor= mydb.cursor()

mycursor.execute("SELECT * FROM newbook WHERE Id BETWEEN 10 AND 40")

for x in mycursor:
    print(x)