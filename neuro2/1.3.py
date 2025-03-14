import random

# Инициализация генератора случайных чисел
random.seed(42)

# Инициализация весов для двух нейронов (каждый имеет 2 входа)
neurons_weights = [
    [random.uniform(-0.5, 0.5) for _ in range(2)],  # Нейрон 1
    [random.uniform(-0.5, 0.5) for _ in range(2)]  # Нейрон 2
]

eta = 0.5  # Коэффициент обучения

# Обучающие данные (нормализованные векторы из задачи 1)
training_vectors = [
    [0.97, 0.20],
    [1.00, 0.00],
    [-0.72, 0.70],
    [-0.67, 0.74],
    [-0.80, 0.60],
    [0.00, -1.00],
    [0.20, -0.97],
    [-0.30, -0.95]
]

# Обучение по правилу Хебба с учителем
for x in training_vectors:
    # Определение целевых значений (d1 и d2) по первой компоненте вектора
    d = [1, 0] if x[0] >= 0 else [0, 1]

    # Обновление весов для каждого нейрона
    for i in range(2):  # Цикл по нейронам
        for j in range(2):  # Цикл по входам нейрона
            delta = eta * x[j] * d[i]
            neurons_weights[i][j] += delta

# Вывод результатов
print("Веса после обучения:")
for idx, w in enumerate(neurons_weights):
    print(f"Нейрон {idx + 1}: [{w[0]:.4f}, {w[1]:.4f}]")