import numpy as np

# Метод Кардано для кубического уравнения
def cardano_method(alpha):
    # Исходные коэффициенты
    a, b, c = 2, 2, 2

    # Коэффициенты приведенной формы
    p = b - (a**2 / 3)
    q = c - (a * b / 3) + (2 * a**3 / 27) + alpha

    # Кардано для нахождения одного корня
    term1 = (-q / 2) + np.sqrt((q / 2)**2 + (p / 3)**3)
    term2 = (-q / 2) - np.sqrt((q / 2)**2 + (p / 3)**3)

    s1 = term1**(1 / 3) if term1 >= 0 else -(-term1)**(1 / 3)
    s2 = term2**(1 / 3) if term2 >= 0 else -(-term2)**(1 / 3)

    y1 = s1 + s2
    x1 = y1 - a / 3
    return x1

# Метод Ньютона для эталонного решения
def newton_method(alpha, x0=-1, tol=1e-6, max_iter=100):
    def f(x):
        return x**3 + 2*x**2 + 2*x + alpha

    def f_prime(x):
        return 3*x**2 + 4*x + 2

    x = x0
    for _ in range(max_iter):
        fx = f(x)
        fpx = f_prime(x)
        if abs(fpx) < tol:
            raise ValueError("Производная близка к нулю")
        x_next = x - fx / fpx
        if abs(x_next - x) < tol:
            return x_next
        x = x_next
    raise RuntimeError("Метод Ньютона не сошелся за заданное число итераций")

# Исследование для различных alpha
alphas = [10**15, 10**16, 10**17]  # Большие значения alpha
results = []

for alpha in alphas:
    root_cardano = cardano_method(alpha)
    root_newton = newton_method(alpha)
    relative_error = abs(root_cardano - root_newton) / abs(root_newton)
    results.append((alpha, root_cardano, root_newton, relative_error))

# Вывод результатов
print("Исследование потери точности метода Кардано:")
print(f"{'alpha':<15} {'Cardano Root':<20} {'Newton Root':<20} {'Relative Error':<20}")
for alpha, cardano, newton, error in results:
    print(f"{alpha:<15} {cardano:<20.10f} {newton:<20.10f} {error:<20.10f}")
