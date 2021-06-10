import csv
import sys
import os

from Sub_Programs.encryption import num_scramble_undo, string_scramble_undo, num_scramble, string_scramble
from Sub_Programs.validation import verify

class user:

    def __init__(self, credentials):

        self.name = string_scramble_undo(credentials[0])
        self.balance = num_scramble_undo(credentials[2])

        self.display_options()
    
    def verify_y_n(self):

        verified = False

        valid = ["y","n"]

        while not verified:
            print("\n")
            usr_input = input("Return to menu y/n: ")

            if usr_input not in valid:
                print("Invalid input")
            else:
                break
        
        return usr_input



    def view_balance(self):

        print("\n")
        print(f"{self.name} your balance is £{self.balance}")

        usr_input = self.verify_y_n()
    
        if usr_input == "y":
            self.display_options()
        
        return
    
    def withdraw(self, amount):
        return
    
    def deposit(self, amount):
        return self.balance + amount

    def display_options(self):
        options = {"1":". Exit","2":". View Balance","3":". Withdraw","4":". Deposit"}

        print("\n")
        print(f"Welcome {self.name}")
        print("From the list below please type in option:")
        for option in options:
            print(option + options[option])
        
        usr_input = self.verify_input(usr_input, options)

        if usr_input:
            pass
        if not usr_input:
            self.display_options

        if usr_input == "Exit":
            print("Have a nice day!")
            print("\n")
            return

        next_func = "self."+((options[usr_input]).lower()[2:]).replace(" ","_")+"()"

        exec(next_func)
            
    def get_input(self, options):

        usr_input = input("Selection: ")

        usr_input = usr_input.lower()

        valid_input = list(str(options.keys()))
        
        if str(usr_input) not in valid_input:
            return False

        if usr_input == str(1):
            return "Exit"
        
        return usr_input

def user_login():

    input_name = input("What is your name: ")
    input_pin = input("What is your pin: ")

    info = [input_name, input_pin, 0]
    info = verify(info)

    return info

def search_csv(info):

    name = info[0]
    pin = info[1]

    original_info = info

    parentDirectory = os.path.abspath(os.path.join(os.getcwd(), os.pardir))
    user_path = parentDirectory + "/TC_Teller/Usually_Hidden/Users_Data/users.csv"

    csv_file = csv.reader(open(user_path, "r"), delimiter=",")

    for row in csv_file:
        if str(name) == row[0]:
            output = "Incorrect pin"
            if str(pin) == row[1]:
                return row

    output = "User not found"

    return output

def user_generation(info):
    logged_in_user = user(string_scramble_undo(info[0]), num_scramble_undo(info[1]))
    print(user.get_balance_user(logged_in_user))

def main_loop():
    print("\n")
    credentials = user_login()

    #Checks to see if list or str returned
    if type(credentials) == str:
        #If string returned must be error message, re-run login
        print(credentials)
    #If its not a string, must be list
    else:
        #Searches the CSV file to see if it can find the user
        credentials = search_csv(credentials)
        #If it returns a string, must be error
        if type(credentials) == str:
            #Prints error
            print(credentials)
        else:
            logged_in_user = user(credentials)

while True:
    main_loop()


