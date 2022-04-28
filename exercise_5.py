# 1 Create a user profile for your new game. This user profile will be stored in a dictionary with keys: 'age', 'username', 'weapons', 'is_active' and 'clan'

# Yeameen = {
#     'age': 24,
#     'username': 'DarkShadow98',
#     'weapons': ['Operator', 'Ak47', 'M4'],
#     'is_active': True,
#     'clan': 'Secret'
# }


# 2 iterate and print all the keys in the above user.
# print(Yeameen.keys())


# 3 Add a new weapon to your user
# Yeameen['weapons'].append('Desert-Eagle')
# print(Yeameen)


# 4 Add a new key to include 'is_banned'. Set it to false
# Yeameen.update({'is_banned': False})
# print(Yeameen)


# 5 Ban the user by setting the previous key to True
# Yeameen['is_banned'] = True
# print(Yeameen)


# 6 create a new user2 by copying the previous user and update the age value and username value.
# new_user = Yeameen.copy()
# new_user.update({'age': 30, 'username': 'Stealth02'})
# print(new_user)
