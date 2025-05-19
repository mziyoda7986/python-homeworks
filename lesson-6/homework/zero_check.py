def check(func):
    def wrapper(num1, num2):
        try:
            return func(num1, num2)
        except ZeroDivisionError:
            return "Denominator can't be zero"
    return wrapper

@check
def div(a, b):
   return a / b

a = float(input("Enter a numerator: "))
b = float(input("Enter a denominator: "))
print(div(a, b))