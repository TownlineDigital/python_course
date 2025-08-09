even = [2, 4, 6, 8]
odd = [1, 3, 5, 7, 9]

numbers = even + odd
print(numbers)

sorted_numbers = sorted(numbers)
print(sorted_numbers)
print(numbers)

digits = sorted('159436287')
print(digits)

digits1 = list('159436287')
print(digits1)

# more_numbers = list(numbers)
# more_numbers = numbers[:]
more_numbers = numbers.copy()
print('more numbers', more_numbers)
print(id(numbers))
print(id(more_numbers))
print(numbers == more_numbers)
print(numbers is more_numbers)