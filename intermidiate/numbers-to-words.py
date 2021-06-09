def num_text():
    units = ["One","Two","Three","Four","Five","Six","Seven","Eight","Nine","Ten"]

    tens = [["Eleven","Twelve","Thirteen","Fourteen","Fifteen","Sixteen","Seventeen","Eighteen","Nineteen"
    ,"Twenty -","Thirty -","Fourty -","Fifty -","Sixty -","Seventy -","Eighty -","Nintey -"],["11","12","13"
    ,"14","15"]]

    hundreds = ["- Hundred and"]

    return units, tens, hundreds

def number_breakdown(number):
    
    unit_assignment = [[],[]]
    unit_labels = ["Unit","Tens","Hundred","Thousand","Hundred thousand","Million","Hundred Million"]
    
    numbers_seperated = list(map(int, str(number)))
    numbers_seperated = numbers_seperated[::-1]

    for i in range(len(numbers_seperated)):
        unit_assignment[0].append(numbers_seperated[i])
        unit_assignment[1].append(unit_labels[i])

    return unit_assignment

def number_grouping(units, tens, hundreds, unit_assignment):
    return

number = 12345
wording = num_text()
print(number_grouping(wording[0], wording[1], wording[2], number_breakdown(number)))
