import mysql.connector

class DBhelper:
    def __init__(self):
        try:
            self.conn= mysql.connector.connect(host="localhost",username="root",password = "",
                                        database="flip")
            self.mycursor = self.conn.cursor()
        except:
            print("Connected to Database")
            
        else:
            print("Some error occured")    
            
    def register(self,name,email,password):
        try:
            self.mycursor.execute("""
            InSERT INTO `users` (`id`,`name`,`email`,`password`)VALUES(NULL,'{}','{}','{}')                      
                                """.format(name,email,password))
            self.conn.commit() 
        except:
            return -1
        else:
            return 1    
             