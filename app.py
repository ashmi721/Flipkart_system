import sys
# from dbhelper import DBhelper
from sqlite3db import SqliteDBhelper
class FlipkartSystem:
    
    def __init__(self):
        # connect to the database 
        # self.db = DBhelper()  
        self.db = SqliteDBhelper()
        self.user_data = None   # to store user data after login
        self.menu()
        
    def menu(self):  
      user_input = input("""
        1 . Enter 1 to register
        2 . Enter 2 to login
        3 . Browse Prodcuts
        4 . Anything else to leave
        Enter your choice:
              """)    
      
      if user_input == "1":
          self.register()
      elif user_input == "2":
          self.user_data = self.login()
          self.user_menu()
      elif user_input == "3":
          self. browse_categories()    
      elif user_input == "4":
          sys.exit(1000)  
      else:
          print("Invalid choice. Please enter a valid option.")            
          self.menu()
              
      
    def register(self):
        name = input("Enter name:")
        email = input("Enter email:")
        gender = input("Enter gender:")
        password = input("Enter password:")
        response = self.db.register(name,email,gender,password)
        
        if response :
            print("Registration successful")
        else:
            print("Registration failed")       
        self.menu()   
        
    def login(self):
        email = input("Enter email:")
        password = input("Enter password:")
        
        data = self.db.search(email,password)
        # print(data)
        if len(data) == 0:
            print("Incorrect email or password")
            self.login()
        else:
             print("Hello",data[0][1])   
             return data[0]
        
    def browse_categories(self):
            print("Available Categories:")
            categories = ["Electronics", "Clothing", "Books", "Home Appliances"]
            for i, category in enumerate(categories, start=1):
                print(f"{i}. {category}")

            category_choice = input("Select a category (enter the number): ")

            try:
                category_choice = int(category_choice)
                if 1 <= category_choice <= len(categories):
                    self.selected_category = categories[category_choice - 1]
                    print(f"You selected the {self.selected_category} category.")
                else:
                    print("Invalid category selection.")
            except ValueError:
                print("Invalid input. Please enter a number.")

            self.profile()
        
    def user_menu(self):
        login_input = input("""
        1 . Enter 1 to see profile
        2 . Enter 2 to edit profile
        3 . Enter 3 to delete profile
        4 . Enter 4 to logout
        Enter your choice:
              """)  
        if login_input =="1":
            self.profile()
        elif login_input =="2":
            self.update()
        elif login_input =="3":
            self.delete()
        elif login_input =="4":
            self.logout()
            self.user_menu()
        else:
           sys.exit(1000)   
                        
    def profile(self):
        if self.user_data:
            print("User Profile:")
            print("Name:",self.user_data[1])
            print("Email:",self.user_data[2])
            print("Gender:",self.user_data[3])
            self.user_menu()
        else:
            print("User not logged in.")
            self.menu()
    
    def update(self):
        if self.user_data:
            user_id = self.user_data[0]
            new_name=input("Enter your new name: ")
            new_email=input("Enter your new email: ")
            new_gender=input("Enter your new gender: ")
             
            if self.db.update_user(user_id,new_name,new_email,new_gender):
                print("Update successful!")    
            else:
                print("Unable to update user.")
        else:
            print("User not logged in.")     
        self.user_menu()    
        
               
    def delete(self):
        if self.user_data:
            user_id = self.user_data[0]
            if self.db.delete_user(user_id):
                print("Delete account successfully.")    
            else:
                print("Unable to delete account.")
        else:
            print("User not logged in.")    
        self.menu()       
                
            
    def logout(self):    
        self.user_data = None
        print("Logged out successfully.") 
        self.menu() 
                     
obj = FlipkartSystem()                           