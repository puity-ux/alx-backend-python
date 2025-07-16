#!/usr/bin/python3
import mysql.connector

def stream_users():
    """Yields rows one by one from the user_data table in ALX_prodev database."""
    connection = mysql.connector.connect(
        host='localhost',
        user='root',
        password='your_password',       # 🔁 Replace with your actual MySQL password
        database='ALX_prodev'
    )

    cursor = connection.cursor()
    cursor.execute("SELECT user_id, name, email, age FROM user_data")
    
    # ✅ Yield one row at a time using a single loop
    for row in cursor:
        yield row

    cursor.close()
    connection.close()
