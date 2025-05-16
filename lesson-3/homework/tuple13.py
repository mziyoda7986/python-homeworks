t = (11, 2, 45, 3, 12, 2, 4, 1, 3, 2, 45)
l = []
minn = min(t)
for i in t:
    if i != minn:
        l.append(i)
print(min(l))