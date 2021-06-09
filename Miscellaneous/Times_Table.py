num_input = int(input("Enter a number: "))

for i in range(num_input):
    row = []
    for x in range(num_input):
        row.append(str((i+1)*(x+1)))
    print(row)