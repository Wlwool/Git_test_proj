# Напишите класс Stack, который:
# Имеет методы push (добавляет элемент), pop (удаляет и возвращает верхний элемент).
# При попытке pop из пустого стека вызывает исключение StackEmptyError (создайте свой класс исключения).
# Отображается в print() как Stack<size=N>, где N — текущее количество элементов.


class Stack:
    def __init__(self):
        self.stack = []

    def push(self, element):
        self.stack.append(element)

    def pop(self):
        if not len(self.stack):
            raise StackEmptyError
        return self.stack.pop()


class StackEmptyError(Exception):
    pass

stack = Stack()
stack.push(1)
print(stack)
stack.pop()
print(stack)



