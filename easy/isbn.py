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

    isbn = isbn.replace("-","")
    
    odd = isbn[1::2]
    even = isbn[0::2]
    
    for num in range(len(even)):
        output += int(even[num])

    for num in range(len(odd)):
        output += int(odd[num])*3

    if output % 10 != 0:
        return str(isbn_original) + "-" + str(10 - (output % 10))

    return str(isbn_original) + "-" + str("0")

while True:
    print(isbn_check())
    print("\n"*2)
