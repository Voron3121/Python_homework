# coding: utf-8

# Задание-2
# Сформировать квадратную матрицу, в каждой строке которой находится ровно один ноль на случайном месте,
# остальные элементы тоже рандомные. Пользователь вводит размер

import random
import pprint

N = int(input("Input size: "))

matr = [[random.randint(1, 100) for j in range(N)] for i in range(N)]

for row in matr:
    row[random.randint(0, N - 1)] = 0

pprint.pprint(matr)