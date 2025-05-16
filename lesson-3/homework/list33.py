l = [1, 4, 2, 3, 4, 1, 2, 3, 3, 1, 2]
num = l.count(3)
ii = -1
for i in range(num):
    ii += l.index(3) + 1
    print(ii)
    l = l[l.index(3)+1:]