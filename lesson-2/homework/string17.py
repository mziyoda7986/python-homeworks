s = input("Enter string: ")
ss = ""
for i in s:
    if i=='a' or i=='i' or i=='o' or i=='e' or i=='u':
        ss += "*"
    else:
        ss += i
print(ss)