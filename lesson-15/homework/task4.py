import matplotlib.pyplot as plt
import numpy as np

x = np.random.uniform(0, 10, 100)
y = np.random.uniform(0, 10, 100)

colors = np.random.rand(100)
markers = ['o', 's', '^', 'D', 'P', '*']
chosen_markers = np.random.choice(markers, 100)

for marker in markers:
    i = (chosen_markers == marker)
    plt.scatter(x[i], y[i], c = colors[i], marker=marker, cmap='viridis')

plt.title('Scatter Plot of 100 Random Points')
plt.xlabel('X-axis')
plt.ylabel('Y-axis', rotation=0)
plt.grid(True)

plt.show()