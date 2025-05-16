dd = {1:'da', 4:'m', 2:'bb', 3:'tt', 7:'y', 8:'a'}
d1 = {} #stores values ​​with length 1
for i in dd.keys():
    if len(dd[i]) < 2:
        d1.update({i: dd[i]})
print(d1)