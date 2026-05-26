import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="university_db"
)
cursor = conn.cursor()
print("✅ Database Connected!")