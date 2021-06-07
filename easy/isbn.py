#Tommy Calvin 07/06/2021
#ISBN Check

#Function to check and return ISBN
def isbn_check():
    #Output of calculated ISBN
    output = 0

    #Asks user for input of digits to ISBM (-'s are not important)
    isbn = input("Enter ISBN (000-0-000-00000 Format): ")
    #Makes it clearer to read with space
    print("\n")
    
    #Creates a backup of input
    isbn_original = isbn

    #Replaces "-" in input with nothing to generate long string
    isbn = isbn.replace("-","")
    
    #Makes variable with all odd index numbers
    odd = isbn[1::2]
    #Makes variable with all even index numbers
    even = isbn[0::2]
    
    #Runs loop for all even index numbers, adding them together
    for num in range(len(even)):
        output += int(even[num])

    #Runs loops for all odd index numbers, multiplying them by 3 and adding them to output
    for num in range(len(odd)):
        output += int(odd[num])*3

    #Checks to see if modulus returns 0 or other
    if output % 10 != 0:
        #If it != 0 than it minus' the remainder from 10 and adds it onto original input (isbn_original)
        return str(isbn_original) + "-" + str(10 - (output % 10))

    #If remainder = 0 returns isbn_original and 0
    return str(isbn_original) + "-" + str("0")

#Repeating loop
while True:
    #Runs function
    print(isbn_check())
    #Creates new line to make it look easier
    print("\n"*2)
