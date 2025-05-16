l = [1, -33, 4, -2, 3, 13, 4, 1, 2, -3, 3, 31, 33, 2]
ll = []
for i in range(0, len(l), 2):
    l1 = []
    l1.append(l[i])
    l1.append(l[i+1])
    ll.append(l1)
print(ll)