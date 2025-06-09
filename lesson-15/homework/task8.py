import matplotlib.pyplot as plt
import numpy as np

time = ['T1', 'T2', 'T3', 'T4']
x = np.arange(len(time))

cat_a = [20, 35, 30, 35]
cat_b = [25, 32, 34, 20]
cat_c = [15, 18, 20, 25]

plt.bar(x, cat_a, label='Category A', color='yellow')
plt.bar(x, cat_b, bottom=cat_a, label='Category B', color='skyblue')
bottom_c = np.array(cat_a)+np.array(cat_b)
plt.bar(x, cat_c, bottom=bottom_c, label='Catrgory C', color='violet')
plt.title('Bar Chars of Categories over Time')
plt.xlabel('time')
plt.ylabel('values', rotation=0)
plt.xticks(x, time)
plt.legend()
plt.grid()

plt.tight_layout()
plt.show()