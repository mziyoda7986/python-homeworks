d = {1:'a', 2:{3:'a', 4:'b'}, 3:'tt', 7:'y', 8:'a'}
b = True
for i in d.values():
    if type(i) == dict:
        print("Nested dictionary")
        b = False
        break
if b:
    print("No Nested dictionary")