#!/usr/bin/python3
""" """

import time
import sqlite3
import functools


def with_db_connection(func):
    """
    A decorator function that establishes a connection to a SQLite database named 'users.db',
    calls the decorated function with the connection as the first argument, and then closes the connection.
    """

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        conn = sqlite3.connect("users.db")
        try:
            return func(conn=conn, *args, **kwargs)
        finally:
            conn.close()

    return wrapper


def retry_on_failure(retries=3, delay=1):
    """
    A decorator factory that retries the decorated function on failure.

    Args:
        retries (int): Number of retry attempts
        delay (int or float): Delay in seconds between retries
    """

    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            attempt = 0
            while attempt < retries:
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    attempt += 1
                    if attempt >= retries:
                        print(f"All {retries} attempts failed.")
                        raise
                    print(
                        f"Attempt {attempt} failed with error: {e}. Retrying in {delay} seconds..."
                    )
                    time.sleep(delay)

        return wrapper

    return decorator


@with_db_connection
@retry_on_failure(retries=3, delay=1)
def fetch_users_with_retry(conn):
    """
    Fetches all users from the database with retry mechanism in case of failure.

    Args:
    conn: Connection object to the database.

    Returns:
        List of tuples representing the users fetched from the database.
    """
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users")
    return cursor.fetchall()


# Run the function
users = fetch_users_with_retry()
print(users)
