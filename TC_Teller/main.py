import csv
import sys
import os

from Sub_Programs.encryption import num_scramble_undo, string_scramble_undo, num_scramble, string_scramble
from Sub_Programs.validation import verify

class user:

    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
    
    def get_balance_user(self):
        return self.balance
    
    def withdraw_user(self, amount):
        self.balance = self.balance - amount
        return balance
    
    def deposit_user(self, amount):
        return self.balance + amount


def user_login():

    input_name = input("What is your name: ")
    input_pin = input("What is your pin: ")

    info = [input_name, input_pin, 0]

    info = verify(info)

    return info

def search_csv(name, pin):

    parentDirectory = os.path.abspath(os.path.join(os.getcwd(), os.pardir))
    user_path = parentDirectory + "/TC_Teller/Usually_Hidden/Users_Data/users.csv"

    csv_file = csv.reader(open(user_path, "r"), delimiter=",")

    for row in csv_file:
        if str(name) == row[0] and str(pin) == row[1]:
            print(row)
    
    print(row)
    

print(user_login())
