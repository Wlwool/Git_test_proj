"""
- Поиск в ширину вычисляет кратчайший путь в невзвешенном графе.
- Алгоритм Дейкстры вычисляет кратчайший путь во взвешенном графе.
- Алгоритм Дейкстры работает только в том случае, если все веса положительны.
- При наличии отрицательных весов используйте алгоритм Беллмана — Форда.
"""

graph = {}

graph["you"] = ["alice", "bob", "claire"]

graph["start"] = {}
graph["start"]["a"] = 6
graph["start"]["b"] = 2

graph["a"] = {}
graph["a"]["finish"] = 1

graph["b"] = {}
graph["b"]["a"] = 3

graph["b"]["finish"] = 5
graph["finish"] = {}

infinity = float("inf")
costs = {}
costs["a"] = 6
costs["b"] = 2
costs["finish"] = infinity


parents = {}
parents["a"] = "start"
parents["b"] = "start"
parents["in"] = None

processed = []  # Массив для отслеживания обработанных узлов


def find_lowest_cost_node(costs):
    lowest_cost = float("inf")
    lowest_cost_node = None
    for node in costs:  # перебираем все узлы
        cost = costs[node]
        if (
            cost < lowest_cost and node not in processed
        ):  # если стоимость узла меньше, чем текущая
            # наименьшая стоимость и узел не обработан ...
            lowest_cost = cost  # он назначается новым узлом с наименьшей стоимостью
            lowest_cost_node = node
    return lowest_cost_node


node = find_lowest_cost_node(
    costs
)  # Поиск узла с наименьшей стоимостью среди обработанных

while node is not None:  # цикл завершается, когда все узлы обработаны
    cost = costs[node]
    neighbors = graph[node]  # получаем список соседей

    for n in neighbors.keys():  # перебираем соседей текущего узла
        new_cost = cost + neighbors[n]  # считаем стоимость пути
        if (
            costs[n] > new_cost
        ):  # если к соседу можно быстрее добраться через текущий узел, то ...
            costs[n] = new_cost  # обновляем стоимость
            parents[n] = node  # этот узел становится родителем для соседа
    processed.append(node)  # помечаем узел как обработанный
    node = find_lowest_cost_node(
        costs
    )  # найти следующий узел для обработки и повторить цикл
