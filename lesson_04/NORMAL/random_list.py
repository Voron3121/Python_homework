# coding: utf-8

# Задание-1:
# Напишите скрипт, заполняющий указанный файл (самостоятельно задайте имя файла)
# произвольными целыми цифрами, в результате в файле должно быть
# 2500-значное произвольное число.
# Найдите и выведите самую длинную последовательность одинаковых цифр
# в вышезаполненном файле.

import random

def get_random_numbers(length):
    num_rand = []

    for i in range(length):
        num_rand.append(str(random.randint(0, 9)))

    if num_rand[0] == "0":
        num_rand[0] = str(random.randint(1, 9))

    return "".join(num_rand)


def get_longest_sequence(numbers):
    max_sequence = 0
    max_sequence_number = None
    last = 0
    count = 0
    for num in numbers:
        if last == num:
            count += 1
        else:
            count = 1

        if count > max_sequence:
            max_sequence = count
            max_sequence_number = last

        last = num

    return max_sequence, max_sequence_number


with open("num_rand.txt", "w") as f:
    nums = get_random_numbers(2500)
    f.write(nums)
    print(get_longest_sequence(nums))
