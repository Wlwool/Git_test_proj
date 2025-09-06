class Node:
    """Узел списка"""
    def __init__(self, data):
        self.data = data  # Данные узла
        self.next = None  # Ссылка на следующий узел


class LinkedList:
    """Односвязный список"""
    def __init__(self):
        self.head = None  # Начало списка

    def append(self, data):
        """Добавление элемента в конец"""
        new_node = Node(data)
        if not self.head:  # Если список пуст
            self.head = new_node
            return
        last = self.head
        while last.next:  # Ищем последний узел
            last = last.next
        last.next = new_node  # Присоединяем новый узел

    def prepend(self, data):
        """Добавление элемента в начало"""
        new_node = Node(data)
        new_node.next = self.head  # Новый узел указывает на текущее начало
        self.head = new_node  # Обновляем начало

    def delete(self, data):
        """Удаление элемента по значению"""
        if not self.head:
            return

        if self.head.data == data:  # Если удаляем первый элемент
            self.head = self.head.next
            return

        current = self.head
        while current.next:
            if current.next.data == data:
                current.next = current.next.next  # Пропускаем удаляемый узел
                return
            current = current.next

    def display(self):
        """Вывод списка"""
        elements = []
        current = self.head
        while current:
            elements.append(str(current.data))
            current = current.next
        print(" -> ".join(elements))

    def reverse(self):
        """Реверс списка"""
        prev = None
        current = self.head
        while current:
            next_node = current.next  # Сохраняем следующий узел
            current.next = prev  # Меняем направление связи
            prev = current  # Перемещаем prev на текущий узел
            current = next_node  # Переходим к следующему узлу
        self.head = prev  # Обновляем голову списка

    def reverse_recursive(self, current, prev):
        """Реверс списка рекурсивно"""
        def _reverse_recursive(current, prev):
            if not current:
                return prev
            next_node = current.next
            current.next = prev
            return _reverse_recursive(next_node, current)
        self.head = _reverse_recursive(current, prev)

ll = LinkedList()
ll.append(1)
ll.append(2)
ll.append(3)
ll.prepend(0)
ll.display()  # 0 -> 1 -> 2
ll.delete(1)
ll.display()  # 0 -> 2

print("Список:")
ll.display()  # 1 -> 2 -> 3 -> 4

ll.reverse()

print("Развернутый список:")
ll.display()  # 4 -> 3 -> 2 -> 1

ll.reverse_recursive(ll.head, None)
