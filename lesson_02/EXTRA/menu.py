# coding: UTF-8

# Есть два словаря. Один это рецепт блюда, второй это список продуктов, которые есть в холодильнике.
#
# Ключ это название продукта, значение - это количество.
#
# Нужно сравнить два словаря и дать словарь, в котором будет список покупок
# Если для рецепта всё есть, то сказать что ничего не нужно
# Разницей по измерению гр, мл, шт. Пренебречь

receipt = {
    'яйцо': 3,
    'мясо': 100,
    'соль': 10
}
fridge = {
    'яйцо': 1,
    'мясо': 50
}
to_buy = {}
for product in receipt:
    if product not in fridge:
        to_buy[product] = receipt[product]
    elif fridge[product] < receipt[product]:
        to_buy[product] = receipt[product] - fridge[product]
if not to_buy:
    print("Ничего покупать не нужно.")
else:
    print("Необходимо купить: ", to_buy)
