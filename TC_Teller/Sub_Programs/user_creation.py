import csv

#CSV Structure - name pin balance

Input_Name = input("What is your name: ")
Input_Pin = input("What is your pin (4 digits): ")
Input_Balance = input("What is your balance: ")

info = [Input_Name, Input_Pin, Input_Balance]

with open('TC_Teller/Users_Data/users.csv') as csv_file:
    csv_write = csv.writer(csv_file, delimiter=",", quotechar='"', quoting=csv.QUOTE_MINIMAL)

    csv_write.writerow(info)