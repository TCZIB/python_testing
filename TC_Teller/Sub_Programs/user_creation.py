import csv
import os

parentDirectory = os.path.abspath(os.path.join(os.getcwd(), os.pardir))
user_path = parentDirectory + "/Users_Data/users.csv"

#CSV Structure - name pin balance

def user_input():

    print("\n")
    Input_Name = input("What is your name: ")
    Input_Pin = input("What is your pin (4 digits): ")
    Input_Balance = input("What is your balance: ")
    
    try:
        int(Input_Pin)
    except:
        return "Pin Invalid"

    if len(Input_Pin) > 4:
        return "Pin too long"
    elif int(Input_Pin) < 4:
        return "Pin too short"

    try: 
        int(Input_Balance)
    except:
        return "Invalid balance"
    
    info = [str(Input_Name), str(Input_Pin), str(Input_Balance)]

    return info

def write(info):

    if type(info) != list:
        return print(info)

    with open(user_path, mode="a") as csv_file:
        csv_write = csv.writer(csv_file, delimiter=",", quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_write.writerow(info)

while True:
    write(user_input())
