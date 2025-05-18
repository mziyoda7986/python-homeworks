import random

comp = 0; user = 0
while comp < 5 and user < 5:
    ch = ['rock', 'paper', 'scissors']
    c = random.choice(ch)
    #print(c)
    u = input("Enter rock(r), paper(p) or scissors(s): ")
    if c == 'rock':
        if u == 'p':
            user += 1
        elif u == 's':
            comp += 1
    elif c == 'paper':
        if u == 's':
            user += 1
        elif u == 'r':
            comp += 1
    else:
        if u == 'r':
            user += 1
        elif u == 'p':
            comp += 1
    print(f"Computer's choice: {c} and user's choice: {u}")
    print("Score: Computer =", comp, ': User =', user)
if comp == 5:
    print("Computer wins!")
else:
    print("User wins!")