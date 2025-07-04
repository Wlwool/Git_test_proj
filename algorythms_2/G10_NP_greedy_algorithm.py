"""
- Жадные алгоритмы стремятся к локальной оптимизации в расчете на то, что в итоге
будет достигнут глобальный оптимум.
- Если у вас имеется NP-трудная задача, лучше всего воспользоваться
приближенным алгоритмом.
- Жадные алгоритмы легко реализовать и быстро выполнить, поэтому
из них получаются хорошие приближенные алгоритмы
"""

states_needed = set(
    ["mt", "wa", "or", "id", "nv", "ut", "ca", "az"]
)  # переданный массив преобразуется в множество

stations = {}
stations["kone"] = set(["id", "nv", "ut"])
stations["ktwo"] = set(["wa", "id", "mt"])
stations["kthree"] = set(["or", "nv", "ca"])
stations["kfour"] = set(["nv", "ut"])
stations["kfive"] = set(["ca", "az"])

final_stations = set()

while states_needed:
    best_station = None
    states_covered = set()

    for station, states_for_station in stations.items():
        covered = states_needed & states_for_station  # пересечение множеств
        if len(covered) > len(states_covered):
            best_station = station
            states_covered = covered

    states_needed -= states_covered
    final_stations.add(best_station)

print(final_stations)
