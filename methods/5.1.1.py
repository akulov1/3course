import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import lagrange

def f(x):
    return 1 / (1 + 25 * x ** 2)

def chebyshev_nodes(n):
    return np.cos((2 * np.arange(1, n + 1) - 1) / (2 * n) * np.pi)

def lagrange_interpolation(x_nodes, y_nodes, x_values):
    polynomial = lagrange(x_nodes, y_nodes)
    return polynomial(x_values)

n_values = [5, 10, 15]
x_plot = np.linspace(-1, 1, 1000) #точки для построения графика

f_values = f(x_plot)

plt.figure(figsize=(18, 12))

for i, n in enumerate(n_values, 1):
    x_nodes_equal = np.linspace(-1, 1, n)#ravnootstoyashie
    y_nodes_equal = f(x_nodes_equal)
    f_lagrange_equal = lagrange_interpolation(x_nodes_equal, y_nodes_equal, x_plot)#Лагранж для равноотсоящих узлов

    x_nodes_cheb = chebyshev_nodes(n)#uzli chebisheva
    y_nodes_cheb = f(x_nodes_cheb)
    f_lagrange_cheb = lagrange_interpolation(x_nodes_cheb, y_nodes_cheb, x_plot)#Лагранж для узлов Чебышева

    plt.subplot(3, 2, 2 * (i - 1) + 1)
    plt.plot(x_plot, f_values, 'r-', label='f(x)')
    plt.plot(x_plot, f_lagrange_equal, 'b--', label=f'Лагранж (равноотстоящие, n={n})')
    plt.scatter(x_nodes_equal, y_nodes_equal, color='blue', marker='o')
    plt.title(f'Равноотстоящие узлы (n={n})')
    plt.legend()
    plt.grid(True)

    plt.subplot(3, 2, 2 * (i - 1) + 2)
    plt.plot(x_plot, f_values, 'r-', label='f(x)')
    plt.plot(x_plot, f_lagrange_cheb, 'g--', label=f'Лагранж (Чебышев, n={n})')
    plt.scatter(x_nodes_cheb, y_nodes_cheb, color='green', marker='o')
    plt.title(f'Узлы Чебышева (n={n})')
    plt.legend()
    plt.grid(True)

plt.suptitle('Интерполяция функции f(x) = 1/(1+25x^2) на отрезке [-1, 1]')
plt.tight_layout()
plt.show()
#для интерполяции Чебышев лучше