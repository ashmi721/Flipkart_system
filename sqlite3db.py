import sqlite3
import sys

class SqliteDBhelper:
    def __init__(self):
        self.conn = None
        self.cur = None
        self.connect()

    def connect(self):
        self.conn = sqlite3.connect("flip.db")
        self.cur = self.conn.cursor()
        self.create_users_table()

    def create_users_table(self):
        try:
            self.cur.execute('''CREATE TABLE IF NOT EXISTS users(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                email TEXT NOT NULL,
                gender TEXT NOT NULL, 
                password TEXT NOT NULL
            )''')
            self.conn.commit()
        except Exception as e:
            print(f"Error creating table: {e}")


    def register(self, name, email, address, password):
        try:
            self.cur.execute("""
            INSERT INTO users (id, name, email,gender, password) VALUES (NULL, ?, ?, ?,?)
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
    def update_user(self, user_id, new_name, new_email, new_gender):
            try:
                self.cur.execute("""
                    UPDATE users 
                    SET name = ?, email = ?, gender = ? 
                    WHERE id = ?
                """, (new_name, new_email, new_gender, user_id))
                self.conn.commit()
                return True
            except Exception as e:
                print(f"Error updating user: {e}")
                return False    
        
    def delete_user(self,user_id):
        try:
            self.cur.execute("""
                    DELETE FROM users WHERE id = ?        
                            
                """,(user_id,))
            self.conn.commit()
            return True
        except Exception as e:
            print(f"Error deleting user:{e}")    
            return False