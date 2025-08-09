car_list = ['bmw car', 'ferrari car', 'ford car', 'audi car', 'Tesla car']

for car in car_list:
    if 'car' not in car:
        print('sorry this list is unacceptable')
        break
else:
    print('this list is fine')