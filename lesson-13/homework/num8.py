import numpy as np

a = np.arange(10, 25).reshape(5, 3)
b = np.arange(1, 7).reshape(3, 2)
ans = np.dot(a, b)
print(ans)