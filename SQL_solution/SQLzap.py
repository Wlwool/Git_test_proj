# Напишите запрос, который для каждой категории товаров выводит:
# Название категории.
# Количество товаров в ней.
# Среднюю цену товаров.
# Только для категорий с более чем 5 товарами.

SELECT category,
    COUNT(*) AS total_products, AVG(price) as average_price
FROM store
GROUP BY category
HAVING COUNT(*) > 5





