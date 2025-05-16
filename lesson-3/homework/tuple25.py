t = (11, 2, 45, 12, 2, 4, 1, 3, 2, 45)
l = list(t)
l.sort()
l1 = []
if l[0] != l[1]:
    l1.append(l[0])
for i in range(1, len(l)-1):
    if l[i-1] != l[i] and l[i] != l[i+1]:
        l1.append(l[i])
if l[-2] != l[-1]:
    l.append(l[-1])
t = tuple(l1)
print(t)