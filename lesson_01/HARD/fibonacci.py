# coding: utf-8

# Задание-2
# Найдите n-ое число Фибоначчи

fib1 = 1
fib2 = 1

num = int(input("Номер элемента ряда Фибоначчи: "))

i = 0
while i < num - 2:
    fib_sum = fib1 + fib2
    fib1 = fib2
    fib2 = fib_sum
    i = i + 1

print(fib2)