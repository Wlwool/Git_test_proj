class PositiveNumber:
    def __set__(self, instance, value):
        if value <= 0:
            raise ValueError("Value must be positive.")
        instance.__dict__[self.name] = value

    def __set_name__(self, owner, name):
        self.name = name


class Product:
    price = PositiveNumber()


p = Product()
p.price = 10
p.price = -5
