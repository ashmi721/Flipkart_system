import sqlite3

class SqliteDBhelper:
     def connect():
        conn = sqlite3.connect("flip.db")
        return conn
        conn = connect() # call the connect() function
        cur = conn.cursor() 
    
        try:
            # Execute the SQL statement to create the table
            cur.execute('''CREATE TABLE IF NOT EXISTS users(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                email TEXT NOT NULL,
                password TEXT NOT NULL
            )''')

            # Commit the changes to the database
            conn.commit()

            # If execution is successful, set a variable to indicate that the table is created
            table_created = True

        except Exception as e:
            # If an exception occurs, set the variable to indicate that the table is not created
            table_created = False
            print(f"Error: {e}")

        # Check if the table is created and print a message accordingly
        if table_created:
            print("Table is created")
        else:
            print("Table creation failed") 