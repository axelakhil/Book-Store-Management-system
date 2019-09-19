import mysql.connector
#######################   CONNECTING TO THE DATABASE NAMED BOOKS   ##############################################################
mydb = mysql.connector.connect(host="localhost", user="admin", passwd="root", database="books")
mycursor = mydb.cursor()

#######   ALREADY COMMITED DATA  #####################################

# self.mycursor.execute("Create TABLE pass(Username VARCHAR(255),Password VARCHAR(255))")
# self.mycursor.execute("INSERT INTO pass VALUES('AKHIL RANA','SUDO')")
# self.mydb.commit()

#GLOBAL VARIABLES FOR USERID AND PASSWORD

username=""
passcode=""

#######READ FUNCTION TO CHECK THE VALIDITY OF ENTERED CREDENTIALS##############################################################

def read(un,passw):
# GETTING UN ,PASSW FROM LOGIN PAGE ENTRIES
    global passcode
    global username
    # CODE TO CHECK WHETEHR CREDENTIALS EXIST IN THE SYSTEM OR NOT
    try:
        mycursor.execute("SELECT * FROM pass WHERE Username=%s and Password=%s", (un, passw))
        for x in mycursor:
            u = list(x)
        #RETURNING AND ASSIGNING THE CREDENTIALS AFTER VERIFICATION FROM DATABASE
        username = u[0]
        passcode = u[1]
        return True
    except:
        #IF CREDENTIALS DON'T MATCH WITH THE DATABASE COMBINATION
        return False






