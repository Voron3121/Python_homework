# coding: utf-8

# Задача-2:
# Даны два произвольные списка.
# Удалите из первого списка элементы, присутствующие во втором списке.

random_list = ["some", "random", "list", "and", 1, 2, 0, 0, 3, 0, 0, 0, 4, 5, 6, 7, 8, 0, 0, 0, 9, "Python", "is", "awesome"]
another_random_list = ["some", "random", 0, "Python", "list", "is", "awesome", "and"]

print("\nУдалим одинаковые элементы из первого списка, которые есть во втором.")
print("Это первый список: ", random_list)
print("Это второй список:", another_random_list)
random_list = [x for x in random_list if x not in another_random_list]
print("А это рзультат:", random_list)
