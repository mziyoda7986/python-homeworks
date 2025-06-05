import numpy as np

a = np.array([
    [1, 2, 3, 4, 5],
    [4, 5, 6, 7, 8],
    [6, 7, 8, 9, 10],
    [9, 8, 7, 6, 5],
    [7, 6, 5, 4, 3]
])

print(a.sum(axis=0), a.sum(axis=1))