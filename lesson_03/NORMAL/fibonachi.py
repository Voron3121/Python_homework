# coding: utf-8

# Задание-1:
# Напишите функцию, возвращающую ряд Фибоначчи с n-элемента до m-элемента.
# Первыми элементами ряда считать цифры 1 1

def fibo(num_1, num_2):
    fibonachi = [1, 1]
    a = 1
    b = 1
    last_number = 2

    while last_number != num_2:
        last_number += 1
        a, b = b, a + b
        fibonachi.append(b)
    print(fibonachi[num_1 - 1: num_2 + 1])


fibo(2, 10)
