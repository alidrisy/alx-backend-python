#!/usr/bin/python3
import seed


def stream_users_in_batches(batch_size):
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
    batches = stream_users_in_batches(batch_size)
    for batch in batches:
        for user in batch:
            if user.get("age", 0) > 25:
                print(user)
