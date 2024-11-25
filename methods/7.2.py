import numpy as np
from scipy.interpolate import CubicSpline

def integrate_trapezoid(f, a, b, n):
    h = 1 / n
    x = np.linspace(a, b, n + 1)
    integral = h * (0.5 * f(x[0]) + 0.5 * f(x[-1]) + np.sum(f(x[1:-1])))
    return integral

def integrate_rectangle(f, a, b, n):
    h = 1 / n
    x = np.linspace(a, b - h, n) + h / 2
    integral = h * np.sum(f(x))
    return integral

# Функция для интегрирования
f_pi = lambda x: 4 / (1 + x**2)

# Значения n
n_values = [8, 32, 128]

print("Формулы трапеции и прямоугольника для π:")
print("n     Трапеции    Error   Прямоугольник    Error")
for n in n_values:
    trapezoid_result = integrate_trapezoid(f_pi, 0, 1, n)
    rectangle_result = integrate_rectangle(f_pi, 0, 1, n)
    print(f"{n:3d}   {trapezoid_result:.8f}   {abs(np.pi - trapezoid_result):.2e}   "
          f"{rectangle_result:.8f}   {abs(np.pi - rectangle_result):.2e}")


def integrate_spline(f, a, b, n):
    x = np.linspace(a, b, n + 1)
    y = f(x)
    spline = CubicSpline(x, y)
    return spline.integrate(a, b)

print("\nСплайн квадратуры для π:")
print("n     Сплайн           Error")
for n in n_values:
    spline_result = integrate_spline(f_pi, 0, 1, n)
    print(f"{n:3d}   {spline_result:.8f}   {abs(np.pi - spline_result):.2e}")


def cubic_spline(x, y, n):
    h = np.diff(x)
    alpha = np.zeros(n)
    l = np.ones(n)
    mu = np.zeros(n)
    z = np.zeros(n)

    for i in range(1, n - 1):
        alpha[i] = (3 / h[i] * (y[i + 1] - y[i]) - 3 / h[i - 1] * (y[i] - y[i - 1]))

    for i in range(1, n - 1):
        l[i] = 2 * (x[i + 1] - x[i - 1]) - h[i - 1] * mu[i - 1]
        mu[i] = h[i] / l[i]
        z[i] = (alpha[i] - h[i - 1] * z[i - 1]) / l[i]

    l[n - 1] = 1
    z[n - 1] = 0
    c = np.zeros(n)
    b = np.zeros(n)
    d = np.zeros(n)

    for j in range(n - 2, -1, -1):
        c[j] = z[j] - mu[j] * c[j + 1]
        b[j] = (y[j + 1] - y[j]) / h[j] - h[j] * (c[j + 1] + 2 * c[j]) / 3
        d[j] = (c[j + 1] - c[j]) / (3 * h[j])

    a = y[:-1]

    return a, b, c, d, x


def spline_integral(x, a, b, c, d, n, step=0.001):
    integral = 0
    for i in range(n - 1):
        for xi in np.arange(x[i], x[i + 1], step):
            h = xi - x[i]
            integral += a[i] + b[i] * h + c[i] * h ** 2 + d[i] * h ** 3
    return integral


def true_integral():
    return np.pi

def f(x):
    return 4/(1+x*x)

n_values = [8, 32, 128]
h_values = [1 / 8, 1 / 32, 1 / 128]

# print("Использование сплайн-квадратуры для интеграла от f(x):")
# print("n     Integral (Spline)       Error")
# for n in n_values:
#
#     x = np.linspace(0, 1, n)
#     y = f(x)
#
#     a, b, c, d, x_new = cubic_spline(x, y, n)
#
#     integral_value = spline_integral(x_new, a, b, c, d, n)
#
#     error = abs(true_integral() - integral_value)
#
#     print(f"{n:3d}   {integral_value:.8f}   {error:.2e}")
