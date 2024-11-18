import numpy as np
import matplotlib.pyplot as plt

# Определение функции f(x)
def f(x):
    return np.where(
        (x >= 0) & (x < 1),
        10 * x,
        10 * (x - 20) / -19
    )

# Построение графика функции
x_vals = np.linspace(0, 20, 500)
y_vals = f(x_vals)

plt.figure(figsize=(8, 5))
plt.plot(x_vals, y_vals, label="y = f(x)", color="blue")
plt.axhline(0, color="black", linewidth=0.5, linestyle="--")
plt.axvline(0, color="black", linewidth=0.5, linestyle="--")
plt.xlabel("x")
plt.ylabel("y")
plt.title("График функции y = f(x)")
plt.legend()
plt.grid()
plt.show()

# Метод Монте-Карло
N = 1000  # количество случайных точек
a = 20 #так как x∈[0,20]
b=10 #так как максимум функции f(x) достигается при x=1, где f(1)=10

# Генерация случайных точек
x_rand = np.random.uniform(0, a, N)
y_rand = np.random.uniform(0, b, N)

#проверка условий попадания точек в фигуру
y_f = f(x_rand)
inside = y_rand < y_f
M = np.sum(inside)

area = M / N * a * b

# Оценка погрешности
abs_dev = np.sqrt((area * (a * b - area)) / N)
otnos_abs = abs_dev / area

print(f"Количество точек N: {N}")
print(f"Количество точек внутри фигуры M: {M}")
print(f"Приближённая площадь фигуры: {area:.4f}")
print(f"Абсолютная погрешность: {abs_dev:.4f}")
print(f"Относительная погрешность: {otnos_abs:.4%}")

plt.figure(figsize=(8, 5))
plt.plot(x_vals, y_vals, label="y = f(x)", color="blue")
plt.scatter(x_rand, y_rand, s=2, c=inside, cmap="coolwarm", label="Точки (внутри/снаружи)")
plt.xlabel("x")
plt.ylabel("y")
plt.title("Метод Монте-Карло")
plt.legend()
plt.grid()
plt.show()
