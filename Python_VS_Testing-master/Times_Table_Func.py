#TC 04/06/2021
#Times table generator

#Defines Time_Table function to interate upon input
def Times_Table(num_input):
    #Creates empty list
    output = []
    #Initial for loop, for each row (Runs for num_input times)
    for i in range(num_input):
        #Creates empty row list
        row = []
        #Loop run per row, iterates same length as num_input
        for x in range(num_input):
            #Appends current row * column
            row.append(str((i+1)*(x+1)))
        #Appends generated row to output list
        output.append(row)
    #Returns output list 
    return output

#Defines output function
def User_Out(output):
    #Loop running for length of output(2D Array)
    for i in range(len(output)):
        #Prints row from output
        x = " ".join(output[i])
        print(x)
    #Back to main loop
    return

#Does continually
while True:
    #Asks for number input
    num_input = int(input("Enter a number: "))
    #Runs user_out with the output from Time_Table function
    User_Out(Times_Table(num_input))
    #Makes it look prettier
    print("\n")
