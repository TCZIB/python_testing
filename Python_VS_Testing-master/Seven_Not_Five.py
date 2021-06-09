numbers = list(range(2000 , 3201))
output = []

for num in numbers:
    if num % 5 != 0 and num % 7 == 1:
        output.append(num-1)

print(output)