import mysql.connector
import pyarduino
import user_password
from hashlib import sha256

mydb = mysql.connector.connect(
    host="localhost",
    user=user_password.userU(),  #change the user
    password=user_password.userPass(),  #change the password
    database="ProjectPAM")
mycursor = mydb.cursor()

def isLoged(userId):
    sql = "SELECT * FROM devices where device_id = %s;"
    adr = (userId, )
    mycursor.execute(sql,adr)
    myresult = mycursor.fetchall()
    if len(myresult) == 0:#Len is 0 if there is not
        return False
    else:
        #ban = isBanned(myresult)#Check if the device is banned
        #if ban:
        #    return False
        return True
    #return False

def isBanned(userId):
    sql = "SELECT device_banned FROM devices where device_id = %s;"
    adr = (userId, )
    mycursor.execute(sql,adr)
    myresult = mycursor.fetchall()
    if myresult[0][0]:
        return True#IS BANNED
    else:
        return False# IS NOT BANNED
    
    #if user[0][2]:
    #    return True#True is banned
    #return False#False is not banned

def newUser(userId, name):
    mycursor.execute("INSERT INTO devices (`device_id`,`owner_name`) VALUES (%s, %s);",(int(userId), name))
    mydb.commit()
    print("User inserted")

def insertToDb(title,userId,desc):  #This insert to table records
    mycursor.execute("INSERT INTO records (`title`,`device_id`,`desc`) VALUES (%s,%s,%s);",(title,int(userId),desc))
    mydb.commit()
    print("Record inserted")

######################################################

def filterCommand(text, userId):
    if text[0] != '/':
        return "Is not a command"
    else:
        if text == "/ledon":
            ledOn("Led ON",userId,"From telegram, led on")
            return "Led ON"
        elif text == "/ledoff":
            ledOff("Led OFF",userId,"From telegram, led off")
            return "Led OFF"

def filterLogin(text):
    if text == "/login":
        return True
    else:
        return False

def login(cnt):
    hashed = sha256(cnt.encode('utf-8')).hexdigest()
    if hashed == '5e884898da28047151d0e56f8dc6292773603d0d6aabbdd62a11ef721d1542d8':#password
        return True
    else:
        return False

################################################

def ledOn(x,u,y):
    pyarduino.ledOn()
    insertToDb(x,u,y)


def ledOff(x,u,y):
    pyarduino.ledOff()
    insertToDb(x,u,y)
################################################