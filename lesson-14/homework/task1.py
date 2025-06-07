import numpy as np

@np.vectorize
def fah_to_cel(x):
    return (x-32)*5/9

a = np.array([32, 68, 100, 212, 77])
print(fah_to_cel(a))