#TC 09/06/2021
#A simple program to obscure data (Not very secure)

def num_scramble(number):
    #Some fancy encryption

    try:
        float(number) * 2
    except:
        return False

    return float(number) * 2

def num_scramble_undo(number):
    #Some fancy decryption

    try:
        float(number) / 2
    except:
        return False
        
    return float(number) / 2

def string_scramble(string):
    #Caeser cipher
    output = ""
    for letter in string:
        output += chr(int(ord(letter) + 10))
    
    return output

def string_scramble_undo(string):
    #Caeser cipher
    output = ""
    for letter in string:
        output += chr(int(ord(letter) - 10))
    
    return output
