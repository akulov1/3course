import numpy as np
import matplotlib.pyplot as plt

# Задаём параметры
N = 10000  # количество случайных точек
a, b = 5, np.sqrt(11)  # размеры охватывающего прямоугольника

# Функция для интегрирования
def f(x):
    return np.sqrt(11 - np.sin(x)**2)

# Генерация случайных точек
x_rand = np.random.uniform(0, a, N)
y_rand = np.random.uniform(0, b, N)

# Проверка условий попадания точек под график
y_f = f(x_rand)
inside = y_rand < y_f
M = np.sum(inside)

# Приближённое значение интеграла
integral = M / N * a * b

# Оценка погрешности
std_dev = np.sqrt((integral * (a * b - integral)) / N)
relative_error = std_dev / integral

# Результаты
print(f"Количество точек N: {N}")
print(f"Количество точек внутри фигуры M: {M}")
print(f"Приближённое значение интеграла: {integral:.4f}")
print(f"Абсолютная погрешность: {std_dev:.4f}")
print(f"Относительная погрешность: {relative_error:.4%}")

# Визуализация точек и графика
x_vals = np.linspace(0, a, 500)
y_vals = f(x_vals)

plt.figure(figsize=(8, 5))
plt.plot(x_vals, y_vals, label="y = sqrt(11 - sin^2(x))", color="blue")
plt.scatter(x_rand, y_rand, s=2, c=inside, cmap="coolwarm", label="Точки (внутри/снаружи)")
plt.xlabel("x")
plt.ylabel("y")
plt.title("Метод Монте-Карло для интеграла")
plt.legend()
plt.grid()
plt.show()
