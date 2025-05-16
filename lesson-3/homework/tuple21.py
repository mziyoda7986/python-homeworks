t = (11, 2, 45, 12, 2, 4, 1, 3, 2, 45)
num = 2
l = []
for i in t:
    for e in range(num):
        l.append(i)
t = tuple(l)
print(t)