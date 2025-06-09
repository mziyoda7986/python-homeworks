import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-5, 5, 1000)
y = np.linspace(-5, 5, 1000)
X, Y = np.meshgrid(x, y)
f = np.cos(X ** 2 + Y ** 2)
fig = plt.figure()
ax = plt.axes(projection='3d')
ax.plot_surface(X, Y, f, cmap='viridis', label='$f(x) = \cos(x^2 + y^2)$')
ax.set_title('3D Surface')
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')
ax.legend()
plt.show()