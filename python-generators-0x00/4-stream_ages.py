#!/usr/bin/python3

"""
This script contains a generator function that streams user ages from a MySQL database.
"""

import seed


def stream_user_ages():
    """
    Generator that streams user ages from the database.
    """
    connection = seed.connect_to_prodev()
    cursor = connection.cursor(dictionary=True)
    cursor.execute("SELECT age FROM user_data")
    for row in cursor:
        yield row["age"]
    connection.close()
    cursor.close()


def main():
    """
    Main function to demonstrate the usage of the stream_user_ages generator.
    """
    average_age = 0
    num_users = 0
    ages = stream_user_ages()
    for age in ages:
        average_age += age
        num_users += 1
    if num_users > 0:
        average_age /= num_users
    print(f"Average age of users: {average_age}")


if __name__ == "__main__":
    main()
