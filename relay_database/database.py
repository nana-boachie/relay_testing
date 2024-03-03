#create a database file
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="relayuser",
  password="TAIL",
  database="relaydatabase"
)

mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM customers")

results = mycursor.fetchall()

# work with results
