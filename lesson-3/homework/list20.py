l = [1, 4, 2, 3, 4, 1, 2, 3, 3, 1, 2]
maxn = max(l)
num = l.count(maxn)
for i in range(num):
    l.remove(maxn)
print(max(l))