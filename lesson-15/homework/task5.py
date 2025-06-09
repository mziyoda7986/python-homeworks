import matplotlib.pyplot as plt
import numpy as np

data = np.random.normal(loc=0, scale=1, size=1000)
plt.hist(data, bins=30, color='lightgreen', edgecolor='black', alpha=0.7)
plt.title('Histogram of Normally Distributed Data')
plt.xlabel('value')
plt.ylabel('frequency')

plt.grid(True)
plt.show()