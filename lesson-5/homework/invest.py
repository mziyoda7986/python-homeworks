def invest(amount, rate, years):
    for i in range(1, years+1):
        amount *= (1+rate)
        print(f"year {i}: ${round(amount, 2)}")

a = float(input("Enter an initial amount: "))
r = float(input("Enyer an annual percentage rate: "))
y = int(input("Enter a number of years: "))
invest(a, r, y)