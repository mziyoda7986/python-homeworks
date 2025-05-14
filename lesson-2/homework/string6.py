s = input()
ss = input()
if len(s) < len(ss):
    a = s
    s = ss
    ss = a
if ss in s:
    print(f"{ss} is found in {s}")
else:
    print(f"{ss} is not found in {s}")