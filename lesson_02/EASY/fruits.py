# coding: utf-8

# Задача-1:
# Дан список фруктов.
# Напишите программу, выводящую фрукты в виде нумерованного списка,
# выровненного по правой стороне.

fruit_list = ['Яблоко', 'Банан', 'Киви', 'Арбуз', 'Манго', 'Груша', 'Помидор', 'Дыня']
for fruit_index, fruit_name in enumerate(fruit_list, start=1):
    print(fruit_index, "{:>10}".format(fruit_name))
