import mysql.connector
import csv
import uuid

# ---------- Prototypes Implementations ----------

def connect_db():
    """Connects to the MySQL server (without selecting a DB)."""
    return mysql.connector.connect(
        host='localhost',
        user='root',
        password='your_password'  # Replace with your MySQL password
    )

def create_database(connection):
    """Creates the ALX_prodev database if it doesn't exist."""
    cursor = connection.cursor()
    cursor.execute("CREATE DATABASE IF NOT EXISTS ALX_prodev")
    cursor.close()

def connect_to_prodev():
    """Connects to the ALX_prodev database."""
    return mysql.connector.connect(
        host='localhost',
        user='root',
        password='your_password',  # Replace with your MySQL password
        database='ALX_prodev'
    )

def create_table(connection):
    """Creates the user_data table with required fields if not exists."""
    cursor = connection.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS user_data (
            user_id CHAR(36) PRIMARY KEY,
            name VARCHAR(255) NOT NULL,
            email VARCHAR(255) NOT NULL,
            age DECIMAL NOT NULL,
            UNIQUE(email)
        )
    """)
    cursor.close()

def insert_data(connection, data):
    """Inserts user data if the email does not already exist."""
    cursor = connection.cursor()
    for name, email, age in data:
        try:
            cursor.execute("""
                INSERT INTO user_data (user_id, name, email, age)
                VALUES (%s, %s, %s, %s)
            """, (str(uuid.uuid4()), name, email, age))
        except mysql.connector.IntegrityError:
            print(f"Duplicate skipped: {email}")
    connection.commit()
    cursor.close()

def read_csv_data(file_path):
    """Reads and yields rows from a CSV file (excluding the header)."""
    with open(file_path, newline='') as csvfile:
        reader = csv.reader(csvfile)
        next(reader)  # skip header
        for row in reader:
            yield row[0], row[1], row[2]  # name, email, age

# ---------- Main Script ----------

if __name__ == "__main__":
    # Step 1: Connect and create database
    root_conn = connect_db()
    create_database(root_conn)
    root_conn.close()

    # Step 2: Connect to ALX_prodev
    db_conn = connect_to_prodev()

    # Step 3: Create table
    create_table(db_conn)

    # Step 4: Load and insert CSV data
    csv_path = "user_data.csv"  # Make sure this file exists in the same directory
    data = read_csv_data(csv_path)
    insert_data(db_conn, data)

    print("Database seeded successfully.")
    db_conn.close()
