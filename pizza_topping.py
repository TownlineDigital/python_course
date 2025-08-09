available_toppings = ['pepperoni', 'meat balls', 'cheese', 'pineapple']
topping_chosen = ''
while topping_chosen not in available_toppings:
    topping_chosen = input('what do you want on your pizza:')
    if topping_chosen.casefold() == 'quit':
        break