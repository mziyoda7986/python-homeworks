a1 = input("list1 = ")
a2 = input("list2 = ")
l1 = []; l2 = []
for i in a1:
    if i >= '0' and i <= '9':
        l1.append(i)
for i in a2:
    if i >= '0' and i <= '9':
        l2.append(i)
l3 = []
for i in l1:
    if not(l2.count(i)):
        l3.append(i)
for i in l2:
    if not(l1.count(i)):
        l3.append(i)
print(l3)