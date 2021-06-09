import csv
import os

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

#Function to valiate list given to it
def validation(info):

    #Breaks down list given to it into smaller variables to be tested
    Input_Name = info[0]
    Input_Pin = info[1]
    Input_Balance = info[2]

    #Tests to see if the pin can be converted to interger
    try:
        int(Input_Pin)
    except:
        #If it cant be converted to an interger it returns an error message
        return "Pin Invalid"

    #Checks to see if the pin is too long
    if len(Input_Pin) > 4:
        return "Pin too long"
    #Checks to see if the pin is too short
    elif int(Input_Pin) < 4:
        return "Pin too short"

    #Tests to see if the balance can be converted to float
    try: 
        float(Input_Balance)
    except:
        #If it cant be converted to a float returns an error message
        return "Invalid balance"
    
    #Once the variables have been validated it convertes each to a string and returns as a list
    info = [str(Input_Name), str(Input_Pin), str(Input_Balance)]

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
    write(validation(get_user_info()))
