import csv
import os
from Sub_Programs.encryption import num_scramble ,string_scramble
from Sub_Programs.validation import verify

#Generates path based on placement of this file, structre should be ~/TC_teller/Sub_Programs/user_creation.py and CSV file shoudld be in /TC_Teller/Users_Data/users.csv 
parentDirectory = os.path.abspath(os.path.join(os.getcwd(), os.pardir))
user_path = parentDirectory + "/Usually_Hidden/Users_Data/users.csv"

#CSV Structure - name pin balance

#Function to get users information
def get_user_info():

    #New line to make it look better
    print("\n")
    #Gets user inputs, asks them a specific question and gets reposnse as string
    Input_Name = input("What is your name: ")
    Input_Pin = input("What is your pin (4 digits): ")
    Input_Balance = input("What is your balance: ")

    #Turns all gathered inputs into a list
    info = [str(Input_Name), str(Input_Pin), str(Input_Balance)]

    #Returns list
    return info

#Function to write validated list to CSV file
def write(info):

    #Checks to see if entered value is valid list or error message
    if type(info) != list:
        #If passed value isnt a list then its and error message, prints error message to console
        return print(info)

    #Opens the users.csv file, uses TC_Teller as root directory (generates in above code), opened to append not write
    with open(user_path, mode="a") as csv_file:
        #Sets the file path, what to seperate with, how to quote and quote type
        csv_write = csv.writer(csv_file, delimiter=",", quotechar='"', quoting=csv.QUOTE_MINIMAL)
        #Writes passed list as a row into csv table
        csv_write.writerow(info)

#Loop to run code above
while True:
    write(verify(get_user_info()))
