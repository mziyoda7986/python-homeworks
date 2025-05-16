t = (11, 2, 45, 12, 2, 4, 1, 3, 2, 45)
l = []
for i in t:
    if i < 4:
        l.append(i)
t = tuple(l)
print(t)