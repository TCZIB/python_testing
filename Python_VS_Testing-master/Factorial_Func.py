#TC 04/06/21
#Factorial Generator

#Defines Factorial function with num_input
def Factorial(num_input):
    #Temporary variable to store output in
    var = 1
    #Loop, runs for length on num_input
    for i in range(num_input):
        #Times previous number by current iteration
        var = var * (i+1)
    #Returns var
    return var

#Does continually
while True:
    #Asks for number input
    num_input = int(input("Enter a number: "))
    #Prints output of Factorial function with number input
    print(Factorial(num_input))