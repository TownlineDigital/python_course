temperature = int(input('how hot is the GPU?'))

# if temperature >= 20 and temperature <= 70:
# if 20 < temperature < 70:
#     print('all good')
# else:
#     print('stop playing')

# use or instead of and

if temperature < 20 or temperature > 70:
    print('stop playing')
else:
    print('all good')