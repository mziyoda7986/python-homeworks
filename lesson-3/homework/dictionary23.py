d1 = {1:'da', 4:'m', 2:'bb', 3:'tt', 7:'y', 8:'a'}
d2 = {11:'da', 4:'m', 21:'bb', 13:'tt', 7:'y', 8:'a'}
s1 = set(d1.keys())
s2 = set(d2.keys())
if s1 & s2 == set():
    print("No common key")
print(s1 & s2)