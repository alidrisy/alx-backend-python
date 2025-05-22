import sqlite3
from faker import Faker
import random


def create_and_populate_users(db_path="example.db", count=100):
    fake = Faker()
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    cursor.execute("DROP TABLE IF EXISTS users")
    cursor.execute(
        """
        CREATE TABLE users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            age INTEGER NOT NULL
        )
    """
    )

    for _ in range(count):
        name = fake.name()
        age = random.randint(18, 70)
        cursor.execute("INSERT INTO users (name, age) VALUES (?, ?)", (name, age))

    conn.commit()
    conn.close()
    print(f"{count} fake users inserted into {db_path}")


if __name__ == "__main__":
    create_and_populate_users()
