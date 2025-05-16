l = [1, 4, 2, 3, 4, 1, 2, 3, 3, 1, 2]
i = 6
if len(l) > i:
    l = l[:i]+l[i+1:]
    print(l)
else:
    print("Error")