def binarySearch(list, item):
    low = 0
    high = len(list) - 1  # в переменных low и high хранятся границы той части списка в которой выполняется поиск
    # mid = (low + high) / 2  # Если значение low + high нечетное, то mid будет округлено в меньшую сторону

    while low <= high:  # пока эта часть не сократится до одного элемента ...
        mid = (low + high) // 2  # проверяем средний элемент
        guess = list[mid]

        if guess == item:  # значение найдено
            return mid
        elif guess > item:
            high = mid - 1
        else:
            low = mid + 1
    return None

my_list = [1, 3, 5, 7, 9]
print(binarySearch(my_list, 3))  # 1
print(binarySearch(my_list, -1))  # None
print(binarySearch(my_list, 7))

"""
# 1.1 Имеется отсортированный список из 128 имен, и вы ищете в нем зна- чение методом бинарного поиска. Какое максимальное количество проверок для этого может потребоваться?
# log_2(128) = 7
# 1.2 Предположим, размер списка увеличился вдвое. Как изменится мак- симальное количество проверок?
8
"""