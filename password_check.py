MINIMUM_LENGTH = 6
password = str(input("Enter password: "))
while len(password) < MINIMUM_LENGTH:
    print("Password must be longer than {}".format(MINIMUM_LENGTH))
    password = str(input("Enter password: "))
for character in password:
    print("*", end="")
