import csv
import sys
import os

from Sub_Programs.encryption import num_scramble_undo, string_scramble_undo, num_scramble, string_scramble
from Sub_Programs.validation import verify

class user:

    def __init__(self, credentials):

        self.name = string_scramble_undo(credentials[0])
        self.balance = num_scramble_undo(credentials[2])
    
    def get_balance_user(self):

        output = f"{self.name} your balance is £{self.balance}"

        return output
    
    def withdraw_user(self, amount):
        self.balance = self.balance - amount
        return balance
    
    def deposit_user(self, amount):
        return self.balance + amount

    def display_options(self):
        print("\n")
        print(f"Welcome {self.name}")
        print("From the list below please type in option:")
        pass

    def user_options(self):
        pass


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
        if str(name) == row[0] and str(pin) == row[1]:
            return row
    
    return "User Not Found"

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
            print(logged_in_user.get_balance_user())

while True:
    main_loop()


