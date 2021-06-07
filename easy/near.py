#TC 07/06/2021
#Takes two strings and see if second string can be found in first by removing letter 

def near(original, new):
    for letter_pos in range(len(original)):
        new_word = original[:letter_pos] + original[(letter_pos+1):]
        if new_word == new:
            return print(True)
    return print(False)

    
near("reset", "rest")
near("dragoon", "dragon")
near("eave", "leave")
near("sleet", "lets")