# # Function - way to define
# def greet():
#     print('Good Morning!')


# greet()


# Parameters  -> used when define a function
# def greet(name, emoji):
#     print(f"Good Morning! {name}, {emoji}")


# # Arguments  -> used when call or invoke a function
# greet('Yeameen', '😆')

# # Keyword arguments
# greet(name='jonny', emoji='😆')


# return
# def sum(num1, num2):
#     def another_func(n1, n2):
#         return n1+n2
#     return another_func(num1, num2)


# total = sum(10, 20)
# print(total)


# DocString  -> Doc string is useful to add comments and definations to functions.
# def test(a):
#     '''
#     Info: this function tests and prints para...
#     '''
#     print(a)


# print(test.__doc__)


# Scope  ->  what variables do I have access to?

# a = 1


# def parent():
#     def confusion():
#         return sum
#     return confusion()


# print(parent())
# print(a)


# 1 - start with local
# 2 - Parent local(check)?
# 3 - Global
# 4 - built in python functions
