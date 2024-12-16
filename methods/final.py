import numpy as np
import matplotlib.pyplot as plt


def solve_explicit(Nx, Nt, T):
    """Явная схема."""
    L = np.pi / 2
    dx = L / Nx
    dt = T / Nt

    x = np.linspace(0, L, Nx + 1)
    t = np.linspace(0, T, Nt + 1)

    u = np.zeros((Nt + 1, Nx + 1))

    # Начальное условие
    u[0, :] = np.sin(x)

    # Граничные условия
    u[:, 0] = 0
    u[:, -1] = np.exp(-t)

    # Коэффициент
    r = dt / dx ** 2
    if r > 0.5:
        raise ValueError("Явная схема неустойчива, уменьшите шаги dx или dt.")

    # Основной цикл явной схемы
    for n in range(0, Nt):
        for i in range(1, Nx):
            u[n + 1, i] = u[n, i] + r * (u[n, i - 1] - 2 * u[n, i] + u[n, i + 1])

    return x, t, u
def solve_implicit(Nx, Nt, T):
    """Неявная схема."""
    L = np.pi / 2
    dx = L / Nx
    dt = T / Nt

    x = np.linspace(0, L, Nx + 1)
    t = np.linspace(0, T, Nt + 1)

    u = np.zeros((Nt + 1, Nx + 1))

    # Начальное условие
    u[0, :] = np.sin(x)

    # Граничные условия
    u[:, 0] = 0
    u[:, -1] = np.exp(-t)

    # Коэффициенты матрицы
    r = dt / dx ** 2
    A = np.zeros((Nx - 1, Nx - 1))
    for i in range(Nx - 1):
        A[i, i] = 1 + 2 * r
        if i > 0:
            A[i, i - 1] = -r
        if i < Nx - 2:
            A[i, i + 1] = -r

    # Основной цикл неявной схемы
    for n in range(0, Nt):
        if Nx > 1:  # Проверяем, чтобы уравнение имело внутренние узлы
            b = u[n, 1:-1].copy()
            # Учёт граничных условий на текущем шаге
            b[0] += r * u[n + 1, 0]  # левая граница (всегда 0)
            b[-1] += r * np.exp(-t[n + 1])  # правая граница exp(-t[n+1])

            u[n + 1, 1:-1] = np.linalg.solve(A, b)
        else:
            u[n + 1, :] = u[n, :]  # Если Nx == 1, внутренние узлы отсутствуют

    return x, t, u


def exact_solution(x, t):
    """Точное решение."""
    return np.exp(-t)[:, None] * np.sin(x)


def plot_results(x, t, u_exp, u_imp, u_exact):
    """Построение графиков в разрезе по времени и пространству."""
    plt.figure(figsize=(16, 12))

    # Сравнение в фиксированный момент времени
    time_idx = len(t) // 2
    plt.subplot(2, 2, 1)
    plt.plot(x, u_exp[time_idx, :], label='Явная схема', marker='o')
    plt.plot(x, u_imp[time_idx, :], label='Неявная схема', marker='x')
    plt.plot(x, u_exact[time_idx, :], label='Точное решение', linestyle='--')
    plt.title(f"Сравнение решений при t = {t[time_idx]:.2f}")
    plt.xlabel("x")
    plt.ylabel("u")
    plt.legend()
    plt.grid()

    # Эволюция решения в фиксированной точке пространства
    space_idx = len(x) // 2
    plt.subplot(2, 2, 2)
    plt.plot(t, u_exp[:, space_idx], label='Явная схема', marker='o')
    plt.plot(t, u_imp[:, space_idx], label='Неявная схема', marker='x')
    plt.plot(t, u_exact[:, space_idx], label='Точное решение', linestyle='--')
    plt.title(f"Эволюция решения в точке x = {x[space_idx]:.2f}")
    plt.xlabel("t")
    plt.ylabel("u")
    plt.legend()
    plt.grid()

    # Ошибки явной схемы
    plt.subplot(2, 2, 3)
    error_exp = np.abs(u_exp - u_exact)
    plt.imshow(error_exp, extent=[0, np.pi / 2, 0, t[-1]], origin='lower', aspect='auto', cmap='viridis')
    plt.colorbar(label='Ошибка')
    plt.title("Ошибка явной схемы")
    plt.xlabel("x")
    plt.ylabel("t")

    # Ошибки неявной схемы
    plt.subplot(2, 2, 4)
    error_imp = np.abs(u_imp - u_exact)
    plt.imshow(error_imp, extent=[0, np.pi / 2, 0, t[-1]], origin='lower', aspect='auto', cmap='viridis')
    plt.colorbar(label='Ошибка')
    plt.title("Ошибка неявной схемы")
    plt.xlabel("x")
    plt.ylabel("t")

    plt.tight_layout()
    plt.show()


def analyze_results(u_exp, u_imp, u_exact):
    """Аналитический анализ ошибок."""
    error_exp = np.abs(u_exp - u_exact)
    error_imp = np.abs(u_imp - u_exact)

    max_error_exp = np.max(error_exp)
    max_error_imp = np.max(error_imp)

    print("Анализ ошибок:")
    print(f"Максимальная ошибка явной схемы: {max_error_exp:.5e}")
    print(f"Максимальная ошибка неявной схемы: {max_error_imp:.5e}")

    print("\nСредняя ошибка по времени и пространству:")
    print(f"Явная схема: {np.mean(error_exp):.5e}")
    print(f"Неявная схема: {np.mean(error_imp):.5e}")


def main():
    # Ввод параметров
    while True:
        try:
            Nx = int(input("Введите число шагов по пространству Nx (целое число > 0): "))
            Nt = int(input("Введите число шагов по времени Nt (целое число > 0): "))
            T = float(input("Введите конечное время T (положительное число): "))
            if Nx <= 0 or Nt <= 0 or T <= 0:
                raise ValueError("Все значения должны быть положительными.")
            break
        except ValueError as e:
            print(f"Ошибка ввода: {e}. Попробуйте снова.")

    # Решение явной схемой
    try:
        x_exp, t_exp, u_exp = solve_explicit(Nx, Nt, T)
    except ValueError as e:
        print(e)
        return

    # Решение неявной схемой
    x_imp, t_imp, u_imp = solve_implicit(Nx, Nt, T)

    # Точное решение
    x_exact = np.linspace(0, np.pi / 2, Nx + 1)
    t_exact = np.linspace(0, T, Nt + 1)
    u_exact = exact_solution(x_exact, t_exact)

    # Построение графиков
    plot_results(x_exact, t_exact, u_exp, u_imp, u_exact)

    # Аналитический анализ
    analyze_results(u_exp, u_imp, u_exact)


if __name__ == "__main__":
    main()
