l = [1, 4, 2, 3, 4, 1, 2, 3, 3, 1]
if not(len(l)%2):
    print(l[len(l)//2-1], l[len(l)//2])
else:
    print(l[len(l)//2])