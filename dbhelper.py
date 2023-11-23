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
                 
                 
    def update_user(self,user_id,new_name,new_email):
        try:
            self.mycursor.execute("""
                                UPDATE userrs SET name=?,email=? WHERE id =?
                                """,(new_name,new_email))  
            self.conn.commit()
        except Exception as e:
            print(f"Error during registration: {e}")                 
            
    def delete_user(self,user_id):
        try:
            self.mycursor.execute("""
                                  DELETE FROM users WHERE id =?
                                  """,(user_id))        
            self.conn.commit()
        except Exception as e:
            print(f"Error during registration: {e}")                 
            