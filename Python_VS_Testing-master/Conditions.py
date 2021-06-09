#TC 04/06/21

#Number input
num_input = int(input("Mark out of 100: "))

#Using ELIF
if num_input >= 85:
    print("Distinction")
elif num_input < 85 and num_input >= 65:
    print("Pass")
else:
    print("Fail")

#No ELIF
if num_input >= 85:
    print("Distinction")

if num_input < 85 and num_input >= 65:
    print("Pass")

if num_input <= 64:
    print("Fail")