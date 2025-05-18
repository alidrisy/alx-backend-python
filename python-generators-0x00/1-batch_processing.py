#!/usr/bin/python3
"""Module for streaming users in batches from a MySQL database and processing them."""

import seed


def stream_users_in_batches(batch_size):
    """
    Generator function to stream users in batches from a MySQL database.

    Args:
    batch_size (int): The size of each batch to fetch from the database.

    Yields:
    list: A list of dictionaries representing user data in each batch.
    """
    connection = seed.connect_to_prodev()
    cursor = connection.cursor(dictionary=True)
    cursor.execute("SELECT * FROM user_data")
    while True:
        batch = cursor.fetchmany(batch_size)
        if not batch:
            break
        yield batch

    cursor.close()
    connection.close()


def batch_processing(batch_size):
    """
    Process users in batches based on the given batch size.

    Args:
    batch_size (int): The size of each batch for processing users.
    """
    batches = stream_users_in_batches(batch_size)
    for batch in batches:
        for user in batch:
            if user.get("age", 0) > 25:
                print(user)
