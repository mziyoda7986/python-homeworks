def fuc(num):
    for i in range(1, num+1):
        if not(num % i):
            print(f"{i} is a factor of {num}")

n = int(input("Enter a positive integer: "))
fuc(n)