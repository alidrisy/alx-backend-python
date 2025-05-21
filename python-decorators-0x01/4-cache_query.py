#!/usr/bin/python3
"""
This script defines a decorator to establish a connection to a SQLite database and another decorator to cache query results.
It also includes a function to fetch users from the database using the provided query while utilizing caching.
"""

import time
import sqlite3
import functools


# Global dictionary to cache query results
query_cache = {}


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


def cache_query(func):
    """
    A decorator function that caches the result of a query to avoid redundant database calls.

    :param func: The function to be decorated.
    :return: The wrapper function that handles caching the query result.
    """

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        query = kwargs.get("query")
        if query is None:
            return func(*args, **kwargs)
        if query in query_cache:
            print("Returning cached data")
            return query_cache[query]
        result = func(*args, **kwargs)
        query_cache[query] = result
        return result

    return wrapper


@with_db_connection
@cache_query
def fetch_users_with_cache(conn, query):
    """
    Fetches users from the database using the provided query while utilizing caching.

    :param conn: SQLite database connection.
    :param query: SQL query to fetch users.
    :return: List of users fetched from the database.
    """
    cursor = conn.cursor()
    cursor.execute(query)
    return cursor.fetchall()


#### First call will cache the result
users = fetch_users_with_cache(query="SELECT * FROM users")

#### Second call will use the cached result
users_again = fetch_users_with_cache(query="SELECT * FROM users")
