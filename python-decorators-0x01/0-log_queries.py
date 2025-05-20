#!/usr/bin/python3
"""
This module contains a decorator `log_queries` for logging function arguments and a function `fetch_all_users` to fetch user data from a SQLite database.
"""
import sqlite3
import functools
from datetime import datetime

def log_queries(func):
    """
    A decorator that logs the arguments passed to the decorated function.

    Args:
        func (callable): The function to be decorated.

    Returns:
        callable: The wrapped function with logging functionality.
    """
    def wrapper(*args, **kwargs):
        if args:
            print("Positional arguments:", args, "at", datetime.now().isoformat())
        if kwargs:
            print("Keyword arguments:", kwargs, "at", datetime.now().isoformat())
        return func(*args, **kwargs)
    return wrapper


@log_queries
def fetch_all_users(query):
    """
    Fetches all users from the database based on the provided SQL query.

    Args:
        query (str): The SQL query to execute.

    Returns:
        list: A list of tuples containing the query results.
    """
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute(query)
    results = cursor.fetchall()
    conn.close()
    return results

# Example usage
users = fetch_all_users(query="SELECT * FROM users")
