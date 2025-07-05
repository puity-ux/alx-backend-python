#!/usr/bin/python3
import mysql.connector

def stream_users_in_batches(batch_size):
    """
    Generator that yields user_data rows in batches from the ALX_prodev database.
    :param batch_size: Number of rows to fetch per batch
    """
    connection = mysql.connector.connect(
        host='localhost',
        user='root',
        password='your_password',  # 🔁 Replace with your actual MySQL password
        database='ALX_prodev'
    )
    cursor = connection.cursor()
    cursor.execute("SELECT user_id, name, email, age FROM user_data")

    while True:
        batch = cursor.fetchmany(batch_size)
        if not batch:
            break
        yield batch

    cursor.close()
    connection.close()


def batch_processing(batch_size):
    """
    Generator that processes batches and yields users over age 25.
    :param batch_size: Number of rows per batch
    """
    for batch in stream_users_in_batches(batch_size):  # Loop 1
        # Process and yield users over age 25
        yield [user for user in batch if user[3] > 25]  # Loop 2 (implicit in list comprehension)
