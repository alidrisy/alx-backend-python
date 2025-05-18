#!/usr/bin/python3
"""
This script contains functions to interact with a MySQL database, including connecting to the database, creating a database, creating a table, and inserting data from a CSV file into the database table.
"""

import mysql.connector
import csv
import uuid


def connect_db():
    """
    Connects to the database and returns the connection object.

    Returns:
    conn: A connection object to interact with the database.
    """
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="abd727868",
    )
    return conn


def create_database(connection):
    """
    Create a database using the provided connection.

    Args:
    connection: The connection object to the database.

    Returns:
    None
    """
    cursor = connection.cursor()
    cursor.execute("CREATE DATABASE IF NOT EXISTS ALX_prodev")
    cursor.close()


def connect_to_prodev():
    """
    Connects to the ALX_prodev database using MySQL.

    Returns:
    MySQL connection object: Connection to the ALX_prodev database.
    """
    conn = mysql.connector.connect(
        host="localhost",  # or your MySQL server IP
        user="root",  # your MySQL username
        password="abd727868",  # your MySQL password
        database="ALX_prodev",
    )
    return conn


def create_table(connection):
    """
    Create a table named user_data in the database using the provided connection.

    Args:
    connection: The connection object to the database.

    Returns:
    None
    """
    cursor = connection.cursor()
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS user_data (
            user_id CHAR(36) PRIMARY KEY,
            name VARCHAR(255) NOT NULL,
            email VARCHAR(255) NOT NULL,
            age DECIMAL NOT NULL,
            INDEX(user_id)
        )
    """
    )
    print("Table user_data created successfully")
    cursor.close()


import csv
import uuid


def insert_data(connection, data):
    """
    Insert data from a CSV file into a database table.

    Args:
    connection: A connection object to the database.
    data: Path to the CSV file containing the data to be inserted.

    Returns:
    None
    """
    cursor = connection.cursor()
    with open(data) as csv_file:
        reader = csv.DictReader(csv_file)
        for row in reader:
            user_id = str(uuid.uuid4())
            cursor.execute(
                """
            INSERT INTO user_data (user_id, name, email, age) VALUES (%s, %s, %s, %s)
            """,
                (user_id, row["name"], row["email"], row["age"]),
            )
    connection.commit()
    cursor.close()
