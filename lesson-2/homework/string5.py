s = input()
s = s.lower()
v = 0
c = 0
for i in s:
    if i=='a' or i=='i' or i=='o' or i=='e' or i=='u':
        v += 1
    else:
        c += 1
print("Vowels:", v)
print("Consonants:", c)