current_choice = '-'
car_parts = []
available_parts = ['wheels', 'lights', 'front wing', 'seats', 'windows', 'stereo']
valid_choices = []
for i in range(1, len(available_parts) + 1):
    valid_choices.append(str(i))
print(valid_choices)

while current_choice != '0':
    if current_choice in '123456':
        index = int(current_choice) - 1
        chosen_part = available_parts[index]

        if chosen_part in car_parts:
            car_parts.remove(chosen_part)
        else:
            car_parts.append(chosen_part)
        # if current_choice == '1':
        #     car_parts.append('wheels')
        # elif current_choice == '2':
        #     car_parts.append('lights')
        # elif current_choice == '3':
        #     car_parts.append('front wing')
        # elif current_choice == '4':
        #     car_parts.append('seats')
        # elif current_choice == '5':
        #     car_parts.append('windows')
        # elif current_choice == '6':
        #     car_parts.append('stereo')
    else:
        print('Please add options from the list below:')
        for number, part in enumerate(available_parts):
            print('{}: {}'.format(number + 1, part))
        # for part in available_parts:
        #     print(available_parts.index(part) + 1, part)
        # print('1: wheels')
        # print('2: lights')
        # print('3: front wing')
        # print('4: seats')
        # print('5: windows')
        # print('6: stereo')
        print('0: finish')
    current_choice = input('Your choice here:')

print(car_parts)

