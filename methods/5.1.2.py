
import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import CubicSpline

def f(x):
    return 1 / (1 + 25 * x ** 2)


n_values = [5, 10, 15] #значения n для сплайна
x_plot = np.linspace(-1, 1, 1000)

f_values = f(x_plot)


plt.figure(figsize=(18, 12))

for i, n in enumerate(n_values, 1):
    x_nodes = np.linspace(-1, 1, n)
    y_nodes = f(x_nodes)

    spline = CubicSpline(x_nodes, y_nodes)#построение кубического сплайна по равноотстоящим узлам
    f_spline = spline(x_plot)

    plt.subplot(3, 1, i)
    plt.plot(x_plot, f_values, 'r-', label='f(x)')
    plt.plot(x_plot, f_spline, 'b--', label=f'Кубический сплайн (n={n})')
    plt.scatter(x_nodes, y_nodes, color='blue', marker='o')
    plt.title(f'Кубический сплайн интерполяции для n={n}')
    plt.legend()
    plt.grid(True)

plt.suptitle('Интерполяция функции f(x) = 1/(1+25x^2) на отрезке [-1, 1] с помощью кубического сплайна')
plt.tight_layout()
plt.show()
