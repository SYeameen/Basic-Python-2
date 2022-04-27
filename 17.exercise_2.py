username = input("Enter your Username: ")
password = input("Enter your Password: ")
censoredPassword = '*' * len(password)
lenthOfPassword = len(password)

print(f"{username.capitalize()}, your password {censoredPassword} is {lenthOfPassword} letters long")
