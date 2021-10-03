from os import system
from mysql import connector


# @author Diyorbek Dev
# github.com/DiyorbekUz/register-login-page 

my_db = connector.connect(
    host = "localhost",
    user="user", #Your user 
    passwd="password", #your password
    database="database" #your database
)

mycursor = my_db.cursor()
# create table | bu buyruqni faqat 1 marta ishlating yani kodni 1-marta run qilgandan keyin kommentga olib qo'ying
query = "CREATE TABLE `users` (id int(11) NOT NULL AUTO_INCREMENT,name varchar(30) NOT NULL, login varchar(30) NOT NULL, password varchar(30) NOT NULL, PRIMARY KEY (`id`)) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8;"
mycursor.execute(query)


# main part
class App:
    def __init__(self, name=None, login=None, password=None):
        self.name = name
        self.login = login
        self.password = password
        self.init_input_options = ["1","2"]
        self.system_options = ["1","2","3","4"]
    def start(self):
        system("clear")
        self.init_message()
        user_input = input("[1/2]: ").strip()
        while user_input not in self.init_input_options:
            system("clear")
            print("Invalid input")
            self.init_message
            user_input = input("[1/2]: ").strip()
    
        if user_input == self.init_input_options[0]:
            self.register()
        else:
            self.log_in()
    def init_message(self):
        print(f"""
        Entering the system:
        Register    [{self.init_input_options[0]}]
        Login       [{self.init_input_options[1]}]
        """)
  

# @author Diyorbek Dev
# github.com/DiyorbekUz/register-login-page

    def register(self):
        input_name = input("input name: ").strip().capitalize()
        while self.is_empty_str(input_name) or not input_name.isalpha():
            system("clear")
            print("You've entered empty name, or you entered number!")
            input_name = input("Your name: ").strip().capitalize()
        
        input_login = input("Input login: ").strip()
        check_login = f"SELECT * FROM users WHERE login='{input_login}'"
        mycursor.execute(check_login)
        result = mycursor.fetchall()
        if result or self.is_empty_str(input_login):
            while True:
                system("clear")
                print("you've entered empty login! or this login already exists")
                input_login = input("Login: ").strip()
                if not result or not self.is_empty_str(input_login):
                    break
        
        input_password = input("Input password: ").strip()
        while self.is_empty_str(input_password):
            system("clear")
            print("You've entered empty password!")
            input_password = input("Your password: ").strip()

        export = f"INSERT INTO users (name, login, password) VALUES ('{input_name}', '{input_login}', '{input_password}');"
        mycursor.execute(export)
        my_db.commit()
        print("Register succsessfuly!!!")
        self.interface()

    def log_in(self):
        global in_login
        in_login = input("Input login: ").strip()
        in_check_login = f"SELECT * FROM users WHERE login='{in_login}'"
        mycursor.execute(in_check_login)
        in_result = mycursor.fetchall()
        if not in_result:
            while True:
                system("clear")
                print("This login is not register!")
                in_login = input("Login: ").strip()
                in_check_login = f"SELECT * FROM users WHERE login='{in_login}'"
                mycursor.execute(in_check_login)
                in_result = mycursor.fetchall()
                if in_result:
                    break
        in_password = input("Input password: ").strip()
        in_check_login = f"SELECT name FROM users WHERE password='{in_password}' AND login='{in_login}';"
        mycursor.execute(in_check_login)
        in_result_all = mycursor.fetchall()
        while not in_result_all:
            system("clear")
            print("This password error!")
            in_password = input("Input password: ").strip()
            in_check_login = f"SELECT name FROM users WHERE password='{in_password}' AND login='{in_login}';"
            mycursor.execute(in_check_login)
            in_result_all = mycursor.fetchall()
        system("clear")
        print("You've succsessfuly sign in!")
        global _login
        _login = in_login
        global _password
        _password = in_password
        self.interface()  


# @author Diyorbek Dev
# github.com/DiyorbekUz/register-login-page

      
    @staticmethod
    def is_empty_str(str_):
        return not str_

    def interface(self):
        print(f"""
            CHange login        [{self.system_options[0]}]
            Change password     [{self.system_options[1]}]  
            Log out             [{self.system_options[2]}]
            Stop system         [{self.system_options[3]}]
        """)

        sys_input = input("[1/2/3/4]: ").strip
        while sys_input not in self.system_options:
            print("Invalid options!")
            sys_input = input("[1/2/3/4]: ").strip()
        if sys_input == self.system_options[0]:
           self.change_login()
        elif sys_input == self.system_options[1]:
            self.change_password()
        elif sys_input == self.system_options[2]:
            self.log_out() 
        else:
            exit() 
    
    def change_login(self):
        system("clear")
        global _login
        new_login = input("Please enter new login: ").strip()
        check_login = f"SELECT * FROM users WHERE login='{new_login}'"
        mycursor.execute(check_login)
        result = mycursor.fetchall()
        while result:
            system("clear")
            print("you've entered empty login! or this login already exists")
            new_login = input("Login: ").strip()
            check_login = f"SELECT * FROM users WHERE login='{new_login}'"
            mycursor.execute(check_login)
            result = mycursor.fetchall()
        change_log = f"UPDATE users SET login='{new_login}' WHERE login='{_login}';"
        mycursor.execute(change_log)
        my_db.commit()
        print("succsessfuly!")
        _login = new_login
        self.interface()
        

    def change_password(self):
        system("clear")
        global _password
        new_password = input("Please enter new password: ").strip()
        while self.is_empty_str(new_password):
            system("clear")
            print("You've entered empty password")
            new_password = input("Please enter new password: ").strip()
        change_log = f"UPDATE users SET password='{new_password}' WHERE password='{_password}';"
        mycursor.execute(change_log)
        my_db.commit()
        print("succsessfuly!")
        _password = new_password
        self.interface()

    def log_out(self):
        self.start()

user = App()
user.start()


# @author Diyorbek Dev
# github.com/DiyorbekUz/register-login-page
