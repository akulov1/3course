import time

# Метод Эйлера для системы дифференциальных уравнений
def solve_lotka_volterra(alpha, r0, f0, dt=0.01, t_end=100):
    r, f = r0, f0
    t = 0
    results = [(t, r, f)]
    while t < t_end:
        dr = (2*r - alpha * r * f) * dt
        df = (-f + alpha * r * f) * dt
        r += dr
        f += df
        t += dt
        results.append((t, r, f))
    return results

# Печать результатов
def print_results(results, step=100):
    print(f"{'Time':>6} {'Rabbits (r)':>15} {'Foxes (f)':>15}")
    print("-" * 40)
    for i, (t, r, f) in enumerate(results):
        if i % step == 0:
            print(f"{t:6.1f} {r:15.4f} {f:15.4f}")

# Анализ
def analyze(alpha, r0, f0, dt=0.01, t_end=100):
    results = solve_lotka_volterra(alpha, r0, f0, dt, t_end)
    r_values = [r for _, r, _ in results]
    f_values = [f for _, _, f in results]
    final_r, final_f = r_values[-1], f_values[-1]

    print(f"\nНачальные условия: r0 = {r0}, f0 = {f0}")
    print_results(results, step=len(results) // 10)
    print(f"\nИтоговые значения: r = {final_r:.4f}, f = {final_f:.4f}")

    if final_r < 1:
        print("Кролики вымерли.")
    if final_f < 1:
        print("Лисы вымерли.")
    if final_r < 1 and final_f < 1:
        print("Оба вида вымерли.")

# Основная программа
if __name__ == "__main__":
    alpha = 0.01

    # Исследование для различных начальных значений r0, f0
    print("Исследование поведения системы для разных начальных условий:")
    initial_conditions = [(2, 3), (15, 22), (1000, 2000)]
    for r0, f0 in initial_conditions:
        analyze(alpha, r0, f0)

    # Поиск начальных условий, при которых вымирают лисы
    print("\nПоиск начальных условий, приводящих к вымиранию лис:")
    analyze(0, 40, 0.5)

    # Поиск начальных условий, при которых вымирают оба вида
    print("\nПоиск начальных условий, приводящих к вымиранию обоих видов:")
    analyze(1, 0.5, 0.5)
