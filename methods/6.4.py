import numpy as np
import matplotlib.pyplot as plt

A = 12  # A = 11 + n, n = 1
B = 10  # B = 11 - n, n = 1
N = 10000  # Количество случайных точек

# Функция rho(phi) для полярной координаты
def rho(phi):
    return np.sqrt(A * np.cos(phi)**2 + B * np.sin(phi)**2)

rho_max = max(np.sqrt(A), np.sqrt(B))
a, b = rho_max, rho_max

x_rand = np.random.uniform(-a, a, N)
y_rand = np.random.uniform(-b, b, N)

# Преобразование случайных точек в полярные координаты для пункта 4
r_rand = np.sqrt(x_rand**2 + y_rand**2)
phi_rand = np.arctan2(y_rand, x_rand)

# Проверка попадания точек внутрь фигуры
rho_vals = rho(phi_rand)
inside = r_rand < rho_vals
M = np.sum(inside)

rectangle_area = (2 * a) * (2 * b)
S = M / N * rectangle_area

print(f"Общее количество точек N: {N}")
print(f"Количество точек внутри фигуры M: {M}")
print(f"Приближённая площадь фигуры: {S:.5f}")

# Построение фигуры и случайных точек, преобразование в декартову систему
phi_vals = np.linspace(0, 2 * np.pi, 500)
rho_curve = rho(phi_vals)
x_curve = rho_curve * np.cos(phi_vals)
y_curve = rho_curve * np.sin(phi_vals)

plt.figure(figsize=(8, 8))
plt.plot(x_curve, y_curve, label="Граница фигуры", color="blue")
plt.scatter(x_rand, y_rand, s=2, c=inside, cmap="coolwarm", label="Точки (внутри/снаружи)")
plt.axhline(0, color="black", linewidth=0.5, linestyle="--")
plt.axvline(0, color="black", linewidth=0.5, linestyle="--")
plt.xlim(-a, a)
plt.ylim(-b, b)
plt.gca().set_aspect('equal', adjustable='box')
plt.xlabel("x")
plt.ylabel("y")
plt.title(f"Метод Монте-Карло: площадь = {S:.5f}")
plt.legend()
plt.grid()
plt.show()
