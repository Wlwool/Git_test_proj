"""
-Сбалансированные бинарные деревья поиска (BST) обеспечивают
такую же производительность в нотации "О-большое", как массивы,
и лучшую производительность вставки.
- Высота дерева влияет на его производительность.
- АВЛ-деревья — популярная разновидность сбалансированных деревьев BST.
Как и большинство сбалансированных деревьев,
 АВЛ-деревья балансируются поворотом.
- B-деревья представляют собой обобщенные деревья BST, у которых каждый
узел может иметь несколько ключей
 и несколько дочерних узлов.
- Время поиска можно сравнить со временем похода в магазин.
B-деревья минимизируют время поиска за счет чтения большего объема
данных за одну операцию.

"""


class Node:
    """
    Узел двоичного дерева (Binary Search Tree).
    Каждый узел содержит значение, а также ссылки на левого и правого потомков
    """

    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value

    def insert(self, value):
        """
        Вставляет новое значение в дерево по правилам BST:
        значения меньше или равны идут в левое поддерево, больше — в правое.
        """
        if value <= self.value:
            if self.left is None:
                self.left = Node(value)
            else:
                self.left.insert(value)
        else:
            if self.right is None:
                self.right = Node(value)
            else:
                self.right.insert(value)

    def find(self, value):
        """
        Ищет значение в дереве. Возвращает True, если найдено, иначе False.
        """
        if value == self.value:
            return True
        elif value < self.value:
            return self.left.find(value) if self.left else False
        else:
            return self.right.find(value) if self.right else False

    def inorder_traversal(self, visit):
        """
        Симметричный (in-order) обход дерева. Вызывает функцию visit на каждом узле.
        Это выведет значения в отсортированном порядке.
        """
        if self.left:
            self.left.inorder_traversal(visit)
        visit(self.value)
        if self.right:
            self.right.inorder_traversal(visit)


if __name__ == "__main__":
    # создаем корень дерева
    tree = Node(10)
    # вставляем несколько значений
    for val in [5, 15, 3, 7, 12, 18]:
        tree.insert(val)

    # печать всех значений дерева в порядке возрастания
    print("В порядке возрастания:")
    tree.inorder_traversal(lambda x: print(x))

    # поиск значений
    print(f"\nПоиск 7: {tree.find(7)}")
    print(f"Поиск 20: {tree.find(20)}")
