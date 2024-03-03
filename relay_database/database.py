import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="yiadom",
    password="12345678"
    )

mycursor = mydb.cursor()
mycursor.execute("CREATE DATABASE relay_databasev1")