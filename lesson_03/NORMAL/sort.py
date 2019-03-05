# coding: utf-8

# Задача-2:
# Напишите функцию, сортирующую принимаемый список по возрастанию.
# Для сортировки используйте любой алгоритм (например пузырьковый).
# Для решения данной задачи нельзя использовать встроенную функцию и метод sort()

def sort_manual(list):
    n = len(list)
    sorted_list = list
    biggest = 0
    for i in list:
        if int(i) > biggest:
            biggest = int(i)
            sorted_list.append(biggest)
            sorted_list.remove(i)
    print(sorted_list)


sort_manual([23, 1, 45, 8, 12, 3, 456])
