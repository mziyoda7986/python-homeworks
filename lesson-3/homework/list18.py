l = [1, 2, 3, 4, 1, 2, 3, 3, 1, 2]
l1 = [1, 2, 3, 3, 4]
if l1[0] in l and l[l.index(l1[0]):l.index(l1[0])+len(l1)] == l1:
    print("Sublist exists within the list")
else:
    print("Sublist does not exist within the list")
