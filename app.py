import sys
# from dbhelper import DBhelper
from sqlite3db import SqliteDBhelper
class Flipkart:
    
    def __init__(self):
        # connect to the database
        ''' this is the connection of the mysql database '''
        # self.db = DBhelper() 
        ''' this is the connection of the sqlite3 database '''
        self.db = SqliteDBhelper()
        self.user_data = None   # to store user data after login
        self.menu()
        
    def menu(self):
        
      user_input = input("""
        1 . Enter 1 to register
        2 . Enter 2 to login
        3 . Anything else to leave
              """)    
      
      if user_input == "1":
          self.register()
      elif user_input == "2":
          self.user_data = self.login()
          self.login_menu()
      else:
          sys.exit(1000)          
      
    # def login_menu(self):
    #     login_input = input("""
    #     1 . Enter 1 to see profile
    #     2 . Enter 2 to edit profile
    #     3 . Enter 3 to delete profile
    #     4 . Enter 4 to logout
    #           """) 
        
    #     if login_input =="1":
    #         self.profile()
    #     elif login_input == "2":
    #         self.update()
    #     elif login_input =="3":
    #         self.delete()
    #     elif login_input =="4":
    #         self.logout()
    #     else:
    #        sys.exit(1000)                 
      
    # def register(self):
    #     name = input("Enter the name:")
    #     email = input("Enter the email:")
    #     password = input("Enter the password:")
    #     response = self.db.register(name,email,password)
        
    #     if response :
    #         print("Registration successful")
    #     else:
    #         print("Registration failed")   
            
    #     self.menu()   
        
    # def login(self):
    #     email = input("Enter email:")
    #     password = input("Enter password:")
        
    #     data = self.db.search(email,password)
    #     # print(data)
    #     if len(data) == 0:
    #         print("Incorrect email or password")
    #         self.login()
    #     else:
    #          print("Hello",data[0][1])   
    #          return data[0]
             
    # def profile(self):
    #     if self.user_data:
    #         print("User Profile:")
    #         print("Name:",self.user_data[1])
    #         print("Email:",self.user_data[2])
    #     else:
    #         print("User not logged in.")
    
    # def update(self):
    #     # Implement profile update logic
    #     pass
    
    # def delete(self):
    #     # Implement profile deletion logic
    #     pass
    
    # def logout(self):
    #     self.user_data = None
    #     print("Logged out successfully.")
    #     self.menu()
                       
obj = Flipkart()                           