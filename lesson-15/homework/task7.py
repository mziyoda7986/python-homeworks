import matplotlib.pyplot as plt

products = ['Product A', 'Product B', 'Product C', 'Product D', 'Product E']
sales = [200, 150, 250, 175, 225]
colors = ['blue', 'red', 'green', 'yellow', 'purple']
plt.bar(products, sales, color=colors, width=0.8, edgecolor='k')
plt.title('Sales Data for Products')
plt.xlabel('Products')
plt.ylabel('Sales', rotation=0)
plt.show()