# class Vector:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#     def __add__(self, other):
#         return Vector(self.x + other.x, self.y + other.y)
#
#     def __sub__(self, other):
#         return Vector(self.x - other.x, self.y - other.y)
#
#     def __mul__(self, other):
#         return Vector(self.x * other, self.y * other)
#
#     def __len__(self):
#         return (self.x**2 + self.y**2) ** 0.5
#
#     def __str__(self):
#         return f'{self.x}, {self.y}'
from typing import overload

Урок 1: HTTP-ошибки в API + переводы
1. 400 - ошибка запроса, сервер не будет и не может обработать запрос , 401 - ошибка авторизации, 429 - слишком много запросов за короткий промежуток времени, 503 - сервис недоступен
2. Ошибка 429 слишком много запросов показывет, что юзер отправил слишком много запросов в одно время
The 503 error indicates that server is unavailable, reason is overloaded

Урок 2: Docker + технический перевод
1. bridge сетевой драйвер по умолчанию, overlay сети объединяют нескольно докер демонов вместе, host удаляет изоляцию сети между контейнером и докер хостом
2. Мост сети по умолчанию создается автоматически, когда вы установили докер.
Netwotk 'host' gives docker container acess to use the host network stack.
3. Meteorolog - погодный бот, который держит вас в курсе прогноза погоды.
Meteorolog - weather bot that keeps you up to date on ther weather forecast

Урок 3:
1. parser - извлекает данные, tag - метка это такой объект который соответствует меткам XML или HTML в оригинальном документе, navigable string - используется для хранения фрагментов текста
2. Метод find_all() вовращает список всех совпадающих тегов(меток).
The select_one() method find the first CSS selector.
3. Meteorolog - weather bot that keeps you up to date on ther weather forecast





