# coding: utf-8

# Задание-1:
# Пользователь вводит число определите, является ли данное число простым. Делится только на себя и на единицу

import math

num = int(input("Введите число: "))

if num < 2:
    print("Число должно быть больше 1")
    quit()
elif num == 2:
    print("Это простое число")
    quit()

i = 2

limit = int(math.sqrt(num))

while i <= limit:
    if num % i == 0:
        print("Это сложное число")
        quit()
    i += 1

print("Это простое число")
