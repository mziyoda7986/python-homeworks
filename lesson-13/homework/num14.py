import numpy as np

a = np.random.rand(3, 3)
b = np.random.rand(3)
print(np.linalg.solve(a, b))