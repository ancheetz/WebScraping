import mysql
import mysql.connector

db = mysql.connector.connect(host="localhost", user="andrea", password="Star1982")
print(db)