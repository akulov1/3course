import math
import matplotlib.pyplot as plt

x_vals = [2, 3, 4, 5, 6, 7]
y_vals = [100, 190, 270, 400, 500, 600]


#линейная аппроксимация y = a * x + b
def linear_fit(x, y):
    n = len(x)
    sum_x = sum(x)
    sum_y = sum(y)
    sum_x2 = sum([xi ** 2 for xi in x])
    sum_xy = sum([xi * yi for xi, yi in zip(x, y)])

    a = (n * sum_xy - sum_x * sum_y) / (n * sum_x2 - sum_x ** 2)
    b = (sum_y - a * sum_x) / n
    return round(a, 2), round(b, 2)


#степенная аппроксимация y = a * x^b
def power_fit(x, y):
    #ln(y) = ln(a) + b * ln(x)
    log_x = [math.log(xi) for xi in x]
    log_y = [math.log(yi) for yi in y]

    b, log_a = linear_fit(log_x, log_y)
    a = math.exp(log_a)
    return round(a, 2), round(b, 2)


# 1.3 Показательная аппроксимация y = a * e^(b * x)
def exponential_fit(x, y):
    # Преобразуем к линейной форме: ln(y) = ln(a) + b * x
    log_y = [math.log(yi) for yi in y]
    b, log_a = linear_fit(x, log_y)
    a = math.exp(log_a)
    return round(a, 2), round(b, 2)


#квадратичная аппроксимация y = a * x^2 + b * x + c
def quadratic_fit(x, y):
    n = len(x)
    sum_x = sum(x)
    sum_x2 = sum([xi ** 2 for xi in x])
    sum_x3 = sum([xi ** 3 for xi in x])
    sum_x4 = sum([xi ** 4 for xi in x])
    sum_y = sum(y)
    sum_xy = sum([xi * yi for xi, yi in zip(x, y)])
    sum_x2y = sum([xi ** 2 * yi for xi, yi in zip(x, y)])

    A = [[sum_x4, sum_x3, sum_x2],
         [sum_x3, sum_x2, sum_x],
         [sum_x2, sum_x, n]]
    B = [sum_x2y, sum_xy, sum_y]

    def det(matrix):
        return (matrix[0][0] * (matrix[1][1] * matrix[2][2] - matrix[2][1] * matrix[1][2])
                - matrix[0][1] * (matrix[1][0] * matrix[2][2] - matrix[2][0] * matrix[1][2])
                + matrix[0][2] * (matrix[1][0] * matrix[2][1] - matrix[2][0] * matrix[1][1]))

    D = det(A)
    D_a = det([[B[0], A[0][1], A[0][2]], [B[1], A[1][1], A[1][2]], [B[2], A[2][1], A[2][2]]])
    D_b = det([[A[0][0], B[0], A[0][2]], [A[1][0], B[1], A[1][2]], [A[2][0], B[2], A[2][2]]])
    D_c = det([[A[0][0], A[0][1], B[0]], [A[1][0], A[1][1], B[1]], [A[2][0], A[2][1], B[2]]])

    a = D_a / D
    b = D_b / D
    c = D_c / D

    return round(a, 2), round(b, 2), round(c, 2)


lin_a, lin_b = linear_fit(x_vals, y_vals)
pow_a, pow_b = power_fit(x_vals, y_vals)
exp_a, exp_b = exponential_fit(x_vals, y_vals)
quad_a, quad_b, quad_c = quadratic_fit(x_vals, y_vals)

print("Линейная аппроксимация: y =", lin_a, "* x +", lin_b)
print("Степенная аппроксимация: y =", pow_a, "* x^", pow_b)
print("Показательная аппроксимация: y =", exp_a, "* e^(", exp_b, "* x)")
print("Квадратичная аппроксимация: y =", quad_a, "* x^2 +", quad_b, "* x +", quad_c)


def linear(x, a, b):
    return a * x + b

def power(x, a, b):
    return a * (x ** b)

def exponential(x, a, b):
    return a * math.exp(b * x)

def quadratic(x, a, b, c):
    return a * x ** 2 + b * x + c


x_range = [i / 10.0 for i in range(15, 75)]

plt.figure(figsize=(12, 8))
plt.plot(x_range, [linear(x, lin_a, lin_b) for x in x_range], label=f"Линейная: y = {lin_a} * x + {lin_b}",
         color="blue")
plt.plot(x_range, [power(x, pow_a, pow_b) for x in x_range], label=f"Степенная: y = {pow_a} * x^{pow_b}", color="green")
plt.plot(x_range, [exponential(x, exp_a, exp_b) for x in x_range],
         label=f"Показательная: y = {exp_a} * e^({exp_b} * x)", color="red")
plt.plot(x_range, [quadratic(x, quad_a, quad_b, quad_c) for x in x_range],
         label=f"Квадратичная: y = {quad_a} * x^2 + {quad_b} * x + {quad_c}", color="purple")
plt.scatter(x_vals, y_vals, color="black", label="Экспериментальные точки")

plt.xlabel("x")
plt.ylabel("y")
plt.title("Метод наименьших квадратов")
plt.legend()
plt.grid(True)
plt.show()
