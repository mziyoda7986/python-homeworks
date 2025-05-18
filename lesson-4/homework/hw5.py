ps = input("Enter a password: ")

b = False
for i in ps:
    if i >= 'A' and i <= 'Z':
        b = True
        break

if len(ps) < 8:
    print("Password is too short.")
elif not(b):
    print("Password must contain an uppercase letter.")
else:
    print("Password is strong.")