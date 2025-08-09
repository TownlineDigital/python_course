actual_age = 665

guess = int(input('what is flamel age weasly?:'))

if guess == actual_age:
    print('You guessed it right 20 point for Gryffindor')

else: #age == actual age
    if guess < actual_age:
        print('please Ron guess higher')
    else:# guess > actual_age
        print('please Mr. Weasly guess lower')

    guess = int(input('>'))

    if guess == actual_age:
        print('You guessed it right 10 point for Gryffindor')
    else:
        print('wrong again')



# if guess < actual_age:
#     print('please Ron guess higher')
#     guess = int(input('>'))
#     if guess == actual_age:
#         print('well done 5 points for Gryffindor')
#     else:
#         print('wrong again')
# elif guess > actual_age:
#     print('please mr Weasly guess lower')
#     guess = int(input('>'))
#     if guess == actual_age:
#         print('well done 5 points for Gryffindor')
#     else:
#         print('wrong again')
# else:
#     print('you guessed it right 10 points for Gryffindor')