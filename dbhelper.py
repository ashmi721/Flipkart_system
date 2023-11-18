import mysql.connector
import sys

class DBhelper:
    def __init__(self):
        try:
            self.conn= mysql.connector.connect(host="localhost",user="root",password = "",
                                        database="flip")
            self.mycursor = self.conn.cursor()
        except Exception as e:
            print(f"Error connecting to the database: {e}")
            sys.exit(1)
        else:
            print("Connected to Database")  
                  
    def register(self, name, email, password):
        try:
            self.mycursor.execute("""
            INSERT INTO `userrs` (`id`, `name`, `email`, `password`) VALUES (NULL, %s, %s, %s)
            """, (name, email, password))
            self.conn.commit()
        except Exception as e:
            print(f"Error during registration: {e}")
            return -1
        else:
            return 1
   
    
    def search(self,email,password):
        self.mycursor.execute(""" SELECT * FROM `userrs` WHERE email LIKE '{}' AND password LIKE '{}' 
                """.format(email,password))
     
        data = self.mycursor.fetchall()
        
        return data
                 