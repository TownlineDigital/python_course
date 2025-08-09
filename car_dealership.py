#            0       1       2        3           4            5
car_list = ['bmw', 'honda', 'ford', 'ferrari', 'volkswagen', 'audi']

car_to_drive = 'Lambo'
car_index = None

# print(len(car_list))

for index in range(len(car_list)):
    if car_list[index] == car_to_drive:
        car_index = index



print('The {} is parked in Zone {}'.format(car_to_drive, car_index))


# for car in car_list:
#     if car == 'ford':
#         break
#     print(car)
