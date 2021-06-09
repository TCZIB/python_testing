#TC 09/06/2021
#A simple program to obscure data (Not very secure)

def num_scramble(number):
    output = ""
    for num in str(number):
        output += str(int(num) + 1)
    
    output = int(output) * 2

    return output

def num_scramble_undo(number):
    output = ""
    number = number / 2
    for num in str(int(number)):
        output += str(int(num) - 1)

    return output

def string_scrable(string):
    pass

def string_scramble_undo(string):
    pass
