low = 1
high = 1000

print('Choose a number between {} and {}'.format(low, high))
input('Press any key to start')
number_of_guesses = 0
while high != low:
    number_of_guesses += 1
    guess_by_PC = low + (high - low) // 2
    hilo_input = input('i guessed {}. Press \n'
                       'l: to guess lower\n'
                       'h: to guess higher\n'
                       'c: if the answer is correct\n'.format(guess_by_PC)).casefold()
    if hilo_input == 'l':
        high = guess_by_PC - 1
    elif hilo_input == 'h':
        low = guess_by_PC + 1
    elif hilo_input == 'c':
        print('i guess it in {} times'.format(number_of_guesses))
        break
    else:
        print('please enter a valid options(h,l,c)')
else:
    print('the secret number is {}, i guessed it in {} times'.format(high, number_of_guesses))

#i want to program to know it self that it is guessing the right ansewr without telling it C



# low = 1
# high = 20
#
# guess = 10
# # when you tell me to guess higher >> low = guess + 1
# low = 11
# high = 20
#
# guess = 15
# #when you tell me to guess lower >> high = guess - 1
# low = 11
# high = 14


# My recommended To-Do List:
# 1. List product on Etsy, TikTok Shop, Instagram, Facebook Marketplace
# 2. Add a section on your landing page that includes testimonials, "Compatible with various pods section"
# 3. Begin creating content (Paid ads or organic promotions)