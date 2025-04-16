# Напишите класс Stack, который:
# Имеет методы push (добавляет элемент), pop (удаляет и возвращает верхний элемент).
# При попытке pop из пустого стека вызывает исключение StackEmptyError (создайте свой класс исключения).
# Отображается в print() как Stack<size=N>, где N — текущее количество элементов.


class Stack:
    def __init__(self):
        self.stack = []

    def push(self, element):
        self.stack.append(element)

    def is_empty(self):
        return len(self.stack) == 0

    def pop(self):
        if self.is_empty():
            raise StackEmptyError("Стек пуст!")
        return self.stack.pop()

    def __repr__(self):
        return f"Stack<size={len(self.stack)}>"


class StackEmptyError(Exception):
    pass

stack = Stack()
stack.push(1)
print(stack)
stack.pop()
print(stack)

stack = Stack()
print(stack)
stack.push(1)
print(stack)
stack.push(2)
print(stack)
print(stack.pop())
print(stack)
