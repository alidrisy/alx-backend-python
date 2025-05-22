import sqlite3


class DatabaseConnection:
    def __init__(self, db_name, engin):
        self.db_name = db_name
        self.engin = engin

    def __enter__(self):
        self.conn = self.engin.connect(self.db_name)
        self.cursor = self.conn.cursor()
        return self.cursor

    def __exit__(self, exc_type, exc_value, traceback):
        if exc_type:
            self.conn.rollback()
        else:
            self.conn.commit()
        self.cursor.close()
        self.conn.close()


# Usage
with DatabaseConnection("users.db", sqlite3) as db:
    db.execute("SELECT * FROM users")
    users = db.fetchall()
    print(users)
