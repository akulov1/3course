import random
import math

random.seed(42)  # Фиксируем seed для воспроизводимости

def normalize_vector(v):
    norm = math.sqrt(v[0]**2 + v[1]**2)
    return [v[0]/norm, v[1]/norm] if norm != 0 else [0.0, 0.0]

def dot_product(v1, v2):
    return v1[0]*v2[0] + v1[1]*v2[1]

def update_weights(w, x, eta):
    new_w = [w[0] + eta*(x[0]-w[0]), w[1] + eta*(x[1]-w[1])]
    return normalize_vector(new_w)

# Обучающие векторы (уже нормализованы)
training_vectors = [
    [0.97, 0.20], [1.00, 0.00], [-0.72, 0.70], [-0.67, 0.74],
    [-0.80, 0.60], [0.00, -1.00], [0.20, -0.97], [-0.30, -0.95]
]

eta = 0.5  # Коэффициент обучения

# Инициализация нейронов
neurons = []
for _ in range(4):
    w = normalize_vector([random.uniform(-1, 1), random.uniform(-1, 1)])
    neurons.append(w)

# Счетчик побед и обучение с штрафами
victories = [0] * 4
for x in training_vectors:
    # Вычисляем модифицированные активации
    activations = [dot_product(neuron, x)/(1 + victories[i]) for i, neuron in enumerate(neurons)]
    winner_idx = activations.index(max(activations))
    victories[winner_idx] += 1  # Увеличиваем счетчик побед
    # Обновляем веса победителя
    neurons[winner_idx] = update_weights(neurons[winner_idx], x, eta)

# Вывод весов
for i, w in enumerate(neurons):
    print(f"Нейрон {i+1}: [{w[0]:.4f}, {w[1]:.4f}]")