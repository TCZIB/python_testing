#TC 07/06/2021
#Takes two strings and see if second string can be found in first by removing letter

#Main function
def near(original, new):
    #Runs for loop based on length of original word
    for letter_pos in range(len(original)):
        #Sets variable new_word as original word with 1 letter removed (One letter at a time in sequence)
        new_word = original[:letter_pos] + original[(letter_pos+1):]
        #If the generated word is equal to the word being tested (new) print True
        if new_word == new:
            #Prints true
            return print(True)
    #If it cannot match to words return False
    return print(False)


#Runs function with words to be found   
near("reset", "rest")
near("dragoon", "dragon")
near("eave", "leave")
near("sleet", "lets")