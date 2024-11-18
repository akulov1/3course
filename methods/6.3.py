import numpy as np
import matplotlib.pyplot as plt

# Радиус круга
R = 1
N = 1000  # Количество случайных точек

# Генерация случайных точек в квадрате [-R, R] x [-R, R]
x_rand = np.random.uniform(-R, R, N)
y_rand = np.random.uniform(-R, R, N)

# Проверяем, какие точки попали внутрь круга
inside_circle = x_rand**2 + y_rand**2 <= R**2
M = np.sum(inside_circle)

# Оценка числа π
pi_estimate = 4 * M / N

# Результаты
print(f"Общее количество точек N: {N}")
print(f"Количество точек внутри круга M: {M}")
print(f"Приближённое значение числа π: {pi_estimate:.5f}")
print(f"Абсолютная ошибка: {abs(np.pi - pi_estimate):.5f}")

# Построение окружности и визуализация точек
phi = np.linspace(0, 2 * np.pi, 500)
x_circle = R * np.cos(phi)
y_circle = R * np.sin(phi)

plt.figure(figsize=(8, 8))
plt.plot(x_circle, y_circle, label="Окружность", color="blue")
plt.scatter(x_rand, y_rand, s=2, c=inside_circle, cmap="coolwarm", label="Точки (внутри/снаружи)")
plt.axhline(0, color="black", linewidth=0.5, linestyle="--")
plt.axvline(0, color="black", linewidth=0.5, linestyle="--")
plt.xlim(-R, R)
plt.ylim(-R, R)
plt.gca().set_aspect('equal', adjustable='box')
plt.xlabel("x")
plt.ylabel("y")
plt.title(f"Метод Монте-Карло: приближённое значение π = {pi_estimate:.5f}")
plt.legend()
plt.grid()
plt.show()
