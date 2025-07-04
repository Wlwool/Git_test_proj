"""
Ваша задача - реализовать класс, который принимает обозначение цвета палитры
в формате HEX в виде строки и может
перевести его в формат RGB при помощи свойств red, green, blue.
Для решения данной задачи напишите только реализацию класса Colour
"""


class Colour:
    def __init__(self, hex_code):
        self.hex_code = hex_code

    @property
    def hex_code(self):
        return self._hex_code

    @hex_code.setter
    def hex_code(self, value):
        if not (
            value.startswith("#")
            and len(value) == 7
            and all(char in "0123456789abcdefABCDEF" for char in value[1:])
        ):
            raise ValueError("Неверный формат HEX-кода")
        self._hex_code = value.lower()

    @property
    def red(self):
        return int(self.hex_code[1:3], 16)

    @property
    def green(self):
        return int(self.hex_code[3:5], 16)

    @property
    def blue(self):
        return int(self.hex_code[5:7], 16)


# решение без проверок
# class Colour:
#     def __init__(self, hex_code):
#         self.hex_code = hex_code
#         self.red = int(self.hex_code[1:3],16)
#         self.green = int(self.hex_code[3:5],16)
#         self.blue = int(self.hex_code[5:7],16)

colour = Colour("#ff0000")
print(colour.red)
print(colour.green)
print(colour.blue)

colour2 = Colour("#00ff2d")
print(colour2.red)
print(colour2.green)
print(colour2.blue)

colour3 = Colour("#aacce4")
print(colour3.red)
print(colour3.green)
print(colour3.blue)
