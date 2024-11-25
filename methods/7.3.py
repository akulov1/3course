import numpy as np

#Для этого мы можем использовать метод Симпсона
# (он подходит для гладких функций и обеспечивает высокую точность
# с меньшим числом разбиений), метод трапеций или метод прямоугольников.

def f(x):
    if 0 <= x <= 2:
        return np.exp(x ** 2)  # e^(x^2) для 0 <= x <= 2
    elif 2 < x <= 4:
        return 1 / (4 - np.sin(16 * np.pi * x))  # 1 / (4 - sin(16 * pi * x)) для 2 <= x <= 4
    else:
        return 0


# Метод Симпсона для численного интегрирования
def simpsons_method(a, b, n):
    h = (b - a) / n  # шаг
    integral = f(a) + f(b)

    for i in range(1, n, 2):
        integral += 4 * f(a + i * h)
    for i in range(2, n - 1, 2):
        integral += 2 * f(a + i * h)

    integral *= h / 3
    return integral

a1, b1 = 0, 2
a2, b2 = 2, 4
n = 100

# Интеграл на интервале [0, 2]
integral1 = simpsons_method(a1, b1, n)

# Интеграл на интервале [2, 4] с методом Симпсона
integral2 = simpsons_method(a2, b2, n)

total_integral = integral1 + integral2

print(f"Интеграл на интервале [0, 2]: {integral1}")
print(f"Интеграл на интервале [2, 4] методом Симпсона: {integral2}")
print(f"Общий интеграл: {total_integral}")
