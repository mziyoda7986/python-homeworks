import numpy as np

@np.vectorize
def pow(x, y):
    return x**y

a = np.array([2, 3, 4, 5])
b = np.array([1, 2, 3, 4])
print(pow(a, b))