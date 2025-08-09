# message = 'im learning python'
#
# for character in message:
#     print(character)

data_coming_in = "6,364.7;695//2/32.14 12/36,97,46"
# print(data_coming_in[1::5])

separators = ''

for character in data_coming_in:
    if not character.isnumeric():
        separators += character

print(separators)

# for character in data_coming_in:
#     if type(character) is not int:
#         separators += character
#
# print(separators)


