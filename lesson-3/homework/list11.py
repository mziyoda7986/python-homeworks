l = [1, 2, 3, 4, 1, 2, 3, 3, 1, 2]
l.sort()
ll = []
ll.append(l[0])
for i in range(1, len(l)):
    if l[i] != ll[len(ll)-1]:
        ll.append(l[i])
print(ll)