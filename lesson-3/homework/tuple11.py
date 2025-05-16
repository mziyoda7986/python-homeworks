t = (11, 2, 3, 12, 2, 4, 1, 3, 2, 45)
n = t.count(3)
i = -1
for e in range(n):
    i = t.index(3, i+1)
    print(i)