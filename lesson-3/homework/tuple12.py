t = (11, 2, 45, 3, 12, 2, 4, 1, 3, 2, 45)
l = []
maxn = max(t)
for i in t:
    if i != maxn:
        l.append(i)
print(max(l))