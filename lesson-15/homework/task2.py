import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 2*np.pi, 1000)
y1 = np.sin(x)
y2 = np.cos(x)

plt.plot(x, y1, label='$f(x) = \sin(x)$', color='blue', linestyle='--')
plt.plot(x, y2, label='$f(x) = \cos(x)$', color='green')
plt.title('Trigonometric functions')
plt.xlabel('x')
plt.ylabel('y', rotation=0)
plt.legend()
plt.show()