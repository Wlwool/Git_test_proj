def calculate_price(known_price, known_weight, target_weight):
    price_per_unit = known_price / known_weight
    return round(price_per_unit * target_weight, 2)  # Округление до копеек

known_price = float(input("Введите цену: "))
known_weight = float(input("Введите известный вес товара в граммах: "))

price_1g = calculate_price(known_price, known_weight, 1)
price_100g = calculate_price(known_price, known_weight, 100)
price_1kg = calculate_price(known_price, known_weight, 1000)

print(f"Цена за 1 грамм: {price_1g} рублей")
print(f"Цена за 100 грамм: {price_100g} рублей")
print(f"Цена за 1 кг: {price_1kg} рублей")


