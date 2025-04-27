"""
Быстрая сортировка

def sum_num(arr):
    total = 0
    for x in arr:
        total += x
    return total

print(sum_num([1,2,3,4,5]))

def sum_recursive(arr):
    if len(arr) == 1:
        return arr[0]
    else:
        return arr[0] + sum_recursive(arr[1:])

print(sum_recursive([1,2,3,4,5]))


def count_elements(arr):
    if not arr:  # базовый случай: пустой список
        return 0
    else:
        return  1 + count_elements(arr[1:])

print(count_elements([1,2,3,4,5]))


def find_max(arr):
    if len(arr) == 1:  # базовый случай: один элемент
        return arr[0]
    else:
        sub_max = find_max(arr[1:])  # рекурсивно находим максимальный элемент в подмассиве
        # возвращаем максимальный элемент между первым элементом и максимальным в подмассиве
        return arr[0] if arr[0] > sub_max else sub_max

print(find_max([1,2,3,4,5]))


def quick_sort(arr):
    if len(arr) <= 2:  # базовый случай: список из одного элемента или пустой список
        return arr
    else:
        pivot = arr[0]  # выбираем опорный элемент(рекурсивный случай)
        print(f"Опорный элемент: {pivot}")
        less = [x for x in arr[1:] if x <= pivot]  # формируем подсписок элементов меньше опорного
        print(f"Элементы меньше опорного: {less}")
        greater = [x for x in arr[1:] if x > pivot]  # формируем подсписок элементов больше опорного
        print(f"Элементы больше опорного: {greater}")
    return quick_sort(less) + [pivot] + quick_sort(greater)

print(quick_sort([1,2,3,4,5]))


def quicksort(array):
    if len(array) < 2:
        return array
    else:
        pivot = array[0]
        print(f"Опорный элемент: {pivot}")
        less = [i for i in array[1:] if i < pivot]
        print(f"Элементы меньше опорного: {less}")
        greater = [i for i in array[1:] if i > pivot]
        print(f"Элементы больше опорного: {greater}")
        return quicksort(less) + [pivot] + quicksort(greater)
print(quicksort([10,5,2,3]))



> Стратегия «разделяй и властвуй» основана на разбиении задачи на уменьшающиеся фрагменты.
Если вы используете стратегию «разделяй и властвуй» со списком, то базовым случаем, скорее всего,
является пустой массив или массив из одного элемента.

> Если вы реализуете алгоритм быстрой сортировки, выберите в качестве опорного случайный элемент.
Среднее время выполнения быстрой сортировки составляет O(n log n)

> Из двух алгоритмов с одинаковой скоростью «O-большое» один может быть быстрее другого.
Именно по этой причине быстрая сортировка быстрее сортировки слиянием.

> При сравнении простой сортировки с бинарной константа почти никогда роли не играет, потому что O(log n)
слишком сильно превосходит O(n) по скорости при большом размере списка.

"""
