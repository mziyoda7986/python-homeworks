s = {1, 5, 3, 4, 2}
ss = set()
for i in s:
    if not(i%2):
        ss.add(i)
print(ss)