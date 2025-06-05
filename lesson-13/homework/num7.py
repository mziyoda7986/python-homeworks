import numpy as np
import random

a = np.random.rand(5, 5)*10
print(a)
print((a-a.min())/(a.max()-a.min()))