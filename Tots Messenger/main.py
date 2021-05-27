import os
import requests
import sys

logged_in = False
logged_in_user_name = 0
logged_in_user_id = 0

api_login = 'https://your_website.com/tots_api/api_user/validate_user.php'
api_register = 'https://your_website.com/tots_api/api_user/register_user.php'
api_check_username = 'https://your_website.com/tots_api/api_user/check_username.php'

def main():
    os.system('cls' if os.name == 'nt' else 'clear') 
    print("Welcome to Tots Project !")
    text = input("To login, type login, to register, type register: ")
    if text == "login":
        login()
        return
    elif text == "register":
        register()
        return
    elif text == "cmdlist":
        print("========================================================== \
            \n|                Tots project - CMDList                  | \
            \n========================================================== \
            \n1 - serverstatus - Shows the API Status.")
        print("")
        main_without_text()
    else :
        main()
        return

def main_without_text():
    text = input("")
    if text == "login":
        login()
        return
    elif text == "register":
        register()
        return
    elif text == "cmdlist":
        print("========================================================== \
            \n|                Tots project - CMDList                  | \
            \n========================================================== \
            \n1 - serverstatus - Shows the API Status.")
        print("")
        main_without_text()
    else :
        main()
        return
    
def login():
    username_input = input("Please enter your username: ")
    password_input = input("Please enter your password: ")
    response = requests.post("" + api_login+"?user="+username_input+"&pass="+password_input, data=0).text
    response = response.replace('<p>', '').replace('</p>', '') 
    print("")
    if response == "rejected":
        print("Invalid credentials")    
        print("")
        print("")
        login()
        return

def register():
    username_input = input("Please enter your desired username: ")
    response = requests.post("" + api_check_username+"?user="+username_input, data=0).text
    response = response.replace('<p>', '').replace('</p>', '') 
    if response == "taken":
        print("That username is already taken. Try again...")
        print("")
        print("")
        register()
        return
    elif response == "valid":
        password_input = input("Please enter your desired password: ")
        response = requests.post("" + api_register+"?user="+username_input+"&pass="+password_input, data=0)
main()