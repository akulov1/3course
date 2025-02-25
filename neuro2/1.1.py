import random
import math

random.seed(42)  # Для воспроизводимости результатов

def normalize_vector(v):
    norm = math.sqrt(v[0]**2 + v[1]**2)
    if norm == 0:
        return [0.0, 0.0]
    return [v[0]/norm, v[1]/norm]

def dot_product(v1, v2):
    return v1[0]*v2[0] + v1[1]*v2[1]

def update_weights(w, x, eta):
    new_w = [
        w[0] + eta * (x[0] - w[0]),
        w[1] + eta * (x[1] - w[1])
    ]
    return normalize_vector(new_w)

# Обучающие векторы (уже нормализованы)
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

eta = 0.5  # Коэффициент обучения

# Инициализация весов 4 нейронов
neurons = []
for _ in range(4):
    w1 = random.uniform(-1, 1)
    w2 = random.uniform(-1, 1)
    normalized = normalize_vector([w1, w2])
    neurons.append(normalized)

# Процесс обучения
for x in training_vectors:
    # Вычисление выходов нейронов
    outputs = [dot_product(neuron, x) for neuron in neurons]
    # Определение победителя
    winner_idx = outputs.index(max(outputs))
    # Обновление весов победителя
    neurons[winner_idx] = update_weights(neurons[winner_idx], x, eta)

# Вывод весов после обучения
for idx, neuron in enumerate(neurons):
    print(f"Нейрон {idx + 1}: [{neuron[0]:.4f}, {neuron[1]:.4f}]")