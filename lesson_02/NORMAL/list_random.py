# coding: utf-8

# Задача-3:
# Напишите алгоритм, заполняющий список произвольными целыми числами
# в диапазоне от -100 до 100. В списке должно быть n - элементов.

import random

n = int(input('Введите количество случайных элементов в списке: '))
my_list = []
for el in range(n):
    my_list.append(random.randint(-100, 100))
print(my_list)
