import numpy as np
import matplotlib.pyplot as plt


def jacobi_method(A, b, x0, tol=1e-6, max_iter=1000):
    n = len(b)
    x = x0.copy()
    x_prev = x0.copy()
    nevyazki = []

    for k in range(max_iter):
        for i in range(n):
            sum1 = sum(A[i][j] * x_prev[j] for j in range(n) if j != i)
            x[i] = (b[i] - sum1) / A[i][i]

        nevyazka = np.linalg.norm(np.dot(A, x) - b)
        nevyazki.append(nevyazka)

        if nevyazka < tol:
            break

        x_prev = x.copy()

    return x, nevyazki, k


def seidel_method(A, b, x0, tol=1e-6, max_iter=1000):
    n = len(b)
    x = x0.copy()
    nevyazki = []

    for k in range(max_iter):
        x_prev = x.copy()
        for i in range(n):
            sum1 = sum(A[i][j] * x[j] for j in range(i))
            sum2 = sum(A[i][j] * x_prev[j] for j in range(i + 1, n))
            x[i] = (b[i] - sum1 - sum2) / A[i][i]

        nevyazka = np.linalg.norm(np.dot(A, x) - b)
        nevyazki.append(nevyazka)

        if nevyazka < tol:
            break

    return x, nevyazki, k


def solve_and_plot(A, b, x0, tol=1e-6):
    x_jacobi, nevyazki_jacobi, iter_jacobi = jacobi_method(A, b, x0, tol)
    x_gauss_seidel, nevyazki_seidel, iter_seidel = seidel_method(A, b, x0, tol)

    # Построение графика
    plt.figure(figsize=(12, 6))
    plt.plot(nevyazki_jacobi, label=f'Метод Якоби (Итерации: {iter_jacobi})')
    plt.plot(nevyazki_seidel, label=f'Метод Зейделя (Итерации: {iter_seidel})')
    plt.yscale('log')
    plt.xlabel('Итерации')
    plt.ylabel('Норма невязки')
    plt.title('Сходимость итерационных методов')
    plt.legend()
    plt.grid(True)
    plt.show()

    return (x_jacobi, iter_jacobi), (x_gauss_seidel, iter_seidel)


A = np.array([
    [12.14, 1.32, -0.78,-2.75,14.78],
    [-0.89,16.75,1.88,-1.55,-12.14],
    [2.65, -1.27, -15.64,-0.64, -11.65],
    [2.44,1.52,1.93,-11.43,4.26]
], dtype=float)


b = A[:, -1]
A = A[:, :-1]

x0 = np.zeros(len(b))

solve_and_plot(A, b, x0)
