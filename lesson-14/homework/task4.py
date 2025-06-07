import numpy as np

a = np.array([
    [10, -2, 3],
    [-2, 8, -1],
    [3, -1, 6]
])
b = np.array([12, -5, 15])
print(np.linalg.solve(a, b))