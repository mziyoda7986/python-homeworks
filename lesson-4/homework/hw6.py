for i in range(2, 100):
    b = True
    for e in range(2, int(i**0.5)+1):
        #print(i, e)
        if not(i % e):
            b = False
            break
    if b:
        print(i)