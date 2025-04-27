# def look_for_key(main_box):
#     pile =main_box.make_a_pile_to_look_through()
#     while pile is not empty:
#         box = pile.grab_a_box()
#         for item in box:
#             if item.is_a_box():
#                 pile.append(item)
#             elif item.is_a_key():
#                 print("found the key!")

# def look_for_key(box):
#     for item in box:
#         if item.is_a_box():
#             look_for_key(item)
#         elif item.is_a_key():
#             print("Found the key!")

# def countdown(i):
#     print(i)
#     if i <= 0:
#         return
#     else:
#         countdown(i - 1)

# def greet(name):
#     print("Hello, " + name + "!")
#     greet2(name)
#     print("Getting ready to say bye...")
#     bye()
#
# def greet2(name):
#     print("How are you, " + name + "?")
# def bye():
#     print("Ok bye!")
#
# greet('Nico')

def fact(x):
    if x == 1:
        return 1
    else:
        return  x * fact(x - 1)

print(fact(3))


"""
Когда функция вызывает сама себя, это называется рекурсией.
В каждой рекурсивной функции должно быть два случая: рекурсивный случай и базовый случай.
Стек поддерживает две операции: добавление нового элемента и извлечение верхнего элемента.
Все вызовы функций хранятся в стеке. Если функция вызывает другую функцию, она помещается на вершину стека.
Если стек вызовов станет очень большим, он займет слишком много памяти и программа будет остановлена.
"""