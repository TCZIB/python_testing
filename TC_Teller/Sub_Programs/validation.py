from Sub_Programs.encryption import num_scramble ,string_scramble

#Function to valiate list given to it
def verify(info):

    #Breaks down list given to it into smaller variables to be tested
    Input_Name = info[0]
    Input_Pin = info[1]
    Input_Balance = info[2]

    #Tests to see if the pin can be converted to interger
    try:
        int(Input_Pin)
    except:
        #If it cant be converted to an interger it returns an error message
        return "Pin Invalid"

    #Checks to see if the pin is valid
    if len(Input_Pin) != 4:
        return "Pin invalid"

    #Tests to see if the balance can be converted to float
    try: 
        float(Input_Balance)
    except:
        #If it cant be converted to a float returns an error message
        return "Invalid balance"
    
    #Once the variables have been validated it convertes each to a string and returns as a list
    #Also note, the scramble functions are run to make sure saved infrmation isnt readable
    info = [str(string_scramble(Input_Name)), str(num_scramble(Input_Pin)), str(num_scramble(Input_Balance))]

    return info
