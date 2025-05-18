#!/usr/bin/python3
"""
This module contains a generator function that streams user data from the database.
"""
import seed


def stream_users():
    """
    Generator function that streams user data from the database.

    Yields:
    - tuple: A row of user data from the database.
    """
    connection = seed.connect_to_prodev()
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM user_data")
    while True:
        row = cursor.fetchone()
        if row is None:
            break
        yield row
