l = ['a', 'e', 'i', 'o', 'u']
s = input()
ss = ''
c = 0
for i in range(len(s)-1):
    c += 1
    ss += s[i]
    if c > 2 and not(l.count(s[i])):
        ss += '_'
        l.append(s[i])
        c = 0
ss += s[-1]
print(ss)