# Dictionary  <- In other languages its called Hash Table/Map/Object. Its also a kind of data structure.
# dict


# dictionary = {
#     'a': 12,  # 'key':value pair
#     'b': 20,
#     'c': 5
# }
# print(dictionary)
# print(dictionary['b'])


# my_list = [
#     {
#         'a': [1, 5, 10],
#         'b':'Sweets',
#         'c':True
#     },
#     {
#         'x': [3, 50, 75],
#         'y':'Pastry',
#         'z':False
#     }
# ]
# print(my_list[0]['b'])


# Dictionary Methods    <- For more methods go to google

# Most Common Way to create dictionary
# user = {
#     'basket': [1, 2, 3],
#     'greet': 'Hello'
# }
# print(user.get('age', 30))


# Not a very common way to create dictionary
# user_2 = dict(name='Alex bex')
# print(user_2)


# Dictionary Methods-2
# user = {
#     'basket': [1, 2, 3, 4],
#     'age': 24,
#     'greet': 'hello'
# }

# print('greet' in user.keys())
# print('tips' in user.keys())
# print(24 in user.values())
# print(user.items())  # Most special method
# print(user.update({'new_person': 'Yeameen'}))
# print(user)
