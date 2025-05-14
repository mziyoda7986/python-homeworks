n = input()
n = n.lower()
n1 = n[::-1]
if n == n1:
    print("Palindrome")
else:
    print("Not Palindrome")
