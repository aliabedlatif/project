username = input("enter the username:")
password = int(input("enter the password:"))

if username == "admin" and password == 1234:
    print("access granted")
else:
    print("access denied")