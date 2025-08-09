inputs_coming_in = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17]

del inputs_coming_in[0:2]
print(inputs_coming_in)



del inputs_coming_in[16:]
print(inputs_coming_in)

min_valid = 5
max_valid = 12

# for index, value in enumerate(inputs_coming_in):
#     if(value < min_valid) or (value > max_valid):
#         del inputs_coming_in[index]
#
# print(inputs_coming_in)

# 0  1  2  3  4  5  6  7  8  9  10  11  12  13  14  15
#[3, 5, 6, 7, 8, 9, 10, 11, 12, 14, 16]

stop = 0
for index, value in enumerate(inputs_coming_in):
    if value >= min_valid:
        stop = index
        break
print(stop)
del inputs_coming_in[:stop]
print(inputs_coming_in)

start = 0
for index in range(len(inputs_coming_in)-1, -1, -1):
    if inputs_coming_in[index] <= max_valid:
        start = index + 1
        break

print(start)
del inputs_coming_in[start:]
print(inputs_coming_in)