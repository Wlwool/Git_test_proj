"""
Ваша задача - создать класс Date, который хранит информацию о дате: день, месяц и год.
Также класс Date должен иметь фабричный метод from_str, который принимает строку в
формате день-месяц-год и возвращает на ее основании вновь созданный экземпляр класса Date.

Проанализируйте входные данные тестовых значений для понимая
состава атрибутов класса Date.
Для решения задания необходимо написать только реализацию класса Date.
"""


class Date:
    def __init__(self, date, month, year):
        self.day = date
        self.month = month
        self.year = year

    @classmethod
    def from_str(cls, date_str):
        day, month, year = map(int, date_str.split("-"))
        return cls(day, month, year)


print("\n Sample Input 1:\n")
day_1 = Date(20, 9, 1997)
print(day_1.day)
print(day_1.month)
print(day_1.year)

day_2 = Date(1, 2, 2003)
print(day_2.day, day_2.month, day_2.year)

print("\n Sample Input 2:\n")
day_1 = Date.from_str("12-4-2024")
day_2 = Date.from_str("06-09-2022")
print(day_1.day, day_1.month, day_1.year)
print(day_2.day, day_2.month, day_2.year)
