# coding: utf-8

# Задача-1:
# Дан список, заполненный произвольными целыми числами, получите новый список,
# элементами которого будут квадратные корни элементов исходного списка,
# но только если результаты извлечения корня не имеют десятичной части и
# если такой корень вообще можно извлечь

import math

# Решение №1

my_list = [2, -5, 8, 9, -25, 25, 4]
new_list = []
for item in my_list:
    if item > 0 and math.sqrt(item) % 1 == 0:
        new_list.append(int(math.sqrt(item)))
print(new_list)

# Решение №2

my_list = [-6, -9, 0, 81, -16, 4, 0.5, 25]
new_list = []
for element in my_list:
    if (element > 0) and (int(math.sqrt(element)) == math.sqrt(element)):
        new_list.append(int(math.sqrt(element)))
print(new_list)
