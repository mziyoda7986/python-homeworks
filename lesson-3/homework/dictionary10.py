d = {1:'a', 2:'cd', 3:'tt', 7:'y'}
k = 3
if(bool(k in d.keys())):
    print(f"key: {k}, value: {d[k]}")
else:
    print("Key doesn't exist")