import sqlite3


class ExecuteQuery:
    def __init__(self, query, params=None, db_path="example.db"):
        self.query = query
        self.params = params or []
        self.db_path = db_path

    def __enter__(self):
        self.conn = sqlite3.connect(self.db_path)
        self.cursor = self.conn.cursor()
        try:
            self.cursor.execute(self.query, self.params)
            self.results = self.cursor.fetchall()
        except sqlite3.DatabaseError as e:
            self.conn.rollback()
            raise e
        return self.results

    def __exit__(self, exc_type, exc_value, traceback):
        self.cursor.close()
        self.conn.close()


query = "SELECT * FROM users WHERE age > ?"
params = [25]

with ExecuteQuery(query, params) as results:
    for row in results:
        print(row)
