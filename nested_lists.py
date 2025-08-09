num1 = [23, 41, 68, 82]
num2 = [21, 3, 15, 75, 94]

numbers = [num1, num2]
print(numbers)

for number_list in numbers:
    print(number_list)
    for individual_number in number_list:
        print(individual_number)