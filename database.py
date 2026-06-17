import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="qwer1234",
    database="EXPENSE_TRACKER"
)

cursor = conn.cursor()