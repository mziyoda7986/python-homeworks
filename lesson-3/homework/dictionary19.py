d = {1:'a', 2:'bb', 3:'tt', 7:'y', 8:'a'}
l = list(d.values())
c = 0
for i in l:
    if l.count(i) == 1:
        c += 1
print(c)