import sqlite3

database = "bank.db"

# create the database connection


def get_connection():
    connection = sqlite3.connect(database)
    return connection


def create_tables():
    connection = get_connection()  # connect to the database

    # an object that python uses to interact with the database
    cursor = connection.cursor()

# using cursor to create the database tables

    cursor.execute("""
CREATE TABLE IF NOT EXISTS users(
id INTEGER PRIMARY KEY AUTOINCREMENT,
full_name TEXT NOT NULL,
email TEXT NOT NULL UNIQUE,
password TEXT NOT NULL,
balance REAL DEFAULT 0)
    """)
    connection.commit()  # save the changes
    connection.close()
