#Tommy Calvin 07/06/2021
#Grade calculator

#Function to gather marks based on subject
def request_inputs(subjects, best_score):
    #Creates empty dictionary
    subject_marks = {}
    #Runs for loop as many times as subjec in subjects
    for subject in subjects:
        #Creates a new dictionary entry with the key being the curretn subject, asks for grade out of 100 as value
        subject_marks[subject] = int(input("What was your mark in "+subject+": "))

    #Runs generate_percentage function, passing through best_score(max attainable score), and generated dictionary
    return generate_percentage(subject_marks, best_score)

#Function to generate percentage score
def generate_percentage(subject_marks, best_score):
    #Sets list subjects as all kets from dictionary
    subjects = subject_marks.keys()
    #Init total_marks variable as 0
    total_marks = 0
    #Sets max_marks for all subjects taken * max attainable score
    max_marks = len(subjects) * best_score
    #Runs for loop based on all keys of dicitonary
    for subject in subjects:
        #Searches current key in dictionary and adds value (Test score) to total_mark
        total_marks += subject_marks[subject]

    #Generates percentage for all subjects
    percentage = (total_marks / max_marks) * 100

    #Runs output_message function to give user final output
    output_message(round(percentage, 2))

#Function to print to console
def output_message(percentage):

    #If table to see what grade user scored from percentage generated, changed variable grade to generated grade
    if percentage >= 70:
        grade = "A"
    elif percentage >= 60:
        grade = "B"
    elif percentage >= 50:
        grade = "C"
    elif percentage >= 40:
        grade = "D"
    elif percentage <= 39:
        grade = "Fail"

    #Prints percentage and grade to console
    print("Your percentage score is: " + str(percentage) + "%")
    print("You scored a grade of: " + grade)

#Change subjects here, add or remove as needed
subjects = ["Mathmatics", "Chemistry", "Physics"]
#Max attainable score for test, can be any int
best_score = 100

#Runs request_input function which then runs generate_percentage and finally output_message
request_inputs(subjects, best_score)