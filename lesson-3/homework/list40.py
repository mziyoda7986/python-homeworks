l = [1, -33, 4, -2, 3, 13, 4, 1, 2, -3, 3, 31, 33, 2]
l.sort()
ll = []
if l[0] != l[1]:
    ll.append(l[0])
for i in range(1, len(l)-1):
    if l[i-1] != l[i] and l[i] != l[i+1]:
        ll.append(l[i])
if l[-1] != l[-2]:
    ll.append(l[-1])
print(ll)