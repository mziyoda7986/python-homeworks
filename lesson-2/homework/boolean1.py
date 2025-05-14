un = input("Enter username: ")
ps = input("Enter password: ")
if bool(un.strip()) and bool(ps.strip()):
    print("Entered successfully!")
else:
    print("Please enter again!")  