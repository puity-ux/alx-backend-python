#!/usr/bin/python3
import mysql.connector

def stream_user_ages():
    """
    Generator that yields user ages one by one from the user_data table.
    """
    connection = mysql.connector.connect(
        host='localhost',
        user='root',
        password='your_password',  # 🔁 Replace with your MySQL password
        database='ALX_prodev'
    )
    cursor = connection.cursor()
    cursor.execute("SELECT age FROM user_data")

    for (age,) in cursor:  # ✅ Loop 1
        yield age

    cursor.close()
    connection.close()


def compute_average_age():
    """
    Computes the average age of users using the stream_user_ages generator.
    Uses no more than 2 loops and does not load all data into memory.
    """
    total_age = 0
    count = 0

    for age in stream_user_ages():  # ✅ Loop 2
        total_age += age
        count += 1

    if count == 0:
        print("No users found.")
    else:
        avg = total_age / count
        print(f"Average age of users: {avg:.2f}")
