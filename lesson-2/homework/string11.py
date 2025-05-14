s = input("Enter string: ")
b = True
for i in s:
    if i.isdigit():
        print("String has a digit")
        b = False
        break
if b:
    print("String has not any digit")