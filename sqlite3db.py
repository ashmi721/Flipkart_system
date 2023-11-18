import sqlite3
import sys

class SqliteDBhelper:
    def __init__(self):
        try:
            self.conn = sqlite3.connect("flip.db")
            self.cur = self.conn.cursor()
        except Exception as e:
            print(f"Error connecting to the database: {e}")
            sys.exit(1)
        else:
            print("Connected to Database")

    def create_users_table(self):
        try:
            self.cur.execute('''CREATE TABLE IF NOT EXISTS users(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                email TEXT NOT NULL,
                address TEXT NOT NULL,
                password TEXT NOT NULL
            )''')
            self.conn.commit()
        except Exception as e:
            print(f"Error creating table: {e}")

    def register(self, name, email, address, password):
        try:
            self.cur.execute("""
            INSERT INTO users (id, name, email, address, password) VALUES (NULL, ?, ?, ?,?)
            """, (name, email,address, password))
            self.conn.commit()
        except Exception as e:
            print(f"Error during registration: {e}")
            return -1
        else:
            return 1

    def search(self, email, password):
        self.cur.execute("""
            SELECT * FROM users WHERE email = ? AND password = ?
        """, (email, password))
        data = self.cur.fetchall()
        return data

 
