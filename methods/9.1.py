import math
import time

def erf_euler(x_values, step=0.001):
    erf_values = []
    for x in x_values:
        y = 0
        current_x = 0
        while current_x < x:
            dy = (2 / math.sqrt(math.pi)) * math.exp(-current_x**2) * step
            y += dy
            current_x += step
        erf_values.append(y)
    return erf_values

def erf_numeric(x, n=1000):
    a, b = 0, x
    h = (b - a) / n
    integral = 0
    current_x = a
    while current_x < b:
        integral += (2 / math.sqrt(math.pi)) * math.exp(-current_x**2) * h
        current_x += h
    return integral

# Основная программа
if __name__ == "__main__":
    # Значения x, для которых считаем erf(x)
    x_values = [round(0.1 * i, 1) for i in range(21)]

    # Метод Эйлера
    start_time_euler = time.time()
    erf_euler_values = erf_euler(x_values)
    time_euler = time.time() - start_time_euler

    # Численное интегрирование
    start_time_numeric = time.time()
    erf_numeric_values = [erf_numeric(x) for x in x_values]
    time_numeric = time.time() - start_time_numeric

    # Печать результатов
    print("x      | erf(x) Эйлер | erf(x) ЛР6 | Разница | Табличное")
    print("---------------------------------------------------------")
    for x, euler_val, numeric_val in zip(x_values, erf_euler_values, erf_numeric_values):
        print(f"{x:.1f}   | {euler_val:.6f}     | {numeric_val:.6f}      | {abs(euler_val - numeric_val):.6f} | {math.erf(x):.6f}")

    # Печать времени выполнения
    print("\nВремя выполнения:")
    print(f"Метод Эйлера: {time_euler:.6f} секунд")
    print(f"Численное интегрирование: {time_numeric:.6f} секунд")
