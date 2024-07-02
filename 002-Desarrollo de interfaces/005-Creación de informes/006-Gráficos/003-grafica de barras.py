import matplotlib.pyplot as plt

categories = ['A', 'B', 'C', 'D']
values = [25, 15, 35, 25]

plt.bar(categories, values, color='skyblue')

plt.title('Muestra')
plt.xlabel('Categorias')
plt.ylabel('Valores')

plt.show()
