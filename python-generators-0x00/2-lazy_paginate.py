#!/usr/bin/python3
import mysql.connector

def paginate_users(page_size, offset):
    """
    Fetch a single page of users starting from the given offset.
    Returns a list of user rows up to `page_size` rows.
    """
    connection = mysql.connector.connect(
        host='localhost',
        user='root',
        password='your_password',  # 🔁 Replace with your MySQL password
        database='ALX_prodev'
    )
    cursor = connection.cursor()
    query = """
        SELECT user_id, name, email, age
        FROM user_data
        ORDER BY user_id
        LIMIT %s OFFSET %s
    """
    cursor.execute(query, (page_size, offset))
    rows = cursor.fetchall()
    cursor.close()
    connection.close()
    return rows


def lazy_paginate(page_size):
    """
    Generator that yields pages of user data lazily, one page at a time.
    Only fetches the next page when needed.
    Uses only one loop.
    """
    offset = 0
    while True:  # ✅ Only loop used
        page = paginate_users(page_size, offset)
        if not page:
            break
        yield page
        offset += page_size
