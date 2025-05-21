# users_generator_with_query_logger.py

import sqlite3
import functools


# Create fake users for demonstration purposes
def create_fake_users():
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            email TEXT
        )
    """
    )
    fake_users = [
        ("Alice Johnson", "alice@example.com"),
        ("Bob Smith", "bob@example.com"),
        ("Charlie Brown", "charlie@example.com"),
        ("Diana Prince", "diana@example.com"),
        ("Ethan Hunt", "ethan@example.com"),
    ]
    cursor.executemany("INSERT INTO users (name, email) VALUES (?, ?)", fake_users)
    conn.commit()
    conn.close()


create_fake_users()
