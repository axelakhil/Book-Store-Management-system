import mysql.connector
import operation_sdu as sdu
mydb=mysql.connector.connect(host="localhost", user="admin", passwd="root", database="books")

mycursor= mydb.cursor()


def existing(title):
         try:
             mycursor.execute("select * from newbook where title=%s", (title,))
             return True
         except:
             return False


