#!/usr/bin/python3
"""A module demonstrating the use of decorators for managing database transactions."""

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
        """Wrapper function that manages the database connection."""
        conn = sqlite3.connect("users.db")
        try:
            return func(conn=conn, *args, **kwargs)
        finally:
            conn.close()

    return wrapper


def transactional(func):
    """
    A decorator function that wraps the decorated function in a transaction, committing changes if successful
    or rolling back changes if an exception occurs.

    Args:
        func: The function to be decorated.

    Returns:
        The wrapper function that manages the transaction.
    """

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        conn = kwargs["conn"]
        try:
            result = func(*args, **kwargs)
            conn.commit()
            return result
        except Exception as e:
            conn.rollback()
            raise e

    return wrapper


@with_db_connection
@transactional
def update_user_email(conn, user_id, new_email):
    """Function to update a user's email in the database."""
    cursor = conn.cursor()
    cursor.execute("UPDATE users SET email = ? WHERE id = ?", (new_email, user_id))


update_user_email(user_id=120, new_email="Crawford_Cartwright@hotmail.com")
