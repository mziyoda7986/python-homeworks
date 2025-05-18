def is_prime(num):
    if num > 1:
        for i in range(2, int(num**0.5)+1):
            if not(num % i):
                return False
        return True
    else:
        return False
    
x = int(input("Enter a number: "))
print(is_prime(x))