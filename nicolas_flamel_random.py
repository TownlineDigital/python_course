import random

highest_age = 20

actual_age = random.randint(1, highest_age)

# print(actual_age)
guess = None
print('what is flamel age weasly? (1 to {})'.format(highest_age))

while guess != actual_age:
    guess = int(input())
    if guess == actual_age:
        print('You guess it right 10 points for you!!')
    else:
        if guess < actual_age:
            print('Please Ron guess higher')
        else:
            print('Please Mr. weasly guess lower')