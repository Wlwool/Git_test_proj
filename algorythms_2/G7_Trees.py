"""
from os import listdir
from os.path import isfile, join
from collections import deque

def print_names(start_dir):
    search_queue = deque()  # очередь используется для отслеживания папок в которых должен проводиться поиск
    search_queue.append(start_dir)
    while search_queue:  # пока очередь не пуста извлекаем из нее папку
        directory = search_queue.popleft()
        for file in sorted(listdir(directory)):  # перебрать все файлы и папки в этой папке
            full_path = join(directory, file)
            if isfile(full_path):
                print(full_path)  # если это файл вывести его имя
            else:
                search_queue.append(full_path)  # если это папка добавить ее в конец очереди поиска папок

print_names("pics")


# поиск в грубину
from os import listdir
from os.path import isfile, join

def printnames(dir):
    for file in sorted(listdir(dir)):
        fullpath = join(dir, file)
        if isfile(fullpath):
            print(file)  # Если это файл, вывести его имя
        else:
            printnames(fullpath)

printnames("pics")



- Деревья — это разновидность графов, но в деревьях не может быть циклов.
- Поиск в глубину — еще один алгоритм обхода графа. Он не подходит для поиска кратчайших путей.
- Бинарное дерево — особая разновидность деревьев, у которой каждый узел может иметь не более двух дочерних узлов.
- Существует много типов кодирования символов. Юникод является международным стандартом, а UTF-8 — самая популярная кодировка в Юникоде.
"""
