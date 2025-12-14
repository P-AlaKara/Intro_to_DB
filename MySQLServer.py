import mysql.connector

try:
    db = mysql.connector.connect(
        host="localhost",
        user="root",
        password="200303"
    )

    cursor = db.cursor()
    cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
    print("Database 'alx_book_store' created successfully!")

except mysql.connector.Error as e:
    print(f"Error while connecting to MySQL: {e}")

finally:
    if 'cursor' in locals():
        cursor.close()
    if 'db' in locals() and db.is_connected():
        db.close()
