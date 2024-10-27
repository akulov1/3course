import matplotlib.pyplot as plt
import numpy as np

# Реализация функции f(x) = 1 / (1 + 25 * x^2)
def f(x):
    return 1 / (1 + 25 * x**2)

# Реализация кубического сплайна с нулевыми вторыми производными на концах (натуральный сплайн)
def cubic_spline(x, y, xi):
    n = len(x)
    a = y.copy()
    h = [x[i+1] - x[i] for i in range(n-1)]

    # Составление системы уравнений
    alpha = [0] + [3 * (a[i+1] - a[i]) / h[i] - 3 * (a[i] - a[i-1]) / h[i-1] for i in range(1, n-1)] + [0]

    l = [1] + [0] * (n-1)
    mu = [0] * (n-1)
    z = [0] * n

    for i in range(1, n-1):
        l[i] = 2 * (x[i+1] - x[i-1]) - h[i-1] * mu[i-1]
        mu[i] = h[i] / l[i]
        z[i] = (alpha[i] - h[i-1] * z[i-1]) / l[i]

    l[n-1] = 1
    z[n-1] = 0
    c = [0] * n
    b = [0] * (n-1)
    d = [0] * (n-1)

    # Обратный проход
    for j in range(n-2, -1, -1):
        c[j] = z[j] - mu[j] * c[j+1]
        b[j] = (a[j+1] - a[j]) / h[j] - h[j] * (c[j+1] + 2 * c[j]) / 3
        d[j] = (c[j+1] - c[j]) / (3 * h[j])

    # Вычисление значений сплайна в точке xi
    i = max(0, min(n-2, np.searchsorted(x, xi) - 1))
    dx = xi - x[i]
    spline_value = a[i] + b[i] * dx + c[i] * dx**2 + d[i] * dx**3
    return spline_value

# Построение графика функции и сплайна
def plot_spline_and_function(n_values):
    x_exact = np.linspace(-1, 1, 1000)
    y_exact = f(x_exact)

    plt.figure(figsize=(12, 8))
    plt.plot(x_exact, y_exact, label="f(x)", color="blue")

    for n in n_values:
        x_points = np.linspace(-1, 1, n+1)
        y_points = f(x_points)

        # Построение сплайна на мелкой сетке
        x_spline = np.linspace(-1, 1, 1000)
        y_spline = [cubic_spline(x_points, y_points, xi) for xi in x_spline]

        plt.plot(x_spline, y_spline, label=f"Сплайн при n={n}", linestyle='--')

        # Отобразим узловые точки
        plt.scatter(x_points, y_points, color="red")

    plt.title("График функции f(x) и кубического сплайна")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.legend()
    plt.grid(True)
    plt.show()

# Выполнение задачи 1
plot_spline_and_function([4, 8, 16])

# Данные для второй задачи
x_table = [2, 3, 5, 7]
y_table = [4, -2, 6, -3]

# Проверка значений сплайна в узловых точках
spline_values_at_nodes = [cubic_spline(x_table, y_table, xi) for xi in x_table]

# Построение графика сплайна и отображение узловых точек
def plot_table_spline(x_table, y_table):
    x_spline = np.linspace(min(x_table), max(x_table), 1000)
    y_spline = [cubic_spline(x_table, y_table, xi) for xi in x_spline]

    plt.figure(figsize=(12, 8))
    plt.plot(x_spline, y_spline, label="Кубичексий сплайн", color="green")
    plt.scatter(x_table, y_table, color="red", label="Узлы")

    plt.title("График кубического сплайна для заданной таблицы")
    plt.xlabel("x")
    plt.ylabel("f(x)")
    plt.legend()
    plt.grid(True)
    plt.show()

# Выполнение второй задачи
plot_table_spline(x_table, y_table)

# Вывод значений сплайна в узловых точках для проверки
spline_values_at_nodes
