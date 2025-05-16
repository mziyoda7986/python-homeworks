d = {1:'a', 2:'cd', 3:'tt', 7:'y'}
k = 3
if(bool(k in d.keys())):
    d.pop(k)
    print(d)
else:
    print("Key doesn't exist")