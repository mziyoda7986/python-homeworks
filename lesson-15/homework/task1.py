import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-10, 10, 1000)
y = x ** 2 - 4 * x + 4
plt.plot(x, y, label='$f(x) = x^2 - 4x + 4$')
plt.title('Parabola')
plt.xlabel('x')
plt.ylabel('y', rotation=0)
plt.legend()
plt.show()