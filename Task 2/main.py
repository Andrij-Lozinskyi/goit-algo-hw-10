import matplotlib.pyplot as plt
import numpy as np
import scipy.integrate as spi

def f(x):
    return 2*x ** 3 + 4

a = 0  # Нижня межа
b = 2  # Верхня межа
n = 100000  

# Створення діапазону значень для x
x = np.linspace(-0.5, 2.5, 400)
y = f(x)

# Створення графіка
fig, ax = plt.subplots()

# Малювання функції
ax.plot(x, y, 'r', linewidth=2)

# Заповнення області під кривою
ix = np.linspace(a, b)
iy = f(ix)
ax.fill_between(ix, iy, color='gray', alpha=0.3)

# Налаштування графіка
ax.set_xlim([x[0], x[-1]])
ax.set_ylim([0, max(y) + 0.1])
ax.set_xlabel('x')
ax.set_ylabel('f(x)')

# Додавання меж інтегрування та назви графіка
ax.axvline(x=a, color='gray', linestyle='--')
ax.axvline(x=b, color='gray', linestyle='--')
ax.set_title('Графік інтегрування f(x) = x^2 від ' + str(a) + ' до ' + str(b))
plt.grid()
plt.show()

result, error = spi.quad(f, a, b)

x_random = np.random.uniform(a, b, n)
y_random = np.random.uniform(0, max(f(a), f(b)), n)

points_under_graph = np.sum(y_random < f(x_random))

area = (points_under_graph / n) * (b - a) * (max(f(a), f(b)) - 0)

print("Інтеграл: ", result)
print("Monte Carlo: ", area)