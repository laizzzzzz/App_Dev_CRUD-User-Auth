import mysql.connector

database = mysql.connector.connect(
    host='localhost',
    user='root',
    passwd=''
)

# prepare a cursor object
cursorObject = database.cursor()

# create a database
cursorObject.execute("CREATE DATABASE WebsiteKo_db")

print("Sheesh!! Done creating the database.")