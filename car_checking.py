car = 'bmw m3'

car_name = input('what car would you like?')
if car_name in car:
    print('{} is in {}'.format(car_name, car))
else:
    print('sorry we do not have this car')