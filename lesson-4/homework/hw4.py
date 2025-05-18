import random

b = True
while b:
    n = random.randint(1, 100)
    i = 0
    while True and i < 10:
        i += 1
        g = int(input("Guess the number: "))
        if g > n:
            print("Too high!")
        elif g < n:
            print("Too low!")
        else:
            print("You guessed it right!")
            b = False
            break
    else:
        ans = input("You lost. Want to play again? ")
        if not(ans.lower() in ['y', 'yes', 'ok']):
            break
