l = [1, 4, 2, 3, 4, 1, 2, 3, 3, 1, 2]
minn = min(l)
num = l.count(minn)
for i in range(num):
    l.remove(minn)
print(min(l))