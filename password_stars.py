MINIMUM_LENGTH = 5
password = input("Enter your password: ")
while len(password) < MINIMUM_LENGTH:
    print("The password doesn't meet the minimum length")
    password = input("Enter your password: ")
print("*" * len(password))


