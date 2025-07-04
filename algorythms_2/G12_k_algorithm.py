import math


# Реализация k-ближайших соседей
def euclidean_distance(a, b):
    """Вычисляет евклидово расстояние между двумя точками."""
    return math.sqrt(sum((x - y) ** 2 for x, y in zip(a, b)))


def knn(data, query, k):
    """
    kNN классификатор.
    data: список кортежей (features, label)
    query: точка для классификации
    k: число соседей
    """
    # Вычисляем расстояния до всех точек
    distances = [(euclidean_distance(features, query), label)
                 for features, label in data]
    # Сортируем по возрастанию расстояния
    distances.sort(key=lambda x: x[0])
    # Берём k ближайших
    neighbors = distances[:k]
    # Голосуем
    votes = {}
    for _, label in neighbors:
        votes[label] = votes.get(label, 0) + 1
    # Выбираем метку с максимальным числом голосов
    return max(votes.items(), key=lambda x: x[1])[0]


# Пример данных: точки на плоскости с метками 'A' и 'B'
dataset = [
    ([1, 2], "A"),
    ([2, 3], "A"),
    ([3, 3], "A"),
    ([6, 5], "B"),
    ([7, 7], "B"),
    ([8, 6], "B"),
]

# Тестовые запросы
test_points = [[2, 2], [5, 5], [7, 5]]

# Проверка работы алгоритма для разных k
results = {}
for k in [1, 3, 5]:
    results[k] = [knn(dataset, point, k) for point in test_points]

# Вывод результатов
for k, predicts in results.items():
    print(f"k = {k}:")
    for pt, label in zip(test_points, predicts):
        print(f"  Точка {pt} -> Класс {label}")
    print()


# k = 1:
#   Точка [2, 2] -> Класс A
#   Точка [5, 5] -> Класс B
#   Точка [7, 5] -> Класс B
#
# k = 3:
#   Точка [2, 2] -> Класс A
#   Точка [5, 5] -> Класс B
#   Точка [7, 5] -> Класс B
#
# k = 5:
#   Точка [2, 2] -> Класс A
#   Точка [5, 5] -> Класс B
#   Точка [7, 5] -> Класс B
