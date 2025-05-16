t = (11, 2, 45, 12, 2, 4, 1, 3, 2, 45)
l = []
for i in range(0, len(t)-1, 2):
    l1 = []
    l1.append(t[i])
    l1.append(t[i+1])
    t1 = tuple(l1)
    l.append(t1)
t = tuple(l)
print(t)
