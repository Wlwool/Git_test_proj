# Python метакласс — это класс, который создаёт другие классы.
# По умолчанию все классы создаются с использованием метакласса type.
# Однако, определяя собственный метакласс, вы можете изменить поведение создания классов.

# Запрет атрибутов с цифрой

class NoDigitAttrMeta(type):
    def __new__(cls, name, bases, dct):
        for attr in dct:
            if attr[0].isdigit():
                raise ValueError(f'Атрибут {attr} начинается с цифры!')
        return super().__new__(cls, name, bases, dct)


class MyClass(metaclass=NoDigitAttrMeta):
    2bad = 10