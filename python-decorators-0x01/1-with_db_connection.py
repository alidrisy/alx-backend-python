#!/usr/bin/python3
"""
This script defines a decorator function 'with_db_connection' that establishes a connection to a SQLite database named 'users.db',
calls the decorated function with the connection as the first argument, and then closes the connection.
It also includes a function 'get_user_by_id' that fetches a user from the 'users' table in the database by their ID.
"""

import sqlite3
import functools


def with_db_connection(func):
    """
    A decorator function that establishes a connection to a SQLite database named 'users.db',
    calls the decorated function with the connection as the first argument, and then closes the connection.

    Args:
        func: The function to be decorated.

    Returns:
        The wrapper function that manages the database connection.
    """

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        """ """
        conn = sqlite3.connect("users.db")
        try:
            return func(conn, *args, **kwargs)
        finally:
            conn.close()

    return wrapper


@with_db_connection
def get_user_by_id(conn, user_id):
    """ """
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE id = ?", (user_id,))
    return cursor.fetchone()


#### Fetch user by ID with automatic connection handling

user = get_user_by_id(user_id=12)
print(user)
