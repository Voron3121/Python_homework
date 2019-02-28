# coding: utf-8

# Задача-3:
# Дан произвольный список из целых чисел.
# Получите НОВЫЙ список из элементов исходного, выполнив следующие условия:
# если элемент кратен двум, то разделить его на 4, если не кратен, то умножить на два.

first_list = [4, 9, 18, 3, 10, 42]
new_list = []
last_name = len(first_list)
for i in range(last_name):
    if first_list[i] % 2 == 0:
        new_list.append(first_list[i] / 4)
    else:
        new_list.append(first_list[i] * 2)
print(new_list)
