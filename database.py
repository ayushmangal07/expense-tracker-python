import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="your_password",
    database="EXPENSE_TRACKER"
)

cursor = conn.cursor()