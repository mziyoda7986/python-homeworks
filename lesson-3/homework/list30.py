l = [1, 4, 2, 3, 4, 1, 2, 3, 3, 1, 2]
l1 = l.copy()
l.sort()
print(bool(l1==l))