import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-10, 10, 1000)
y1 = x ** 3
y2 = np.sin(x)
y3 = np.exp(x)
y4 = np.where(x >= 0, np.log(x+1), np.nan)

plt.subplot(2, 2, 1)
plt.plot(x, y1, label = '$f(x) = x^3$', color='red')
plt.title('Parabola')
plt.xlabel('x')
plt.ylabel('y', rotation=0)
plt.legend(loc='lower right')

plt.subplot(2, 2, 2)
plt.plot(x, y2, label = '$f(x) = \sin(x)$', color='green')
plt.title('Trigonometric function')
plt.xlabel('x')
plt.ylabel('y', rotation=0)
plt.legend(loc='lower right')

plt.subplot(2, 2, 3)
plt.plot(x, y3, label = '$f(x) = e^x$', color='blue')
plt.title('Exponential function')
plt.xlabel('x')
plt.ylabel('y', rotation=0)
plt.legend(loc='lower right')

plt.subplot(2, 2, 4)
plt.plot(x, y4, label = '$f(x) = \log(x+1)$', color='black')
plt.title('Logarithmic function')
plt.xlabel('x')
plt.ylabel('y', rotation=0)
plt.legend(loc='lower right')

plt.show()