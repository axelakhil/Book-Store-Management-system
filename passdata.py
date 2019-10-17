import mysql.connector
#######################   CONNECTING TO THE DATABASE NAMED BOOKS   ##############################################################
mydb = mysql.connector.connect(host="localhost", user="admin", passwd="root", database="books")
mycursor = mydb.cursor()

#######   ALREADY COMMITED DATA  #####################################

# self.mycursor.execute("Create TABLE pass(Username VARCHAR(255),Password VARCHAR(255))")
# self.mycursor.execute("INSERT INTO pass VALUES('AKHIL RANA','SUDO')")ru
# self.mydb.commit()


#######READ FUNCTION TO CHECK THE VALIDITY OF ENTERED CREDENTIALS##############################################################

def read(un,passw):
#verifying the login details
        mycursor.execute("SELECT * FROM pass WHERE Username=%s and Password=%s", (un, passw))
        b=mycursor.fetchall()
        if(b==[]):
            return False
        else:
            return True

def signup(un,passw,ms):
    mycursor.execute("select * from pass where Username=%s",(un,))
    b=mycursor.fetchall()

    if(b==[] and ms=='123456A'):
        mycursor.execute("INSERT INTO pass VALUES(%s,%s)", (un,passw,))
        mydb.commit()
        return True
    else:
        return False




