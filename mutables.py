shopping_list = ['milk', 'pasta', 'eggs', 'spam', 'bread', 'rice']

another_list = shopping_list
print(id(shopping_list))
print(id(another_list))

shopping_list.append('bananas')
print(shopping_list)
print()
print(another_list)

a = b = c = d = another_list
b.append('cockies')
print(d)
print(shopping_list)
print(a)