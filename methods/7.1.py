import numpy as np
from scipy.special import erf

# Функция ошибки для численного интегрирования
def erf_numeric(x, n=1000):
    a, b = 0, x  # пределы интегрирования
    h = (b - a) / n  # шаг
    t = np.linspace(a, b, n + 1)
    y = (2 / np.sqrt(np.pi)) * np.exp(-t**2)
    integral = h * (np.sum(y[:-1]) + np.sum(y[1:])) / 2
    return integral

# Генерация таблицы значений
x_values = np.arange(0.0, 2.1, 0.1)
erf_values_numeric = [erf_numeric(x) for x in x_values]
erf_values_exact = [erf(x) for x in x_values]

# Вывод таблицы
print(" x    erf через интеграл   erf табличное     Error")
for x, num, exact in zip(x_values, erf_values_numeric, erf_values_exact):
    print(f"{x:4.1f}   {num}   {exact}   {abs(num - exact):.2e}")
